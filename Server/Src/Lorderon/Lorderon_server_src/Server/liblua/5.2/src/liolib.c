#if !defined(_FILE_OFFSET_BITS)
#define	_LARGEFILE_SOURCE	1
#define _FILE_OFFSET_BITS	64
#endif
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define liolib_c
#define LUA_LIB
#include "lua.h"
#include "lauxlib.h"
#include "lualib.h"
#if !defined(lua_checkmode)
#define lua_checkmode(mode) \ (*mode != '\0' && strchr("rwa", *(mode++)) != NULL &&	\ (*mode != '+' || ++mode) &&	\ (*mode != 'b' || ++mode) && \ (*mode == '\0'))
#endif
#if !defined(lua_popen)	
#if defined(LUA_USE_POPEN)	
#define lua_popen(L,c,m) ((void)L, fflush(NULL), popen(c,m))
#define lua_pclose(L,file) ((void)L, pclose(file))
#elif defined(LUA_WIN)		
#define lua_popen(L,c,m) ((void)L, _popen(c,m))
#define lua_pclose(L,file) ((void)L, _pclose(file))
#else			
#define lua_popen(L,c,m) ((void)((void)c, m), \ luaL_error(L, LUA_QL("popen") " not supported"), (FILE*)0)
#define lua_pclose(L,file) ((void)((void)L, file), -1)
#endif				
#endif			
#if !defined(lua_fseek)	&& !defined(LUA_ANSI)	
#if defined(LUA_USE_POSIX)	
#define l_fseek(f,o,w) fseeko(f,o,w)
#define l_ftell(f) ftello(f)
#define l_seeknum	 off_t
#elif defined(LUA_WIN) && !defined(_CRTIMP_TYPEINFO) \ && defined(_MSC_VER) && (_MSC_VER >= 1400)	
#define l_fseek(f,o,w) _fseeki64(f,o,w)
#define l_ftell(f) _ftelli64(f)
#define l_seeknum __int64
#endif	
#endif		
#if !defined(l_fseek)		
#define l_fseek(f,o,w) fseek(f,o,w)
#define l_ftell(f) ftell(f)
#define l_seeknum long
#endif
#define IO_PREFIX	"_IO_"
#define IO_INPUT	(IO_PREFIX "input")
#define IO_OUTPUT	(IO_PREFIX "output")
typedef luaL_Stream LStream;
#define tolstream(L) ((LStream *)luaL_checkudata(L, 1, LUA_FILEHANDLE))
#define isclosed(p) ((p)->closef == NULL)
static int io_type (lua_State *L) {
  LStream *p;
  luaL_checkany(L, 1);
  p = (LStream *)luaL_testudata(L, 1, LUA_FILEHANDLE);
  if (p == NULL)
    lua_pushnil(L); 
  else if (isclosed(p))
    lua_pushliteral(L, "closed file");
  else
    lua_pushliteral(L, "file");
  return 1;
}

static int f_tostring (lua_State *L) {
  LStream *p = tolstream(L);
  if (isclosed(p))
    lua_pushliteral(L, "file (closed)");
  else
    lua_pushfstring(L, "file (%p)", p->f);
  return 1;
}

static FILE *tofile (lua_State *L) {
  LStream *p = tolstream(L);
  if (isclosed(p))
    luaL_error(L, "attempt to use a closed file");
  lua_assert(p->f);
  return p->f;
}

static LStream *newprefile (lua_State *L) {
  LStream *p = (LStream *)lua_newuserdata(L, sizeof(LStream));
  p->closef = NULL;  
  luaL_setmetatable(L, LUA_FILEHANDLE);
  return p;
}

static int aux_close (lua_State *L) {
  LStream *p = tolstream(L);
  lua_CFunction cf = p->closef;
  p->closef = NULL;  
  return (*cf)(L);  
}

static int io_close (lua_State *L) {
  if (lua_isnone(L, 1))  
    lua_getfield(L, LUA_REGISTRYINDEX, IO_OUTPUT); 
  tofile(L);  
  return aux_close(L);
}

static int f_gc (lua_State *L) {
  LStream *p = tolstream(L);
  if (!isclosed(p) && p->f != NULL)
    aux_close(L); 
  return 0;
}

static int io_fclose (lua_State *L) {
  LStream *p = tolstream(L);
  int res = fclose(p->f);
  return luaL_fileresult(L, (res == 0), NULL);
}

