/*************************************************************************
  > File Name: stacktp.h
  > Author: niotong
  > Mail: niotong2014@sina.com 
  > Created Time: 2016年10月10日 星期一 23时34分41秒
 ************************************************************************/


#ifndef STACKTP_H_
#define STACKTP_H_

template <class Type>
class Stack{
	private:
		enum {MAX = 5};
		Type items[MAX];
		int top;
	public:
		Stack();
		bool isfull() const;	//const 作用是不允许修改成员变量
		bool isempty() const;

		// push() returns false if stack already is full,true otherwise
		bool push(const Type & item);
		// pop() returns false if stack already is empty,true otherwise
		bool pop(Type & item);
};

//为毛实现也要在模板的申明中？
template <class Type>
Stack<Type>::Stack(){
	top = 0;
}

template <class Type>
bool Stack<Type>::isempty() const{
	return top == 0;
}

template <class Type>
bool Stack<Type>::isfull() const{
	return top == MAX;
}

template <class Type>
bool Stack<Type>::push(const Type & item){
	if(top < MAX){
		items[top++] = item;
		return true;
	}else{
		return false;
	}   
}

template <class Type>
bool Stack<Type>::pop(Type & item){
	if (top > 0){ 
		item = items[--top];
		return true;
	}else{
		return false;
	}
}


#endif
