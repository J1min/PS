#include <iostream>
using namespace std;

#define ID_LEN 20

struct Car
{
	char gamerID[ID_LEN];
	int fuelGauge;
	int curSpeed;
};

int main(void)
{
	struct Car car1;
	Car car2;
	return 0;
}