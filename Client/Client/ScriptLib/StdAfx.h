//Lorderon Client Binary Dev by Lordbecvold
#pragma once
#include "../eterLib/StdAfx.h"
#include "../eterGrnLib/StdAfx.h"
#ifdef AT
#undef AT 
#endif
#ifdef _DEBUG
	#undef _DEBUG
	#include "../../Extern/Python2/Python.h"
	#define _DEBUG
#else
	#include "../../Extern/Python2/Python.h"
#endif
#include "../../Extern/Python2/node.h"
#include "../../Extern/Python2/grammar.h"
#include "../../Extern/Python2/token.h"
#include "../../Extern/Python2/parsetok.h"
#include "../../Extern/Python2/errcode.h"
#include "../../Extern/Python2/compile.h"
#include "../../Extern/Python2/symtable.h"
#include "../../Extern/Python2/eval.h"
#include "../../Extern/Python2/marshal.h"
#ifdef AT
#undef AT 
#endif
#include "PythonUtils.h"
#include "PythonLauncher.h"
#include "PythonMarshal.h"
#include "Resource.h"

void initdbg();

class IPythonExceptionSender
{
	public:
		void Clear()
		{
			m_strExceptionString = "";
		}
		void RegisterExceptionString(const char * c_szString)
		{
			m_strExceptionString += c_szString;
		}
		virtual void Send() = 0;
	protected:
		std::string m_strExceptionString;
};

extern IPythonExceptionSender * g_pkExceptionSender;

void SetExceptionSender(IPythonExceptionSender * pkExceptionSender);
