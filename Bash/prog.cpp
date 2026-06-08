#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <stdio.h>
#include <chrono>

int main (int argc, char **argv) {
    FILE * file;
    std::string ch;
    std::ifstream in (argv[1]);
    if (in.is_open())
    {
        getline (in, ch);
    }
    in.close();
    std::cout << ch << std::endl;
    return 0;
}