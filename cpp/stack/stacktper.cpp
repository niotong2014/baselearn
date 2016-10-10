/*************************************************************************
	> File Name: stacktper.cpp
	> Author: niotong
	> Mail: niotong2014@sina.com 
	> Created Time: 2016年10月10日 星期一 23时49分17秒
 ************************************************************************/

#include<iostream>
#include <cctype>
#include "stacktp.h"

int main(){
	using namespace std;
	Stack<int> st;
	char ch;
	int po;
	cout << "Please enter A to add a purchase order,\n"
		<<"P to process a PO, or Q to quit.\n";
	while(cin >> ch && toupper(ch) != 'Q'){
		while(cin.get() != '\n'){
			continue;
		}
		if (!isalpha(ch)){
			cout << '\a';
			continue;
		}
		switch(ch){
			case 'A':
			case 'a':
				cout << "Enter a PO number to add:";
				cin >> po;
				if( st.isfull()){
					cout << "Stack already full\n";
				}else{
					st.push(po);
				}
				break;
			case 'P':
			case 'p':
				if(st.isempty()){
					cout << "Stack already empty\n";
				}else{
					st.pop(po);
					cout << "PO #" << po << "poped\n";
				}
				break;
			default:
				break;
		}
		cout << "Please enter A to add a purchase order,\n"
			<<"P to process a PO, or Q to quit.\n";

	}
	cout << "Bye\n";
	return 0;


	return 0;
}