static LStream *newfile (lua_State *L) {
  LStream *p = newprefile(L);
  p->f = NULL;
  p->closef = &io_fclose;
  return p;
}

static void opencheck (lua_State *L, const char *fname, const char *mode) {
  LStream *p = newfile(L);
  p->f = fopen(fname, mode);
  if (p->f == NULL)
    luaL_error(L, "cannot open file " LUA_QS " (%s)", fname, strerror(errno));
}

static int io_open (lua_State *L) {
  const char *filename = luaL_checkstring(L, 1);
  const char *mode = luaL_optstring(L, 2, "r");
  LStream *p = newfile(L);
  const char *md = mode; 
  luaL_argcheck(L, lua_checkmode(md), 2, "invalid mode");
  p->f = fopen(filename, mode);
  return (p->f == NULL) ? luaL_fileresult(L, 0, filename) : 1;
}

static int io_pclose (lua_State *L) {
  LStream *p = tolstream(L);
  return luaL_execresult(L, lua_pclose(L, p->f));
}

static int io_popen (lua_State *L) {
  const char *filename = luaL_checkstring(L, 1);
  const char *mode = luaL_optstring(L, 2, "r");
  LStream *p = newprefile(L);
  p->f = lua_popen(L, filename, mode);
  p->closef = &io_pclose;
  return (p->f == NULL) ? luaL_fileresult(L, 0, filename) : 1;
}

static int io_tmpfile (lua_State *L) {
  LStream *p = newfile(L);
  p->f = tmpfile();
  return (p->f == NULL) ? luaL_fileresult(L, 0, NULL) : 1;
}

static FILE *getiofile (lua_State *L, const char *findex) {
  LStream *p;
  lua_getfield(L, LUA_REGISTRYINDEX, findex);
  p = (LStream *)lua_touserdata(L, -1);
  if (isclosed(p))
    luaL_error(L, "standard %s file is closed", findex + strlen(IO_PREFIX));
  return p->f;
}

static int g_iofile (lua_State *L, const char *f, const char *mode) {
  if (!lua_isnoneornil(L, 1)) {
    const char *filename = lua_tostring(L, 1);
    if (filename)
      opencheck(L, filename, mode);
    else {
      tofile(L);  
      lua_pushvalue(L, 1);
    }
    lua_setfield(L, LUA_REGISTRYINDEX, f);
  }
  lua_getfield(L, LUA_REGISTRYINDEX, f);
  return 1;
}
static int io_input (lua_State *L) {
  return g_iofile(L, IO_INPUT, "r");
}

static int io_output (lua_State *L) {
  return g_iofile(L, IO_OUTPUT, "w");
}

static int io_readline (lua_State *L);

static void aux_lines (lua_State *L, int toclose) {
  int i;
  int n = lua_gettop(L) - 1;  
  luaL_argcheck(L, n <= LUA_MINSTACK - 3, LUA_MINSTACK - 3, "too many options");
  lua_pushvalue(L, 1);  
  lua_pushinteger(L, n);  
  lua_pushboolean(L, toclose);  
  for (i = 1; i <= n; i++) lua_pushvalue(L, i + 1);  
  lua_pushcclosure(L, io_readline, 3 + n);
}

static int f_lines (lua_State *L) {
  tofile(L); 
  aux_lines(L, 0);
  return 1;
}

static int io_lines (lua_State *L) {
  int toclose;
  if (lua_isnone(L, 1)) lua_pushnil(L);  
  if (lua_isnil(L, 1)) {  
    lua_getfield(L, LUA_REGISTRYINDEX, IO_INPUT);  
    lua_replace(L, 1);
    tofile(L);  
    toclose = 0;  
  }
  else {  
    const char *filename = luaL_checkstring(L, 1);
    opencheck(L, filename, "r");
    lua_replace(L, 1);  
    toclose = 1; 
  }
  aux_lines(L, toclose);
  return 1;
}

static int read_number (lua_State *L, FILE *f) {
  lua_Number d;
  if (fscanf(f, LUA_NUMBER_SCAN, &d) == 1) {
    lua_pushnumber(L, d);
    return 1;
  }
  else {
   lua_pushnil(L); 
   return 0;  
  }
}

static int test_eof (lua_State *L, FILE *f) {
  int c = getc(f);
  ungetc(c, f);
  lua_pushlstring(L, NULL, 0);
  return (c != EOF);
}

