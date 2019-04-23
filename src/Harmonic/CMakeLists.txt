aux_source_directory(. src)
get_filename_component(name ${CMAKE_CURRENT_LIST_DIR} NAME)
add_executable(${name} ${src})
target_link_libraries(${name} Threads::Threads)