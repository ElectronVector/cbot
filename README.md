# cbot

A tool for automating manual steps and generating code when unit testing C language CMake-based projects.

## Goals

- Make it easy to set up new projects and add new unit tests.
- Use CMake for builds and CTest for running tests.
- Generate code and automate tasks as needed, but the resulting output files can be built and run by CMake and Ctest without requiring `cbot`.