static int read_line (lua_State *L, FILE *f, int chop) {
  luaL_Buffer b;
  luaL_buffinit(L, &b);
  for (;;) {
    size_t l;
    char *p = luaL_prepbuffer(&b);
    if (fgets(p, LUAL_BUFFERSIZE, f) == NULL) {  
      luaL_pushresult(&b);  
      return (lua_rawlen(L, -1) > 0);  
    }
    l = strlen(p);
    if (l == 0 || p[l-1] != '\n')
      luaL_addsize(&b, l);
    else {
      luaL_addsize(&b, l - chop);  
      luaL_pushresult(&b);  
      return 1;  
    }
  }
}

#define MAX_SIZE_T	(~(size_t)0)
static void read_all (lua_State *L, FILE *f) {
  size_t rlen = LUAL_BUFFERSIZE;  
  luaL_Buffer b;
  luaL_buffinit(L, &b);
  for (;;) {
    char *p = luaL_prepbuffsize(&b, rlen);
    size_t nr = fread(p, sizeof(char), rlen, f);
    luaL_addsize(&b, nr);
    if (nr < rlen) break;  
    else if (rlen <= (MAX_SIZE_T / 4))  
      rlen *= 2;  
  }
  luaL_pushresult(&b); 
}

static int read_chars (lua_State *L, FILE *f, size_t n) {
  size_t nr;  
  char *p;
  luaL_Buffer b;
  luaL_buffinit(L, &b);
  p = luaL_prepbuffsize(&b, n);  
  nr = fread(p, sizeof(char), n, f); 
  luaL_addsize(&b, nr);
  luaL_pushresult(&b);  
  return (nr > 0);  
}

static int g_read (lua_State *L, FILE *f, int first) {
  int nargs = lua_gettop(L) - 1;
  int success;
  int n;
  clearerr(f);
  if (nargs == 0) {  
    success = read_line(L, f, 1);
    n = first+1;  
  }
  else {  
    luaL_checkstack(L, nargs+LUA_MINSTACK, "too many arguments");
    success = 1;
    for (n = first; nargs-- && success; n++) {
      if (lua_type(L, n) == LUA_TNUMBER) {
        size_t l = (size_t)lua_tointeger(L, n);
        success = (l == 0) ? test_eof(L, f) : read_chars(L, f, l);
      }
      else {
        const char *p = lua_tostring(L, n);
        luaL_argcheck(L, p && p[0] == '*', n, "invalid option");
        switch (p[1]) {
          case 'n': 
            success = read_number(L, f);
            break;
          case 'l':  
            success = read_line(L, f, 1);
            break;
          case 'L':  
            success = read_line(L, f, 0);
            break;
          case 'a':  
            read_all(L, f);  
            success = 1;
            break;
          default:
            return luaL_argerror(L, n, "invalid format");
        }
      }
    }
  }
  if (ferror(f))
    return luaL_fileresult(L, 0, NULL);
  if (!success) {
    lua_pop(L, 1); 
    lua_pushnil(L);  
  }
  return n - first;
}

static int io_read (lua_State *L) {
  return g_read(L, getiofile(L, IO_INPUT), 1);
}

static int f_read (lua_State *L) {
  return g_read(L, tofile(L), 2);
}

static int io_readline (lua_State *L) {
  LStream *p = (LStream *)lua_touserdata(L, lua_upvalueindex(1));
  int i;
  int n = (int)lua_tointeger(L, lua_upvalueindex(2));
  if (isclosed(p))  
    return luaL_error(L, "file is already closed");
  lua_settop(L , 1);
  for (i = 1; i <= n; i++)  
    lua_pushvalue(L, lua_upvalueindex(3 + i));
  n = g_read(L, p->f, 2);  
  lua_assert(n > 0); 
  if (!lua_isnil(L, -n))  
    return n; 
  else {  
    if (n > 1) {  
      return luaL_error(L, "%s", lua_tostring(L, -n + 1));
    }
    if (lua_toboolean(L, lua_upvalueindex(3))) {  
      lua_settop(L, 0);
      lua_pushvalue(L, lua_upvalueindex(1));
      aux_close(L);  
    }
    return 0;
  }
}

