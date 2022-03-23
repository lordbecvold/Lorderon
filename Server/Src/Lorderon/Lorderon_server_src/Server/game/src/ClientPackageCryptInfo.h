//Lorderon server core Dev by Lordbecvold
#ifndef __INC_CLIENTPACKAGE_CRYPTINFO_H
#define __INC_CLIENTPACKAGE_CRYPTINFO_H
#include <boost/unordered_map.hpp>
#pragma pack(1)

typedef struct SSupplementaryDataBlockInfo
{
	DWORD dwPackageIdentifier;
	DWORD dwFileIdentifier;
	std::vector<BYTE> vecSDBStream;

	void Serialize( BYTE* pStream )
	{
		memcpy(pStream, &dwPackageIdentifier, sizeof(DWORD));
		memcpy(pStream+4, &dwFileIdentifier, sizeof(DWORD));
		BYTE bSize = vecSDBStream.size();
		memcpy(pStream+8, &bSize,  sizeof(BYTE));
		memcpy(pStream+9, &vecSDBStream[0], bSize);
	}
	DWORD GetSerializedSize() const
	{
		return sizeof(DWORD)*2 + sizeof(BYTE) + vecSDBStream.size();
	}
} TSupplementaryDataBlockInfo;
#pragma pack()
class CClientPackageCryptInfo
{
public:
	CClientPackageCryptInfo();
	~CClientPackageCryptInfo();
	bool LoadPackageCryptInfo( const char* pCryptInfoDir );
	void GetPackageCryptKeys( BYTE** ppData, int& iDataSize );
	bool GetRelatedMapSDBStreams(const char* pMapName, BYTE** ppData, int& iDataSize );

private:
	bool LoadPackageCryptFile( const char* pCryptFile );

private:
	int m_nCryptKeyPackageCnt;
	std::vector<BYTE> m_vecPackageCryptKeys;
	BYTE* m_pSerializedCryptKeyStream;
	typedef struct SPerFileSDBInfo
	{
		SPerFileSDBInfo() : m_pSerializedStream(NULL) {}
		~SPerFileSDBInfo()
		{
			if(m_pSerializedStream)
			{
				delete[]m_pSerializedStream;
			}
		}
		DWORD GetSize() const
		{
			DWORD dwSize = 4; 
			for(int i = 0; i < (int)vecSDBInfos.size(); ++i)
			{
				dwSize += vecSDBInfos[i].GetSerializedSize();
			}
			return dwSize;
		}
		BYTE* GetSerializedStream()
		{
			if(m_pSerializedStream)
				return m_pSerializedStream;
			m_pSerializedStream = new BYTE[GetSize()];
			int iWrittenOffset = 0;
			int iSDBInfoSize   = vecSDBInfos.size();
			memcpy( m_pSerializedStream, &iSDBInfoSize, sizeof(int) );
			iWrittenOffset += sizeof(int);
			for(int i = 0; i < iSDBInfoSize; ++i)
			{
				vecSDBInfos[i].Serialize( m_pSerializedStream + iWrittenOffset );
				iWrittenOffset += vecSDBInfos[i].GetSerializedSize();
			}
			return m_pSerializedStream;
		}
		std::vector<TSupplementaryDataBlockInfo> vecSDBInfos;
	private:
		BYTE* m_pSerializedStream;

	} TPerFileSDBInfo;
	typedef boost::unordered_map<std::string, TPerFileSDBInfo > TPackageSDBMap;	
	TPackageSDBMap m_mapPackageSDB;
};
#endif 
