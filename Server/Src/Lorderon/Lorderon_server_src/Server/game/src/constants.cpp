//Lorderon server core Dev by Lordbecvold
#include "stdafx.h"
#include "char.h"
#include "../../common/CommonDefines.h"
TJobInitialPoints JobInitialPoints[JOB_MAX_NUM] =
{
	{   6,  4,  3,  3,  600,   200,     40,    20,    36, 44,     18, 22,     800,      5,      1, 3  }, 
	{   4,  3,  6,  3,  650,   200,     40,    20,    36, 44,     18, 22,     800,      5,      1, 3  }, 
	{   5,  3,  3,  5,  650,   200,     40,    20,    36, 44,     18, 22,     800,      5,      1, 3  }, 
	{   3,  4,  3,  6,  700,   200,     40,    20,    36, 44,     18, 22,     800,      5,      1, 3  },  
#ifdef ENABLE_WOLFMAN_CHARACTER
	{   2,  6,  6,  2,  600,   200,     40,    20,    36, 44,     18, 22,     800,      5,      1, 3  }, 
#endif
};

const TMobRankStat MobRankStats[MOB_RANK_MAX_NUM] =
{
	{  20,  },
	{  20,  },
	{  25,  }, 
	{  30,  },
	{  50,  }, 
	{ 100,  }  
};

TBattleTypeStat BattleTypeStats[BATTLE_TYPE_MAX_NUM] =

{
	{	  0,	  0,	  0,	-10	}, 
	{	 10,	-20,	-10,	-15	}, 
	{	 -5,	 -5,	 10,	 10	}, 
	{	  0,	  0,	  0,	  0	}, 
	{	 10,	-10,	  0,	-15	}, 
	{	-10,	 10,	-10,	  0	}, 
	{	 20,	-20,	  0,	-10	}, 
	{	-20,	 20,	-10,	  0	}, 
};

const DWORD * exp_table = NULL;

const DWORD exp_table_common[PLAYER_MAX_LEVEL_CONST + 1] =
{
	0,	
	300,
	800,
	1500,
	2500,
	4300,
	7200,
	11000,
	17000,
	24000,
	33000,	
	43000,
	58000,
	76000,
	100000,
	130000,
	169000,
	219000,
	283000,
	365000,
	472000,	
	610000,
	705000,
	813000,
	937000,
	1077000,
	1237000,
	1418000,
	1624000,
	1857000,
	2122000,	
	2421000,
	2761000,
	3145000,
	3580000,
	4073000,
	4632000,
	5194000,
	5717000,
	6264000,
	6837000,	
	7600000,
	8274000,
	8990000,
	9753000,
	10560000,
	11410000,
	12320000,
	13270000,
	14280000,
	15340000,	
	16870000,
	18960000,
	19980000,
	21420000,
	22930000,
	24530000,
	26200000,
	27960000,
	29800000,
	32780000,	
	36060000,
	39670000,
	43640000,
	48000000,
	52800000,
	58080000,
	63890000,
	70280000,
	77310000,
	85040000,	
	93540000,
	102900000,
	113200000,
	124500000,
	137000000,
	150700000,
	165700000,
	236990000,
	260650000,
	286780000,	
	315380000,
	346970000,
	381680000,
	419770000,
	461760000,
	508040000,
	558740000,
	614640000,
	676130000,
	743730000,	
	1041222000,
	1145344200,
	1259878620,
	1385866482,
	1524453130,
	1676898443,
	1844588288,
	2029047116,
	2050000000,	
	2150000000u,	
	2210000000u,
	2250000000u,
	2280000000u,
	2310000000u,
	2330000000u,	
	2350000000u,
	2370000000u,
	2390000000u,
	2400000000u,
	2410000000u,	
	2420000000u,
	2430000000u,
	2440000000u,
	2450000000u,
	2460000000u,	
	2470000000u,
	2480000000u,
	2490000000u,
	2490000000u,
	2500000000u,	
	2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u, 
	2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,
	2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u, 
	2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u, 
	2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u, 
	2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u, 
	2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u, 
	2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u, 
	2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,
	2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u, 
	2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u, 
	2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,
	2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u,2500000000u, 
};

