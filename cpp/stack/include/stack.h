/*************************************************************************
	> File Name: stack.h
	> Author: niotong
	> Mail: niotong2014@sina.com 
	> Created Time: 2016年10月10日 星期一 23时34分41秒
 ************************************************************************/


#ifndef STACK_H_
#define STACK_H_

typedef unsigned long Item;

class Stack{
	private:
		enum {MAX = 10};
		Item items[MAX];
		int top;
	public:
		Stack();
		bool isfull() const;	//const 作用是不允许修改成员变量
		bool isempty() const;

		// push() returns false if stack already is full,true otherwise
		bool push(const Item & item);
		// pop() returns false if stack already is empty,true otherwise
		bool pop(Item & item);
};

#endif
