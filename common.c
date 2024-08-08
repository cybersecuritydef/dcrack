#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void die(const char *msg){
    fprintf(stderr, "%s\n", msg);
    exit(EOF);
}
