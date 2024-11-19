# Coding-Task-for-Hawk-Eye-Innovations-Graduate-Scheme

## Challenge Selected
*"Software Engineering: Card Game*
*Objective: Create a card game like Higher/Lower.*
*Instructions:*
*Design a standard 52-card deck model, with an option to add Jokers.*
*Implement a shuffling mechanism and basic game rules.*
*Build a simple CLI for game play (bonus if you add a GUI!).*
*This is a great task to highlight your software engineering and problem-solving skills. If you’re creative with game features or UI, you’ll stand out!*

## Running Guidance
This submission contains two versions of the game depending on the preference of the tester.

The python version of the game is implemented using tkinter and is the more basic version of the two.
To run this, enter the Python_game folder use the yml file to duplicate the enviornment and then run the main.py file.

The web app version of the game is more interactive and has a couple extra features. 
To run this app simply open the Website_game folder and run the run_website.py file.
This is the recommended version to use.

## Decisions
I intially developed the programe in python to get a basic sense of how to get the mechanisms to work. I used tkinter as it is the most 
commonly used and supported gui tool for python. However, it is a bit limited in what it can do and I wasn't very happy with the way it looked.
I was also not as happy with my first impelmentation of the code as it seemed a bit involved and i think it could be simplified. 

The formation of the actual card stack was relatively straight forward and consisted of a class for the card in which it was placed into a deck class
as a list. These items could then be shuffled and popped from the list and replaced and reshuffled when the turn was over. The method to evaluate the
two cards consisted of a player and a dealer in which each was dealt a card. These cards were then compared and an output of whether the player or the dealer
won could be displayed. The reasoning for this was to allow for a possible extension to a blackjack game whereby one is trying to beat the dealer.

I wanted more functionality with my GUI and make it more visually appealing so I decided to build a local website for it. For the website implementation I 
realized that if i wasn't going to implement the additional blackjack feature then i only needed to evaluate the current and the next car in the pile rather
then draw two cards simultaneously, this simplified the code a bit and allowed for faster implementation. I also was able to make sure of some of the nice features
of CSS such as simple animations and background images, to make the experience more appealing. 

## Improvements
Theres definetly room to implement additional games that could be selected in the home screen which might be interesting, such as the black jack previousl mentioned. 
Besides that I would look to continue to improve the gui to possible make a mini virtual enviornment where one is playing cards on a poker table improving the 
animations further and making use of more HTML5 packages. 
