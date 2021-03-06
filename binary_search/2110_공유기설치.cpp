#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, c;
vector<int> v;

/* 
 *           1 2 4 8 9
 * result 1  o o o o o
 * result 2  o x o o x
 * result 3  o x o o x
 * result 4  o x x o x
 * result 5  o x x x x
 */ 


// mid = 4

bool check(int mid, vector<int> &v) {
	// 1일 때 다 o
	int count = 1;
	for (int i = 0; i < (v.size()-1); i++) {
		// 1 + 4 >= 2 ? x
		// 2 + 4 >= 4 ? x
		// 4 + 4 >= 8 ? o
		// 8 + 4 >= 9 ? x
		// count = 2
		if (v[i] + mid <= v[i + 1]) {
			count++;
		}
	}
	// 2 >= 3 : false
	return count >= c;
}

int main(void) {

	cin >> n >> c;

	v.resize(n);

	for (int i = 0; i < n; i++) {
		cin >> v[i];
	}

	sort(v.begin(), v.end());

	int l = 1; // 1
	int r = v[n - 1] - v[0]; // 1 2 4 8 9 에서 1 과 9 의 차이 = 8
	int result = 0;

	while (l <= r) {
		// (1 + 8) / 2 = 4
		// mid = 3
		int mid = (l + r) / 2;
		if (check(mid, v)) {
			// 0 < 2
			if (result < mid) {
				// result = 2
				result = mid;
			}
			// l = 2 + 1 = 3
			l = mid + 1;
		}
		else {
			// r = 4 - 1 = 3
			r = mid - 1;
		}
	}

	cout << result;

	return 0;
}