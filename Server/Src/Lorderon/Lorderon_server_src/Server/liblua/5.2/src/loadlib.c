#if defined(_WIN32)
#include <windows.h>
#endif
#include <stdlib.h>
#include <string.h>
#define loadlib_c
#define LUA_LIB
#include "lua.h"
#include "lauxlib.h"
#include "lualib.h"
#if !defined(LUA_PATH)
#define LUA_PATH	"LUA_PATH"
#endif
#if !defined(LUA_CPATH)
#define LUA_CPATH	"LUA_CPATH"
#endif
#define LUA_PATHSUFFIX "_" LUA_VERSION_MAJOR "_" LUA_VERSION_MINOR
#define LUA_PATHVERSION	 LUA_PATH LUA_PATHSUFFIX
#define LUA_CPATHVERSION LUA_CPATH LUA_PATHSUFFIX
#if !defined (LUA_PATH_SEP)
#define LUA_PATH_SEP		";"
#endif
#if !defined (LUA_PATH_MARK)
#define LUA_PATH_MARK		"?"
#endif
#if !defined (LUA_EXEC_DIR)
#define LUA_EXEC_DIR		"!"
#endif
#if !defined (LUA_IGMARK)
#define LUA_IGMARK		"-"
#endif
#if !defined(LUA_CSUBSEP)
#define LUA_CSUBSEP		LUA_DIRSEP
#endif
#if !defined(LUA_LSUBSEP)
#define LUA_LSUBSEP		LUA_DIRSEP
#endif
#define LUA_POF		"luaopen_"
#define LUA_OFSEP	"_"
#define CLIBS		"_CLIBS"
#define LIB_FAIL	"open"
#define ERRLIB		1
#define ERRFUNC		2
#define setprogdir(L)		((void)0)
static void ll_unloadlib (void *lib);
static void *ll_load (lua_State *L, const char *path, int seeglb);
static lua_CFunction ll_sym (lua_State *L, void *lib, const char *sym);
#if defined(LUA_USE_DLOPEN)
#include <dlfcn.h>
static void ll_unloadlib (void *lib) {
  dlclose(lib);
}

static void *ll_load (lua_State *L, const char *path, int seeglb) {
  void *lib = dlopen(path, RTLD_NOW | (seeglb ? RTLD_GLOBAL : RTLD_LOCAL));
  if (lib == NULL) lua_pushstring(L, dlerror());
  return lib;
}

static lua_CFunction ll_sym (lua_State *L, void *lib, const char *sym) {
  lua_CFunction f = (lua_CFunction)dlsym(lib, sym);
  if (f == NULL) lua_pushstring(L, dlerror());
  return f;
}

#elif defined(LUA_DL_DLL)
#undef setprogdir
#if !defined(LUA_LLE_FLAGS)
#define LUA_LLE_FLAGS	0
#endif

static void setprogdir (lua_State *L) {
  char buff[MAX_PATH + 1];
  char *lb;
  DWORD nsize = sizeof(buff)/sizeof(char);
  DWORD n = GetModuleFileNameA(NULL, buff, nsize);
  if (n == 0 || n == nsize || (lb = strrchr(buff, '\\')) == NULL)
    luaL_error(L, "unable to get ModuleFileName");
  else {
    *lb = '\0';
    luaL_gsub(L, lua_tostring(L, -1), LUA_EXEC_DIR, buff);
    lua_remove(L, -2);  
  }
}

static void pusherror (lua_State *L) {
  int error = GetLastError();
  char buffer[128];
  if (FormatMessageA(FORMAT_MESSAGE_IGNORE_INSERTS | FORMAT_MESSAGE_FROM_SYSTEM,
      NULL, error, 0, buffer, sizeof(buffer)/sizeof(char), NULL))
    lua_pushstring(L, buffer);
  else
    lua_pushfstring(L, "system error %d\n", error);
}

