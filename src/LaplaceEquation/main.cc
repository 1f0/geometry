#include "../vtk.h"
#include <igl/cotmatrix.h>
#include <igl/invert_diag.h>
#include <igl/massmatrix.h>
#include <igl/per_vertex_normals.h>
#include <igl/readOBJ.h>
#include <igl/writeOBJ.h>
#include <iostream>
using namespace std;

int main(int argc, char **argv) {
    if (argc < 3)
        return printf("[usage] %s input.obj output.vtk\n", argv[0]);

    Eigen::MatrixXd V;
    Eigen::MatrixXi F;
    igl::readOBJ(argv[1], V, F);

    Eigen::MatrixXd field;
    igl::per_vertex_normals(V, F, field);

    vtk::out_vector_field(argv[2], V, F, field, "normals");
}