const int * aiPercentByDeltaLev = NULL;
const int * aiPercentByDeltaLevForBoss = NULL;
const int aiPercentByDeltaLevForBoss_euckr[MAX_EXP_DELTA_OF_LEV] =
{
	1,      
	3,          
	5,          
	7,          
	15,         
	30,         
	60,         
	90,      
	91,       
	92,       
	93,     
	94,    
	95,      
	97,    
	99,         
	100,      
	105,     
	110,     
	115,      
	120,        
	125,      
	130,      
	135,     
	140,        
	145,        
	150,      
	155,        
	160,       
	165,        
	170,        
	180       
};

const int aiPercentByDeltaLev_euckr[MAX_EXP_DELTA_OF_LEV] =
{
	1,  
	5,  
	10, 
	20, 
	30, 
	50, 
	70, 
	80, 
	85, 
	90, 
	92, 
	94, 
	96, 
	98, 
	100,    
	100,    
	105,    
	110,   
	115,    
	120,   
	125,    
	130,    
	135,   
	140,   
	145,    
	150,   
	155,    
	160,    
	165,    
	170,    
	180,    
};

const DWORD party_exp_distribute_table[PLAYER_EXP_TABLE_MAX + 1] =
{
	0,
	10,		10,		10,		10,		15,		15,		20,		25,		30,		40,		
	50,		60,		80,		100,	120,	140,	160,	184,	210,	240,	
	270,	300,	330,	360,	390,	420,	450,	480,	510,	550,	
	600,	640,	700,	760,	820,	880,	940,	1000,	1100,	1180,	
	1260,	1320,	1380,	1440,	1500,	1560,	1620,	1680,	1740,	1800,	
	1860,	1920,	2000,	2100,	2200,	2300,	2450,	2600,	2750,	2900,	
	3050,	3200,	3350,	3500,	3650,	3800,	3950,	4100,	4250,	4400,	
	4600,	4800,	5000,	5200,	5400,	5600,	5800,	6000,	6200,	6400,	
	6600,	6900,	7100,	7300,	7600,	7800,	8000,	8300,	8500,	8800,	
	9000,	9000,	9000,	9000,	9000,	9000,	9000,	9000,	9000,	9000,	
	10000,	10000,	10000,	10000,	10000,	10000,	10000,	10000,	10000,	10000,	
	12000,	12000,	12000,	12000,	12000,	12000,	12000,	12000,	12000,	12000,	
};