static void ll_unloadlib (void *lib) {
  FreeLibrary((HMODULE)lib);
}

static void *ll_load (lua_State *L, const char *path, int seeglb) {
  HMODULE lib = LoadLibraryExA(path, NULL, LUA_LLE_FLAGS);
  (void)(seeglb);  
  if (lib == NULL) pusherror(L);
  return lib;
}

static lua_CFunction ll_sym (lua_State *L, void *lib, const char *sym) {
  lua_CFunction f = (lua_CFunction)GetProcAddress((HMODULE)lib, sym);
  if (f == NULL) pusherror(L);
  return f;
}
#else
#undef LIB_FAIL
#define LIB_FAIL	"absent"
#define DLMSG	"dynamic libraries not enabled; check your Lua installation"

static void ll_unloadlib (void *lib) {
  (void)(lib);  
}

static void *ll_load (lua_State *L, const char *path, int seeglb) {
  (void)(path); (void)(seeglb); 
  lua_pushliteral(L, DLMSG);
  return NULL;
}


static lua_CFunction ll_sym (lua_State *L, void *lib, const char *sym) {
  (void)(lib); (void)(sym);  
  lua_pushliteral(L, DLMSG);
  return NULL;
}
#endif

static void *ll_checkclib (lua_State *L, const char *path) {
  void *plib;
  lua_getfield(L, LUA_REGISTRYINDEX, CLIBS);
  lua_getfield(L, -1, path);
  plib = lua_touserdata(L, -1);  
  lua_pop(L, 2);  
  return plib;
}

static void ll_addtoclib (lua_State *L, const char *path, void *plib) {
  lua_getfield(L, LUA_REGISTRYINDEX, CLIBS);
  lua_pushlightuserdata(L, plib);
  lua_pushvalue(L, -1);
  lua_setfield(L, -3, path);  
  lua_rawseti(L, -2, luaL_len(L, -2) + 1);  
  lua_pop(L, 1); 
}

static int gctm (lua_State *L) {
  int n = luaL_len(L, 1);
  for (; n >= 1; n--) {  
    lua_rawgeti(L, 1, n);  
    ll_unloadlib(lua_touserdata(L, -1));
    lua_pop(L, 1); 
  }
  return 0;
}

static int ll_loadfunc (lua_State *L, const char *path, const char *sym) {
  void *reg = ll_checkclib(L, path); 
  if (reg == NULL) {  
    reg = ll_load(L, path, *sym == '*');
    if (reg == NULL) return ERRLIB;  
    ll_addtoclib(L, path, reg);
  }
  if (*sym == '*') { 
    lua_pushboolean(L, 1);  
    return 0;  
  }
  else {
    lua_CFunction f = ll_sym(L, reg, sym);
    if (f == NULL)
      return ERRFUNC;  
    lua_pushcfunction(L, f);  
    return 0; 
  }
}

static int ll_loadlib (lua_State *L) {
  const char *path = luaL_checkstring(L, 1);
  const char *init = luaL_checkstring(L, 2);
  int stat = ll_loadfunc(L, path, init);
  if (stat == 0) 
    return 1;  
  else {  
    lua_pushnil(L);
    lua_insert(L, -2);
    lua_pushstring(L, (stat == ERRLIB) ?  LIB_FAIL : "init");
    return 3; 
  }
}

static int readable (const char *filename) {
  FILE *f = fopen(filename, "r");  
  if (f == NULL) return 0; 
  fclose(f);
  return 1;
}

static const char *pushnexttemplate (lua_State *L, const char *path) {
  const char *l;
  while (*path == *LUA_PATH_SEP) path++;  
  if (*path == '\0') return NULL;  
  l = strchr(path, *LUA_PATH_SEP); 
  if (l == NULL) l = path + strlen(path);
  lua_pushlstring(L, path, l - path);  
  return l;
}

