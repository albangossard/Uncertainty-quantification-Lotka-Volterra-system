/***

MC for Lotka Volterra model in C++

Authors: Pauline Guntzburger, Lucie Van Nieuwenhuyze and Alban Gossard
Date: 2018nov30
***/

#include "MC.h"


double get_wall_time(){
    struct timeval time;
    if (gettimeofday(&time,NULL)){
        return 0;
    }
    return (double)time.tv_sec + (double)time.tv_usec * .000001;
}



void runMC(double* x, int dimx, double* y, int dimy, double T, double alpha, double beta, double delta, double gamma){

    double dt = T/(dimx-1.);
    // cout<<"dt="<<dt<<endl;

    for (int n=0; n<dimx-1; ++n){
        x[n+1]=x[n]+dt*x[n]*(alpha-beta*y[n]);
        y[n+1]=y[n]+dt*y[n]*(delta*x[n]-gamma);
    }
        
}