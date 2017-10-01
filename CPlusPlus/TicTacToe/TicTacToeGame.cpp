//
// Created by Aditya Putravu on 20/08/2017.
//

#include "TicTacToeGame.h"
#include <iostream>
#include <string>

using namespace std;

TicTacToeGame::TicTacToeGame() {


}

void TicTacToeGame::playGame() {
    clearBoard();

    string p1 = " X ";
    string p2 = " O ";
    string currentPlayer = p1;

    int x,y;
    int turn = 0;

    bool isDone = false;
    while(not isDone) {
        printBoard();
        cout << endl;
        x = getXCord();
        y = getYCord();


        if (placeMarker(x, y, currentPlayer) == false) {
            cout << "******ERROR: Location already occupied!******\n";
        }
        else {
            turn ++;

            //Before player switch
            if(checkVictory(currentPlayer)){
                printBoard();
                cout << "The game is over!!!\nPlayer: " << currentPlayer << " has won!\n";
                isDone = true;

            }else if(turn == 9){
                printBoard();
                cout << "It's a tie game!";
                isDone = true;

            }

            //Switch players only if location unoccupied
            if (currentPlayer == p1) {
                currentPlayer = p2;
            } else {
                currentPlayer = p1;
            }

        }


    }

}

void TicTacToeGame::clearBoard(){

    for(int i=0;i<3; i++){
        for (int j = 0; j < 3; ++j) {
            board[i][j] = " _ ";
        }

    }

}

void TicTacToeGame::printBoard() {

    cout << endl;
    cout << "   | 1 | 2 | 3 |\n";

    for(int i=0;i<3;i++){
        cout << "-------------------" << endl;
        cout << " " << i+1 << " ";
        cout << "|" << board[i][0]<< "|" << board[i][1]<< "|" << board[i][2] << "|" << endl;

    }
    cout << "-------------------" << endl;
    cout << "   |   |   |   |\n";
}

int TicTacToeGame::getXCord() {
    int x;

    bool badInput = true;

    while(badInput) {
        cout << "Enter the X Coordinate: ";
        cin >> x;

        if(x<1 || x>3){
            cout << "******ERROR: Invalid Coordinate!******\n";
        }else{badInput=false;}
    }

    return x - 1;
}

int TicTacToeGame::getYCord() {
    int y;

    bool badInput = true;

    while(badInput) {
        cout << "Enter the Y Coordinate: ";
        cin >> y;

        if(y<1 || y>3){
            cout << "******ERROR: Invalid Coordinate!******\n";
        }else{badInput=false;}
    }

    return y - 1;

}

bool TicTacToeGame::placeMarker(int x, int y, string currentPlayer) {

    if(board[y][x] == " _ "){
        board[y][x] = currentPlayer;
        return true;
    }else{return false;}
}

bool TicTacToeGame::checkVictory(string currentPlayer) {

    //Check th rows
    for (int i = 0; i < 3; ++i) {
        if ((board[i][0] == currentPlayer) && (board[i][0] == board[i][1]) && (board[i][1] == board[i][2])) {
            // Change the winning tiles to this symbol
            board[i][0] = " ✅ ";
            board[i][1] = " ✅ ";
            board[i][2] = " ✅ ";
            return true; // won
        }
    }
    //Check columns
    for (int i = 0; i < 3; ++i) {
        if ((board[0][i] == currentPlayer) && (board[0][i] == board[1][i]) && (board[1][i] == board[2][i])) {
            // Change the winning tiles to this symbol
            board[0][i] = " ✅ ";
            board[1][i] = " ✅ ";
            board[2][i] = " ✅ ";
            return true; // won
        }
    }

    // x=-y diagonal check
    if ((board[0][0] == currentPlayer) && (board[0][0] == board[1][1]) && (board[1][1] == board[2][2])) {
        // Change the winning tiles to this symbol
        board[0][0] = " ✅ ";
        board[2][2] = " ✅ ";
        board[1][1] = " ✅ ";

        return true; // won
    }
    // x=y diagonal check
    if ((board[2][0] == currentPlayer) && (board[2][0] == board[1][1]) && (board[1][1] == board[0][2])) {
        // Change the winning tiles to this symbol
        board[2][0] = " ✅ ";
        board[1][1] = " ✅ ";
        board[0][2] = " ✅ ";
        return true; // won
    }
    return false;


}