Coord aArroundCoords[ARROUND_COORD_MAX_NUM] =
{
	{	     0,	      0	    },
	{        0,      50     },
	{       35,     35      },
	{       50,     -0      },
	{       35,     -35     },
	{       0,      -50     },
	{       -35,    -35     },
	{       -50,    0       },
	{       -35,    35      },
	{       0,      100     },
	{       71,     71      },
	{       100,    -0      },
	{       71,     -71     },
	{       0,      -100    },
	{       -71,    -71     },
	{       -100,   0       },
	{       -71,    71      },
	{       0,      150     },
	{       106,    106     },
	{       150,    -0      },
	{       106,    -106    },
	{       0,      -150    },
	{       -106,   -106    },
	{       -150,   0       },
	{       -106,   106     },
	{       0,      200     },
	{       141,    141     },
	{       200,    -0      },
	{       141,    -141    },
	{       0,      -200    },
	{       -141,   -141    },
	{       -200,   0       },
	{       -141,   141     },
	{       0,      250     },
	{       177,    177     },
	{       250,    -0      },
	{       177,    -177    },
	{       0,      -250    },
	{       -177,   -177    },
	{       -250,   0       },
	{       -177,   177     },
	{       0,      300     },
	{       212,    212     },
	{       300,    -0      },
	{       212,    -212    },
	{       0,      -300    },
	{       -212,   -212    },
	{       -300,   0       },
	{       -212,   212     },
	{       0,      350     },
	{       247,    247     },
	{       350,    -0      },
	{       247,    -247    },
	{       0,      -350    },
	{       -247,   -247    },
	{       -350,   0       },
	{       -247,   247     },
	{       0,      400     },
	{       283,    283     },
	{       400,    -0      },
	{       283,    -283    },
	{       0,      -400    },
	{       -283,   -283    },
	{       -400,   0       },
	{       -283,   283     },
	{       0,      450     },
	{       318,    318     },
	{       450,    -0      },
	{       318,    -318    },
	{       0,      -450    },
	{       -318,   -318    },
	{       -450,   0       },
	{       -318,   318     },
	{       0,      500     },
	{       354,    354     },
	{       500,    -0      },
	{       354,    -354    },
	{       0,      -500    },
	{       -354,   -354    },
	{       -500,   0       },
	{       -354,   354     },
	{       0,      550     },
	{       389,    389     },
	{       550,    -0      },
	{       389,    -389    },
	{       0,      -550    },
	{       -389,   -389    },
	{       -550,   0       },
	{       -389,   389     },
	{       0,      600     },
	{       424,    424     },
	{       600,    -0      },
	{       424,    -424    },
	{       0,      -600    },
	{       -424,   -424    },
	{       -600,   0       },
	{       -424,   424     },
	{       0,      650     },
	{       460,    460     },
	{       650,    -0      },
	{       460,    -460    },
	{       0,      -650    },
	{       -460,   -460    },
	{       -650,   0       },
	{       -460,   460     },
	{       0,      700     },
	{       495,    495     },
	{       700,    -0      },
	{       495,    -495    },
	{       0,      -700    },
	{       -495,   -495    },
	{       -700,   0       },
	{       -495,   495     },
	{       0,      750     },
	{       530,    530     },
	{       750,    -0      },
	{       530,    -530    },
	{       0,      -750    },
	{       -530,   -530    },
	{       -750,   0       },
	{       -530,   530     },
	{       0,      800     },
	{       566,    566     },
	{       800,    -0      },
	{       566,    -566    },
	{       0,      -800    },
	{       -566,   -566    },
	{       -800,   0       },
	{       -566,   566     },
	{       0,      850     },
	{       601,    601     },
	{       850,    -0      },
	{       601,    -601    },
	{       0,      -850    },
	{       -601,   -601    },
	{       -850,   0       },
	{       -601,   601     },
	{       0,      900     },
	{       636,    636     },
	{       900,    -0      },
	{       636,    -636    },
	{       0,      -900    },
	{       -636,   -636    },
	{       -900,   0       },
	{       -636,   636     },
	{       0,      950     },
	{       672,    672     },
	{       950,    -0      },
	{       672,    -672    },
	{       0,      -950    },
	{       -672,   -672    },
	{       -950,   0       },
	{       -672,   672     },
	{       0,      1000    },
	{       707,    707     },
	{       1000,   -0      },
	{       707,    -707    },
	{       0,      -1000   },
	{       -707,   -707    },
	{       -1000,  0       },
	{       -707,   707     },
};

const DWORD guild_exp_table[GUILD_MAX_LEVEL+1] =
{
	0,
	15000UL,
	45000UL,
	90000UL,
	160000UL,
	235000UL,
	325000UL,
	430000UL,
	550000UL,
	685000UL,
	835000UL,
	1000000UL,
	1500000UL,
	2100000UL,
	2800000UL,
	3600000UL,
	4500000UL,
	6500000UL,
	8000000UL,
	10000000UL,
	42000000UL
};

const DWORD guild_exp_table2[GUILD_MAX_LEVEL+1] =
{
	0,
	6000UL,
	18000UL,
	36000UL,
	64000UL,
	94000UL,
	130000UL,
	172000UL,
	220000UL,
	274000UL,
	334000UL,
	400000UL,
	600000UL,
	840000UL,
	1120000UL,
	1440000UL,
	1800000UL,
	2600000UL,
	3200000UL,
	4000000UL,
	16800000UL
};

const int aiMobEnchantApplyIdx[MOB_ENCHANTS_MAX_NUM] =
{
	APPLY_CURSE_PCT,
	APPLY_SLOW_PCT,
	APPLY_POISON_PCT,
	APPLY_STUN_PCT,
	APPLY_CRITICAL_PCT,
	APPLY_PENETRATE_PCT,
#if defined(ENABLE_WOLFMAN_CHARACTER) && !defined(USE_MOB_BLEEDING_AS_POISON)
	APPLY_BLEEDING_PCT,
#endif
};
const int aiMobResistsApplyIdx[MOB_RESISTS_MAX_NUM] =
{
	APPLY_RESIST_SWORD,
	APPLY_RESIST_TWOHAND,
	APPLY_RESIST_DAGGER,
	APPLY_RESIST_BELL,
	APPLY_RESIST_FAN,
	APPLY_RESIST_BOW,
	APPLY_RESIST_FIRE,
	APPLY_RESIST_ELEC,
	APPLY_RESIST_MAGIC,
	APPLY_RESIST_WIND,
	APPLY_POISON_REDUCE,
#if defined(ENABLE_WOLFMAN_CHARACTER) && !defined(USE_MOB_CLAW_AS_DAGGER)
	APPLY_RESIST_CLAW,
#endif
#if defined(ENABLE_WOLFMAN_CHARACTER) && !defined(USE_MOB_BLEEDING_AS_POISON)
	APPLY_BLEEDING_REDUCE,
#endif
};

