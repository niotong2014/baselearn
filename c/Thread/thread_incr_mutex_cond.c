/*************************************************************************
	> File Name: thread_incr.c
	> Author: niotong
	> Mail: niotong2014@sina.com 
	> Created Time: 2016年10月02日 星期日 19时45分31秒
 ************************************************************************/

#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>

//生产-消费模式
static int glob = 0;
static pthread_mutex_t mtx = PTHREAD_MUTEX_INITIALIZER;
static pthread_cond_t cond = PTHREAD_COND_INITIALIZER;

static void* customer(void * arg){
	int loops = *((int*) arg);
	int loc,j,s;
	for(j = 0;j <loops;j++){

		s = pthread_mutex_lock(&mtx);
		//加锁，相当于关门
		if(s !=0 ){
			printf("pthread_mutex_lock failed!\n");
		}

		while(glob == 0){	//条件判断是不是应该自己操作
			s = pthread_cond_wait(&cond,&mtx);	//符合条件表明不是自己应该操作的，然后释放掉锁，然后等待，知道pthread_cond_signal通知它，然后它再加锁
			if(s != 0){
				printf("pthread_cond_wait failed\n");
			}
		}
		while(glob > 0){	//该自己干活了.
			glob--;
		}

		s = pthread_mutex_unlock(&mtx);
		//释放锁，相当于开门
		if(s !=0 ){
			printf("pthread_mutex_unlock failed!\n");
		}

	}

	return NULL;
}
static void* producter(void * arg){
	int loops = *((int*) arg);
	int loc,j,s;
	for(j = 0;j <loops;j++){

		s = pthread_mutex_lock(&mtx);
		if(s !=0 ){
			printf("pthread_mutex_lock failed!\n");
		}

		glob++;

		s = pthread_mutex_unlock(&mtx);
		if(s !=0 ){
			printf("pthread_mutex_unlock failed!\n");
		}
//可以加判断，看唤不唤醒pthread_cond_wait
		s = pthread_cond_signal(&cond);
		if(s != 0){
			printf("pthread_cond_signal failed\n");
		}
	}

	return NULL;
}

int main(int argc,char* argv[]){
	pthread_t t1,t2;
	int loops,s;
	loops = (argc>1)?atoi(argv[1]):10000000;

	s = pthread_create(&t1,NULL,customer,&loops);
	if(s != 0){
		printf("pthread_create failed!\n");
	}

	s = pthread_create(&t2,NULL,producter,&loops);
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
