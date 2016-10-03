#include <stdio.h>
#include <stdlib.h>
#include "single.h"

single* nodemalloc(){
	single * node = malloc(sizeof(single));
	node->val = 0;
	node->next = NULL;
	return node;
}

//头插
nodefirstadd(single * head,single * node){
	node->next = head->next;
	head->next = node;
}

//尾插
nodelastadd(single * head,single * node){
	single * temp = NULL;
	for(temp = head;temp->next != NULL;temp = temp->next);
	temp->next = node;
}

//头删
noderm(single * head, int val){
	single * temp = NULL;
	single * rmnode = NULL;
	for(temp = head;temp->next != NULL;temp = temp->next){
		if(temp->next->val == val){
			rmnode = temp->next;
			temp->next = temp->next->next;
			free(rmnode);
		}
	}
}

void nodeprintf(single * head){
	single * temp = head->next;
	while(temp != NULL){
		printf("%d\n",temp->val);
		temp = temp->next;
	}
}
