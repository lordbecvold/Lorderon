//Lorderon Client Binary Dev by Lordbecvold
#pragma once
#include "Packet.h"

class CPythonTicketLogs
{
public:
	CPythonTicketLogs(void);
	~CPythonTicketLogs(void);
	void AddLogDetails(TPacketTicketLogsData p);
	TPacketTicketLogs Request(int);
	static CPythonTicketLogs* instance();
private:
	std::vector<TPacketTicketLogs> m_vecData_A;
	static CPythonTicketLogs * curInstance_A;
};
class CPythonTicketLogsReply
{
public:
	CPythonTicketLogsReply(void);
	~CPythonTicketLogsReply(void);
	void AddLogDetails(TPacketTicketLogsDataReply p);
	TPacketTicketLogsReply Request(int);
	static CPythonTicketLogsReply* instance();
private:
	std::vector<TPacketTicketLogsReply> m_vecData_B;
	static CPythonTicketLogsReply * curInstance_B;
};