const int aiSocketPercentByQty[5][4] =
{
	{  0,  0,  0,  0 },
	{  3,  0,  0,  0 },
	{ 10,  1,  0,  0 },
	{ 15, 10,  1,  0 },
	{ 20, 15, 10,  1 }
};

const int aiWeaponSocketQty[WEAPON_NUM_TYPES] =
{
	3, 
	3, 
	3, 
	3, 
	3, 
	3, 
	0, 
	0, 
#ifdef ENABLE_WOLFMAN_CHARACTER
	3, 
#endif
};

const int aiArmorSocketQty[ARMOR_NUM_TYPES] =
{
	3, 
	1, 
	1, 
	0, 
	0, 
	0  
};

TItemAttrMap g_map_itemAttr;
TItemAttrMap g_map_itemRare;

const TApplyInfo aApplyInfo[MAX_APPLY_NUM] =
{
	{ POINT_NONE,			},   
	{ POINT_MAX_HP,		        },   
	{ POINT_MAX_SP,		        },   
	{ POINT_HT,			        },   
	{ POINT_IQ,			        },   
	{ POINT_ST,			        },   
	{ POINT_DX,			        },   
	{ POINT_ATT_SPEED,		        },   
	{ POINT_MOV_SPEED,		        },   
	{ POINT_CASTING_SPEED,	        },  
	{ POINT_HP_REGEN,			},   
	{ POINT_SP_REGEN,			},   
	{ POINT_POISON_PCT,		        },   
	{ POINT_STUN_PCT,		        },   
	{ POINT_SLOW_PCT,		        },   
	{ POINT_CRITICAL_PCT,		},   
	{ POINT_PENETRATE_PCT,	        },   
	{ POINT_ATTBONUS_HUMAN,	        },   
	{ POINT_ATTBONUS_ANIMAL,	        },   
	{ POINT_ATTBONUS_ORC,		},   
	{ POINT_ATTBONUS_MILGYO,	        },   
	{ POINT_ATTBONUS_UNDEAD,	        },   
	{ POINT_ATTBONUS_DEVIL,	        },   
	{ POINT_STEAL_HP,		        },   
	{ POINT_STEAL_SP,		        },  
	{ POINT_MANA_BURN_PCT,	        },   
	{ POINT_DAMAGE_SP_RECOVER,	        },   
	{ POINT_BLOCK,		        },   
	{ POINT_DODGE,		        },   
	{ POINT_RESIST_SWORD,		},  
	{ POINT_RESIST_TWOHAND,	        },   
	{ POINT_RESIST_DAGGER,	        },  
	{ POINT_RESIST_BELL,		},   
	{ POINT_RESIST_FAN,		        },  
	{ POINT_RESIST_BOW,		        },   
	{ POINT_RESIST_FIRE,		}, 
	{ POINT_RESIST_ELEC,		},   
	{ POINT_RESIST_MAGIC,		},  
	{ POINT_RESIST_WIND,		},   
	{ POINT_REFLECT_MELEE,	        },  
	{ POINT_REFLECT_CURSE,	        },   
	{ POINT_POISON_REDUCE,	        },   
	{ POINT_KILL_SP_RECOVER,	        },   
	{ POINT_EXP_DOUBLE_BONUS,	        }, 
	{ POINT_GOLD_DOUBLE_BONUS,	        },   
	{ POINT_ITEM_DROP_BONUS,	        },   
	{ POINT_POTION_BONUS,		},   
	{ POINT_KILL_HP_RECOVERY,	        }, 
	{ POINT_IMMUNE_STUN,		},   
	{ POINT_IMMUNE_SLOW,		},   
	{ POINT_IMMUNE_FALL,		},   
	{ POINT_NONE,			},   
	{ POINT_BOW_DISTANCE,		},   
	{ POINT_ATT_GRADE_BONUS,	        },  
	{ POINT_DEF_GRADE_BONUS,	        }, 
	{ POINT_MAGIC_ATT_GRADE_BONUS,      },   
	{ POINT_MAGIC_DEF_GRADE_BONUS,      }, 
	{ POINT_CURSE_PCT,			},   
	{ POINT_MAX_STAMINA			},   
	{ POINT_ATTBONUS_WARRIOR		},   
	{ POINT_ATTBONUS_ASSASSIN		},   
	{ POINT_ATTBONUS_SURA		},   
	{ POINT_ATTBONUS_SHAMAN		},   
	{ POINT_ATTBONUS_MONSTER		},   
	{ POINT_ATT_BONUS		},   
	{ POINT_MALL_DEFBONUS		},   
	{ POINT_MALL_EXPBONUS		},   
	{ POINT_MALL_ITEMBONUS		},   
	{ POINT_MALL_GOLDBONUS		},   
	{ POINT_MAX_HP_PCT			},		
	{ POINT_MAX_SP_PCT			},		
	{ POINT_SKILL_DAMAGE_BONUS		},	
	{ POINT_NORMAL_HIT_DAMAGE_BONUS	},	
	{ POINT_SKILL_DEFEND_BONUS		},	
	{ POINT_NORMAL_HIT_DEFEND_BONUS	},	
	{ POINT_PC_BANG_EXP_BONUS	},		
	{ POINT_PC_BANG_DROP_BONUS	},		
	{ POINT_NONE,		},				
	{ POINT_RESIST_WARRIOR,		},		
	{ POINT_RESIST_ASSASSIN,	},		
	{ POINT_RESIST_SURA,		},		
	{ POINT_RESIST_SHAMAN,		},		
	{ POINT_ENERGY				},		
	{ POINT_DEF_GRADE			},		
	{ POINT_COSTUME_ATTR_BONUS	},		
	{ POINT_MAGIC_ATT_BONUS_PER },			
	{ POINT_MELEE_MAGIC_ATT_BONUS_PER		},			
	{ POINT_RESIST_ICE,			},   
	{ POINT_RESIST_EARTH,		},   
	{ POINT_RESIST_DARK,		},   
	{ POINT_RESIST_CRITICAL,		},   
	{ POINT_RESIST_PENETRATE,		},   
#ifdef ENABLE_WOLFMAN_CHARACTER
	{ POINT_BLEEDING_REDUCE,		},	
	{ POINT_BLEEDING_PCT,			},	
	{ POINT_ATTBONUS_WOLFMAN,		},	
	{ POINT_RESIST_WOLFMAN,			},	
	{ POINT_RESIST_CLAW,			},	
#else
	{ POINT_NONE,					},	
	{ POINT_NONE,					},	
	{ POINT_NONE,					},	
	{ POINT_NONE,					},	
	{ POINT_NONE,					},	
#endif
#ifdef ENABLE_ACCE_COSTUME_SYSTEM
	{ POINT_ACCEDRAIN_RATE,			},	
#else
	{ POINT_NONE,			},
#endif

#ifdef ENABLE_MAGIC_REDUCTION_SYSTEM
	{ POINT_RESIST_MAGIC_REDUCTION,	},	
#else
	{ POINT_NONE,					},	
#endif
};

