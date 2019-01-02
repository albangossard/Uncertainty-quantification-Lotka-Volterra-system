%module MC
%{
#define SWIG_FILE_WITH_INIT
#include "MC.h"
%}


%include "numpy.i"
%include "std_list.i"
%include "std_vector.i"


%init %{
    import_array();
%}

%apply (double* IN_ARRAY1, int DIM1) {(double* x, int dimx)}
%apply (double* IN_ARRAY1, int DIM1) {(double* y, int dimy)}


%include "MC.h"
