#include <iostream>
#include <vector>

using namespace std;
vector<int> v;
vector<int>::iterator iter;
long long k, n;

bool check(int x) {
	long long count = 0;
	for (iter = v.begin(); iter != v.end(); iter++) {
		count += *iter / x;
	}
	return count >= n;
}

int main(void) {

	long long length, max = 0;
	
	cin >> k >> n;

	v.resize(k);

	for (iter = v.begin(); iter != v.end(); iter++) {
		cin >> length;
		if (max < length)
			max = length;
		*iter = length;
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