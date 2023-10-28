#include <iostream>
#include <argparse/argparse.hpp>
#include <string>
#include <filesystem>
#include <fstream>
#include <system_error>
#include <zobj.hpp>

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

    ifstream input(program.get<string>("input"), ios::binary);
    if (!input.is_open())
    {
        cerr << "Cannot open `" << program.get<string>("input") << "`" << endl;
        exit(0);
    }

    try
    {
        auto obj = ZObj::fromFile(input);
        
        cout << "Version: " << obj->version << endl;
    }
    catch (const std::runtime_error &err)
    {
        cerr << err.what() << endl;
        exit(0);
    }

    return 0;
}
