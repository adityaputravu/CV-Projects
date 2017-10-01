//
// Created by Aditya Putravu on 20/08/2017.
//

#ifndef YTTUT_TICTACTOEGAME_H
#define YTTUT_TICTACTOEGAME_H

#include <iostream>

using namespace std;


class TicTacToeGame {
public:
    TicTacToeGame();

    //gamesloop
    void playGame();

private:
    string board[3][3];

    //Clears the board
    void clearBoard();
    //prints board
    void printBoard();
    //gets x and y cord
    int getXCord();
    int getYCord();
    //palces cehcker and check validity pos
    bool placeMarker(int x, int y, string currentPlayer);
    //checks victory
    bool checkVictory(string currentPlayer);

};


#endif //YTTUT_TICTACTOEGAME_H
