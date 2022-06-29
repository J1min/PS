#include <bits/stdc++.h>
using namespace std;
namespace A
{
	namespace B
	{
		namespace C
		{
			bool a = false;
		}
	}
}
int main()
{
	cout << A::B::C::a << endl;
	namespace ABC = A::B::C;
	cout << ABC::a;
}