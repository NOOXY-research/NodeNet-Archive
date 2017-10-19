#include<iostream>
#include"matrix.h"
using namespace std;
int main() {
  matrix M1(1000, 1000), M2(1000, 1000);
  // M.print();
  for(int i = 0; i < 1000; i++) {
    M1 = M1 + M2;
  }
  // M = M + M;
  M1.print();
}
