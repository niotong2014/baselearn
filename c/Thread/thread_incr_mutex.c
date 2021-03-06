/*************************************************************************
	> File Name: thread_incr.c
	> Author: niotong
	> Mail: niotong2014@sina.com 
	> Created Time: 2016年10月02日 星期日 19时45分31秒
 ************************************************************************/

#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>

static int glob = 0;
static pthread_mutex_t mtx = PTHREAD_MUTEX_INITIALIZER;

static void* threadFunc(void * arg){
	int loops = *((int*) arg);
	int loc,j,s;
	for(j = 0;j <loops;j++){
		s = pthread_mutex_lock(&mtx);
		if(s !=0 ){
			printf("pthread_mutex_lock failed!\n");
		}
		loc = glob;
		loc++;
		glob = loc;
		s = pthread_mutex_unlock(&mtx);
		if(s !=0 ){
			printf("pthread_mutex_unlock failed!\n");
		}
	}

	return NULL;
}

int main(int argc,char* argv[]){
	pthread_t t1,t2;
	int loops,s;
	loops = (argc>1)?atoi(argv[1]):10000000;

	s = pthread_create(&t1,NULL,threadFunc,&loops);
	if(s != 0){
		printf("pthread_create failed!\n");
	}

	s = pthread_create(&t2,NULL,threadFunc,&loops);
	if(s != 0){
		printf("pthread_create failed!\n");
	}

	s = pthread_join(t1,NULL);
	if(s != 0){
		printf("pthread_join failed!\n");
	}
	s = pthread_join(t2,NULL);
	if(s != 0){
		printf("pthread_join failed!\n");
	}
	printf("glob = %d\n",glob);
	return 0;
}
