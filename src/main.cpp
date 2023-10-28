#include <iostream>
#include <argparse/argparse.hpp>
#include <string>
#include <filesystem>

using namespace std;
using namespace argparse;

int main(int argc, char *argv[])
{
    ArgumentParser program("zobj2elf");
    program.add_argument("input")
        .help("input file");
    
    program.add_argument("-o", "--output")
        .help("output file")
        .default_value(string("a.out"));

    try
    {
        program.parse_args(argc, argv);
    }
    catch (const std::runtime_error &err)
    {
        std::cout << err.what() << std::endl;
        std::cout << program;
        exit(0);
    }

    if (!filesystem::exists(program.get<string>("input")))
    {
        cerr << "Input file `" << program.get<string>("input") << "` does not exist." << endl;
        exit(1);
    }

    return 0;
}
