#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define lua_c
#include "lua.h"
#include "lauxlib.h"
#include "lualib.h"
#if !defined(LUA_PROMPT)
#define LUA_PROMPT		"> "
#define LUA_PROMPT2		">> "
#endif
#if !defined(LUA_PROGNAME)
#define LUA_PROGNAME		"lua"
#endif
#if !defined(LUA_MAXINPUT)
#define LUA_MAXINPUT		512
#endif
#if !defined(LUA_INIT)
#define LUA_INIT		"LUA_INIT"
#endif
#define LUA_INITVERSION \ LUA_INIT "_" LUA_VERSION_MAJOR "_" LUA_VERSION_MINOR
#if defined(LUA_USE_ISATTY)
#include <unistd.h>
#define lua_stdin_is_tty()	isatty(0)
#elif defined(LUA_WIN)
#include <io.h>
#include <stdio.h>
#define lua_stdin_is_tty()	_isatty(_fileno(stdin))
#else
#define lua_stdin_is_tty()	1 
#endif
#if defined(LUA_USE_READLINE)
#include <stdio.h>
#include <readline/readline.h>
#include <readline/history.h>
#define lua_readline(L,b,p)	((void)L, ((b)=readline(p)) != NULL)
#define lua_saveline(L,idx) \
        if (lua_rawlen(L,idx) > 0) \ add_history(lua_tostring(L, idx));
#define lua_freeline(L,b)	((void)L, free(b))
#elif !defined(lua_readline)
#define lua_readline(L,b,p) \ ((void)L, fputs(p, stdout), fflush(stdout), \ fgets(b, LUA_MAXINPUT, stdin) != NULL) 
#define lua_saveline(L,idx)	{ (void)L; (void)idx; }
#define lua_freeline(L,b)	{ (void)L; (void)b; }
#endif
static lua_State *globalL = NULL;
static const char *progname = LUA_PROGNAME;
static void lstop (lua_State *L, lua_Debug *ar) {
  (void)ar;  
  lua_sethook(L, NULL, 0, 0);
  luaL_error(L, "interrupted!");
}
static void laction (int i) {
  signal(i, SIG_DFL); 
  lua_sethook(globalL, lstop, LUA_MASKCALL | LUA_MASKRET | LUA_MASKCOUNT, 1);
}

static void print_usage (const char *badoption) {
  luai_writestringerror("%s: ", progname);
  if (badoption[1] == 'e' || badoption[1] == 'l')
    luai_writestringerror("'%s' needs argument\n", badoption);
  else
    luai_writestringerror("unrecognized option '%s'\n", badoption);
  luai_writestringerror(
  "usage: %s [options] [script [args]]\n"
  "Available options are:\n"
  "  -e stat  execute string " LUA_QL("stat") "\n"
  "  -i       enter interactive mode after executing " LUA_QL("script") "\n"
  "  -l name  require library " LUA_QL("name") "\n"
  "  -v       show version information\n"
  "  -E       ignore environment variables\n"
  "  --       stop handling options\n"
  "  -        stop handling options and execute stdin\n"
  ,
  progname);
}

static void l_message (const char *pname, const char *msg) {
  if (pname) luai_writestringerror("%s: ", pname);
  luai_writestringerror("%s\n", msg);
}

static int report (lua_State *L, int status) {
  if (status != LUA_OK && !lua_isnil(L, -1)) {
    const char *msg = lua_tostring(L, -1);
    if (msg == NULL) msg = "(error object is not a string)";
    l_message(progname, msg);
    lua_pop(L, 1);
    lua_gc(L, LUA_GCCOLLECT, 0);
  }
  return status;
}

static void finalreport (lua_State *L, int status) {
  if (status != LUA_OK) {
    const char *msg = (lua_type(L, -1) == LUA_TSTRING) ? lua_tostring(L, -1) : NULL;
    if (msg == NULL) msg = "(error object is not a string)";
    l_message(progname, msg);
    lua_pop(L, 1);
  }
}

static int traceback (lua_State *L) {
  const char *msg = lua_tostring(L, 1);
  if (msg)
    luaL_traceback(L, L, msg, 1);
  else if (!lua_isnoneornil(L, 1)) { 
    if (!luaL_callmeta(L, 1, "__tostring"))  
      lua_pushliteral(L, "(no error message)");
  }
  return 1;
}

static int docall (lua_State *L, int narg, int nres) {
  int status;
  int base = lua_gettop(L) - narg;  
  lua_pushcfunction(L, traceback);  
  lua_insert(L, base);  
  globalL = L;  
  signal(SIGINT, laction);
  status = lua_pcall(L, narg, nres, base);
  signal(SIGINT, SIG_DFL);
  lua_remove(L, base);  
  return status;
}

