#include <iostream>
//E=15, S=28, M=19
using namespace std;
int main() {
  int a, b, c;
  int count = 1;
  cin >> a >> b >> c;
  while(true){
    bool isA = ((count-a)%15 == 0);
    bool isB = ((count-b)%28 == 0);
    bool isC = ((count-c)%19 == 0);
    if(isA && isB && isC){
      break;
    } else {
      count++;
    }
  }
  cout << count << "\n";
}