#include <iostream>
using namespace std;
int n;
int m;
int price[20];
int preference[20];
// ver3. repetitive dp + sliding window
// 초밥 가격 100의 배수 -> 가격을 100으로 나누기
// 모든 초밥의 가격은 2만원 이하 -> 가격을 100으로 나누었으므로 200원 이하
// -> budget-200 ~ budget 까지 계산된 값을 저장할 공간이 필요함 -> 201개의 메모리 필요
int sw[201];
int FindMaxPref_sliding_window()
{
	m = m / 100; // 총 예산 100으로 나누기
	sw[0] = 0;
	for(int budget=1 ; budget <= m ; budget++)
	{
		sw[budget%201] = 0;
		for(int i = 0 ; i < n ; i++)
		{
			int targetPrice = price[i]/100; // 스시 가격 100으로 나누기
			int targetPref = preference[i];
			if(budget < targetPrice) continue;
			sw[budget%201] = max(sw[budget%201], sw[(budget-targetPrice)%201]+targetPref);
		}
	}
	return sw[m%201];
}

int main(void)
{
	cin >> n >> m;
	for(int i = 0 ; i < m ; i++)
		cin >> price[i] >> preference[i];
	cout << FindMaxPref_sliding_window() << endl;
	return 0;
}
