#include "Node.h"
int main()
{
    std::ofstream generatedunittest("autogenerated_unittest.py");
    std::cout << "What is the name of the item:" << std::endl;
    std::string headname = "";
    std::getline(std::cin,headname);
    Node head(headname);
    std::cout << "Formatted String: " << NodeUtility::parsestringformat(head) << std::endl;
    NodeUtility::outputfile("myfile");
    NodeUtility::create::testclass(head,generatedunittest);
    return 0;
}
