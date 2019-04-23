project(Geometry CXX C)
cmake_minimum_required(VERSION 3.1)
set(CMAKE_CXX_STANDARD 11)

# find_package(Eigen3 REQUIRED)
# include_directories(${EIGEN3_INCLUDE_DIR})
include_directories($ENV{HOME}/libs/libigl/include)

foreach(subdir ${SUBDIRS})
    add_subdirectory(${subdir})
endforeach()
