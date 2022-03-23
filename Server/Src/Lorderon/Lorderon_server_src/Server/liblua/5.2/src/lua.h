#ifndef lua_h
#define lua_h
#include <stdarg.h>
#include <stddef.h>
#include "luaconf.h"
#define LUA_V 523
#define LUA_VERSION_MAJOR	"5"
#define LUA_VERSION_MINOR	"2"
#define LUA_VERSION_NUM		502
#define LUA_VERSION_RELEASE	"3"
#define LUA_VERSION	"Lua " LUA_VERSION_MAJOR "." LUA_VERSION_MINOR
#define LUA_RELEASE	LUA_VERSION "." LUA_VERSION_RELEASE
#define LUA_COPYRIGHT	LUA_RELEASE "  Copyright (C) 1994-2013 Lua.org, PUC-Rio"
#define LUA_AUTHORS	"R. Ierusalimschy, L. H. de Figueiredo, W. Celes"
#define LUA_SIGNATURE	"\033Lua"
#define LUA_MULTRET	(-1)
#define LUA_REGISTRYINDEX	LUAI_FIRSTPSEUDOIDX
#define lua_upvalueindex(i)	(LUA_REGISTRYINDEX - (i))
#define LUA_OK 0
#define LUA_YIELD	1
#define LUA_ERRRUN 2
#define LUA_ERRSYNTAX	3
#define LUA_ERRMEM 4
#define LUA_ERRGCMM 5
#define LUA_ERRERR 6
typedef struct lua_State lua_State;
typedef int (*lua_CFunction) (lua_State *L);
typedef const char * (*lua_Reader) (lua_State *L, void *ud, size_t *sz);
typedef int (*lua_Writer) (lua_State *L, const void* p, size_t sz, void* ud);
typedef void * (*lua_Alloc) (void *ud, void *ptr, size_t osize, size_t nsize);
#define LUA_TNONE (-1)
#define LUA_TNIL 0
#define LUA_TBOOLEAN 1
#define LUA_TLIGHTUSERDATA	2
#define LUA_TNUMBER 3
#define LUA_TSTRING 4
#define LUA_TTABLE 5
#define LUA_TFUNCTION 6
#define LUA_TUSERDATA 7
#define LUA_TTHREAD 8
#define LUA_NUMTAGS 9
#define LUA_MINSTACK 20
#define LUA_RIDX_MAINTHREAD	1
#define LUA_RIDX_GLOBALS 2
#define LUA_RIDX_LAST LUA_RIDX_GLOBALS
typedef LUA_NUMBER lua_Number;
typedef LUA_INTEGER lua_Integer;
typedef LUA_UNSIGNED lua_Unsigned;
#if defined(LUA_USER_H)
#include LUA_USER_H
#endif
extern const char lua_ident[];
LUA_API lua_State *(lua_newstate) (lua_Alloc f, void *ud);
LUA_API void (lua_close) (lua_State *L);
LUA_API lua_State *(lua_newthread) (lua_State *L);
LUA_API lua_CFunction (lua_atpanic) (lua_State *L, lua_CFunction panicf);
LUA_API const lua_Number *(lua_version) (lua_State *L);
LUA_API int (lua_absindex) (lua_State *L, int idx);
LUA_API int (lua_gettop) (lua_State *L);
LUA_API void (lua_settop) (lua_State *L, int idx);
LUA_API void (lua_pushvalue) (lua_State *L, int idx);
LUA_API void (lua_remove) (lua_State *L, int idx);
LUA_API void (lua_insert) (lua_State *L, int idx);
LUA_API void (lua_replace) (lua_State *L, int idx);
LUA_API void (lua_copy) (lua_State *L, int fromidx, int toidx);
LUA_API int (lua_checkstack) (lua_State *L, int sz);
LUA_API void (lua_xmove) (lua_State *from, lua_State *to, int n);
LUA_API int (lua_isnumber) (lua_State *L, int idx);
LUA_API int (lua_isstring) (lua_State *L, int idx);
LUA_API int (lua_iscfunction) (lua_State *L, int idx);
LUA_API int (lua_isuserdata) (lua_State *L, int idx);
LUA_API int (lua_type) (lua_State *L, int idx);
LUA_API const char *(lua_typename) (lua_State *L, int tp);
LUA_API lua_Number (lua_tonumberx) (lua_State *L, int idx, int *isnum);
LUA_API lua_Integer (lua_tointegerx) (lua_State *L, int idx, int *isnum);
LUA_API lua_Unsigned (lua_tounsignedx) (lua_State *L, int idx, int *isnum);
LUA_API int (lua_toboolean) (lua_State *L, int idx);
LUA_API const char *(lua_tolstring) (lua_State *L, int idx, size_t *len);
LUA_API size_t (lua_rawlen) (lua_State *L, int idx);
LUA_API lua_CFunction (lua_tocfunction) (lua_State *L, int idx);
LUA_API void *(lua_touserdata) (lua_State *L, int idx);
LUA_API lua_State *(lua_tothread) (lua_State *L, int idx);
LUA_API const void *(lua_topointer) (lua_State *L, int idx);
#define LUA_OPADD	0
#define LUA_OPSUB	1
#define LUA_OPMUL	2
#define LUA_OPDIV	3
#define LUA_OPMOD	4
#define LUA_OPPOW	5
#define LUA_OPUNM	6
LUA_API void (lua_arith) (lua_State *L, int op);
#define LUA_OPEQ	0
#define LUA_OPLT	1
#define LUA_OPLE	2
LUA_API int (lua_rawequal) (lua_State *L, int idx1, int idx2);
LUA_API int (lua_compare) (lua_State *L, int idx1, int idx2, int op);
LUA_API void (lua_pushnil) (lua_State *L);
LUA_API void (lua_pushnumber) (lua_State *L, lua_Number n);
LUA_API void (lua_pushinteger) (lua_State *L, lua_Integer n);
LUA_API void (lua_pushunsigned) (lua_State *L, lua_Unsigned n);
LUA_API const char *(lua_pushlstring) (lua_State *L, const char *s, size_t l);
LUA_API const char *(lua_pushstring) (lua_State *L, const char *s);
LUA_API const char *(lua_pushvfstring) (lua_State *L, const char *fmt, va_list argp);
LUA_API const char *(lua_pushfstring) (lua_State *L, const char *fmt, ...);
LUA_API void (lua_pushcclosure) (lua_State *L, lua_CFunction fn, int n);
LUA_API void (lua_pushboolean) (lua_State *L, int b);
LUA_API void (lua_pushlightuserdata) (lua_State *L, void *p);
LUA_API int (lua_pushthread) (lua_State *L);
LUA_API void (lua_getglobal) (lua_State *L, const char *var);
LUA_API void (lua_gettable) (lua_State *L, int idx);
LUA_API void (lua_getfield) (lua_State *L, int idx, const char *k);
LUA_API void (lua_rawget) (lua_State *L, int idx);
LUA_API void (lua_rawgeti) (lua_State *L, int idx, int n);
LUA_API void (lua_rawgetp) (lua_State *L, int idx, const void *p);
LUA_API void (lua_createtable) (lua_State *L, int narr, int nrec);
LUA_API void *(lua_newuserdata) (lua_State *L, size_t sz);
LUA_API int (lua_getmetatable) (lua_State *L, int objindex);
LUA_API void (lua_getuservalue) (lua_State *L, int idx);
LUA_API void (lua_setglobal) (lua_State *L, const char *var);
LUA_API void (lua_settable) (lua_State *L, int idx);
LUA_API void (lua_setfield) (lua_State *L, int idx, const char *k);
LUA_API void (lua_rawset) (lua_State *L, int idx);
LUA_API void (lua_rawseti) (lua_State *L, int idx, int n);
LUA_API void (lua_rawsetp) (lua_State *L, int idx, const void *p);
LUA_API int (lua_setmetatable) (lua_State *L, int objindex);
LUA_API void (lua_setuservalue) (lua_State *L, int idx);
LUA_API void (lua_callk) (lua_State *L, int nargs, int nresults, int ctx, lua_CFunction k);
#define lua_call(L,n,r) lua_callk(L, (n), (r), 0, NULL)
LUA_API int (lua_getctx) (lua_State *L, int *ctx);
LUA_API int (lua_pcallk) (lua_State *L, int nargs, int nresults, int errfunc, int ctx, lua_CFunction k);
#define lua_pcall(L,n,r,f)	lua_pcallk(L, (n), (r), (f), 0, NULL)
LUA_API int (lua_load) (lua_State *L, lua_Reader reader, void *dt, const char *chunkname, const char *mode);
LUA_API int (lua_dump) (lua_State *L, lua_Writer writer, void *data);
LUA_API int (lua_yieldk) (lua_State *L, int nresults, int ctx, lua_CFunction k);
#define lua_yield(L,n) lua_yieldk(L, (n), 0, NULL)
LUA_API int (lua_resume) (lua_State *L, lua_State *from, int narg);
LUA_API int (lua_status) (lua_State *L);
#define LUA_GCSTOP 0
#define LUA_GCRESTART 1
#define LUA_GCCOLLECT 2
#define LUA_GCCOUNT 3
#define LUA_GCCOUNTB 4
#define LUA_GCSTEP 5
#define LUA_GCSETPAUSE 6
#define LUA_GCSETSTEPMUL 7
#define LUA_GCSETMAJORINC	8
#define LUA_GCISRUNNING 9
#define LUA_GCGEN 10
#define LUA_GCINC 11
LUA_API int (lua_gc) (lua_State *L, int what, int data);
LUA_API int (lua_error) (lua_State *L);
LUA_API int (lua_next) (lua_State *L, int idx);
LUA_API void (lua_concat) (lua_State *L, int n);
LUA_API void (lua_len) (lua_State *L, int idx);
LUA_API lua_Alloc (lua_getallocf) (lua_State *L, void **ud);
LUA_API void (lua_setallocf) (lua_State *L, lua_Alloc f, void *ud);
#define lua_tonumber(L,i)	lua_tonumberx(L,i,NULL)
#define lua_tointeger(L,i) lua_tointegerx(L,i,NULL)
#define lua_tounsigned(L,i)	lua_tounsignedx(L,i,NULL)
#define lua_pop(L,n) lua_settop(L, -(n)-1)
#define lua_newtable(L) lua_createtable(L, 0, 0)
#define lua_register(L,n,f) (lua_pushcfunction(L, (f)), lua_setglobal(L, (n)))
#define lua_pushcfunction(L,f) lua_pushcclosure(L, (f), 0)
#define lua_isfunction(L,n) (lua_type(L, (n)) == LUA_TFUNCTION)
#define lua_istable(L,n) (lua_type(L, (n)) == LUA_TTABLE)
#define lua_islightuserdata(L,n) (lua_type(L, (n)) == LUA_TLIGHTUSERDATA)
#define lua_isnil(L,n) (lua_type(L, (n)) == LUA_TNIL)
#define lua_isboolean(L,n) (lua_type(L, (n)) == LUA_TBOOLEAN)
#define lua_isthread(L,n)	(lua_type(L, (n)) == LUA_TTHREAD)
#define lua_isnone(L,n) (lua_type(L, (n)) == LUA_TNONE)
#define lua_isnoneornil(L, n)	(lua_type(L, (n)) <= 0)
#define lua_pushliteral(L, s)	\ lua_pushlstring(L, "" s, (sizeof(s)/sizeof(char))-1)
#define lua_pushglobaltable(L) \ lua_rawgeti(L, LUA_REGISTRYINDEX, LUA_RIDX_GLOBALS)
#define lua_tostring(L,i)	lua_tolstring(L, (i), NULL)
#define LUA_HOOKCALL 0
#define LUA_HOOKRET	1
#define LUA_HOOKLINE 2
#define LUA_HOOKCOUNT 3
#define LUA_HOOKTAILCALL 4
#define LUA_MASKCALL (1 << LUA_HOOKCALL)
#define LUA_MASKRET	(1 << LUA_HOOKRET)
#define LUA_MASKLINE (1 << LUA_HOOKLINE)
#define LUA_MASKCOUNT	(1 << LUA_HOOKCOUNT)
typedef struct lua_Debug lua_Debug; 
typedef void (*lua_Hook) (lua_State *L, lua_Debug *ar);
LUA_API int (lua_getstack) (lua_State *L, int level, lua_Debug *ar);
LUA_API int (lua_getinfo) (lua_State *L, const char *what, lua_Debug *ar);
LUA_API const char *(lua_getlocal) (lua_State *L, const lua_Debug *ar, int n);
LUA_API const char *(lua_setlocal) (lua_State *L, const lua_Debug *ar, int n);
LUA_API const char *(lua_getupvalue) (lua_State *L, int funcindex, int n);
LUA_API const char *(lua_setupvalue) (lua_State *L, int funcindex, int n);
LUA_API void *(lua_upvalueid) (lua_State *L, int fidx, int n);
LUA_API void  (lua_upvaluejoin) (lua_State *L, int fidx1, int n1, int fidx2, int n2);
LUA_API int (lua_sethook) (lua_State *L, lua_Hook func, int mask, int count);
LUA_API lua_Hook (lua_gethook) (lua_State *L);
LUA_API int (lua_gethookmask) (lua_State *L);
LUA_API int (lua_gethookcount) (lua_State *L);

struct lua_Debug {
  int event;
  const char *name;	
  const char *namewhat;	
  const char *what;	
  const char *source;	
  int currentline;	
  int linedefined;	
  int lastlinedefined;	
  unsigned char nups;	
  unsigned char nparams;
  char isvararg;        
  char istailcall;	
  char short_src[LUA_IDSIZE]
  struct CallInfo *i_ci;  
};
#endif
