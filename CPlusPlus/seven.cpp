#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){

    string shopItemNames[3] = {
                                "Gloves",
                                "Boots",
                                "Maces"
                               };

    vector<string> itemNames;
    itemNames.push_back("Gloves"); // Add to vector on the end.
    itemNames.push_back("Hats");
    itemNames.push_back("Axes");
    itemNames.push_back("Rocks");

    // itemsNames.pop_back(); // Removes the last one

    cout << itemNames.size() << endl;


    /* Vectors can't delete or add in the middle, only to end
       This trick is if you don't care about order
       Copy last item and replace with middle item
       */

    itemNames[1] = itemNames.back();
    itemNames.pop_back();

    for (int i = 0; i < itemNames.size(); ++i) {
        cout << itemNames[i] << endl;
    }

    return 0;
}
