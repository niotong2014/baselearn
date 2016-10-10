/*************************************************************************
	> File Name: namesp.h
	> Author: niotong
	> Mail: niotong2014@sina.com 
	> Created Time: 2016年10月04日 星期二 17时34分47秒
 ************************************************************************/

#include <string>
namespace pers{
	struct Person{
		std::string fname;
		std::string lname;
	};
	void getPerson (Person &);
	void showPerson(const Person &);
}

namespace debts{
	using namespace pers;
	struct Debt{
		Person name;
		double amount;
	};
	void getDebt(Debt &);
	void showDebt(const Debt &);
	double sumDebts(const Debt ar[],int n);
}