const int aiItemMagicAttributePercentHigh[ITEM_ATTRIBUTE_MAX_LEVEL] =
{
	30, 40, 20, 8, 2
};

const int aiItemMagicAttributePercentLow[ITEM_ATTRIBUTE_MAX_LEVEL] =
{
	50, 40, 10, 0, 0
};

const int aiItemAttributeAddPercent[ITEM_ATTRIBUTE_MAX_NUM] =
{
	100, 80, 60, 50, 30, 0, 0,
};

const int aiExpLossPercents[PLAYER_EXP_TABLE_MAX + 1] =
{
	0,
	5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 
	4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 
	4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 
	3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 
	3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 
	2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
	2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 
	1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
	1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
	1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
	1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
	1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
};

const int aiSkillBookCountForLevelUp[10] =
{
	3, 3, 3, 3, 3, 4, 4, 5, 5, 6
};

const int aiGrandMasterSkillBookCountForLevelUp[10] =
{
	3, 3, 5, 5, 7, 7, 10, 10, 10, 20,
};

const int aiGrandMasterSkillBookMinCount[10] =
{
	1, 1, 1, 2,  2,  3,  3,  4,  5,  6
};

const int aiGrandMasterSkillBookMaxCount[10] =
{
	5,  7,  9, 11, 13, 15, 20, 25, 30, 35
};

