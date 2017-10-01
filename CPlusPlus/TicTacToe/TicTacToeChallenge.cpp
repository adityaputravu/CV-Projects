#include <iostream>
#include <string>

#include "TicTacToeGame.cpp"


using namespace std;

int main(){

    int input;
    bool gameEnd;

    TicTacToeGame game;
    cout << "Would you like to play the game?" << endl
         << "<1> Yes!" << endl
         << "<2> No!" << endl;
    cin >> input;
    if(input==1){
        gameEnd = false;
    }else if(input==2){
        gameEnd = true;
    }

    while(not gameEnd){

        game.playGame();

        cout << "Would you like to replay the game?" << endl
             << "<1> Yes!" << endl
             << "<2> No!" << endl;
        cin >> input;
        if(input==1){
            gameEnd = false;
        }else if(input==2){
            gameEnd = true;
        }



    }

    cout << "Bye bye!" << endl;


    return 0;
}