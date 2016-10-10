/*************************************************************************
	> File Name: namessp.cpp
	> Author: niotong
	> Mail: niotong2014@sina.com 
	> Created Time: 2016年10月04日 星期二 17时52分38秒
 ************************************************************************/

#include<iostream>
#include "namesp.h"

void other(void);
void another(void);

int main(void){
	using debts::Debt;
	using debts::showDebt;

	Debt golf = {{"niotong","yuan"},12.0};
	showDebt(golf);
	other();
	another();
	return 0;
}

void other(void){
	using std::cout;
	using std::endl;
	using namespace debts; //因为命名空间中已经using namespace pers了，所以不用单独using了
	Person dg = {"Doodles","Glister"};
	showPerson(dg);
	cout << endl;
	Debt zippy[3];
	int i;
	for(i = 0;i<3;i++){
		getDebt(zippy[i]);
	}
	for(i = 0;i<3;i++){
		showDebt(zippy[i]);
	}
	cout << "Total debt:$" << sumDebts(zippy,3) <<endl;
	return;
}

void another(void){
	using pers::Person;
	Person collector = {"Milo","Rightshift"};
	pers::showPerson(collector);
	std::cout << std::endl;
}
