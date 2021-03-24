#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<vector<int>> arr;
vector<int> box;
vector<int> number;

void lotto(int num, vector<int> v){
  vector<int> ind;
  int cnt = 0;
  for(int i=0; i<6; i++){
        ind.push_back(1);
      }
      for(int i=0; i<num-6; i++){
        ind.push_back(0);
      }
      //1 1 1 1 1 1 0
      //1 1 1 1 1 0 1
      // .....
      //0 1 1 1 1 1 1
      do{
        for(int i=0; i<num; i++){
          if(ind[i] == 1){
            box.push_back(v[i]);
          }
        }
        arr.push_back(box);
        box.clear();
        cnt++;
      }while(prev_permutation(ind.begin(), ind.end()));
      number.push_back(cnt);
}
int main() {
    int count = 0;
    while(true){
      int num;
      cin >> num;
      if(num == 0){
        for(int i=0; i<arr.size(); i++){
          for(int j=0; j<6; j++){
            cout << arr[i][j] << " ";
          }
          cout << "\n";
          if(i >= number[count]-1){
            cout << "\n";
            count++;
            number[count] += number[count-1];
          }
        }
        break;
      }
      vector<int>v;
      v.resize(num);
      for(int i=0; i<num; i++){
        cin >> v[i];
      }
      sort(v.begin(), v.end());
      lotto(num, v);
    }
}