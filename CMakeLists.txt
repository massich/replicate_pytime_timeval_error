cmake_minimum_required(VERSION 3.2)
project(mwe CXX)

message("CMAKE_MODULE_PATH is " ${CMAKE_MODULE_PATH})

include (CTest)
enable_testing ()

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE)

add_executable(hello main.cpp)

add_test( NAME test_hello COMMAND ./hello)
set_tests_properties (test_hello PROPERTIES PASS_REGULAR_EXPRESSION "hello world")
