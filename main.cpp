#include<stdio.h>
#include<stdlib.h> //realloc() calloc()
#include<iostream>
#include<string.h>//memcpy()
#include<math.h>//pow()
using namespace std;
void training(double& weight_map,int layers_size,int *neurons_size)
{

}
class matrix
{
    public:
    double *last_answer;
    double *initializer(int,int,double);
    double *product(double*,int,int,double*,int,int);
    double *sigmoid(double*,int,int);
    int print_matrix(double*,int,int);
    ~matrix();
};
double *matrix::initializer(int Xrow,int Xcolumn,double n)
{
    last_answer=(double*)calloc(Xrow*Xcolumn,sizeof(double));
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
    last_answer=(double*)calloc(Xrow*Ycolumn,sizeof(double));
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
    last_answer=(double*)calloc(Xrow*Xcolumn,sizeof(double));
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
    printf(">>>*martix (%dX%d)\n",Xrow,Xcolumn);
    for(i=0;i<Xrow;i++)
    {
        printf(">>>");
        for(j=0;j<Xcolumn;j++)
        {
            printf("%.5lf ",X[i*Xcolumn+j]);
        }
        printf("\n");
    }
}
matrix::~matrix()
{
    free(last_answer);
}
class ANN//artificial network manager
{
    double *temp,*temp2;
    public:
    int insize,outsize,*nsize,nsize_sum=0,*wsize,wsize_sum=0,laysize,amount/*input*/;//size each layer which is pointer,layersize is hidden layer
    double *neuronmap,*weightmap,*inputmap,*outputmap;
    ANN(int,int,int,int*);
    ~ANN();
    double *feed_data(int,double*);
    void print_info();
};
ANN::ANN(int input_size,int output_size,int layers_size,int *neurons_size)
{
    int i,j,wsizecount=0;
    insize=input_size;
    outsize=output_size;
    laysize=layers_size;
    nsize=(int*)calloc(layers_size,sizeof(int));
    memcpy(nsize,neurons_size,sizeof(int)*layers_size);
    wsize=(int*)calloc(layers_size+1,sizeof(int));//initailize wsize array
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
    outputmap=(double*)calloc(outsize,sizeof(double));
    inputmap=(double*)calloc(insize,sizeof(double));
    neuronmap=(double*)calloc(nsize_sum,sizeof(double));
    weightmap=(double*)calloc(wsize_sum,sizeof(double));
    matrix mtrx;
    memcpy(weightmap,mtrx.initializer(wsize_sum,1,1),wsize_sum*sizeof(double));
}
double *ANN::feed_data(int amount_of_data,double *data)
{
    inputmap=(double*)calloc(insize*amount_of_data,sizeof(double));
    memcpy(inputmap,data,sizeof(double)*insize*amount_of_data);
    amount=amount_of_data;
    int i,j,neurons=0,weights=0;
    matrix mtrx;
    temp=(double*)calloc(amount*nsize[0],sizeof(double));
    memcpy(temp,mtrx.product(inputmap,amount,insize,weightmap,insize,nsize[0]),amount*nsize[0]*sizeof(double));
    memcpy(temp,mtrx.sigmoid(temp,amount,nsize[0]),amount*nsize[0]*sizeof(double));
    for(i=1;i<laysize;i++)
    {
    weights+=wsize[i-1];
    temp2=(double*)calloc(amount*nsize[i-1],sizeof(double));
    memcpy(temp2,temp,amount*nsize[i-1]*sizeof(double));
    temp=(double*)calloc(amount*nsize[i],sizeof(double));
    memcpy(temp,mtrx.product(temp2,amount,nsize[i-1],weightmap+weights,nsize[i-1],nsize[i]),amount*nsize[i]*sizeof(double));
    memcpy(temp,mtrx.sigmoid(temp,amount,nsize[i]),amount*nsize[i]*sizeof(double));
    }
    weights+=wsize[laysize-1];
    outputmap=(double*)calloc(amount*outsize,sizeof(double));
    memcpy(outputmap,mtrx.product(temp,amount,nsize[laysize-1],weightmap+weights,nsize[laysize-1],outsize),amount*outsize*sizeof(double));
    memcpy(outputmap,mtrx.sigmoid(outputmap,amount,outsize),amount*outsize*sizeof(double));
    return outputmap;
}
void ANN::print_info()
{
    int i;
    matrix maprinter;
    printf(">>>*ANN info\n");
    printf(">>>variable to be test:%d\n",wsize[1]);
    printf(">>>size in layer:\n>>>");
    printf("(I):%d ",insize);
    for(i=0;i<laysize;i++)
    {
        printf("(W[%d]):%d (N[%d]):%d ",i,wsize[i],i,nsize[i]);
    }
    printf("(W[%d]):%d ",laysize,wsize[laysize]);
    printf("(O):%d ",outsize);
}
ANN::~ANN()
{
    free(temp);
    free(temp2);
    free(nsize);
    free(wsize);
    free(neuronmap);
    free(weightmap);
    free(inputmap);
    free(outputmap);
}
int main()
{
    matrix mtrx;//announce of matrix
    int ann_nsize[5]={1,1,1,1,1};//announce array for import neurons size in each layer
    double data[4]={12,12,12,12},data2[4]={1,2,3,4},A[6]={3,2,1,9,7,8},B[8]={4,8,10,1,7,9,11,9};//announce an array as an 2(row)*2(column)matrix for feeding data
    ANN ann(2,2,5,ann_nsize);//announce an ann model (input size,output size,layer size, importation of neuron size as pointer)
    printf("feed data result:\n");
    mtrx.print_matrix(ann.feed_data(2,data),2,2);//print result of feeding data
    printf("test matrix production:\n");
    ann.print_info();//print info about ann
}