const int CHN_aiPartyBonusExpPercentByMemberCount[9] =
{
	0, 0, 12, 18, 26, 40, 53, 70, 100
};

const int KOR_aiPartyBonusExpPercentByMemberCount[9] =
{
	0,
	0,
	30,
	60, 
	75, 
	90, 
	105, 
	110, 
	140, 
};

const int KOR_aiUniqueItemPartyBonusExpPercentByMemberCount[9] =
{
	0,
	0,
	15*2,
	14*3,
	13*4,
	12*5,
	11*6,
	10*7,
	10*8,
};

const int * aiChainLightningCountBySkillLevel = NULL;

const int aiChainLightningCountBySkillLevel_euckr[SKILL_MAX_LEVEL+1] =
{
	0,
	2,	
	2,	
	2,	
	2,
	2,	
	2,	
	2,	
	2,	
	3,	
	3,	
	3,	
	3,	
	3,	
	3,	
	3,	
	3,	
	3,	
	3,	
	4,	
	4,	
	4,	
	4,	
	4,	
	5,	
	5,	
	5,	
	5,	
	5,	
	5,	
	5,	
	5,	
	5,	
	5,	
	5,	
	5,	
	5,	
	5,	
	5,	
	5,	
	5,	
};

const SStoneDropInfo aStoneDrop[STONE_INFO_MAX_NUM] =
{
	{8005,	60,	{30,	30,	30,	9,	1}	},
	{8006,	60,	{28,	29,	31,	11,	1}	},
	{8007,	60,	{24,	29,	32,	13,	2}	},
	{8008,	60,	{22,	28,	33,	15,	2}	},
	{8009,	60,	{21,	27,	33,	17,	2}	},
	{8010,	60,	{18,	26,	34,	20,	2}	},
	{8011,	60,	{14,	26,	35,	22,	3}	},
	{8012,	60,	{10,	26,	37,	24,	3}	},
	{8013,	60,	{2,	26,	40,	29,	3}	},
	{8014,	60,	{0,	26,	41,	30,	3}	},
};

const char * c_apszEmpireNames[EMPIRE_MAX_NUM] =
{
	"EMPIRE_MAX_NUM_1",
	"EMPIRE_MAX_NUM_2",
	"EMPIRE_MAX_NUM_3",
	"EMPIRE_MAX_NUM_4"
};

const char * c_apszPrivNames[MAX_PRIV_NUM] =
{
	"",
	"MAX_PRIV_NUM_1",
	"MAX_PRIV_NUM_2",
	"MAX_PRIV_NUM_3",
	"MAX_PRIV_NUM4",
};

const int aiPolymorphPowerByLevel[SKILL_MAX_LEVEL + 1] =
{
	10,   
	11,   
	11,   
	12,   
	13,   
	13,   
	14,   
	15,   
	16,   
	17,   
	18,   
	19,   
	20,   
	22,   
	23,   
	24,   
	26,   
	27,   
	29,  
	31,   
	33,   
	35,   
	37,   
	39,   
	41,   
	44,   
	46,   
	49,  
	52,   
	55,   
	59,  
	62,   
	66,  
	70,  
	74,  
	79,   
	84,   
	89,  
	94,   
	100,  
};

TGuildWarInfo KOR_aGuildWarInfo[GUILD_WAR_TYPE_MAX_NUM] =
{
	{ 0,        0,      0,      0,      0,      0       },
	{ 110,      0,      100,    50,     0,      100     },
	{ 111,      0,      100,    50,     0,      10      },
};

const int aiAccessorySocketAddPct[ITEM_ACCESSORY_SOCKET_MAX_NUM] =
{
	50, 50, 50
};

const int aiAccessorySocketEffectivePct[ITEM_ACCESSORY_SOCKET_MAX_NUM + 1] =
{
	0, 10, 20, 40
};

const int aiAccessorySocketDegradeTime[ITEM_ACCESSORY_SOCKET_MAX_NUM + 1] =
{
	0, 3600 * 24, 3600 * 12, 3600 * 6
};

