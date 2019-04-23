#ifndef _VTK_H_
#define _VTK_H_
#include <eigen3/Eigen>
#include <iostream>

void out_vector_field(const string &filename, const Matrix &V, const Matrix &F,
                      const Matrix &field);

#endif