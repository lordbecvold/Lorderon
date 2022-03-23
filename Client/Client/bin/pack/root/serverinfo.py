#Lorderon Client Dev by Lordbecvold
import app
import localeInfo
app.ServerName = None
SRV1 = {
	"name":"LORDERON",
	"host":"89.203.249.110",
	"auth1":30001,
	"ch1":13002,
	"ch2":13102,
	"ch3":13202,
}
STATE_NONE = "OFFLINE"
STATE_DICT = {
	0 : "OFFLINE",
	1 : "ONLINE",
	2 : "BUSY",
	3 : "FULL"
}
STATE_DICT_NAME = {
	"OFFLINE" : "OFFLINE",
	"ONLINE" : "ONLINE",
	"BUSY" : "BUSY",
	"FULL" : "FULL"
}
SERVER1_CHANNEL_DICT = {
	1:{"key":11,"name":"Channel 1","ip":SRV1["host"],"tcp_port":SRV1["ch1"],"udp_port":SRV1["ch1"],"state":STATE_NONE,},
	2:{"key":12,"name":"Channel 2","ip":SRV1["host"],"tcp_port":SRV1["ch2"],"udp_port":SRV1["ch2"],"state":STATE_NONE,},
	3:{"key":13,"name":"Channel 3","ip":SRV1["host"],"tcp_port":SRV1["ch3"],"udp_port":SRV1["ch3"],"state":STATE_NONE,},
}
REGION_NAME_DICT = {
	0 : SRV1["name"],
}
REGION_AUTH_SERVER_DICT = {
	0 : {
		1 : { "ip":SRV1["host"], "port":SRV1["auth1"], },
		2 : { "ip":SRV1["host"], "port":SRV1["auth1"], },
	}
}
REGION_DICT = {
	0 : {
		1 : { "name" :SRV1["name"], "channel" : SERVER1_CHANNEL_DICT, },
	},
}
MARKADDR_DICT = {
	10 : { "ip" : SRV1["host"], "tcp_port" : SRV1["ch1"], "mark" : "10.tga", "symbol_path" : "10", },
	11 : { "ip" : SRV1["host"], "tcp_port" : SRV1["ch2"], "mark" : "10.tga", "symbol_path" : "11", },
	12 : { "ip" : SRV1["host"], "tcp_port" : SRV1["ch3"], "mark" : "10.tga", "symbol_path" : "12", },
}
TESTADDR = { "ip" : SRV1["host"], "tcp_port" : SRV1["ch1"], "udp_port" : SRV1["ch1"], }
