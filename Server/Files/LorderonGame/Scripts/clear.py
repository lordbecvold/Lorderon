#Lorderon server Clear script.
from subprocess import check_output as sp_co, call as sp_call, CalledProcessError as sp_CalledProcessError
from os import getcwd as os_getcwd, chdir as os_chdir

def fShell(szCmd, bRet=False):
	try:
		if bRet:
			return sp_co(szCmd, shell=True)[:-1]	
		else:
			return sp_call(szCmd, shell=True)
	except sp_CalledProcessError:
		return -1

def cleStart():
	from json import load as j_loads
	v_lst=(
		"p2p_packet_info.txt","packet_info.txt","profile.txt","stdout","syslog","syserr",
		"usage.txt","VERSION.txt","DEV_LOG.log","mob_count","*.core"
	)
	szPWD=os_getcwd()
	with open("lists/clear.list", "r") as fList:
		mList = j_loads(fList)
	for dic1 in mList:
		os_chdir(dic1["path"])
		fShell("cat /dev/null > PTS")
		fShell("rm -rf log/* cores/*")
		os_chdir(szPWD)
	with open("lists/start.list", "r") as fList:
		mList = j_loads(fList)
	for dic1 in mList:
		os_chdir(dic1["path"])
		fShell("echo --- delete inside '%s' ---"%dic1["path"])
		fShell("rm -fv %s"%" ".join(v_lst))
		os_chdir(szPWD)

if __name__ == "__main__":
	cleStart()
##########################################################################################################################################