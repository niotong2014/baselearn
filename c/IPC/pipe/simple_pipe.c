/*************************************************************************
	> File Name: simple_pipe.c
	> Author: niotong
	> Mail: niotong2014@sina.com 
	> Created Time: 2016年10月03日 星期一 15时01分58秒
 ************************************************************************/

#include<stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

#define BUF_SIZE 10
int main(int argc,char * argv[]){
	int pfd[2];
	char buf[BUF_SIZE];
	ssize_t numRead;

	if(argc !=2)
		return 1;

	if(pipe(pfd) == -1)
		printf("pipe() failed\n");

	//fork一个子进程
	switch(fork()){
		case -1:
			printf("fork() failed!\n");
			break;
		case 0:	//fork成功，子进程执行以下程序
			if(close(pfd[1]) == -1){
				printf("close the write point of pipe!(child)\n");
			}
			for(;;)	{
				numRead = read(pfd[0],buf,BUF_SIZE);
				if(numRead == -1){
					printf("read failed!(child)\n");
				}
				if(numRead == 0){
					break;
				}
				//stdin 0
				//stdout 1
				//stderr 2
				if(write(1,buf,numRead) != numRead){
					printf("write in stdout failed!\n");
				}
			}
			write(0,"\n",1);
			if(close(pfd[0]) == -1)
				printf("close the read point of pipe!(child)\n");
			_exit(EXIT_SUCCESS);
		default://父进程执行以下程序
			if(close(pfd[0]) == -1)
				printf("close the read point of pipe!(parent)\n");
			if(write(pfd[1],argv[1],strlen(argv[1])) != strlen(argv[1]))
				printf("write failed ! \n");

			if(close(pfd[1]) == -1)
				printf("close the write point of pipe!(parent)\n");
			wait(NULL);
			exit(EXIT_SUCCESS);
	}

}
