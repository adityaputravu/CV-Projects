#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){

    string shopItemNames[3] = {
                                "Snow Hat",
                                "Hamster",
                                "Dog"
                               };

    vector<string> itemNames;
    itemNames.push_back("Snow Hat"); // Add to vector on the end.
    itemNames.push_back("Scarf");
    itemNames.push_back("Boxes");
    itemNames.push_back("Rocks");

    cout << itemNames.size() << endl;

    itemNames[1] = itemNames.back();
    itemNames.pop_back();

    for (int i = 0; i < itemNames.size(); ++i) {
        cout << itemNames[i] << endl;
    }

    return 0;
}

