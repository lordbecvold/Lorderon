//Lorderon Client Binary Dev by Lordbecvold
#pragma once

#define WIN32_LEAN_AND_MEAN		
#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif
#pragma warning(disable: 4100 4127 4189 4231 4505 4512 4706) 
#pragma warning(disable:4995)	
#pragma warning(disable:4710)	
#pragma warning(disable:4786)	
#pragma warning(disable:4244)	
#include <windows.h>
#include <assert.h>
#include <stdio.h>
#pragma warning ( disable : 4201 )
#include <mmsystem.h>
#pragma warning ( default : 4201 )
#include <imagehlp.h>
#include <time.h>
#pragma warning ( push, 3 )
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <map>
#pragma warning ( pop )
#if _MSC_VER >= 1400
#define stricmp _stricmp
#define strnicmp _strnicmp
#define strupt _strupr
#define strcmpi _strcmpi
#define fileno _fileno
#define atoi _atoi64
#endif

#ifndef NANOBEGIN
	#ifdef __BORLANDC__
		#define NANOBEGIN     __emit__ (0xEB,0x03,0xD6,0xD7,0x01)
		#define NANOEND       __emit__ (0xEB,0x03,0xD6,0xD7,0x00)
	#else
		#define NANOBEGIN     __asm _emit 0xEB __asm _emit 0x03 __asm _emit 0xD6 __asm _emit 0xD7 __asm _emit 0x01
		#define NANOEND       __asm _emit 0xEB __asm _emit 0x03 __asm _emit 0xD6 __asm _emit 0xD7 __asm _emit 0x00
	#endif
#endif

#include "vk.h"
#include "filename.h"
#include "ServiceDefs.h"
