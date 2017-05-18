#include <iostream>
#include <iomanip>//setprecision
#include <math.h>//pow()
using namespace std;
class matrix {
  public:
    matrix();
    ~matrix();
    matrix(int row, int column);
    matrix(int row, int column, double value);
    int setmatrix(int row, int column, double* a);
    int setmatrix(double* a);
    int get_row();
    int get_column();
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
  private:
    int row, column;
    double *a;
};
matrix::matrix() {
  this->row = 1;
  this->column = 1;
  this->a = new double[1];
  a[0] = 0;
}
matrix::~matrix() {
  delete [] a;
}
matrix::matrix(int row, int column) {
  int i, j;
  this->a = new double[row * column];
  this->row = row;
  this->column = column;
  for(i = 0; i < row; i++) {
      for(j = 0; j < column; j++) {
        this->a[i * column + j] = 0;
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
        this->a[i * column + j] = value;
      }
  }
}
int matrix::setmatrix(int row, int column, double* a) {
  int i, j;
  this->a = new double[row * column];
  this->row = row;
  this->column = column;
  for(i = 0; i < row; i++) {
    for(j = 0; j < column; j++) {
      this->a[i * column + j] = a[i * column + j];
    }
  }
  return 0;
}
int matrix::setmatrix(double* a) {
  cout << "<>" << endl;
  int i, j;
  for(i = 0; i < this->row; i++) {
    for(j = 0; j < this->column; j++) {
      this->a[i * this->column + j] = a[i * this->column + j];
    }
  }
  return 0;
}
int matrix::get_row() {
  return this->row;
}
int matrix::get_column() {
  return this->column;
}
int matrix::print() {
  int i, j;
  cout << ">>>" << this->row << " by " << this->column << " matrix." << endl;
  cout << ">>>   ";
  for(j = 0; j < this->column; j++) {
    cout << "c" << j + 1 <<"   ";
  }
  cout << endl;
  for(i = 0; i < this->row; i++) {
    cout << ">>>r" << i + 1 << " ";
      for(j = 0; j < this->column; j++) {
        cout << fixed;
        cout << setprecision(2);
        cout << this->a[i * column + j] << " ";
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
class ANN {
  public:
    ANN(int layers_size,int *neurons_size);
    ANN(int layers_size,int *neurons_size,matrix *weight);
    int print();
    matrix feed(matrix input);
    int feed_and_train();
  private:
    int layers_size, *neurons_size;
    matrix *weight;
};
ANN::ANN(int layers_size,int *neurons_size) {
  int i, j, neurons_size_sum = 0;
  this->layers_size = layers_size;
  this->neurons_size = new int[layers_size];
  this->weight = new matrix[layers_size - 1];
  for(i = 0; i < layers_size; i++) {
    this->neurons_size[i] = neurons_size[i];
    if(i < layers_size -1) {
      matrix new_matrix(neurons_size[i], neurons_size[i + 1], 1);
      this->weight[i] = new_matrix;
    }
  }
}
int ANN::print()
{
  int i, j;
  cout<<">>>*ANN info"<<endl;
  for(i = 0; i < this->layers_size; i++) {
    cout<<">>>";
    cout << "N(" <<  i << "): " << this->neurons_size[i]<<endl;
    if(i < this->layers_size -1) {
      this->weight[i].print();
    }
  }
  cout<<endl;
  return 0;
}
matrix ANN::feed(matrix input) {
  int i, j;
  matrix a1, a2;
  for(i = 0; i < this->layers_size -1 ; i++) {
    //a1 = (input * ).sigmoid();
  }
}
int main() {
  int neurons_size[4] = {2, 3, 4, 2};
  double x[4] = {3, 2, 1, 0}, y[2] = {8, 2};
  ANN myann(4, neurons_size);
  myann.print();
  matrix X;
  //matrix Y(2, 1);
  //X.setmatrix(x);
  //Y.setmatrix(y);
  //(X * Y).print();
}
