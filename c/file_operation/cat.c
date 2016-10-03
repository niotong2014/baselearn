/*************************************************************************
	> File Name: cat.c
	> Author: niotong
	> Mail: niotong2014@sina.com 
	> Created Time: 2016年10月02日 星期日 14时48分00秒
 ************************************************************************/

#include<stdio.h>

#include<fcntl.h>
#include<sys/stat.h>
#include <sys/types.h>
#include<unistd.h>

main(int argc, char* argv[]){
	if(argc == 1)
		printf("no filepath\n");
	char a[20];
	char* filepath = argv[1];
	int fd = open(argv[1],O_RDWR);
	if(fd == -1){
		exit(1);
	}
	if(read(fd,a,19) == -1){
		exit(1);
	}
	printf("read:%s\n",a);
	if(write(fd,"caonima",8) == -1){
		exit("write");
	}
	if(read(fd,a,19) == -1){
		exit(1);
	}
	printf("read:%s\n",a);
	if( close(fd) == -1){
		exit(1);
	}
}
