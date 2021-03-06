#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int abs(int a) {
  if(a >= 0){
    return a;
  } else if (a < 0){
    return -a;
  }
}
int main() {
  int num;
  int sum = 0;
  int result = 0;
  vector<int> v;
  cin >> num;
  v.resize(num);

  for(int i=0; i<num; i++){
    cin >> v[i];
  }
  sort(v.begin(), v.end());
  for(int j=2; j<=num; j++){
    result += abs(v[j-2]-v[j-1]);
  }
  while(next_permutation(v.begin(), v.end())){
    for(int k=2; k<=num; k++){
      sum += abs(v[k-2] - v[k-1]);
    }
    if(sum > result){
      result = sum;
    }
    sum = 0;
  }
  cout << result << "\n";
}