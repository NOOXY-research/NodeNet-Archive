#include <iostream>
#include <iomanip>//setprecision
#include <math.h>//pow()
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
using namespace std;
double sigmoid(double x1);
double dsigmoid(double x1);
double logit(double x1);
double sigmoid(double x1) {
  double answer;
  answer = (1.0) / (1 + pow(2.7182818284590452353602874713527, -x1));
  return answer;
}
double dsigmoid(double x1) {
  double answer;
  answer = (pow(2.7182818284590452353602874713527, -x1)) / pow((1 + pow(2.7182818284590452353602874713527, -x1)), 2);
  return answer;
}
double logit(double x1) {
  double answer;
  answer = log(x1 / (1 - (x1)));
  return answer;
}
class matrix {
  public:
    matrix();
    matrix(const matrix& m1);
    matrix& operator =(const matrix& m1);
    ~matrix();
    matrix(int row, int column);
    matrix(int row, int column, double value);
    matrix(int row, int column, double* value);
    int setmatrix(int row, int column, double* a);
    int setmatrix(double* a);
    int get_row();
    int get_column();
    int print();
    double length();
    matrix transfer(double (*function)(double));
    matrix transpose();
    friend matrix multi(const matrix& m1, const matrix& m2);
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
matrix& matrix::operator =(const matrix& m1) {
  if(&m1 == this)
    return *this;
  int i, j;
  this->a = new double[m1.row * m1.column];
  this->row = m1.row;
  this->column = m1.column;
  for(i = 0; i < m1.row; i++) {
      for(j = 0; j < m1.column; j++) {
          this->a[i * m1.column + j] = m1.a[i * m1.column + j];
      }
  }
  return *this;
}
matrix::matrix(const matrix& m1) {
  if(&m1 != this) {
    int i, j;
    this->a = new double[m1.row * m1.column];
    this->row = m1.row;
    this->column = m1.column;
    for(i = 0; i < m1.row; i++) {
        for(j = 0; j < m1.column; j++) {
            this->a[i * m1.column + j] = m1.a[i * m1.column + j];
        }
    }
  }
}
matrix::~matrix() {
  delete [] a;
}
matrix::matrix(int row, int column) {
  srand (time(NULL));
  int i, j;
  this->a = new double[row * column];
  this->row = row;
  this->column = column;
  for(i = 0; i < this->row; i++) {
      for(j = 0; j < this->column; j++) {
        this->a[i * this->column + j] = rand() % 10 - rand() % 10;
      }
  }
}
matrix::matrix(int row, int column, double value) {
  int i, j;
  this->a = new double[row * column];
  this->row = row;
  this->column = column;
  for(i = 0; i < this->row; i++) {
      for(j = 0; j < this->column; j++) {
        this->a[i * this->column + j] = value;
      }
  }
}
matrix::matrix(int row, int column, double* value) {
  int i, j;
  this->a = new double[row * column];
  this->row = row;
  this->column = column;
  for(i = 0; i < this->row; i++) {
      for(j = 0; j < this->column; j++) {
        this->a[i * this->column + j] = value[i * this->column + j];
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
      this->a[i * this->column + j] = a[i * this->column + j];
    }
  }
  return 0;
}
int matrix::setmatrix(double* a) {
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
    cout << "c" << j + 1 <<"      ";
  }
  cout << endl;
  for(i = 0; i < this->row; i++) {
    cout << ">>>r" << i + 1 << " ";
      for(j = 0; j < this->column; j++) {
        cout << fixed;
        cout << setprecision(5);
        cout << this->a[i * this->column + j] << " ";
      }
      cout << endl;
  }
  return 0;
}
double matrix::length() {
  double sum = 0;
  int i, j;
  for(i = 0; i < this->row; i++) {
    for(j = 0; j < this->column; j++) {
      sum += pow(this->a[i * this->column + j], 2);
    }
  }
  return sqrt(sum);
}
matrix matrix::transfer(double (*function)(double)) {
  matrix answer(this->row, this->column);
  int i, j;
  for(i = 0; i < this->row; i++) {
      for(j = 0; j < this->column; j++) {
          answer.a[i * this->column + j] = (*function)(this->a[i * this->column + j]);
      }
  }
  return answer;
}
matrix matrix::transpose(){
  matrix answer(this->column, this->row);
  int i, j;
  for(i = 0; i < this->column; i++) {
      for(j = 0; j < this->row; j++) {
          answer.a[i * this->row + j] = this->a[j * this->column + i];
      }
  }
  return answer;
}
matrix multi(const matrix& m1, const matrix& m2) {
  if (m1.row != m2.row || m1.column != m2.column) {
    cout << "matrix error: multi" << endl;
    matrix err(0, 0);
    return err;
  }
  int i, j;
  matrix answer(m1.row, m1.column);
  for(i = 0; i < m1.row; i++) {
      for(j = 0; j < m1.column; j++) {
          answer.a[i * m1.column + j] = m1.a[i * m1.column + j] * m2.a[i * m1.column + j];
      }
  }
  return answer;
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
    int setweight(matrix *weight);
    int print();
    int feed_and_train(matrix input, matrix output, double speed);
    matrix feed(matrix input);
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
      matrix new_matrix(neurons_size[i], neurons_size[i + 1]);
      this->weight[i] = new_matrix;
    }
  }
}
ANN::ANN(int layers_size,int *neurons_size,matrix *weight) {
  int i, j, neurons_size_sum = 0;
  this->layers_size = layers_size;
  this->neurons_size = new int[layers_size];
  this->weight = new matrix[layers_size - 1];
  for(i = 0; i < this->layers_size; i++) {
    this->neurons_size[i] = neurons_size[i];
    if(i < this->layers_size -1) {
      if (weight[i].get_row() != neurons_size[i] || weight[i].get_column() != neurons_size[i + 1])
        cout << "ann error: weights not fit neurons size" << endl;
      this->weight[i] = weight[i];
    }
  }
}
int ANN::setweight(matrix *weight) {
  int i, j;
  for(i = 0; i < this->layers_size; i++) {
    if(i < this->layers_size -1) {
      if (weight[i].get_row() != this->neurons_size[i] || weight[i].get_column() != this->neurons_size[i + 1])
        cout << "ann error: weights not fit neurons size" << endl;
      this->weight[i] = weight[i];
    }
  }
  return 0;
}
int ANN::print() {
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
int ANN::feed_and_train(matrix input, matrix output,double speed) {
  int i, j;
  matrix delta[this->layers_size], dj_dweight[this->layers_size - 1], a[this->layers_size], z[this->layers_size];
  matrix a1, a2;
  z[0] = input;
  a1 = input.transfer(sigmoid);
  for(i = 0; i < this->layers_size -1; i++) {
    a[i] = a1;
    z[i + 1] = a1 * weight[i];
    a2 = (a1 * weight[i]).transfer(sigmoid);
    a1 = a2;
  }
  delta[this->layers_size - 1] = multi(-(output.transfer(sigmoid) - a1), z[this->layers_size - 1].transfer(dsigmoid));
  for(i = this->layers_size - 1; i > 0 ; i--) { // i start max layers_size
    dj_dweight[i - 1] = a[i - 1].transpose() * delta[i];
    delta[i - 1] = multi(delta[i] * weight[i - 1].transpose(), z[i - 1].transfer(dsigmoid));
  }
  for(i = 0; i < this->layers_size - 1; i++) {
    this->weight[i] = this->weight[i] - speed * dj_dweight[i];
  }
  speed = speed;
  return 0;
}
matrix ANN::feed(matrix input) {
  int i, j;
  matrix a1, a2;
  a1 = input.transfer(sigmoid);
  for(i = 0; i < this->layers_size -1 ; i++) {
    a2 = (a1 * weight[i]).transfer(sigmoid);
    a1 = a2;
  }
  return a1;
}
int main() {
  int neurons_size[5] = {1, 4, 4, 1};
  double x[10] = {0, 1, 2, 3, 4}, y[10] = {0, 2, 4, 6, 8};
  matrix X, Y;
  X.setmatrix(5, 1, x);
  Y.setmatrix(5, 1, y);
  ANN myann(4, neurons_size);
  cout << "***--before" << endl;
  myann.print();
  cout << "-----out" << endl;
  (Y.transfer(sigmoid)).print();
  cout << "-----feed" << endl;
  (myann.feed(X)).print();
  cout << "-----out origin" << endl;
  (Y).print();
  cout << "-----feed origin" << endl;
  ((myann.feed(X)).transfer(logit)).print();
  cout << "-----err" << endl;
  cout << ">>>" << (myann.feed(X) - Y.transfer(sigmoid)).length() << endl;
  cout << "***--after_train" << endl;
  double firsterr = (myann.feed(X) - Y.transfer(sigmoid)).length();
  for (int i = 0; i < ((myann.feed(X) - Y.transfer(sigmoid)).length() / firsterr) * 100; i++)
    cout << "*";
  int count = 0;
  while((myann.feed(X) - Y.transfer(sigmoid)).length() > 0.0005) {
    if(count % 100 == 0) {
      for (int i = 0; i < ((myann.feed(X) - Y.transfer(sigmoid)).length() / firsterr) * 100; i++)
        cout << "*";
      cout << endl;
    }
    myann.feed_and_train(X, Y, 5);
    count ++;
  }
  myann.print();
  cout << "-----out" << endl;
  (Y.transfer(sigmoid)).print();
  cout << "-----feed" << endl;
  (myann.feed(X)).print();
  cout << "-----out origin" << endl;
  (Y).print();
  cout << "-----feed origin" << endl;
  ((myann.feed(X)).transfer(logit)).print();
  cout << "-----err" << endl;
  cout << ">>>" << (myann.feed(X) - Y.transfer(sigmoid)).length() << endl;
  cout << "-----predict -1 (answer -2)" << endl;
  double p[1] = {-1};
  matrix P(1, 1, p);
  (myann.feed(P).transfer(logit)).print();
}
