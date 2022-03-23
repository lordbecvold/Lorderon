#ifndef lundump_h
#define lundump_h
#include "lobject.h"
#include "lzio.h"

LUAI_FUNC Closure* luaU_undump (lua_State* L, ZIO* Z, Mbuffer* buff, const char* name);
LUAI_FUNC void luaU_header (lu_byte* h);
LUAI_FUNC int luaU_dump (lua_State* L, const Proto* f, lua_Writer w, void* data, int strip);
#define LUAC_TAIL "\x19\x93\r\n\x1a\n"
#define LUAC_HEADERSIZE (sizeof(LUA_SIGNATURE)-sizeof(char)+2+6+sizeof(LUAC_TAIL)-sizeof(char))
#endif
