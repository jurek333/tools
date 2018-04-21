# tools
Simple scripts and programs for personal use.

## switch
 - switch - list available enviroments
 - switch <available-name-and-version> - setup enviroment of choosen tool

## vim
 - vims runs vim in server mode
 - vimc <files> opens selected files remotely on server-vim
 This way one can use terminal and opens files on already running instance of vim.

## cmake
 - *create_cmake* create CMakeLists.txt file in current folder - run in project folder
    This tool gets current folder name as project name and scans recurrently for source files.
    As efect we have cmake file with project name and all *c/cpp/cc/c++/cxx* source fiels
 - *build_cmake* run cmake in build subfolder and build it - run in project folder
    This script creates build folder if it doesn't exist. Runs cmake there and next build it in Release mode.
