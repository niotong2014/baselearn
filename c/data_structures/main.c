/*************************************************************************
	> File Name: main.c
	> Author: niotong
	> Mail: niotong2014@sina.com 
	> Created Time: 2016年10月02日 星期日 17时26分08秒
 ************************************************************************/

#include<stdio.h>
#include "single.h"

main(){
	int a;
	single * node;
	single * head = nodemalloc();
	for(a = 0;a<10;a++){
		printf("please input a num:\n");
		node = nodemalloc();
		scanf("%d",&(node->val));
		printf("mard%d\n",a);
//		nodefirstadd(head,node);
		nodelastadd(head,node);
	}
	nodeprintf(head);
	noderm(head,2);
	nodeprintf(head);

}
