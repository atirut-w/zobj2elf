#include <memory>
#include <fstream>

using namespace std;

class ZObj
{
public:
    int version;

    ZObj();
    static unique_ptr<ZObj> fromFile(ifstream &input);
};
