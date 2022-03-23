#include <locale.h>
#include <string.h>
#define llex_c
#define LUA_CORE
#include "lua.h"
#include "lctype.h"
#include "ldo.h"
#include "llex.h"
#include "lobject.h"
#include "lparser.h"
#include "lstate.h"
#include "lstring.h"
#include "ltable.h"
#include "lzio.h"
#define next(ls) (ls->current = zgetc(ls->z))
#define currIsNewline(ls)	(ls->current == '\n' || ls->current == '\r')
int token_preserved[NUM_PRESERVED] = 
{ TK_DO };

static const char *const luaX_tokens [] = {
    "and", "break", "begin", "else", "elseif",
    "end", "false", "for", "function", "goto", "if",
    "in", "local", "nil", "not", "or", "repeat",
    "return", "then", "true", "until", "while",
	  "quest", "state", "with", "when",
	  "do",
    "..", "...", "==", ">=", "<=", "~=", "::", "<eof>",
    "<number>", "<name>", "<string>"
};

#define save_and_next(ls) (save(ls, ls->current), next(ls))
static l_noret lexerror (LexState *ls, const char *msg, int token);
static void save (LexState *ls, int c) {
  Mbuffer *b = ls->buff;
  if (luaZ_bufflen(b) + 1 > luaZ_sizebuffer(b)) {
    size_t newsize;
    if (luaZ_sizebuffer(b) >= MAX_SIZET/2)
      lexerror(ls, "lexical element too long", 0);
    newsize = luaZ_sizebuffer(b) * 2;
    luaZ_resizebuffer(ls->L, b, newsize);
  }
  b->buffer[luaZ_bufflen(b)++] = cast(char, c);
}

void luaX_init (lua_State *L) {
  int i;
  for (i=0; i<NUM_RESERVED-NUM_PRESERVED; i++) {
    TString *ts = luaS_new(L, luaX_tokens[i]);
    luaS_fix(ts); 
    ts->tsv.extra = cast_byte(i+1);  
  }
  int j;
  for(j=0;j<NUM_PRESERVED; i++, j++)
  {
    TString *ts = luaS_new(L, luaX_tokens[i]);
    luaS_fix(ts); 
    ts->tsv.extra = cast_byte(token_preserved[j]-FIRST_RESERVED+1);  
  }
}

const char *luaX_token2str (LexState *ls, int token) {
  if (token < FIRST_RESERVED) { 
    lua_assert(token == cast(unsigned char, token));
    return (lisprint(token)) ? luaO_pushfstring(ls->L, LUA_QL("%c"), token) : luaO_pushfstring(ls->L, "char(%d)", token);
  }
  else {
    const char *s = luaX_tokens[token - FIRST_RESERVED];
    if (token < TK_EOS)
      return luaO_pushfstring(ls->L, LUA_QS, s);
    else  
      return s;
  }
}

static const char *txtToken (LexState *ls, int token) {
  switch (token) {
    case TK_NAME:
    case TK_STRING:
    case TK_NUMBER:
      save(ls, '\0');
      return luaO_pushfstring(ls->L, LUA_QS, luaZ_buffer(ls->buff));
    default:
      return luaX_token2str(ls, token);
  }
}

static l_noret lexerror (LexState *ls, const char *msg, int token) {
  char buff[LUA_IDSIZE];
  luaO_chunkid(buff, getstr(ls->source), LUA_IDSIZE);
  msg = luaO_pushfstring(ls->L, "%s:%d: %s", buff, ls->linenumber, msg);
  if (token)
    luaO_pushfstring(ls->L, "%s near %s", msg, txtToken(ls, token));
  luaD_throw(ls->L, LUA_ERRSYNTAX);
}

l_noret luaX_syntaxerror (LexState *ls, const char *msg) {
  lexerror(ls, msg, ls->t.token);
}

TString *luaX_newstring (LexState *ls, const char *str, size_t l) {
  lua_State *L = ls->L;
  TValue *o; 
  TString *ts = luaS_newlstr(L, str, l); 
  setsvalue2s(L, L->top++, ts);  
  o = luaH_set(L, ls->fs->h, L->top - 1);
  if (ttisnil(o)) {  
    setbvalue(o, 1);  
    luaC_checkGC(L);
  }
  else {  
    ts = rawtsvalue(keyfromval(o)); 
  }
  L->top--;  
  return ts;
}

static void inclinenumber (LexState *ls) {
  int old = ls->current;
  lua_assert(currIsNewline(ls));
  next(ls);  
  if (currIsNewline(ls) && ls->current != old)
    next(ls); 
  if (++ls->linenumber >= MAX_INT)
    luaX_syntaxerror(ls, "chunk has too many lines");
}

void luaX_setinput (lua_State *L, LexState *ls, ZIO *z, TString *source, int firstchar) {
  ls->decpoint = '.';
  ls->L = L;
  ls->current = firstchar;
  ls->lookahead.token = TK_EOS; 
  ls->z = z;
  ls->fs = NULL;
  ls->linenumber = 1;
  ls->lastline = 1;
  ls->source = source;
  ls->envn = luaS_new(L, LUA_ENV); 
  luaS_fix(ls->envn);  
  luaZ_resizebuffer(ls->L, ls->buff, LUA_MINBUFFER); 
}

