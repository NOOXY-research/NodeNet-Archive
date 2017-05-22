#include <iostream>
#include <fstream> //file
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
    int save_to_file(string filename);
    int load_from_file(string filename);
    double length();
    matrix transfer(double (*function)(double));
    matrix transpose();
    friend matrix multi(const matrix& m1, const matrix& m2);
    friend matrix operator +(const matrix& m1, const matrix& m2);
    friend matrix operator -(const matrix& m1, const matrix& m2);
    friend matrix operator *(const matrix& m1, const matrix& m2);
    friend matrix operator *(const double& x1, const matrix& m1);
    friend matrix operator *(const matrix& m1, const double& x1);
    friend matrix operator /(const double& x1, const matrix& m1);
    friend matrix operator /(const matrix& m1, const double& x1);
    friend matrix operator -(const matrix& m1);
    friend bool operator ==(const matrix& m1, const matrix& m2);
    friend ostream& operator<<(ostream &out, const matrix& m1);
    friend istream& operator>>(istream &in, matrix& m1);
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
  delete [] this->a;
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
    // delete [] this->a;
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
        this->a[i * this->column + j] = rand() % 5 - rand() % 5;
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
  delete [] this->a;
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
    cout << "c" << j + 1 <<"    ";
  }
  cout << endl;
  for(i = 0; i < this->row; i++) {
    cout << ">>>r" << i + 1 << " ";
      for(j = 0; j < this->column; j++) {
        cout << fixed;
        cout << setprecision(3);
        cout << this->a[i * this->column + j] << " ";
      }
      cout << endl;
  }
  return 0;
}
int matrix::save_to_file(string filename) {
  ofstream myfile (filename + ".mtrx");
  myfile <<  (*this);
  return 0;
}
int matrix::load_from_file(string filename) {
  ifstream myfile (filename + ".mtrx");
  if(myfile.is_open()) {
      myfile >> (*this);
  }
  else {
    return -1;
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
matrix operator *(const double& x1, const matrix& m1) {
  int i, j;
  matrix answer(m1.row, m1.column);
  for(i = 0; i < m1.row; i++) {
      for(j = 0; j < m1.column; j++) {
          answer.a[i * m1.column + j] = x1 * m1.a[i * m1.column + j];
      }
  }
  return answer;
}
matrix operator *(const matrix& m1, const double& x1) {
  int i, j;
  matrix answer(m1.row, m1.column);
  for(i = 0; i < m1.row; i++) {
      for(j = 0; j < m1.column; j++) {
          answer.a[i * m1.column + j] = x1 * m1.a[i * m1.column + j];
      }
  }
  return answer;
}
matrix operator /(const double& x1, const matrix& m1) {
  int i, j;
  matrix answer(m1.row, m1.column);
  for(i = 0; i < m1.row; i++) {
      for(j = 0; j < m1.column; j++) {
          answer.a[i * m1.column + j] = x1 / m1.a[i * m1.column + j];
      }
  }
  return answer;
}
matrix operator /(const matrix& m1, const double& x1) {
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
ostream& operator<<(ostream &out, const matrix& m1) {
  int i, j;
  out << " " << m1.row << " " << m1.column;
  for(i = 0; i < m1.row; i++) {
      for(j = 0; j < m1.column; j++) {
        cout << fixed;
        cout << setprecision(10);
        out << " " << m1.a[i * m1.column + j];
      }
  }
  return out;
}
istream& operator>>(istream &in, matrix& m1) {
  int i, j;
  in >> m1.row >> m1.column;
  delete [] m1.a;
  m1.a = new double [m1.row * m1.column];
  for(i = 0; i < m1.row; i++) {
      for(j = 0; j < m1.column; j++) {
          in >> m1.a[i * m1.column + j];
      }
  }
  return in;
}
class ANN {
  public:
    ANN();
    ANN(int layers_size,int *neurons_size);
    ANN(int layers_size,int *neurons_size,matrix *weight);
    ANN(const ANN& ann1);
    ANN& operator =(const ANN& ann1);
    ~ANN();
    int setweight(matrix *weight);
    int randomweight();
    int print();
    int save_to_file(string filename);
    int load_from_file(string filename);
    int train(matrix input, matrix output, double speed);
    int train_pro(matrix input, matrix output, double err, int max_times, double speed, int loop);
    matrix feed(matrix input);
  private:
    int layers_size, *neurons_size;
    matrix *weight;
};
ANN::ANN () {
  this->layers_size = 1;
  this->neurons_size = new int[1];
  this->weight = new matrix[1];
}
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
ANN::ANN(const ANN& ann1) {
  int i, j, neurons_size_sum = 0;
  this->layers_size = ann1.layers_size;
  this->neurons_size = new int[ann1.layers_size];
  this->weight = new matrix[ann1.layers_size - 1];
  for(i = 0; i < this->layers_size; i++) {
    this->neurons_size[i] = ann1.neurons_size[i];
    if(i < this->layers_size -1) {
      this->weight[i] = ann1.weight[i];
    }
  }
}
ANN& ANN::operator =(const ANN& ann1) {
  if(&ann1 == this)
    return *this;
  int i, j, neurons_size_sum = 0;
  delete [] neurons_size;
  delete [] weight;
  this->layers_size = ann1.layers_size;
  this->neurons_size = new int[ann1.layers_size];
  this->weight = new matrix[ann1.layers_size - 1];
  for(i = 0; i < this->layers_size; i++) {
    this->neurons_size[i] = ann1.neurons_size[i];
    if(i < this->layers_size -1) {
      this->weight[i] = ann1.weight[i];
    }
  }
  return *this;
}
ANN::~ANN () {
  delete [] weight;
  delete [] neurons_size;
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
int ANN::randomweight() {
  int i, j;
  for(i = 0; i < this->layers_size - 1; i++) {
    matrix new_matrix(this->neurons_size[i], this->neurons_size[i + 1]);
    this->weight[i] = new_matrix;
  }
  return 0;
}
int ANN::print() {
  int i, j;
  cout<<">>>-----ANN info-----"<<endl;
  for(i = 0; i < this->layers_size; i++) {
    cout<<">>>";
    cout << "N(" <<  i << "): " << this->neurons_size[i]<<endl;
    if(i < this->layers_size -1) {
      this->weight[i].print();
    }
  }
  return 0;
}
int ANN::save_to_file(string filename) {
  int i, j;
  ofstream myfile (filename + ".ann");
  myfile << this->layers_size;
  for(i = 0; i < this->layers_size; i++) {
    myfile << " " << this->neurons_size[i];
  }
  for(i = 0; i < this->layers_size - 1; i++) {
    myfile << this->weight[i];
  }
  myfile.close();
  return 0;
}
int ANN::load_from_file(string filename) {
  int i, j;
  ifstream myfile (filename + ".ann");
  if(myfile.is_open()) {
    delete [] this->neurons_size;
    delete [] this->weight;
    myfile >> this->layers_size;
    this->neurons_size = new int[this->layers_size];
    this->weight = new matrix[this->layers_size - 1];
    for(i = 0; i < this->layers_size; i++) {
      myfile >> this->neurons_size[i];
    }
    for(i = 0; i < this->layers_size - 1; i++) {
      myfile >> this->weight[i];
    }
  }
  else {
    return -1;
  }
  return 0;
}
int ANN::train(matrix input, matrix output,double speed) {
  if (input.get_column() != this->neurons_size[0]) {
    cout << "ann error: neurons size not fit" << endl;
    matrix err(0, 0);
    return -1;
  }
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
int ANN::train_pro(matrix input, matrix output, double err, int max_times, double speed, int loop) {
  ANN good;
  double speed_max = speed;
  // this->train(input, output, speed);
  double good_err = 99999, firsterr = (this->feed(input) - output.transfer(sigmoid)).length();
  cout << "firsterr: " << firsterr << endl;
  int count = 0;
  while((this->feed(input) - output.transfer(sigmoid)).length() > err && (count < max_times || max_times == -1)) {
    if(count % loop == 0) {
      for (int i = 0; i < ((this->feed(input) - output.transfer(sigmoid)).length() / firsterr) * 160; i++)
        cout << "*";
      if ( good_err == (this->feed(input) - output.transfer(sigmoid)).length()) {
        cout << " stucked";
        speed =  double( rand() % (int(speed_max + 1))  - (rand() % 99999) * 0.00001);
      }
      if ( good_err > (this->feed(input) - output.transfer(sigmoid)).length()) {
        good_err = (this->feed(input) - output.transfer(sigmoid)).length();
        good = (*this);
      }
      if ( good_err < (this->feed(input) - output.transfer(sigmoid)).length()) {
        cout << " bad";
        (*this) = good;
        speed =  double( rand() % (int(speed_max + 1))  - (rand() % 99999) * 0.00001);
      }
      cout << endl;
      good->save_to_file("latest");
    }
    this->train(input, output, speed);
    count ++;
  }
  this->print();
  cout << ">>>-----out origin-----" << endl;
  (output).print();
  cout << ">>>-----feed origin-----" << endl;
  ((this->feed(input)).transfer(logit)).print();
  cout << ">>>-----err value-----" << endl;
  cout << fixed;
  cout << setprecision(10);
  cout << ">>>" << (this->feed(input) - output.transfer(sigmoid)).length() << endl;
  cout << ">>>-----try times-----" << endl;
  cout << count << endl;
  if (count < max_times) {
    return count;
  }
  else {
    return -1;
  }
}
matrix ANN::feed(matrix input) {
  if (input.get_column() != this->neurons_size[0]) {
    cout << "ann error: neurons size not fit" << endl;
    matrix err(0, 0);
    return err;
  }
  int i, j;
  matrix a1, a2;
  a1 = input.transfer(sigmoid);
  for(i = 0; i < this->layers_size -1 ; i++) {
    a2 = (a1 * weight[i]).transfer(sigmoid);
    a1 = a2;
  }
  return a1;
}
int manager () {
  while(1) {
    string ann_name;
    char cmd;
    bool secmenu = 0;
    ANN myann;
    cout << "Artificial neural network (ANN) manager. ver 1.0.1" << endl;
    cout << "copyright(c)2017 MAGNET inc." << endl;
    cout << "For more information \"www.nooxy.tk\"." << endl;
    cout << "1. Create new ANN (c). 2. Load from old (l). 3. recover from latest train (r) 4. Create matrix(.mtrx) (m) 5. Print matrix(.mtrx) (p) 6. exit (e)." << endl << ">>>";
    cin >> cmd;
    switch (cmd) {
      case 'c':
      {
        int layers_size;
        cout << "Input \"ANN's name.\"" << endl << ">>>";
        cin >> ann_name;
        cout << "Input \"ANN's layers size.\"" << endl << ">>>";
        cin >> layers_size;
        int neurons_size[layers_size];
        for(int i = 0; i < layers_size; i++) {
          cout << "Input \"layer (" << i + 1 << "/" << layers_size << ") neurons size\"." << endl << ">>>";
          cin >> neurons_size[i];
        }
        ANN temp(layers_size, neurons_size);
        myann = temp;
        myann.save_to_file(ann_name);
        secmenu = 1;
        break;
      }
      case 'l':
      {
        cout << "Input \"ANN's name\"." << endl << ">>>";
        cin >> ann_name;
        myann.load_from_file(ann_name);
        secmenu = 1;
        break;
      }
      case 'r':
      {
        cout << "Input \"ANN's name\"." << endl << ">>>";
        cin >> ann_name;
        myann.load_from_file("latest");
        myann.save_to_file(ann_name);
        secmenu = 1;
        break;
      }
      case 'm':
      {
        string matrix_name;
        matrix M;
        cout << "Input \"matrix name(probably \"in\"/\"out\")\", \"row(probably the number of data amount)\", \"column(probably the number of input or output layer\'s neuron size)\"." << endl;
        cout << "And then input \"elements\" row after row." << endl << ">>>";
        cin >> matrix_name >> M;
        M.save_to_file(matrix_name);
        break;
      }
      case 'p':
      {
        string matrix_name;
        matrix M;
        cout << "Input \"matrix name(probably \"in\"/\"out\")\"." << endl << ">>>";
        cin >> matrix_name;
        M.load_from_file(matrix_name);
        M.print();
        break;
      }
      case 'e':
      {
        return 0;
        break;
      }
      default :
      {
        return 0;
        break;
      }
    }
    cout << "Your ANN : " << ann_name << endl;
    myann.print();
    while (secmenu) {
      char cmd2;
      cout <<"1. Train (t). 2. Feed (f). 3.Help (h) 4. save (s) 5. back (b)." << endl << ">>>";
      cin >> cmd2;
      switch (cmd2) {
        case 't':
        {
          matrix IN, OUT;
          if (IN.load_from_file("in") || OUT.load_from_file("out")) {
            cout << "error: \"in.mtrx\" or \"out.mtrx\" not found. Please create it first." << '\n';
          }
          else {
            double speed, min_err;
            int times, loop;
            cout << "Input \"min err value(0.1)\", \"speed(3)\" , \"max training times (-1 for infinite)\", \"times per loop(2500)\"." << '\n'  << ">>>";
            cin >> min_err >> speed >> times >> loop;
            myann.train_pro(IN, OUT, min_err, times, speed, loop);
          }
          break;
        }
        case 'f':
        {
          matrix FEED;
          cout << "input \"row(number of data amount)\", \"column(number of input layer\'s neuron size)\"" << endl;
          cout << "And then input \"elements\" row after row." << endl << ">>>";
          cin >> FEED;
          cout << "result:" << endl << myann.feed(FEED);
          break;
        }
        case 'h':
        {
          cout << "You need in.mtrx and out.mtrx to train. Can simply create by tool provide from us from first menu." << endl;
          cout << "Or you can manually create it by text editor. Form showing below." << endl;
          cout << "\"row(probably the number of data amount)\", \"column(probably the number of input or output layer\'s neuron size)\"" << endl;
          cout << "And then input \"elements\" row after row." << endl;
          cout << "Beware each thing should seperated by space." << endl;
          cout << "For example 2 * 3 matrix." << endl;
          cout << "                  input / output neuron size (column\'s size)" << endl;
          cout << "                                   1 2" << endl;
          cout << " amount of data (row\'s size)       3 4" << endl;
          cout << "                                   5 6" << endl;
          cout << "In .mtrx file should be like" << endl;
          cout << "2 3 1 2 3 4 5 6" << endl;
          break;
        }
        case 's':
        {
          myann.save_to_file(ann_name);
          break;
        }
        case 'b':
        {
          cout << endl;
          secmenu = 0;
          break;
        }
        default :
        {
          secmenu = 0;
          break;
        }
      }
    }
  }
  return 0;
}
int main() {
  manager();
}
