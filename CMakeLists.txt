cmake_minimum_required(VERSION 3.22)
project(zobj2elf)

add_executable(zobj2elf
    "src/main.cpp"
    "src/zobj.cpp"
)
target_include_directories(zobj2elf PRIVATE "include")

add_subdirectory(3rd/argparse)
target_link_libraries(zobj2elf argparse)
