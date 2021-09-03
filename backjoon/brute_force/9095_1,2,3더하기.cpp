#include <iostream>
#include <vector>
using namespace std;

int count = 0;
vector<int> v;
void df(int data) {
  if(data == 0){
    count++;
    return;
  }
  if(data-3>=0){
    df(data-3);
  }
  if(data-2>=0){
    df(data-2);
  }
  if(data-1>=0){
    df(data-1);
  }
}
int main() {
  // cin,cout 속도향상
  ios_base::sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);
  int num;
  cin >> num;
  v.resize(num);
  for(int i=0; i<num; i++){
    cin >> v[i];
  }
  for(int j=0; j<num; j++){
    if(v[j] == 3){
      count = 4;
    }else if(v[j] == 2){
      count = 2;
    }else if(v[j] == 1){
      count = 1;
    }else {
      df(v[j]);
    }
    cout << count << "\n";
    count = 0;
  }
}
