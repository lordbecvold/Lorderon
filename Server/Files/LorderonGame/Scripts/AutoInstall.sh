#Lorderon Server Control script.
gecho () { echo -e "\033[32m$1\033[0m"; }
recho () { echo -e "\033[93m$1\033[0m"; }
_recho () { echo -e "\033[4;93m$1\033[0m"; }
r_echo () { echo -e "\033[1;32m$1\033[0m"; }
cecho () { echo -e "\033[36m$1\033[0m"; }

recho "--------------------------Lorderon Server AutoInstaller-------------------------"
gecho "Select action number"
recho "--------------------------------------------------------------------------------
1. - Extract ports
2. - Install Python & Python27
3. - Install Nload & Htop
4. - Install mysql56-server & enable mysql after start (rc.conf)
5. - Install Apache24 && enable apache24 after start (rc.conf)
6. - Install PHP72
7. - Install PHP extensions
8. - Install Java-12
9. - Install Screen









--------------------------------------------------------------------------------"
_recho "0. Nic"
if [ -z $1 ]; then
	read phase
else
	phase=$1
fi
case  $phase in
1|start)
	portsnap fetch extract
;;
2|start)
	pkg install python && pkg install python27
;;
3|start)
	pkg install nload && pkg install htop
;;
4|start)
	pkg install mysql56-server && sysrc mysql_enable="yes"
;;
5|start)
	pkg install apache24 && sysrc apache24_enable="yes"
;;
6|start)
	pkg install php72
;;
7|start)
	pkg install php72-curl php72-extensions php72-json php72-xml \
php72-zip php72-intl php72-mysqli php72-pdo_mysql php72-pdo \
php72-pear php72-soap php72-phar
;;
8|start)
	pkg install openjdk12
;;
9|start)
	pkg install screen
;;
0|quit)
	cecho "Server manager closed!"
;;
*)
	cecho "Vote not found!"
esac
