#Lorderon Server Control script.
v_base=$PWD
v_mt2f=$v_base
v_foldername=server
v_localename=czech
v_bin=python2.7

gecho () { echo -e "\033[32m$1\033[0m"; }
recho () { echo -e "\033[93m$1\033[0m"; }
_recho () { echo -e "\033[4;93m$1\033[0m"; }
r_echo () { echo -e "\033[1;32m$1\033[0m"; }
cecho () { echo -e "\033[36m$1\033[0m"; }

recho "--------------------------Lorderon Server ControlPanel--------------------------"
gecho "Select action number"
recho "--------------------------------------------------------------------------------
1)Start Dev (AUTH, DB, CH_1, CH_99)
2)Server Normal (AUTH, DB, CH_1, CH_2, CH_3, CH_99)
3)Server stop
4)Delete Logs
5)Compile quest
6)Restart Dev (AUTH, DB, CH_1, CH_99)
7)Server Backup
8)Mysql-Server start
9)Mysql-Server stop
10)Mysql-Server restart


--------------------------------------------------------------------------------
99)Go to auto config Panel.
--------------------------------------------------------------------------------"
_recho "0. Nic"
if [ -z $1 ]; then
	read phase
else
	phase=$1
fi
case  $phase in
1|start)
	chmod -R 777 /root
	cd $v_mt2f
	$v_bin Scripts/start_dev.py
	cd $v_base
	cecho "Server starting closed!"
;;
2|start)
	chmod -R 777 /root
	cd $v_mt2f
	$v_bin Scripts/start.py
	cd $v_base
	cecho "Server starting closed!"
;;
3|stop|close)
	cd $v_mt2f
	$v_bin Scripts/stop.py
	cd $v_base
	cecho "Server is offline"
;;
4|cleanall|clearall)
	cd $v_mt2f
	$v_bin Scripts/clear.py
	cd $v_base
	cecho "Logs deleted!"
;;
5|quest)
	cd $v_mt2f/$v_foldername/share/locale/$v_localename/quest
	$v_bin pre_qc.py -ac
	cd $v_base
	cecho "Quest Compile closed!"
;;
6|start)
	chmod -R 777 /root/LorderonGame
	cd $v_mt2f
	$v_bin Scripts/stop_dev.py
	cd $v_base
	cecho "Server closed!"
	cd $v_mt2f/$v_foldername/share/locale/$v_localename/quest
	$v_bin pre_qc.py -ac
	cd $v_base
	cecho "Quest Compile closed!"
	cd $v_mt2f
	$v_bin Scripts/clear.py
	cd $v_base
	cecho "Logs deleted!"
	cd $v_mt2f
	$v_bin Scripts/clear.py
	cd $v_base
	cecho "Complete logs clear!"
	cd $v_mt2f
	$v_bin Scripts/start_dev.py
	cd $v_base
	cecho "Server starting closed!"
;;
7|start)
	cd /root
	tar cfz LorderonGame.tar.gz LorderonGame/
	mv LorderonGame.tar.gz /root/LorderonGame/Backup
	cd /var/db
	tar cfz mysql.tar.gz mysql/
	mv mysql.tar.gz /root/LorderonGame/Backup
;;
8|start)
	service mysql-server start
	cecho "Mysql Server Starting closed!"
;;
9|start)
	service mysql-server stop
	cecho "Mysql Server Stoping closed!"
;;
10|start)
	service mysql-server restart
	cecho "Mysql Server Restarting closed!"
;;
99|start)
	cd /root/LorderonGame/Scripts && sh AutoInstall.sh
;;
0|quit)
	cecho "Server manager closed!"
;;
*)
	cecho "Vote not found!"
esac
