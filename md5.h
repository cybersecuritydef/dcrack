#ifndef __MD5_H__
#define __MD5_H__

#include <openssl/md5.h>

void md5(const char *inbuf, const size_t inlen, char *outbuf);

#endif