static int g_write (lua_State *L, FILE *f, int arg) {
  int nargs = lua_gettop(L) - arg;
  int status = 1;
  for (; nargs--; arg++) {
    if (lua_type(L, arg) == LUA_TNUMBER) {
      status = status &&
          fprintf(f, LUA_NUMBER_FMT, lua_tonumber(L, arg)) > 0;
    }
    else {
      size_t l;
      const char *s = luaL_checklstring(L, arg, &l);
      status = status && (fwrite(s, sizeof(char), l, f) == l);
    }
  }
  if (status) return 1;  
  else return luaL_fileresult(L, status, NULL);
}

static int io_write (lua_State *L) {
  return g_write(L, getiofile(L, IO_OUTPUT), 1);
}

static int f_write (lua_State *L) {
  FILE *f = tofile(L);
  lua_pushvalue(L, 1);  
  return g_write(L, f, 2);
}

static int f_seek (lua_State *L) {
  static const int mode[] = {SEEK_SET, SEEK_CUR, SEEK_END};
  static const char *const modenames[] = {"set", "cur", "end", NULL};
  FILE *f = tofile(L);
  int op = luaL_checkoption(L, 2, "cur", modenames);
  lua_Number p3 = luaL_optnumber(L, 3, 0);
  l_seeknum offset = (l_seeknum)p3;
  luaL_argcheck(L, (lua_Number)offset == p3, 3, "not an integer in proper range");
  op = l_fseek(f, offset, mode[op]);
  if (op)
    return luaL_fileresult(L, 0, NULL);  
  else {
    lua_pushnumber(L, (lua_Number)l_ftell(f));
    return 1;
  }
}

static int f_setvbuf (lua_State *L) {
  static const int mode[] = {_IONBF, _IOFBF, _IOLBF};
  static const char *const modenames[] = {"no", "full", "line", NULL};
  FILE *f = tofile(L);
  int op = luaL_checkoption(L, 2, NULL, modenames);
  lua_Integer sz = luaL_optinteger(L, 3, LUAL_BUFFERSIZE);
  int res = setvbuf(f, NULL, mode[op], sz);
  return luaL_fileresult(L, res == 0, NULL);
}

static int io_flush (lua_State *L) {
  return luaL_fileresult(L, fflush(getiofile(L, IO_OUTPUT)) == 0, NULL);
}

static int f_flush (lua_State *L) {
  return luaL_fileresult(L, fflush(tofile(L)) == 0, NULL);
}

static const luaL_Reg iolib[] = {
  {"close", io_close},
  {"flush", io_flush},
  {"input", io_input},
  {"lines", io_lines},
  {"open", io_open},
  {"output", io_output},
  {"popen", io_popen},
  {"read", io_read},
  {"tmpfile", io_tmpfile},
  {"type", io_type},
  {"write", io_write},
  {NULL, NULL}
};

static const luaL_Reg flib[] = {
  {"close", io_close},
  {"flush", f_flush},
  {"lines", f_lines},
  {"read", f_read},
  {"seek", f_seek},
  {"setvbuf", f_setvbuf},
  {"write", f_write},
  {"__gc", f_gc},
  {"__tostring", f_tostring},
  {NULL, NULL}
};

static void createmeta (lua_State *L) {
  luaL_newmetatable(L, LUA_FILEHANDLE);  
  lua_pushvalue(L, -1);  
  lua_setfield(L, -2, "__index"); 
  luaL_setfuncs(L, flib, 0);  
  lua_pop(L, 1); 
}

static int io_noclose (lua_State *L) {
  LStream *p = tolstream(L);
  p->closef = &io_noclose; 
  lua_pushnil(L);
  lua_pushliteral(L, "cannot close standard file");
  return 2;
}

static void createstdfile (lua_State *L, FILE *f, const char *k, const char *fname) {
  LStream *p = newprefile(L);
  p->f = f;
  p->closef = &io_noclose;
  if (k != NULL) {
    lua_pushvalue(L, -1);
    lua_setfield(L, LUA_REGISTRYINDEX, k);  
  }
  lua_setfield(L, -2, fname);  
}

LUAMOD_API int luaopen_io (lua_State *L) {
  luaL_newlib(L, iolib); 
  createmeta(L);
  createstdfile(L, stdin, IO_INPUT, "stdin");
  createstdfile(L, stdout, IO_OUTPUT, "stdout");
  createstdfile(L, stderr, NULL, "stderr");
  return 1;
}
