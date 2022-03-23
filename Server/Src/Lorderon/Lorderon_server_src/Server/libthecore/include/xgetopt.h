//Lorderon server core Dev by Lordbecvold
#ifndef XGETOPT_H
#define XGETOPT_H
extern int optind, opterr, optreset;
extern TCHAR *optarg;
int getopt(int argc, TCHAR *argv[], TCHAR *optstring);
#endif
