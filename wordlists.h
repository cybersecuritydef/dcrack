#ifndef __WORDLISTS_H__
#define __WORDLISTS_H__

#define LEN 256

struct lists{
    char *word;
    struct lists *next;
};

struct wordlists{
    struct lists *words;
    size_t count;
};

struct wordlists *read_wordlists(const char *filename);

void free_wordlists(struct wordlists *words);

#endif
