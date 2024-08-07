#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void die(const char *msg){
    perror(msg);
    exit(EOF);
}
