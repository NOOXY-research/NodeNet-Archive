#include <iomanip>//setprecision
#include <iostream>
#include <string.h>//memcpy()
#include <math.h>//pow()
using namespace std;
void training(double& weight_map,int layers_size,int *neurons_size)
{

}
class matrix
{
    public:
    matrix();
    double *last_answer;
    double *initializer(int,int,double);
    double *product(double*,int,int,double*,int,int);
    double *sigmoid(double*,int,int);
    int print_matrix(double*,int,int);
    ~matrix();
};
matrix::matrix()
{
  last_answer=new double[1];
}
double *matrix::initializer(int Xrow,int Xcolumn,double n)
{
    delete [] last_answer;
    last_answer=new double[Xrow*Xcolumn];
    int i,j;
    for(i=0;i<Xrow;i++)
    {
        for(j=0;j<Xcolumn;j++)
        {
            last_answer[i*Xcolumn+j]=n;
        }
    }
    return last_answer;
}
double *matrix::product(double* X,int Xrow,int Xcolumn,double* Y,int Yrow,int Ycolumn)
{
    delete [] last_answer;
    last_answer=new double[Xrow*Ycolumn];
    int i,j,I;
    for(i=0;i<Xrow;i++)
    {
        for(j=0;j<Ycolumn;j++)
        {
            double temp=0;
            for(I=0;I<Xcolumn;I++)
            {
                temp+=X[i*Xcolumn+I]*Y[I*Ycolumn+j];
            }
            last_answer[i*Ycolumn+j]=temp;
        }
    }
    return last_answer;
}
double *matrix::sigmoid(double *X,int Xrow,int Xcolumn)
{
  delete [] last_answer;
    last_answer=new double[Xrow*Xcolumn];
    int i,j;
    for(i=0;i<Xrow;i++)
    {
        for(j=0;j<Xcolumn;j++)
        {
            last_answer[i*Xcolumn+j]=(1.0)/(1+pow( 2.7182818284590452353602874713527,-X[i+j]));
        }
    }
    return last_answer;
    //return
}
int matrix::print_matrix(double*X,int Xrow,int Xcolumn)
{
    int i,j;
    cout<<">>>*martix ("<<Xrow<<"X"<<Xcolumn<<")"<<endl;
    for(i=0;i<Xrow;i++)
    {
        cout<<">>>";
        for(j=0;j<Xcolumn;j++)
        {
            cout<<X[i*Xcolumn+j]<<" ";
        }
        cout<<endl;
    }
}
matrix::~matrix()
{
    delete [] last_answer;
}
class ANN//artificial network manager
{
    public:
    double *temp,*temp2;
    int insize,outsize,*nsize,nsize_sum,*wsize,wsize_sum,laysize,amount;/*input*/;//size each layer which is pointer,layersize is hidden layer
    double *weightmap,*inputmap,*outputmap;
    ANN(int,int,int,int*);
    ~ANN();
    double *feed_data(int,double*);
    void print_info();
};
ANN::~ANN()
{
    delete [] temp;
    delete [] temp2;
    delete [] nsize;
    delete [] wsize;
    delete [] weightmap;
    delete [] inputmap;
    delete [] outputmap;
}
ANN::ANN(int input_size,int output_size,int layers_size,int *neurons_size)
{
  outputmap=new double[1];
  inputmap=new double[1];
  weightmap=new double[wsize_sum];
  temp=new double[1];
  temp2=new double[1];
  nsize=new int[layers_size];
  wsize=new int[layers_size+1];
  nsize_sum=0;
  wsize_sum=0;
  int i,j,wsizecount=0;
  insize=input_size;
  outsize=output_size;
  laysize=layers_size;
  memcpy(nsize,neurons_size,sizeof(int)*layers_size);
  //initailize wsize array
  wsize[0]=input_size*neurons_size[0];wsize[layers_size]=output_size*neurons_size[layers_size-1];
  wsize_sum=input_size*neurons_size[0]+output_size*neurons_size[layers_size-1];//layersize+1 is the last wsize actually,but array count from o
  for(i=1;i<layers_size;i++)
  {
      wsize[i]=neurons_size[i-1]*neurons_size[i];
      wsize_sum+=neurons_size[i-1]*neurons_size[i];
  }
  for(i=0;i<layers_size;i++)
  {
      nsize_sum+=neurons_size[i];
  }

  matrix mtrx;
  memcpy(weightmap,mtrx.initializer(wsize_sum,1,1),wsize_sum*sizeof(double));
}
double *ANN::feed_data(int amount_of_data,double *data)
{
    delete [] inputmap;
    inputmap=new double[insize*amount_of_data];
    memcpy(inputmap,data,sizeof(double)*insize*amount_of_data);
    amount=amount_of_data;
    int i,j,neurons=0,weights=0;
    matrix mtrx;
    delete [] temp;
    temp=new double[amount*nsize[0]];
    memcpy(temp,mtrx.product(inputmap,amount,insize,weightmap,insize,nsize[0]),amount*nsize[0]*sizeof(double));
    memcpy(temp,mtrx.sigmoid(temp,amount,nsize[0]),amount*nsize[0]*sizeof(double));
    for(i=1;i<laysize;i++)
    {
    weights+=wsize[i-1];
    delete [] temp2;
    temp2=new double[amount*nsize[i-1]];
    memcpy(temp2,temp,amount*nsize[i-1]*sizeof(double));
    delete [] temp;
    temp=new double[amount*nsize[i]];
    memcpy(temp,mtrx.product(temp2,amount,nsize[i-1],weightmap+weights,nsize[i-1],nsize[i]),amount*nsize[i]*sizeof(double));
    memcpy(temp,mtrx.sigmoid(temp,amount,nsize[i]),amount*nsize[i]*sizeof(double));
    }
    weights+=wsize[laysize-1];
    delete [] outputmap;
    outputmap=new double[amount*outsize];
    memcpy(outputmap,mtrx.product(temp,amount,nsize[laysize-1],weightmap+weights,nsize[laysize-1],outsize),amount*outsize*sizeof(double));
    memcpy(outputmap,mtrx.sigmoid(outputmap,amount,outsize),amount*outsize*sizeof(double));
    return outputmap;
}
void ANN::print_info()
{
    int i;
    cout<<">>>*ANN info"<<endl;
    cout<<">>>variable to be test:"<<wsize[1]<<endl;;
    cout<<">>>size in layer:"<<endl<<">>>";
    cout<<"(I):"<<insize<<" ";
    for(i=0;i<laysize;i++)
    {
        cout<<"(W["<<i<<"]):"<<wsize[i]<<" (N["<<i<<"]):"<<nsize[i]<<" ";
    }
    cout<<"(W["<<i<<"]):"<<wsize[i]<<" ";
    cout<<"(O):"<<outsize<<" ";
}
int main()
{
    matrix mtrx;//announce of matrix
    int ann_nsize[1]={1};//announce array for import neurons size in each layer
    double data[2]={1,1},data2[4]={1,2,3,4},A[6]={3,2,1,9,7,8},B[8]={4,8,10,1,7,9,11,9};//announce an array as an 2(row amount)*2(column insize)matrix for feeding data
    ANN ann(2,2,1,ann_nsize);//announce an ann model (input size,output size,layer size, importation of neuron size as pointer)
    cout<<"feed data result: "<<endl;;
    mtrx.print_matrix(ann.feed_data(1,data),1,2);//print result of feeding data
    cout<<"test matrix production: "<<endl;
    ann.print_info();//print info about ann
}