static const char *searchpath (lua_State *L, const char *name, const char *path, const char *sep, const char *dirsep) {
  luaL_Buffer msg; 
  luaL_buffinit(L, &msg);
  if (*sep != '\0')  
    name = luaL_gsub(L, name, sep, dirsep);  
  while ((path = pushnexttemplate(L, path)) != NULL) {
    const char *filename = luaL_gsub(L, lua_tostring(L, -1), LUA_PATH_MARK, name);
    lua_remove(L, -2);  
    if (readable(filename))  
      return filename; 
    lua_pushfstring(L, "\n\tno file " LUA_QS, filename);
    lua_remove(L, -2);  
    luaL_addvalue(&msg);  
  }
  luaL_pushresult(&msg);  
  return NULL;  
}

static int ll_searchpath (lua_State *L) {
  const char *f = searchpath(L, luaL_checkstring(L, 1), luaL_checkstring(L, 2), luaL_optstring(L, 3, "."), luaL_optstring(L, 4, LUA_DIRSEP));
  if (f != NULL) return 1;
  else { 
    lua_pushnil(L);
    lua_insert(L, -2);
    return 2;  
  }
}
static const char *findfile (lua_State *L, const char *name, const char *pname, const char *dirsep) {
  const char *path;
  lua_getfield(L, lua_upvalueindex(1), pname);
  path = lua_tostring(L, -1);
  if (path == NULL)
    luaL_error(L, LUA_QL("package.%s") " must be a string", pname);
  return searchpath(L, name, path, ".", dirsep);
}

static int checkload (lua_State *L, int stat, const char *filename) {
  if (stat) {  
    lua_pushstring(L, filename); 
    return 2;  
  }
  else
    return luaL_error(L, "error loading module " LUA_QS " from file " LUA_QS ":\n\t%s", lua_tostring(L, 1), filename, lua_tostring(L, -1));
}

static int searcher_Lua (lua_State *L) {
  const char *filename;
  const char *name = luaL_checkstring(L, 1);
  filename = findfile(L, name, "path", LUA_LSUBSEP);
  if (filename == NULL) return 1; 
  return checkload(L, (luaL_loadfile(L, filename) == LUA_OK), filename);
}

static int loadfunc (lua_State *L, const char *filename, const char *modname) {
  const char *funcname;
  const char *mark;
  modname = luaL_gsub(L, modname, ".", LUA_OFSEP);
  mark = strchr(modname, *LUA_IGMARK);
  if (mark) {
    int stat;
    funcname = lua_pushlstring(L, modname, mark - modname);
    funcname = lua_pushfstring(L, LUA_POF"%s", funcname);
    stat = ll_loadfunc(L, filename, funcname);
    if (stat != ERRFUNC) return stat;
    modname = mark + 1; 
  }
  funcname = lua_pushfstring(L, LUA_POF"%s", modname);
  return ll_loadfunc(L, filename, funcname);
}

static int searcher_C (lua_State *L) {
  const char *name = luaL_checkstring(L, 1);
  const char *filename = findfile(L, name, "cpath", LUA_CSUBSEP);
  if (filename == NULL) return 1;  
  return checkload(L, (loadfunc(L, filename, name) == 0), filename);
}

static int searcher_Croot (lua_State *L) {
  const char *filename;
  const char *name = luaL_checkstring(L, 1);
  const char *p = strchr(name, '.');
  int stat;
  if (p == NULL) return 0;  
  lua_pushlstring(L, name, p - name);
  filename = findfile(L, lua_tostring(L, -1), "cpath", LUA_CSUBSEP);
  if (filename == NULL) return 1; 
  if ((stat = loadfunc(L, filename, name)) != 0) {
    if (stat != ERRFUNC)
      return checkload(L, 0, filename);  
    else {  
      lua_pushfstring(L, "\n\tno module " LUA_QS " in file " LUA_QS, name, filename);
      return 1;
    }
  }
  lua_pushstring(L, filename);  
  return 2;
}

