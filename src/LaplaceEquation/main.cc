#include <igl/readOBJ.h>
#include <igl/writeOBJ.h>
#include <iostream>
using namespace std;

int main(int argc, char **argv) {
    Eigen::MatrixXd V;
    Eigen::MatrixXi F;
    igl::readOBJ(argv[1], V, F);
}
