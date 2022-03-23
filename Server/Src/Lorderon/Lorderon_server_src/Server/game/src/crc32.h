//Lorderon server core Dev by Lordbecvold
#ifndef __INC_CRC32_H__
#define __INC_CRC32_H__
typedef unsigned long crc_t;
crc_t GetCRC32(const char * buffer, size_t count);
crc_t GetCaseCRC32(const char * buffer, size_t count);
crc_t GetFastHash(const char * key, size_t len);
#endif
