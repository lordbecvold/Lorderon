#Lorderon source manager script
#Compiler root directory /root/Lorderon/etc
gecho () { echo -e "\033[32m$1\033[0m"; }
recho () { echo -e "\033[93m$1\033[0m"; }
_recho () { echo -e "\033[4;93m$1\033[0m"; }
r_echo () { echo -e "\033[1;32m$1\033[0m"; }
cmd_echo () { echo -e "\033[36m$1\033[0m"; }
recho "----------------------------Lorderon source manager-----------------------------"
gecho "Please select action number"
recho "--------------------------------------------------------------------------------
1) Complete Build Game & db (All library)
2) Build Only Game source
3) Build Only db source
4) Complete clean project Game & db (All library)
----------------------------------Other actions---------------------------------
a)server_source Backup
b)Backup recovery












--------------------------------------------------------------------------------"
_recho "0. Exit manager"
if [ -z $1 ]; then
	read phase
else
	phase=$1
fi
case  $phase in
1|start)
	cd /root/Lorderon/Lorderon_server_src/Server && gmake all -j4
	cmd_echo "Complete Source Build Closed!"
;;
2|start)
	cd /root/Lorderon/Lorderon_server_src/Server/game/src && gmake clean && gmake
	cmd_echo "Building game source closed!"
;;
3|start)
	cd /root/Lorderon/Lorderon_server_src/Server/db/src && gmake clean && gmake
	cmd_echo "Building db source closed!"
;;
4|start)
	cd /root/Lorderon/Lorderon_server_src/Server/libthecore/src && gmake clean 
	cd /root/Lorderon/Lorderon_server_src/Server/libsql && gmake clean
	cd /root/Lorderon/Lorderon_server_src/Server/libserverkey && gmake clean
	cd /root/Lorderon/Lorderon_server_src/Server/libpoly && gmake clean
	cd /root/Lorderon/Lorderon_server_src/Server/liblua/5.0 && gmake clean
	cd /root/Lorderon/Lorderon_server_src/Server/libgame/src && gmake clean
	cd /root/Lorderon/Lorderon_server_src/Server/game/src && gmake clean
	cd /root/Lorderon/Lorderon_server_src/Server/quest_core && gmake clean
	cd /root/Lorderon/Lorderon_server_src/Server/db/src && gmake clean
	cmd_echo "Source clean closed!"
;;
a|start)
	cd /root/Lorderon && tar cfz Lorderon_server_src.tar.gz Lorderon_server_src/ 
	mv Lorderon_server_src.tar.gz /root/Lorderon/Backup
	cmd_echo "Source Backup closed!"
;;
b|start)
	cd /root/Lorderon/
	rm -r Lorderon_server_src/
	cd /root/Lorderon/Backup/
	tar zxvf Lorderon_server_src.tar.gz
	mv Lorderon_server_src /root/Lorderon
	cmd_echo "Source Backup closed!"
;;
0|quit)
	cmd_echo "source manager closed."
;;
*)
	cmd_echo "Action not found"
esac
