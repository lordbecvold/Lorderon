#define lopcodes_c
#define LUA_CORE
#include "lopcodes.h"

LUAI_DDEF const char *const luaP_opnames[NUM_OPCODES+1] = {
  "MOVE",
  "LOADK",
  "LOADKX",
  "LOADBOOL",
  "LOADNIL",
  "GETUPVAL",
  "GETTABUP",
  "GETTABLE",
  "SETTABUP",
  "SETUPVAL",
  "SETTABLE",
  "NEWTABLE",
  "SELF",
  "ADD",
  "SUB",
  "MUL",
  "DIV",
  "MOD",
  "POW",
  "UNM",
  "NOT",
  "LEN",
  "CONCAT",
  "JMP",
  "EQ",
  "LT",
  "LE",
  "TEST",
  "TESTSET",
  "CALL",
  "TAILCALL",
  "RETURN",
  "FORLOOP",
  "FORPREP",
  "TFORCALL",
  "TFORLOOP",
  "SETLIST",
  "CLOSURE",
  "VARARG",
  "EXTRAARG",
  NULL
};

#define opmode(t,a,b,c,m) (((t)<<7) | ((a)<<6) | ((b)<<4) | ((c)<<2) | (m))
LUAI_DDEF const lu_byte luaP_opmodes[NUM_OPCODES] = {
  opmode(0, 1, OpArgR, OpArgN, iABC)		
 ,opmode(0, 1, OpArgK, OpArgN, iABx)		
 ,opmode(0, 1, OpArgN, OpArgN, iABx)		
 ,opmode(0, 1, OpArgU, OpArgU, iABC)		
 ,opmode(0, 1, OpArgU, OpArgN, iABC)	
 ,opmode(0, 1, OpArgU, OpArgN, iABC)		
 ,opmode(0, 1, OpArgU, OpArgK, iABC)		
 ,opmode(0, 1, OpArgR, OpArgK, iABC)		
 ,opmode(0, 0, OpArgK, OpArgK, iABC)		
 ,opmode(0, 0, OpArgU, OpArgN, iABC)		
 ,opmode(0, 0, OpArgK, OpArgK, iABC)	
 ,opmode(0, 1, OpArgU, OpArgU, iABC)	
 ,opmode(0, 1, OpArgR, OpArgK, iABC)		
 ,opmode(0, 1, OpArgK, OpArgK, iABC)		
 ,opmode(0, 1, OpArgK, OpArgK, iABC)	
 ,opmode(0, 1, OpArgK, OpArgK, iABC)		
 ,opmode(0, 1, OpArgK, OpArgK, iABC)		
 ,opmode(0, 1, OpArgK, OpArgK, iABC)		
 ,opmode(0, 1, OpArgK, OpArgK, iABC)	
 ,opmode(0, 1, OpArgR, OpArgN, iABC)		
 ,opmode(0, 1, OpArgR, OpArgN, iABC)		
 ,opmode(0, 1, OpArgR, OpArgN, iABC)	
 ,opmode(0, 1, OpArgR, OpArgR, iABC)	
 ,opmode(0, 0, OpArgR, OpArgN, iAsBx)	
 ,opmode(1, 0, OpArgK, OpArgK, iABC)		
 ,opmode(1, 0, OpArgK, OpArgK, iABC)		
 ,opmode(1, 0, OpArgK, OpArgK, iABC)		
 ,opmode(1, 0, OpArgN, OpArgU, iABC)	
 ,opmode(1, 1, OpArgR, OpArgU, iABC)	
 ,opmode(0, 1, OpArgU, OpArgU, iABC)
 ,opmode(0, 1, OpArgU, OpArgU, iABC)		
 ,opmode(0, 0, OpArgU, OpArgN, iABC)	
 ,opmode(0, 1, OpArgR, OpArgN, iAsBx)	
 ,opmode(0, 1, OpArgR, OpArgN, iAsBx)
 ,opmode(0, 0, OpArgN, OpArgU, iABC)		
 ,opmode(0, 1, OpArgR, OpArgN, iAsBx)		
 ,opmode(0, 0, OpArgU, OpArgU, iABC)		
 ,opmode(0, 1, OpArgU, OpArgN, iABx)	
 ,opmode(0, 1, OpArgU, OpArgN, iABC)	
 ,opmode(0, 0, OpArgU, OpArgU, iAx)	
};
