#include<iostream>
#include<cstring>


using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
	char ops[10];
	// 공집합으로 활용할 s ( 비트로 집합 활용 )
	int s = 0;
	int check_num;
	int x;

	int list_size;
	cin >> list_size;

	for (int i = 0; i < list_size; i++) {
		cin >> ops;
		if (!strcmp(ops, "add")) {
            cin >> x;
            x--;
			s = s | (1 << x);
		}
		else if (!strcmp(ops, "remove")) {
            cin >> x;
            x--;
			s = s & ~(1 << x);
		}
		else if (!strcmp(ops, "check")) {
            cin >> x;
            x--;
			check_num = (s & (1 << x));
			if (check_num) {
				cout << "1\n";
			}
			else {
				cout << "0\n";
			}
		}
		else if (!strcmp(ops, "toggle")) {
            cin >> x;
            x--;
			s = s ^ (1 << x);
		}
		else if (!strcmp(ops, "all")) {
			s = (1 << 20) - 1;
		}
		else if (!strcmp(ops, "empty")) {
			s = 0;
		}
	}
	return 0;
}