static int searcher_preload (lua_State *L) {
  const char *name = luaL_checkstring(L, 1);
  lua_getfield(L, LUA_REGISTRYINDEX, "_PRELOAD");
  lua_getfield(L, -1, name);
  if (lua_isnil(L, -1)) 
    lua_pushfstring(L, "\n\tno field package.preload['%s']", name);
  return 1;
}

static void findloader (lua_State *L, const char *name) {
  int i;
  luaL_Buffer msg;  
  luaL_buffinit(L, &msg);
  lua_getfield(L, lua_upvalueindex(1), "searchers");  
  if (!lua_istable(L, 3))
    luaL_error(L, LUA_QL("package.searchers") " must be a table");
  for (i = 1; ; i++) {
    lua_rawgeti(L, 3, i);  
    if (lua_isnil(L, -1)) { 
      lua_pop(L, 1); 
      luaL_pushresult(&msg); 
      luaL_error(L, "module " LUA_QS " not found:%s", name, lua_tostring(L, -1));
    }
    lua_pushstring(L, name);
    lua_call(L, 1, 2);  
    if (lua_isfunction(L, -2))  
      return;  
    else if (lua_isstring(L, -2)) {  
      lua_pop(L, 1); 
      luaL_addvalue(&msg);  
    }
    else
      lua_pop(L, 2);  
  }
}

static int ll_require (lua_State *L) {
  const char *name = luaL_checkstring(L, 1);
  lua_settop(L, 1);  
  lua_getfield(L, LUA_REGISTRYINDEX, "_LOADED");
  lua_getfield(L, 2, name);  
  if (lua_toboolean(L, -1))  
    return 1;  
  lua_pop(L, 1);  
  findloader(L, name);
  lua_pushstring(L, name); 
  lua_insert(L, -2);  
  lua_call(L, 2, 1);  
  if (!lua_isnil(L, -1))  
    lua_setfield(L, 2, name);  
  lua_getfield(L, 2, name);
  if (lua_isnil(L, -1)) {   
    lua_pushboolean(L, 1); 
    lua_pushvalue(L, -1);  
    lua_setfield(L, 2, name); 
  }
  return 1;
}

#if defined(LUA_COMPAT_MODULE)

static void set_env (lua_State *L) {
  lua_Debug ar;
  if (lua_getstack(L, 1, &ar) == 0 || lua_getinfo(L, "f", &ar) == 0 || lua_iscfunction(L, -1))
    luaL_error(L, LUA_QL("module") " not called from a Lua function");
  lua_pushvalue(L, -2);  
  lua_setupvalue(L, -2, 1);
  lua_pop(L, 1);  
}

static void dooptions (lua_State *L, int n) {
  int i;
  for (i = 2; i <= n; i++) {
    if (lua_isfunction(L, i)) { 
      lua_pushvalue(L, i);  
      lua_pushvalue(L, -2);  
      lua_call(L, 1, 0);
    }
  }
}

static void modinit (lua_State *L, const char *modname) {
  const char *dot;
  lua_pushvalue(L, -1);
  lua_setfield(L, -2, "_M");  
  lua_pushstring(L, modname);
  lua_setfield(L, -2, "_NAME");
  dot = strrchr(modname, '.'); 
  if (dot == NULL) dot = modname;
  else dot++;
  lua_pushlstring(L, modname, dot - modname);
  lua_setfield(L, -2, "_PACKAGE");
}

static int ll_module (lua_State *L) {
  const char *modname = luaL_checkstring(L, 1);
  int lastarg = lua_gettop(L);  
  luaL_pushmodule(L, modname, 1);  
  lua_getfield(L, -1, "_NAME");
  if (!lua_isnil(L, -1))  
    lua_pop(L, 1);
  else {  
    lua_pop(L, 1);
    modinit(L, modname);
  }
  lua_pushvalue(L, -1);
  set_env(L);
  dooptions(L, lastarg);
  return 1;
}

