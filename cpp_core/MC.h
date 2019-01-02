/***

MC for Lotka Volterra model in C++

Authors: Pauline Guntzburger, Lucie Van Nieuwenhuyze and Alban Gossard
Date: 2018nov30
***/

#include <iostream>
#include <fstream>
#include <cmath>
#include <Python.h>
#include <omp.h>


using namespace std;


void runMC(double* x, int dimx, double* y, int dimy, double T, double alpha, double beta, double delta, double gamma);
