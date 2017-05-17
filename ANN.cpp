#include <iomanip>//setprecision
#include <iostream>
#include <string.h>//memcpy()
#include <math.h>//pow()
using namespace std;

class matrix {
  public:
    matrix();
    int print();
    int sigmoid();
    friend martix& operator =(const matrix& m1);
    friend martix operator +(const matrix& m1, const matrix& m2);
    friend martix operator -(const matrix& m1, const matrix& m2);
    friend martix operator *(const matrix& m1, const matrix& m2);
    friend martix operator /(const matrix& m1, const matrix& m2);
    friend martix operator -(const matrix& m1);
    friend bool operator ==(const matrix& m1, const matrix& m2);
    friend istream operator >>(istream& ins, matrix& m1);
    friend ostream operator <<(ostream& ins, matrix& m1);
  private:
    int row, column;
    double *a;
};
int main() {
  matrix mymatix;
}
