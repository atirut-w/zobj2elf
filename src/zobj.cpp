#include <zobj.hpp>
#include <string>
#include <exception>

using namespace std;

ZObj::ZObj()
{
    version = 0;
}

unique_ptr<ZObj> ZObj::fromFile(ifstream &input)
{
    auto obj = make_unique<ZObj>();

    string signature(8, '\0');
    input.read(&signature[0], 8);
    if (signature.rfind("Z80RMF", 0) != 0)
    {
        throw runtime_error("Invalid signature");
    }
    obj->version = stoi(signature.substr(6, 2));

    return obj;
}
