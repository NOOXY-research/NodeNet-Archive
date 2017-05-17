#include <iostream>
#include <iomanip>//setprecision
#include <math.h>//pow()
using namespace std;
class matrix {
  public:
    matrix();
    matrix(int row, int column);
    matrix(int row, int column, double value);
    int setmatrix(int row, int column, double* a);
    int print();
    int sigmoid();
    matrix& operator =(const matrix& m1);
    friend matrix operator +(const matrix& m1, const matrix& m2);
    friend matrix operator -(const matrix& m1, const matrix& m2);
    friend matrix operator *(const matrix& m1, const matrix& m2);
    friend matrix operator *(const int& x1, const matrix& m1);
    friend matrix operator *(const matrix& m1, const int& x1);
    friend matrix operator /(const int& x1, const matrix& m1);
    friend matrix operator /(const matrix& m1, const int& x1);
    friend matrix operator -(const matrix& m1);
    friend bool operator ==(const matrix& m1, const matrix& m2);
    friend istream& operator >>(istream& ins,const matrix& m1);
    friend ostream& operator <<(ostream& ins,const matrix& m1);
  private:
    int row, column;
    double *a;
};
matrix::matrix() {

}
matrix::matrix(int row, int column) {
  int i, j;
  this->a = new double[row * column];
  this->row = row;
  this->column = column;
  for(i = 0; i < row; i++) {
      for(j = 0; j < column; j++) {
        a[i*column+j] = 0;
      }
  }
}
matrix::matrix(int row, int column, double value) {
  int i, j;
  this->a = new double[row * column];
  this->row = row;
  this->column = column;
  for(i = 0; i < row; i++) {
      for(j = 0; j < column; j++) {
        a[i*column+j] = value;
      }
  }
}
int matrix::setmatrix(int row, int column, double* a) {
  int i, j;
  this->a = new double[row * column];
  for(i = 0; i < row; i++) {
    for(j = 0; j < column; j++) {
      this->a[i * column + j] = a[i * column + j];
    }
  }
  return 0;
}
int matrix::print() {
  int i, j;
  cout << ">>>" << row << " by " << column << " matrix." << endl;
  cout << ">>>   ";
  for(j = 0; j < column; j++) {
    cout << "c" << j + 1 <<"   ";
  }
  cout << endl;
  for(i = 0; i < row; i++) {
    cout << ">>>r" << i + 1 << " ";
      for(j = 0; j < column; j++) {
        cout << fixed;
        cout << setprecision(2);
        cout << a[i * column + j] << " ";
      }
      cout << endl;
  }
  return 0;
}
int matrix::sigmoid() {
  int i, j;
  for(i = 0; i < row; i++) {
      for(j = 0; j < column; j++) {
          a[i * column + j] = (1.0) / (1 + pow(2.7182818284590452353602874713527, -a[i * column + j]));
      }
  }
  return 0;
}
matrix& matrix::operator =(const matrix& m1) {
  if(&m1 == this)
    return *this;
  int i, j;
  this->row = m1.row;
  this->column = m1.column;
  for(i = 0; i < m1.row; i++) {
      for(j = 0; j < m1.column; j++) {
          this->a[i * m1.column + j] = m1.a[i * m1.column + j];
      }
  }
  return *this;
}
matrix operator +(const matrix& m1, const matrix& m2) {
  if (m1.row != m2.row || m1.column != m2.column) {
    cout << "matrix error: operator +" << endl;
    matrix err(0, 0);
    return err;
  }
  int i, j;
  matrix answer(m1.row, m1.column);
  for(i = 0; i < m1.row; i++) {
      for(j = 0; j < m1.column; j++) {
          answer.a[i * m1.column + j] = m1.a[i * m1.column + j] + m2.a[i * m1.column + j];
      }
  }
  return answer;
}
matrix operator -(const matrix& m1, const matrix& m2) {
  if (m1.row != m2.row || m1.column != m2.column) {
    cout << "matrix error: operator -" << endl;
    matrix err(0, 0);
    return err;
  }
  int i, j;
  matrix answer(m1.row, m1.column);
  for(i = 0; i < m1.row; i++) {
      for(j = 0; j < m1.column; j++) {
          answer.a[i * m1.column + j] = m1.a[i * m1.column + j] - m2.a[i * m1.column + j];
      }
  }
  return answer;
}
matrix operator *(const matrix& m1, const matrix& m2) {
  if (m1.column != m2.row) {
    cout << "matrix error: operator *" << endl;
    matrix err(0, 0);
    return err;
  }
  matrix answer(m1.row, m2.column);
  int i, j, k;
  for(i = 0; i < m1.row; i++) {
      for(j = 0; j < m2.column; j++) {
          double temp = 0;
          for(k = 0; k < m1.column; k++) {
              temp += m1.a[i * m1.column + k] * m2.a[k * m2.column + j];
          }
          answer.a[i * m2.column + j] = temp;
      }
  }
  return answer;
}
matrix operator *(const int& x1, const matrix& m1) {
  int i, j;
  matrix answer(m1.row, m1.column);
  for(i = 0; i < m1.row; i++) {
      for(j = 0; j < m1.column; j++) {
          answer.a[i * m1.column + j] = x1 * m1.a[i * m1.column + j];
      }
  }
  return answer;
}
matrix operator *(const matrix& m1, const int& x1) {
  int i, j;
  matrix answer(m1.row, m1.column);
  for(i = 0; i < m1.row; i++) {
      for(j = 0; j < m1.column; j++) {
          answer.a[i * m1.column + j] = x1 * m1.a[i * m1.column + j];
      }
  }
  return answer;
}
matrix operator /(const int& x1, const matrix& m1) {
  int i, j;
  matrix answer(m1.row, m1.column);
  for(i = 0; i < m1.row; i++) {
      for(j = 0; j < m1.column; j++) {
          answer.a[i * m1.column + j] = x1 / m1.a[i * m1.column + j];
      }
  }
  return answer;
}
matrix operator /(const matrix& m1, const int& x1) {
  int i, j;
  matrix answer(m1.row, m1.column);
  for(i = 0; i < m1.row; i++) {
      for(j = 0; j < m1.column; j++) {
          answer.a[i * m1.column + j] = m1.a[i * m1.column + j] / x1;
      }
  }
  return answer;
}
matrix operator -(const matrix& m1) {
  int i, j;
  matrix answer(m1.row, m1.column);
  for(i = 0; i < m1.row; i++) {
      for(j = 0; j < m1.column; j++) {
          answer.a[i * m1.column + j] = -m1.a[i * m1.column + j];
      }
  }
  return answer;
}
bool operator ==(const matrix& m1, const matrix& m2) {
  int i, j;
  bool answer = true;
  for(i = 0; i < m1.row; i++) {
      for(j = 0; j < m1.column; j++) {
          if(m1.a[i * m1.column + j] != m2.a[i * m1.column + j])
            answer = false;
      }
  }
  return answer;
}
int main() {
  matrix mymatix(3, 2);
  matrix mymatix2(4, 2);
  double a[6] = {1, 2, 3, 4, 5, 6};
  mymatix.setmatrix(3, 2, a);
  mymatix.sigmoid();
  mymatix2 = mymatix2 + mymatix;
  mymatix2.print();
}
