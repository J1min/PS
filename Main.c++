#include <iostream>
using namespace std;

class SimpleClass
{
private:
	int num;
public:
	SimpleClass(int n): num(n) {}
	SimpleClass& Adder(int n)
	{
		num += n;
		return *this;
	}
	SimpleClass& ShowSimpleData()
	{ 
		cout << num << endl;
		return *this;
	}
};

int main(void)
{
	SimpleClass sc1(100);
	SimpleClass sc2 = sc1.Adder(100);
	SimpleClass& sc3 = sc1.Adder(100);
	
	sc1.ShowSimpleData();
	sc2.ShowSimpleData();
	sc3.ShowSimpleData();
	
	return 0;
}