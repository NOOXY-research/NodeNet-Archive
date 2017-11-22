#include<iostream>
#include <time.h>
#include"matrix_CUDA.h"
using namespace std;

int main() {
  time_t seconds;
  int normal, CUDA;
  double a[4] = {1, 2, 3, 4};
  matrix A(2, 2, a);
  A.load_from_file("big");

  seconds = time (NULL);
  for(int i = 0; i < 5000; i++) {
    (A * A);
  }
  normal = time(NULL) - seconds;
  cout << "CPU done" << endl;

  seconds = time (NULL);
  cuda_init();
  for(int i = 0; i < 5000; i++) {
    (A * A);
  }
  CUDA = time(NULL) - seconds;
  cout << "GPU done" << endl;

  cout << normal << " " << CUDA << " " << time (NULL) << endl;
 }
