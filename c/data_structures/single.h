#include <stdio.h>
typedef struct singlenode{
	int val;
	struct singlenode * next;
} single;

single * nodemalloc();
nodefirstadd(single * , single *);
nodelastadd(single * , single *);
noderm(single *,int);
void nodeprintf(single *);
