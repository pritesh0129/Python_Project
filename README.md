Project Report


1.Project Overview

This is a card matching game played on computer. The game has been developed using Python, an easy to understand programming language, commonly used today.
Here is how it is played – upon launching the game, players are presented with cards in a square arrangement. Click on any two cards to turn them backside. Cards remain opened if they are similar images, but when they are different images, then both the cards would return to their previous state. The objective of the game is to uncover all the pairs of identical cards with minimum clicks.
Development of this game has been done using Python’s standard tkinter module. This game doesn’t require any third-party applications, and just Python is needed for running it.

2.Problem Statement

Memory games are fun and also help improve concentration. But most online or digital versions of memory games need an internet connection, or they are built using complicated game engines that are hard for a beginner to understand.
This project was created to solve that problem. The main goals were:
1.Build a memory game that works offline, without any internet connection
2.Use only Python's built-in tools so the player does not need to install anything extra
3.Make sure the game does not crash even if something goes wrong, like a missing image file
4.Write the code in a clean and simple way so beginners can read and understand it


3.Technology Stack

Programming Language : Python 3.x
GUI Module :  tkinter (Python's built-in module)
File and Path Handling : os Module 
Card Suffling : random Module 
IDE / Editor : Python IDLE / VS Code


4.Implementation

The implementation follows a simple logic:

1.Open The  Window 
When you run the program, a game window opens on your screen. This is done using tkinter, a module in Python used to create windows and buttons.
2.Load All The Pictures
The program reads card_back.png, game_bg.png, and all PNG files from the cards/ folder. If any file is missing, it shows a simple pop-up message instead of crashing.
3.Build The Screen
The program creates three things on screen — a title at the top, an info bar with the attempt counter and buttons, and a card grid in the middle where the cards will appear.
4.Place The Card On The Screen 
Each card image is added twice to make pairs, then the list is shuffled randomly. All cards are placed face-down on the screen in a grid of 4 columns.
5.Player Clicks The First Card
When the player clicks a card, it flips over and shows its face image. The program saves which card was clicked and waits for the next click.
6.Player Clicks The Second Card
The second card also flips over and the attempt counter goes up by 1. The program then waits 0.8 seconds before checking if the two cards match.
7.Check If The Cards Match
If both cards show the same picture, they stay open and their border turns green. If they are different, both cards flip back face-down and the player tries again.
8.Check If The Game Is Won 
After every match, the program checks if all pairs are found. If yes, a congratulations pop-up appears and the game resets automatically.
9.Restart at Any Time 
If the player clicks the Restart button, the cards are reshuffled and the attempt counter resets to 0. The game starts fresh from Step 4.





5.Sample Test Cases

Action                                                                                              Output

1.Click a card                                                                      Card flips and shows the face image

2.Click two matching cards                                                          Both cards stay revealed with a green                                  								                             border 

3.Click two non-matching cards                                                      Both cards flip back to hidden after 0.8            								                                            seconds

4.Match all card pairs                                                              Congratulations popup appears with 									                                                            attempt count

5.Click Restart button                                                              Game resets with shuffled cards and                                      								                            attempt counter at 0

6.No card images in folder                                                          Error dialog shown: missing image files



6.Challenges Faced

During our development process for this game, we experienced some minor issues. First, we could not see our images on the buttons initially since Python would get rid of them from its memory. However, this issue was solved by adding an image storage system within the class. This will make sure that all images remain in the computer's memory while the game is running. Second, we realized that tkinter PhotoImage function only allows images in PNG format. Therefore, all our card images had to be saved in the PNG format before being used in our code. Third, we had a problem with mismatched cards where players could click a button within the 0.8-second interval. As such, we incorporated a simple On/Off switch named can_click to limit additional clicks while the game is waiting. Fourth, to have a grid with an automatic row calculation feature, we modified the code to consider the total number of images for determining the rows needed. Fifth, we included a pop-up message in case the user tries to open a non-existent file.


7.Results and Observations

The game was tested on Windows 11 using Python 3.11.Here are some things we noticed during testing:

The card flipping works smoothly — swapping the button image gives a clean, natural feel without needing any animation library.
The 0.8 second delay before flipping cards back is just right — long enough to see both pictures, but short enough that it does not slow the game down.
The game uses very little memory. The program runs comfortably on any basic computer.
The green border on matched cards is a simple but effective way to show the player which pairs they have already found.
