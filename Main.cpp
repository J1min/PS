#include <iostream>
using namespace std;

bool relation[10][10];
int n;
int m;

int CountParing(bool taken[])
{
	bool check = true;  // 모든 학생들이 짝을 지었는지 확인
	int first = -1;     // 짝이 없는 학생들 중 가장 낮은 번호
	for(int i = 0 ; i < n ; i++)
		if(!taken[i]){    // 짝이 없는 학생이 있으면
			check = false;
			first = i;
			break;
		}
	if(check) return 1;  // 모든 학생들이 짝을 이루었으면 짝을 짓는 방법의 수 1가지
	
	int count = 0;       // 현재 짝이 없는 학생들로 짝을 지을 수 있는 경우의 수
	for(int j = first+1 ; j < n ; j++) // first 번호의 학생과 짝을 이룰 수 있는 학생의 번호는 first보다 큰 번호
	{
		if(!taken[j] && relation[first][j]) // j번 학생이 짝이 없고, first번 학생과 친구 관계이면
		{
			taken[first] = true;
			taken[j] = true;
			count += CountParing(taken);
			taken[first] = false;
			taken[j] = false;
		}
	}
	return count;
}

int main() {
	cin >> n >> m;
	for(int i = 0 ; i < m ; i++)
	{
		int s1, s2;
		cin >> s1 >> s2;
		relation[s1][s2] = true;
		relation[s2][s1] = true;
	}
	bool taken[10];
	for(int i = 0 ;i  < 10 ; i++)
		taken[i] = false;
	
	cout << CountParing(taken) << endl;
	
	return 0;
}