static void print_version (void) {
  luai_writestring(LUA_COPYRIGHT, strlen(LUA_COPYRIGHT));
  luai_writeline();
}

static int getargs (lua_State *L, char **argv, int n) {
  int narg;
  int i;
  int argc = 0;
  while (argv[argc]) argc++;  
  narg = argc - (n + 1); 
  luaL_checkstack(L, narg + 3, "too many arguments to script");
  for (i=n+1; i < argc; i++)
    lua_pushstring(L, argv[i]);
  lua_createtable(L, narg, n + 1);
  for (i=0; i < argc; i++) {
    lua_pushstring(L, argv[i]);
    lua_rawseti(L, -2, i - n);
  }
  return narg;
}

static int dofile (lua_State *L, const char *name) {
  int status = luaL_loadfile(L, name);
  if (status == LUA_OK) status = docall(L, 0, 0);
  return report(L, status);
}

static int dostring (lua_State *L, const char *s, const char *name) {
  int status = luaL_loadbuffer(L, s, strlen(s), name);
  if (status == LUA_OK) status = docall(L, 0, 0);
  return report(L, status);
}

static int dolibrary (lua_State *L, const char *name) {
  int status;
  lua_getglobal(L, "require");
  lua_pushstring(L, name);
  status = docall(L, 1, 1);  
  if (status == LUA_OK)
    lua_setglobal(L, name);  
  return report(L, status);
}

static const char *get_prompt (lua_State *L, int firstline) {
  const char *p;
  lua_getglobal(L, firstline ? "_PROMPT" : "_PROMPT2");
  p = lua_tostring(L, -1);
  if (p == NULL) p = (firstline ? LUA_PROMPT : LUA_PROMPT2);
  return p;
}

#define EOFMARK		"<eof>"
#define marklen		(sizeof(EOFMARK)/sizeof(char) - 1)
static int incomplete (lua_State *L, int status) {
  if (status == LUA_ERRSYNTAX) {
    size_t lmsg;
    const char *msg = lua_tolstring(L, -1, &lmsg);
    if (lmsg >= marklen && strcmp(msg + lmsg - marklen, EOFMARK) == 0) {
      lua_pop(L, 1);
      return 1;
    }
  }
  return 0; 
}

static int pushline (lua_State *L, int firstline) {
  char buffer[LUA_MAXINPUT];
  char *b = buffer;
  size_t l;
  const char *prmt = get_prompt(L, firstline);
  int readstatus = lua_readline(L, b, prmt);
  lua_pop(L, 1);  
  if (readstatus == 0)
    return 0; 
  l = strlen(b);
  if (l > 0 && b[l-1] == '\n') 
    b[l-1] = '\0';  
  if (firstline && b[0] == '=')  
    lua_pushfstring(L, "return %s", b+1);
  else
    lua_pushstring(L, b);
  lua_freeline(L, b);
  return 1;
}

static int loadline (lua_State *L) {
  int status;
  lua_settop(L, 0);
  if (!pushline(L, 1))
    return -1;  
  for (;;) { 
    size_t l;
    const char *line = lua_tolstring(L, 1, &l);
    status = luaL_loadbuffer(L, line, l, "=stdin");
    if (!incomplete(L, status)) break;  
    if (!pushline(L, 0)) 
      return -1;
    lua_pushliteral(L, "\n"); 
    lua_insert(L, -2); 
    lua_concat(L, 3);  
  }
  lua_saveline(L, 1);
  lua_remove(L, 1); 
  return status;
}

static void dotty (lua_State *L) {
  int status;
  const char *oldprogname = progname;
  progname = NULL;
  while ((status = loadline(L)) != -1) {
    if (status == LUA_OK) status = docall(L, 0, LUA_MULTRET);
    report(L, status);
    if (status == LUA_OK && lua_gettop(L) > 0) { 
      luaL_checkstack(L, LUA_MINSTACK, "too many results to print");
      lua_getglobal(L, "print");
      lua_insert(L, 1);
      if (lua_pcall(L, lua_gettop(L)-1, 0, 0) != LUA_OK)
        l_message(progname, lua_pushfstring(L, "error calling " LUA_QL("print") " (%s)", lua_tostring(L, -1)));
    }
  }
  lua_settop(L, 0); 
  luai_writeline();
  progname = oldprogname;
}