static int check_next (LexState *ls, const char *set) {
  if (ls->current == '\0' || !strchr(set, ls->current))
    return 0;
  save_and_next(ls);
  return 1;
}

static void buffreplace (LexState *ls, char from, char to) {
  size_t n = luaZ_bufflen(ls->buff);
  char *p = luaZ_buffer(ls->buff);
  while (n--)
    if (p[n] == from) p[n] = to;
}

#if !defined(getlocaledecpoint)
#define getlocaledecpoint()	(localeconv()->decimal_point[0])
#endif
#define buff2d(b,e)	luaO_str2d(luaZ_buffer(b), luaZ_bufflen(b) - 1, e)
static void trydecpoint (LexState *ls, SemInfo *seminfo) {
  char old = ls->decpoint;
  ls->decpoint = getlocaledecpoint();
  buffreplace(ls, old, ls->decpoint); 
  if (!buff2d(ls->buff, &seminfo->r)) {
    buffreplace(ls, ls->decpoint, '.');  
    lexerror(ls, "malformed number", TK_NUMBER);
  }
}

static void read_numeral (LexState *ls, SemInfo *seminfo) {
  const char *expo = "Ee";
  int first = ls->current;
  lua_assert(lisdigit(ls->current));
  save_and_next(ls);
  if (first == '0' && check_next(ls, "Xx"))  
    expo = "Pp";
  for (;;) {
    if (check_next(ls, expo))
      check_next(ls, "+-"); 
    if (lisxdigit(ls->current) || ls->current == '.')
      save_and_next(ls);
    else  break;
  }
  save(ls, '\0');
  buffreplace(ls, '.', ls->decpoint);  
  if (!buff2d(ls->buff, &seminfo->r))  
    trydecpoint(ls, seminfo);
}

static int skip_sep (LexState *ls) {
  int count = 0;
  int s = ls->current;
  lua_assert(s == '[' || s == ']');
  save_and_next(ls);
  while (ls->current == '=') {
    save_and_next(ls);
    count++;
  }
  return (ls->current == s) ? count : (-count) - 1;
}


static void read_long_string (LexState *ls, SemInfo *seminfo, int sep) {
  save_and_next(ls); 
  if (currIsNewline(ls))  
    inclinenumber(ls); 
  for (;;) {
    switch (ls->current) {
      case EOZ:
        lexerror(ls, (seminfo) ? "unfinished long string" : "unfinished long comment", TK_EOS);
        break;  
      case ']': {
        if (skip_sep(ls) == sep) {
          save_and_next(ls); 
          goto endloop;
        }
        break;
      }
      case '\n': case '\r': {
        save(ls, '\n');
        inclinenumber(ls);
        if (!seminfo) luaZ_resetbuffer(ls->buff);  
        break;
      }
      default: {
        if (seminfo) save_and_next(ls);
        else next(ls);
      }
    }
  } endloop:
  if (seminfo)
    seminfo->ts = luaX_newstring(ls, luaZ_buffer(ls->buff) + (2 + sep), luaZ_bufflen(ls->buff) - 2*(2 + sep));
}

static void escerror (LexState *ls, int *c, int n, const char *msg) {
  int i;
  luaZ_resetbuffer(ls->buff); 
  save(ls, '\\');
  for (i = 0; i < n && c[i] != EOZ; i++)
    save(ls, c[i]);
  lexerror(ls, msg, TK_STRING);
}

static int readhexaesc (LexState *ls) {
  int c[3], i;  
  int r = 0;  
  c[0] = 'x';  
  for (i = 1; i < 3; i++) {  
    c[i] = next(ls);
    if (!lisxdigit(c[i]))
      escerror(ls, c, i + 1, "hexadecimal digit expected");
    r = (r << 4) + luaO_hexavalue(c[i]);
  }
  return r;
}

static int readdecesc (LexState *ls) {
  int c[3], i;
  int r = 0;  
  for (i = 0; i < 3 && lisdigit(ls->current); i++) { 
    c[i] = ls->current;
    r = 10*r + c[i] - '0';
    next(ls);
  }
  if (r > UCHAR_MAX)
    escerror(ls, c, i, "decimal escape too large");
  return r;
}

