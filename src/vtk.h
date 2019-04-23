#ifndef _VTK_H_
#define _VTK_H_
#include <Eigen/Core>
#include <fstream>

namespace vtk {
void out_vector_field(const std::string &filepath, const Eigen::MatrixXd &V,
                      const Eigen::MatrixXi &F, const Eigen::MatrixXd &field,
                      const std::string &dataname = "vecdata") {
    std::ofstream ofs(filepath);
    ofs << "# vtk DataFile Version 2.0\n"
        << "vector field\n" // todo: actual type
        << "ASCII\n"
        << "DATASET POLYDATA\n"                 // todo
        << "POINTS " << V.rows() << " float\n"; // todo

    for (int i = 0; i < V.rows(); ++i) {
        for (int j = 0; j < V.cols(); ++j)
            ofs << V(i, j) << " ";
        ofs << "\n";
    }

    ofs << "POLYGONS " << F.rows() << " " << F.rows() * (1 + F.cols()) << "\n";
    for (int i = 0; i < F.rows(); ++i) {
        ofs << F.cols();
        for (int j = 0; j < F.cols(); ++j)
            ofs << " " << F(i, j);
        ofs << "\n";
    }

    if (field.rows() == V.rows())
        ofs << "POINT_DATA ";
    else
        ofs << "CELL_DATA ";

    ofs << field.rows() << "\n"
        << "VECTORS " << dataname << " float\n";

    for (int i = 0; i < field.rows(); ++i) {
        for (int j = 0; j < field.cols(); ++j)
            ofs << field(i, j) << " ";
        ofs << "\n";
    }
}
}; // namespace vtk

#endif