const int aiAccessorySocketPutPct[ITEM_ACCESSORY_SOCKET_MAX_NUM + 1] =
{
	90, 80, 70, 0
};

#include "../../common/length.h"
typedef struct SValueName
{
    const char * c_pszName;
    long lValue;
} TValueName;

TValueName c_aApplyTypeNames[] =
{
    { "STR", APPLY_STR },
    { "DEX", APPLY_DEX },
    { "CON", APPLY_CON },
    { "INT", APPLY_INT },
    { "MAX_HP", APPLY_MAX_HP },
    { "MAX_SP",	APPLY_MAX_SP },
    { "MAX_STAMINA", APPLY_MAX_STAMINA },
    { "POISON_REDUCE", APPLY_POISON_REDUCE },
    { "EXP_DOUBLE_BONUS", APPLY_EXP_DOUBLE_BONUS },
    { "GOLD_DOUBLE_BONUS", APPLY_GOLD_DOUBLE_BONUS },
    { "ITEM_DROP_BONUS", APPLY_ITEM_DROP_BONUS },
    { "HP_REGEN", APPLY_HP_REGEN },
    { "SP_REGEN", APPLY_SP_REGEN },
    { "ATTACK_SPEED", APPLY_ATT_SPEED },
    { "MOVE_SPEED", APPLY_MOV_SPEED	},
    { "CAST_SPEED",	APPLY_CAST_SPEED },
    { "ATT_BONUS", APPLY_ATT_GRADE_BONUS },
    { "DEF_BONUS", APPLY_DEF_GRADE_BONUS },
    { "MAGIC_ATT_GRADE",APPLY_MAGIC_ATT_GRADE },
    { "MAGIC_DEF_GRADE",APPLY_MAGIC_DEF_GRADE },
    { "SKILL", APPLY_SKILL },
    { "ATTBONUS_ANIMAL",APPLY_ATTBONUS_ANIMAL },
    { "ATTBONUS_UNDEAD",APPLY_ATTBONUS_UNDEAD },
    { "ATTBONUS_DEVIL", APPLY_ATTBONUS_DEVIL },
    { "ATTBONUS_HUMAN", APPLY_ATTBONUS_HUMAN },
    { "ADD_BOW_DISTANCE",APPLY_BOW_DISTANCE },
    { "DODGE", APPLY_DODGE },
    { "BLOCK", APPLY_BLOCK },
    { "RESIST_SWORD", APPLY_RESIST_SWORD },
    { "RESIST_TWOHAND",	APPLY_RESIST_TWOHAND },
    { "RESIST_DAGGER", APPLY_RESIST_DAGGER },
    { "RESIST_BELL", APPLY_RESIST_BELL },
    { "RESIST_FAN",	APPLY_RESIST_FAN },
    { "RESIST_BOW",	APPLY_RESIST_BOW },
    { "RESIST_FIRE", APPLY_RESIST_FIRE },
    { "RESIST_ELEC", APPLY_RESIST_ELEC },
    { "RESIST_MAGIC", APPLY_RESIST_MAGIC },
    { "RESIST_WIND", APPLY_RESIST_WIND },
	{ "REFLECT_MELEE", APPLY_REFLECT_MELEE },
	{ "REFLECT_CURSE", APPLY_REFLECT_CURSE },
    { "RESIST_ICE",	APPLY_RESIST_ICE },
    { "RESIST_EARTH", APPLY_RESIST_EARTH },
    { "RESIST_DARK", APPLY_RESIST_DARK },
    { "RESIST_CRITICAL", APPLY_ANTI_CRITICAL_PCT },
    { "RESIST_PENETRATE", APPLY_ANTI_PENETRATE_PCT },
    { "POISON",	APPLY_POISON_PCT },
    { "SLOW", APPLY_SLOW_PCT },
    { "STUN", APPLY_STUN_PCT },
    { "STEAL_HP", APPLY_STEAL_HP },
    { "STEAL_SP", APPLY_STEAL_SP },
    { "MANA_BURN_PCT", APPLY_MANA_BURN_PCT },
    { "CRITICAL", APPLY_CRITICAL_PCT },
    { "PENETRATE", APPLY_PENETRATE_PCT },
    { "KILL_SP_RECOVER",APPLY_KILL_SP_RECOVER },
    { "KILL_HP_RECOVER",APPLY_KILL_HP_RECOVER },
    { "PENETRATE_PCT", APPLY_PENETRATE_PCT },
    { "CRITICAL_PCT", APPLY_CRITICAL_PCT },
    { "POISON_PCT",	APPLY_POISON_PCT },
    { "STUN_PCT", APPLY_STUN_PCT },
    { "ATT_BONUS_TO_WARRIOR", APPLY_ATTBONUS_WARRIOR },
    { "ATT_BONUS_TO_ASSASSIN", APPLY_ATTBONUS_ASSASSIN },
    { "ATT_BONUS_TO_SURA", APPLY_ATTBONUS_SURA },
    { "ATT_BONUS_TO_SHAMAN", APPLY_ATTBONUS_SHAMAN },
    { "ATT_BONUS_TO_MONSTER", APPLY_ATTBONUS_MONSTER },
    { "ATT_BONUS_TO_MOB", APPLY_ATTBONUS_MONSTER },
    { "MALL_ATTBONUS", APPLY_MALL_ATTBONUS	},
    { "MALL_EXPBONUS", APPLY_MALL_EXPBONUS	},
    { "MALL_DEFBONUS", APPLY_MALL_DEFBONUS	},
    { "MALL_ITEMBONUS",	APPLY_MALL_ITEMBONUS },
    { "MALL_GOLDBONUS", APPLY_MALL_GOLDBONUS },
    { "MAX_HP_PCT",	APPLY_MAX_HP_PCT },
    { "MAX_SP_PCT",	APPLY_MAX_SP_PCT },
    { "SKILL_DAMAGE_BONUS",	APPLY_SKILL_DAMAGE_BONUS	},
    { "NORMAL_HIT_DAMAGE_BONUS",APPLY_NORMAL_HIT_DAMAGE_BONUS	},
    { "SKILL_DEFEND_BONUS",	APPLY_SKILL_DEFEND_BONUS },
    { "NORMAL_HIT_DEFEND_BONUS",APPLY_NORMAL_HIT_DEFEND_BONUS	},
    { "PCBANG_EXP_BONUS", APPLY_PC_BANG_EXP_BONUS	},
    { "PCBANG_DROP_BONUS", APPLY_PC_BANG_DROP_BONUS	},
    { "RESIST_WARRIOR",	APPLY_RESIST_WARRIOR},
    { "RESIST_ASSASSIN", APPLY_RESIST_ASSASSIN},
    { "RESIST_SURA", APPLY_RESIST_SURA},
    { "RESIST_SHAMAN",	APPLY_RESIST_SHAMAN},
    { "INFINITE_AFFECT_DURATION", 0x1FFFFFFF },
	{ "ENERGY", APPLY_ENERGY },		
	{ "COSTUME_ATTR_BONUS", APPLY_COSTUME_ATTR_BONUS },	
	{ "MAGIC_ATTBONUS_PER",	APPLY_MAGIC_ATTBONUS_PER	},
    { "MELEE_MAGIC_ATTBONUS_PER",	APPLY_MELEE_MAGIC_ATTBONUS_PER	},
#ifdef ENABLE_WOLFMAN_CHARACTER
	{ "BLEEDING_REDUCE",APPLY_BLEEDING_REDUCE },
	{ "BLEEDING_PCT",APPLY_BLEEDING_PCT },
	{ "ATT_BONUS_TO_WOLFMAN",APPLY_ATTBONUS_WOLFMAN },
	{ "RESIST_WOLFMAN",APPLY_RESIST_WOLFMAN },
	{ "RESIST_CLAW",APPLY_RESIST_CLAW },
#endif
#ifdef ENABLE_ACCE_COSTUME_SYSTEM
	{ "ACCEDRAIN_RATE",APPLY_ACCEDRAIN_RATE },
#endif
#ifdef ENABLE_MAGIC_REDUCTION_SYSTEM
	{ "RESIST_MAGIC_REDUCTION",APPLY_RESIST_MAGIC_REDUCTION },
#endif
    { NULL, 0 }
};

long FN_get_apply_type(const char *apply_type_string)
{
	TValueName	*value_name;
	for (value_name = c_aApplyTypeNames; value_name->c_pszName; ++value_name)
	{
		if (0==strcasecmp(value_name->c_pszName, apply_type_string))
			return value_name->lValue;
	}
	return 0;
}
