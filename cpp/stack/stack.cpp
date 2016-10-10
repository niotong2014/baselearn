/*************************************************************************
	> File Name: stack.cpp
	> Author: niotong
	> Mail: niotong2014@sina.com 
	> Created Time: 2016年10月10日 星期一 23时42分17秒
 ************************************************************************/

#include "stack.h"

Stack::Stack(){
	top = 0;
}

bool Stack::isempty() const{
	return top == 0;
}

bool Stack::isfull() const{
	return top == MAX;
}

bool Stack::push(const Item & item){
	if(top < MAX){
		items[top++] = item;
		return true;
	}else{
		return false;
	}
}

bool Stack::pop(Item & item){
	if (top > 0){
		item = items[--top];
		return true;
	}else{
		return false;
	}
}