static int handle_script (lua_State *L, char **argv, int n) {
  int status;
  const char *fname;
  int narg = getargs(L, argv, n);  
  lua_setglobal(L, "arg");
  fname = argv[n];
  if (strcmp(fname, "-") == 0 && strcmp(argv[n-1], "--") != 0)
    fname = NULL;  
  status = luaL_loadfile(L, fname);
  lua_insert(L, -(narg+1));
  if (status == LUA_OK)
    status = docall(L, narg, LUA_MULTRET);
  else
    lua_pop(L, narg);
  return report(L, status);
}

#define noextrachars(x)		{if ((x)[2] != '\0') return -1;}
#define has_i		0	
#define has_v		1	
#define has_e		2	
#define has_E		3	
#define num_has		4	

static int collectargs (char **argv, int *args) {
  int i;
  for (i = 1; argv[i] != NULL; i++) {
    if (argv[i][0] != '-')  
        return i;
    switch (argv[i][1]) {  
      case '-':
        noextrachars(argv[i]);
        return (argv[i+1] != NULL ? i+1 : 0);
      case '\0':
        return i;
      case 'E':
        args[has_E] = 1;
        break;
      case 'i':
        noextrachars(argv[i]);
        args[has_i] = 1;  
      case 'v':
        noextrachars(argv[i]);
        args[has_v] = 1;
        break;
      case 'e':
        args[has_e] = 1; 
      case 'l': 
        if (argv[i][2] == '\0') {  
          i++; 
          if (argv[i] == NULL || argv[i][0] == '-')
            return -(i - 1);  
        }
        break;
      default:  
        return -i;  
    }
  }
  return 0;
}

static int runargs (lua_State *L, char **argv, int n) {
  int i;
  for (i = 1; i < n; i++) {
    lua_assert(argv[i][0] == '-');
    switch (argv[i][1]) {  
      case 'e': {
        const char *chunk = argv[i] + 2;
        if (*chunk == '\0') chunk = argv[++i];
        lua_assert(chunk != NULL);
        if (dostring(L, chunk, "=(command line)") != LUA_OK)
          return 0;
        break;
      }
      case 'l': {
        const char *filename = argv[i] + 2;
        if (*filename == '\0') filename = argv[++i];
        lua_assert(filename != NULL);
        if (dolibrary(L, filename) != LUA_OK)
          return 0;  
        break;
      }
      default: break;
    }
  }
  return 1;
}

static int handle_luainit (lua_State *L) {
  const char *name = "=" LUA_INITVERSION;
  const char *init = getenv(name + 1);
  if (init == NULL) {
    name = "=" LUA_INIT;
    init = getenv(name + 1);  
  }
  if (init == NULL) return LUA_OK;
  else if (init[0] == '@')
    return dofile(L, init+1);
  else
    return dostring(L, init, name);
}

static int pmain (lua_State *L) {
  int argc = (int)lua_tointeger(L, 1);
  char **argv = (char **)lua_touserdata(L, 2);
  int script;
  int args[num_has];
  args[has_i] = args[has_v] = args[has_e] = args[has_E] = 0;
  if (argv[0] && argv[0][0]) progname = argv[0];
  script = collectargs(argv, args);
  if (script < 0) {  
    print_usage(argv[-script]);
    return 0;
  }
  if (args[has_v]) print_version();
  if (args[has_E]) {  
    lua_pushboolean(L, 1); 
    lua_setfield(L, LUA_REGISTRYINDEX, "LUA_NOENV");
  }
  luaL_checkversion(L);
  lua_gc(L, LUA_GCSTOP, 0); 
  luaL_openlibs(L);  
  lua_gc(L, LUA_GCRESTART, 0);
  if (!args[has_E] && handle_luainit(L) != LUA_OK)
    return 0;  
  if (!runargs(L, argv, (script > 0) ? script : argc)) return 0;
  if (script && handle_script(L, argv, script) != LUA_OK) return 0;
  if (args[has_i]) 
    dotty(L);
  else if (script == 0 && !args[has_e] && !args[has_v]) {  
    if (lua_stdin_is_tty()) {
      print_version();
      dotty(L);
    }
    else dofile(L, NULL); 
  }
  lua_pushboolean(L, 1);  
  return 1;
}

int main (int argc, char **argv) {
  int status, result;
  lua_State *L = luaL_newstate();  
  if (L == NULL) {
    l_message(argv[0], "cannot create state: not enough memory");
    return EXIT_FAILURE;
  }
  lua_pushcfunction(L, &pmain);
  lua_pushinteger(L, argc); 
  lua_pushlightuserdata(L, argv); 
  status = lua_pcall(L, 2, 1, 0);
  result = lua_toboolean(L, -1);  
  finalreport(L, status);
  lua_close(L);
  return (result && status == LUA_OK) ? EXIT_SUCCESS : EXIT_FAILURE;
}