static int ll_seeall (lua_State *L) {
  luaL_checktype(L, 1, LUA_TTABLE);
  if (!lua_getmetatable(L, 1)) {
    lua_createtable(L, 0, 1); 
    lua_pushvalue(L, -1);
    lua_setmetatable(L, 1);
  }
  lua_pushglobaltable(L);
  lua_setfield(L, -2, "__index");  
  return 0;
}

#endif
#define AUXMARK		"\1"
static int noenv (lua_State *L) {
  int b;
  lua_getfield(L, LUA_REGISTRYINDEX, "LUA_NOENV");
  b = lua_toboolean(L, -1);
  lua_pop(L, 1); 
  return b;
}

static void setpath (lua_State *L, const char *fieldname, const char *envname1, const char *envname2, const char *def) {
  const char *path = getenv(envname1);
  if (path == NULL)  
    path = getenv(envname2);  
  if (path == NULL || noenv(L))  
    lua_pushstring(L, def);  
  else {
    path = luaL_gsub(L, path, LUA_PATH_SEP LUA_PATH_SEP, LUA_PATH_SEP AUXMARK LUA_PATH_SEP);
    luaL_gsub(L, path, AUXMARK, def);
    lua_remove(L, -2);
  }
  setprogdir(L);
  lua_setfield(L, -2, fieldname);
}

static const luaL_Reg pk_funcs[] = {
  {"loadlib", ll_loadlib},
  {"searchpath", ll_searchpath},
#if defined(LUA_COMPAT_MODULE)
  {"seeall", ll_seeall},
#endif
  {NULL, NULL}
};
static const luaL_Reg ll_funcs[] = {
#if defined(LUA_COMPAT_MODULE)
  {"module", ll_module},
#endif
  {"require", ll_require},
  {NULL, NULL}
};

static void createsearcherstable (lua_State *L) {
  static const lua_CFunction searchers[] =
    {searcher_preload, searcher_Lua, searcher_C, searcher_Croot, NULL};
  int i;
  lua_createtable(L, sizeof(searchers)/sizeof(searchers[0]) - 1, 0);
  for (i=0; searchers[i] != NULL; i++) {
    lua_pushvalue(L, -2); 
    lua_pushcclosure(L, searchers[i], 1);
    lua_rawseti(L, -2, i+1);
  }
}

LUAMOD_API int luaopen_package (lua_State *L) {
  luaL_getsubtable(L, LUA_REGISTRYINDEX, CLIBS);
  lua_createtable(L, 0, 1);  
  lua_pushcfunction(L, gctm);
  lua_setfield(L, -2, "__gc"); 
  lua_setmetatable(L, -2);
  luaL_newlib(L, pk_funcs);
  createsearcherstable(L);
#if defined(LUA_COMPAT_LOADERS)
  lua_pushvalue(L, -1);  
  lua_setfield(L, -3, "loaders"); 
#endif
  lua_setfield(L, -2, "searchers");  
  setpath(L, "path", LUA_PATHVERSION, LUA_PATH, LUA_PATH_DEFAULT);
  setpath(L, "cpath", LUA_CPATHVERSION, LUA_CPATH, LUA_CPATH_DEFAULT);
  lua_pushliteral(L, LUA_DIRSEP "\n" LUA_PATH_SEP "\n" LUA_PATH_MARK "\n" LUA_EXEC_DIR "\n" LUA_IGMARK "\n");
  lua_setfield(L, -2, "config");
  luaL_getsubtable(L, LUA_REGISTRYINDEX, "_LOADED");
  lua_setfield(L, -2, "loaded");
  luaL_getsubtable(L, LUA_REGISTRYINDEX, "_PRELOAD");
  lua_setfield(L, -2, "preload");
  lua_pushglobaltable(L);
  lua_pushvalue(L, -2);  
  luaL_setfuncs(L, ll_funcs, 1);  
  lua_pop(L, 1);
  return 1; 
}
