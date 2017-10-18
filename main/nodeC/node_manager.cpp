#include <iostream>
#include <iomanip>//setprecision
#include <math.h>//pow()
#include "matrix.h"
#include "ANN.h"
using namespace std;

class ANN_manager{
  public:
    int launch();
    int manage_ANN(ANN& myann, string ann_name);
    int start_project();
};
int ANN_manager::launch () {
  while(1) {
    string ann_name;
    char cmd;
    bool secmenu = 0;
    ANN myann;
    cout << endl;
    cout << "" << endl;
    cout << "" << endl;
    cout << "88b 88  dP\"Yb   dP\"Yb  Yb  dP Yb  dP " << endl;
    cout << "88Yb88 dP   Yb dP   Yb  YbdP   YbdP  " << endl;
    cout << "88 Y88 Yb   dP Yb   dP  dPYb    8P   " << endl;
    cout << "88  Y8  YbodP   YbodP  dP  Yb  dP    " << endl;
    cout << "" << endl;
    cout << "PROJECT node. Copyright(c)2017 NOOXY inc. Taiwan." << endl;
    cout << "" << endl;
    cout << "Artificial neural network (ANN) manager. ver 1.4.0 bulid 2" << endl;
    cout << "For more information or update ->\"http://www.nooxy.tk\"." << endl;
    cout << "" << endl;
    cout << "<<< Home >>>\nCreate ANN [c]. Load ANN [l]. Recover from latest train [r]. Merge ANN [m]. Create matrix(.mtrx) [M]. Print matrix(.mtrx) [p]. Enable GPU [g]. Exit [e]." << endl << ">>>";
    cin >> cmd;
    switch (cmd) {
      case 'c':
      {
        int layers_size;
        cout << "Input \"ANN's name.\" to be created." << endl << ">>>";
        cin >> ann_name;
        cout << "Input \"ANN's layers size.\"" << endl << ">>>";
        cin >> layers_size;
        int neurons_size[layers_size];
        cout << "\"layer (1/" << layers_size << ")\" is input layer and \"layer (" << layers_size << "/" << layers_size << ")\"is output layer." << endl;
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
        cout << "Input \"ANN's name\" to be loaded." << endl << ">>>";
        cin >> ann_name;
        if (myann.load_from_file(ann_name) == -1) {
          cout << ann_name << ".node not found." << endl;
          secmenu = 0;
        }
        else {
          secmenu = 1;
        }
        break;
      }
      case 'r':
      {
        cout << "Input \"ANN's name\" to be recovered." << endl << ">>>";
        cin >> ann_name;
        myann.load_from_file(ann_name + "_latest");
        myann.save_to_file(ann_name);
        secmenu = 1;
        break;
      }
      case 'm':
      {
        string ann_name, merge_ann_name_1, merge_ann_name_2;
        ANN temp, ann1, ann2;
        cout << "Input \"first ann name\"." << endl;
        cin >> merge_ann_name_1;
        cout << "Input \"next ann name\"." << endl;
        cin >> merge_ann_name_2;
        cout << "Input \"ann name that be merged to\"." << endl;
        cin >> ann_name;
        if(ann1.load_from_file(merge_ann_name_1) == -1 || ann2.load_from_file(merge_ann_name_2) == -1) {
          cout << merge_ann_name_1 << ".node or " << merge_ann_name_2 << ".node not found." << endl;
        }
        temp = (ann1 + ann2) / 2;
        temp.save_to_file(ann_name);
        cout << "ANN is merged to " << ann_name << ".node" << endl;
        break;
      }
      case 'M':
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
      case 'g':
      {
        cuda_init();
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
    if (secmenu) {
      cout << "Your ANN : " << ann_name << endl;
      myann.print();
    }
    while (secmenu) {
      if(this->manage_ANN(myann, ann_name) == 0) {
        break;
      }
    }
  }
  return 0;
}
int ANN_manager::manage_ANN (ANN& myann, string ann_name) {
  char cmd;
  cout << endl <<"<<< ANN manager @" << ann_name << " >>>" << endl;
  cout <<"Train [a]. Train by default [b]. Train by random [c] Feed [d]. Feed by \".mtrx\" [e]. Feed test file [f]. Remap weight randomly [g]. Save ANN [s]. Print detail [p]. Return [r]. Help [h]." << endl << ">>>";
  cin >> cmd;
  switch (cmd) {
    case 'a':
    {
      matrix IN, OUT;
      if (IN.load_from_file("in") || OUT.load_from_file("out")) {
        cout << "error: \"in.mtrx\" or \"out.mtrx\" not found. Please create it first." << '\n';
      }
      else {
        double speed, min_err;
        int times, loop;
        cout << "Input \"min error value per data(0.1)\", \"speed(0.01)\" , \"max training times (-1 for infinite)\", \"times per loop(100)\"." << '\n'  << ">>>";
        cin >> min_err >> speed >> times >> loop;
      	min_err = pow(pow(min_err, 2) * IN.get_row(), 0.5);
      	cout << ">>>whole min eroor: " << fixed << setprecision(6) << min_err << endl;
        myann.train_method_batch(IN, OUT, min_err, times, speed, loop, ann_name);
        myann.save_to_file(ann_name);
        cout << "Saved to " << ann_name << ".node" << endl;
      }
      break;
    }
    case 'b':
    {
      double min_err;
      matrix IN, OUT;
      if (IN.load_from_file("in") || OUT.load_from_file("out")) {
        cout << "error: \"in.mtrx\" or \"out.mtrx\" not found. Please create it first." << '\n';
      }
      else {
        cout << "Input \"min error value per data(0.1)\"." << '\n'  << ">>>";
        cin >> min_err;
      	min_err = pow(pow(min_err, 2) * IN.get_row(), 0.5);
      	cout << ">>>whole min error: " << fixed << setprecision(6) << min_err << endl;
        myann.train_method_batch(IN, OUT, min_err, -1, 0.01, 100, ann_name);
        myann.save_to_file(ann_name);
        cout << "Saved to " << ann_name << ".node" << endl;
      }
      break;
    }
    case 'c':
    {
      matrix IN, OUT;
      if (IN.load_from_file("in") || OUT.load_from_file("out")) {
        cout << "error: \"in.mtrx\" or \"out.mtrx\" not found. Please create it first." << '\n';
      }
      else {
        double speed, min_err;
        int times, loop;
        cout << "Input \"min error value per data(0.1)\", \"speed(0.01)\" , \"max training times (-1 for infinite)\", \"times per loop(100)\"." << '\n'  << ">>>";
        cin >> min_err >> speed >> times >> loop;
        min_err = pow(pow(min_err, 2) * IN.get_row(), 0.5);
        cout << ">>>whole min eroor: " << fixed << setprecision(6) << min_err << endl;
        myann.train_method_random(IN, OUT, min_err, times, speed, loop, ann_name);
        myann.save_to_file(ann_name);
        cout << "Saved to " << ann_name << ".node" << endl;
      }
    }
    case 'd':
    {
      matrix FEED;
      cout << "input \"row(number of data amount)\", \"column(number of input layer\'s neuron size)\"" << endl;
      cout << "And then input \"elements\" row after row." << endl << ">>>";
      cin >> FEED;
      cout << "result:" << endl;
      (myann.feed(FEED)).print();
      cout << "result (logit):" << endl;
      ((myann.feed(FEED)).transfer(logit)).print();
      break;
    }
    case 'e':
    {
      matrix FEED;
      string matrix_name;
      cout << "Input \"matrix name be feeded." << endl << ">>>";
      cin >> matrix_name;
      FEED.load_from_file(matrix_name);
      cout << "result:" << endl;
      (myann.feed(FEED)).print();
      cout << "result (logit):" << endl;
      ((myann.feed(FEED)).transfer(logit)).print();
      break;
    }
    case 'f':
    {
      double min_err;
      matrix IN, OUT;
      if (IN.load_from_file("in_test") || OUT.load_from_file("out_test")) {
        cout << "error: \"in_test.mtrx\" or \"out_test.mtrx\" not found. Please create it first." << '\n';
      }
      else {
        cout << "-----origin out-----" << endl;
        OUT.print();
        cout << "-----feed out-----" << endl;
        ((myann.feed(IN)).transfer(logit)).print();
        cout << fixed;
        cout << setprecision(6);
        cout << "error value (sigmoid on): " << (myann.feed(IN) - OUT.transfer(sigmoid)).length() << endl;
      }
      break;
    }
    case 'g':
    {
      myann.randomweight();
      myann.save_to_file(ann_name);
      cout << ann_name << ".node has been remapped randomly." << endl;
      break;
    }
    case 'h':
    {
      cout << "You need in.mtrx and out.mtrx to train. Can simply create by tool provide from us from first menu." << endl;
      cout << "Or you can manually create it by text editor. Form showing below." << endl;
      cout << "\"row(probably the number of data amount)\", \"column(probably the number of input or output layer's neuron size)\"" << endl;
      cout << "And then input \"elements\" row after row." << endl;
      cout << "Beware each thing should seperated by space." << endl;
      cout << "For example 2 * 3 matrix." << endl;
      cout << "                  input / output neuron size (column's size)" << endl;
      cout << "                                   1 2" << endl;
      cout << " amount of data (row's size)       3 4" << endl;
      cout << "                                   5 6" << endl;
      cout << "In .mtrx file should be like" << endl;
      cout << "2 3 1 2 3 4 5 6" << endl;
      break;
    }
    case 's':
    {
      myann.save_to_file(ann_name);
      cout << "Saved to " << ann_name << ".node" << endl;
      break;
    }
    case 'p':
    {
      myann.print_detail();
      break;
    }
    case 'r':
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
  return 1;
}
int main() {
  ANN_manager manager;
  manager.launch();
  // double m[6] = {1, 2, 3, 4, 5, 6};
  // matrix M(3, 2, m);
  // M.print();
  // M.get_row_as_matrix(2);
}
