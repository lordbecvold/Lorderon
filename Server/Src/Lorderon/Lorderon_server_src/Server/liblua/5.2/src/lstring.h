#ifndef lstring_h
#define lstring_h
#include "lgc.h"
#include "lobject.h"
#include "lstate.h"
#define sizestring(s) (sizeof(union TString)+((s)->len+1)*sizeof(char))
#define sizeudata(u) (sizeof(union Udata)+(u)->len)
#define luaS_newliteral(L, s) (luaS_newlstr(L, "" s, \ (sizeof(s)/sizeof(char))-1))
#define luaS_fix(s)	l_setbit((s)->tsv.marked, FIXEDBIT)
#define isreserved(s) ((s)->tsv.tt == LUA_TSHRSTR && (s)->tsv.extra > 0)
#define eqshrstr(a,b) check_exp((a)->tsv.tt == LUA_TSHRSTR, (a) == (b))
LUAI_FUNC unsigned int luaS_hash (const char *str, size_t l, unsigned int seed);
LUAI_FUNC int luaS_eqlngstr (TString *a, TString *b);
LUAI_FUNC int luaS_eqstr (TString *a, TString *b);
LUAI_FUNC void luaS_resize (lua_State *L, int newsize);
LUAI_FUNC Udata *luaS_newudata (lua_State *L, size_t s, Table *e);
LUAI_FUNC TString *luaS_newlstr (lua_State *L, const char *str, size_t l);
LUAI_FUNC TString *luaS_new (lua_State *L, const char *str);
#endif
