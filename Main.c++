#include<iostream>
#include<stack>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0);   cin.tie(0);

	stack<pair<int, int>> s;
	int n;

	cin >> n;
	vector<int> answer(n, -1);
	for (int i = 0; i < n; i++) {
		int in;
		cin >> in;

		if (s.empty()) {
			s.push({ i, in });
		}
		else {
			if (s.top().second < in) {
				while (!s.empty()) {
					if (s.top().second > in) {
						break;
					}

					answer[s.top().first] = in;
					s.pop();
				}
			}
			s.push({ i, in });
		}
	}

	for (int i = 0; i < answer.size(); i++) {
		cout << answer[i] << ' ';
	}

	return 0;
}