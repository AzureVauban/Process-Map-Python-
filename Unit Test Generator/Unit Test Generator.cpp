// Unit Test Generator.cpp : This file contains the 'main' function. Program execution begins and ends there.
// merge changes into Bug Fixing Branch when this is completed
#include "NodeUtility.h"

std::ofstream output("generatedUnitTest.py");
void populate(NodeUtility::Node *object)
{
    std::cout << "What do you need to create " << object->ingredient << ":" << std::endl;
    std::string userinput = "";
    std::vector<std::string> userinputs = {};
    // prompt inputs
    do
    {
        std::getline(std::cin, userinput);
        //std::remove(userinput.begin(), userinput.end(), ' ');
        while (userinput.size() > 0 and userinput.back() == ' ')
        {
            userinput.pop_back();
            userinput.shrink_to_fit();
        }
        bool isalreadypresent = false;
        for (const auto &mystring : userinputs)
        {
            isalreadypresent = mystring == userinput;
            if (isalreadypresent)
            {
                break;
            }
        }
        if (not userinput.empty())
        {
            userinputs.emplace_back(userinput);
        }
        else if (isalreadypresent)
        {
            std::cout << "You already typed that in!" << std::endl;
        }
        else if (userinput == object->ingredient)
        {
            std::cout << "You cannot type that in..." << std::endl;
        }
    } while (!userinput.empty());
    // create child node instances
    bool promptbool = true;
    int amountmadepercraft = 0;
    for (const auto &childname : userinputs)
    {
        if (promptbool)
        {
            auto childinstance = new NodeUtility::Node(childname, object, 0, 1, 1, promptbool);
            promptbool = false;
            amountmadepercraft = childinstance->amountmadepercraft;
        }
        else
        {
            auto childinstance = new NodeUtility::Node(childname, object, 0, amountmadepercraft, 1);
        }
    }
    // recursive runtime
    for (auto childnode : object->children)
    {
        populate(childnode);
    }
}
int main()
{
    using namespace NodeUtility;
    // prompt the name of the head most ingredient
    auto head = new Node("Block of Netherite");
    // prompt subingredients
    /*
    auto netheriteingot = new Node("Netherite Ingot", head, 0, 1, 9);
    auto goldingot = new Node("Gold Ingot", netheriteingot, 0, 1, 4);
    auto netheritescrap = new Node("Netherite Scrap", netheriteingot, 1, 1, 4);
    auto emerald = new Node("Emerald", netheritescrap, 0, 1, 34);
    */
    populate(head);
    // todo create function that determines if an input has been repeated somewhere else and append a number the name to make it unique
    // prompt desired amount
    std::cout << "How much " << head->ingredient << " do you want to create? " << std::endl;
    int desirednumofhead = integer_input();
    // set assert values - do arithmetic
    NodeUtility::setassertvalues(head, desirednumofhead);
    // create and write into file
    //  create docstring
    write::docstring::module(output);
    output << std::endl;
    // create variable declarations
    write::tree_declaration(output, head);
    output << std::endl
           << std::endl;
    // create test class
    write::createclass(output, head);
    // create test methods
    write::tree_method(output, head);
    // clean up allocated memory from tree
    // terminate process
    output << std::endl;
    massdelete(head);
    output.close();
    return 0;
}
