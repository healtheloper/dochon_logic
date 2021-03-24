#include <iostream>
#include <vector>

using namespace std;
vector<int> v;
long long n, m;

bool check(int mid) {
	long long length = 0;

	for (int i = 0; i < n; i++) {
		if (v[i] > mid) {
			length += v[i] - mid;
		}
	}

	return length >= m;
}

int main(void) {

	long long max = 0;

	cin >> n >> m;

	v.resize(n);

	for (int i = 0; i < n; i++) {
		cin >> v[i];
		if (max < v[i]) {
			max = v[i];
		}
	}

	long long l = 1;
	long long r = max;
	long long result = 0;

	while (l <= r) {

		long long mid = (l + r) / 2;

		if (check(mid)) {
			if (result < mid) {
				result = mid;
			}
			l = mid + 1;
		}
		else {
			r = mid - 1;
		}
	}

	cout << result;
	
	return 0;
}