static void read_string (LexState *ls, int del, SemInfo *seminfo) {
  save_and_next(ls);  
  while (ls->current != del) {
	  unsigned char b_current = (unsigned char)ls->current;
	  if (b_current & 0x80)
	  {
		  save_and_next(ls);
		  save_and_next(ls);
	  }
	  else
	  {
		  switch (b_current) {
      case EOZ:
        lexerror(ls, "unfinished string", TK_EOS);
        break; 
      case '\n':
      case '\r':
        lexerror(ls, "unfinished string", TK_STRING);
        break; 
      case '\\': {
        int c;  
        next(ls);  
        switch (ls->current) {
          case 'a': c = '\a'; goto read_save;
          case 'b': c = '\b'; goto read_save;
          case 'f': c = '\f'; goto read_save;
          case 'n': c = '\n'; goto read_save;
          case 'r': c = '\r'; goto read_save;
          case 't': c = '\t'; goto read_save;
          case 'v': c = '\v'; goto read_save;
          case 'x': c = readhexaesc(ls); goto read_save;
          case '\n': case '\r':
            inclinenumber(ls); c = '\n'; goto only_save;
          case '\\': case '\"': case '\'':
            c = ls->current; goto read_save;
          case EOZ: goto no_save;  
          case 'z': {  
            next(ls);  
            while (lisspace(ls->current)) {
              if (currIsNewline(ls)) inclinenumber(ls);
              else next(ls);
            }
            goto no_save;
          }
          default: {
            if (!lisdigit(ls->current))
              escerror(ls, &ls->current, 1, "invalid escape sequence");
            c = readdecesc(ls);
            goto only_save;
          }
        }
       read_save: next(ls);  
       only_save: save(ls, c);  
       no_save: break;
      }
      default:
        save_and_next(ls);
	}
    }
  }
  save_and_next(ls);  
  seminfo->ts = luaX_newstring(ls, luaZ_buffer(ls->buff) + 1, luaZ_bufflen(ls->buff) - 2);
}

int llex (LexState *ls, SemInfo *seminfo) {
  luaZ_resetbuffer(ls->buff);
  for (;;) {
    switch (ls->current) {
      case '\n': case '\r': {  
        inclinenumber(ls);
        break;
      }
      case ' ': case '\f': case '\t': case '\v': {  
        next(ls);
        break;
      }
      case '-': {  
        next(ls);
        if (ls->current != '-') return '-';
        next(ls);
        if (ls->current == '[') {  
          int sep = skip_sep(ls);
          luaZ_resetbuffer(ls->buff);  
          if (sep >= 0) {
            read_long_string(ls, NULL, sep);  
            luaZ_resetbuffer(ls->buff);  
            break;
          }
        }
        while (!currIsNewline(ls) && ls->current != EOZ)
          next(ls); 
        break;
      }
      case '[': {  
        int sep = skip_sep(ls);
        if (sep >= 0) {
          read_long_string(ls, seminfo, sep);
          return TK_STRING;
        }
        else if (sep == -1) return '[';
        else lexerror(ls, "invalid long string delimiter", TK_STRING);
      }
      case '=': {
        next(ls);
        if (ls->current != '=') return '=';
        else { next(ls); return TK_EQ; }
      }
      case '<': {
        next(ls);
        if (ls->current != '=') return '<';
        else { next(ls); return TK_LE; }
      }
      case '>': {
        next(ls);
        if (ls->current != '=') return '>';
        else { next(ls); return TK_GE; }
      }
      case '~': {
        next(ls);
        if (ls->current != '=') return '~';
        else { next(ls); return TK_NE; }
      }
      case '!': {
        next(ls);
        if (ls->current != '=') return '~';
        else { next(ls); return TK_NE; }
      }
      case ':': {
        next(ls);
        if (ls->current != ':') return ':';
        else { next(ls); return TK_DBCOLON; }
      }
      case '"': case '\'': {  
        read_string(ls, ls->current, seminfo);
        return TK_STRING;
      }
      case '.': {  
        save_and_next(ls);
        if (check_next(ls, ".")) {
          if (check_next(ls, "."))
            return TK_DOTS;   
          else return TK_CONCAT;   
        }
        else if (!lisdigit(ls->current)) return '.';
      }
      case '0': case '1': case '2': case '3': case '4':
      case '5': case '6': case '7': case '8': case '9': {
        read_numeral(ls, seminfo);
        return TK_NUMBER;
      }
      case EOZ: {
        return TK_EOS;
      }
      default: {
        if (lislalpha(ls->current)) {  
          TString *ts;
          do {
            save_and_next(ls);
          } while (lislalnum(ls->current));
          ts = luaX_newstring(ls, luaZ_buffer(ls->buff), luaZ_bufflen(ls->buff));
          seminfo->ts = ts;
          if (isreserved(ts)) 
            return ts->tsv.extra - 1 + FIRST_RESERVED;
          else {
            return TK_NAME;
          }
        }
        else {  
          int c = ls->current;
          next(ls);
          return c;
        }
      }
    }
  }
}

void luaX_next (LexState *ls) {
  ls->lastline = ls->linenumber;
  if (ls->lookahead.token != TK_EOS) {  
    ls->t = ls->lookahead;
    ls->lookahead.token = TK_EOS;  
  }
  else
    ls->t.token = llex(ls, &ls->t.seminfo); 
}

int luaX_lookahead (LexState *ls) {
  lua_assert(ls->lookahead.token == TK_EOS);
  ls->lookahead.token = llex(ls, &ls->lookahead.seminfo);
  return ls->lookahead.token;
}
