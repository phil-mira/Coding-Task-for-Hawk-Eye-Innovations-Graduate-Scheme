import random
import tkinter as tk
from PIL import Image, ImageTk
import os

# Define the suits and ranks
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Include jokers by default
include_jokers = True

# Define the Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

# Define the Deck class
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)
    
    def replace(self, card):
        self.cards.append(card)
        self.shuffle()

    def deal(self):
        return self.cards.pop() if self.cards else None

# Define the Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
        self.guess = None

    #Draw a card from the deck
    def draw(self, deck):
        card = deck.deal()
        if card:
            self.hand.append(card)
        return card

    #Place card in hand back into deck
    def replace(self, deck):
        for card in self.hand:
            deck.replace(card)
        self.hand = []
                   

class GameScreen:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.pack()

        
        # Display the instructions for the game
        with open("Instructions.txt", "r") as file:
            instructions = file.read()
        self.description_label = tk.Label(self.frame, text=instructions)
        self.root.geometry("800x800")  
        self.description_label.pack()

        # Create a start button to start the game
        self.start_button = tk.Button(self.frame, text="Start", command=self.start_game)
        self.start_button.pack(pady=80)

        # Create a checkbutton to include jokers in the deck
        self.joker_var = tk.BooleanVar(value=include_jokers)
        self.joker_checkbutton = tk.Checkbutton(self.frame, text="Include Jokers", variable=self.joker_var, command=self.toggle_jokers)
        self.joker_checkbutton.pack()

    def start_game(self):
        """Start the game by creating a deck, player and dealer, and displaying the player's hand."""

        self.root.geometry("800x900")
        self.frame.destroy()
        self.canvas = tk.Canvas(self.root, width=800, height=800)
        self.canvas.pack()
        self.root.title("Card Game")
        deck = Deck()
        player1 = Player("Player 1")
        dealer = Player("Dealer")
        
        #Display the player's hand and ask for a guess
        player1.draw(deck)
        dealer.draw(deck)
        self.display_card(player1.hand[-1])
        self.guess_label = tk.Label(self.root, text="Will the next card be higher or lower?")
        self.guess_label.pack()


        #Create buttons for player to make a guess
        self.higher_button = tk.Button(self.root, text="Higher", command=lambda: self.higher(player1, dealer))
        self.higher_button.pack()
        self.lower_button = tk.Button(self.root, text="Lower", command=lambda: self.lower(player1, dealer))
        self.lower_button.pack()

    
    def higher(self, player, dealer): 
        """Return the result of the game based on the player's guess and the dealer's card when 
           the player guesses higher.
        """

        player.guess = True
        self.guess_label.destroy()
        self.higher_button.destroy()
        self.lower_button.destroy()
        result = self.evaluate_result(player, dealer, player.guess)
        self.display_result(result, player, dealer)
        
    def lower(self, player, dealer):
        """Return the result of the game based on the player's guess and the dealer's card when
              the player guesses lower.
        """

        player.guess = False
        self.guess_label.destroy()
        self.higher_button.destroy()
        self.lower_button.destroy()
        result = self.evaluate_result(player, dealer, player.guess)
        self.display_result(result, player, dealer)

    def evaluate_result(self, player, dealer, player_guess):
        """ Evaluate the result of the game based on the player's guess and the dealer's card. """

        player_card = player.hand[-1]
        dealer_card = dealer.hand[-1]
        
        if player_guess == (ranks.index(player_card.rank) < ranks.index(dealer_card.rank)):
            result = "You Win"
        else:
            result = "You Lose"

        return result

    def display_result(self, result, player1, dealer):
        """Display the result of the game and provide options to play again or quit."""

        result = self.evaluate_result(player1, dealer, player1.guess)
        dealer_card = dealer.hand[-1]
        self.display_card(dealer_card)
        self.result_label = tk.Label(self.root, text=result)
        self.result_label.pack()
        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.play_again)
        self.play_again_button.pack()
        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit)
        self.quit_button.pack()

    def play_again(self):
        """Resets the game to play again."""

        self.canvas.destroy()
        self.result_label.destroy()
        self.play_again_button.destroy()
        self.quit_button.destroy()
        self.start_game()

    def quit(self):
        self.root.quit()

    def display_card(self, card):
        """Display the image of the card on the canvas."""

        if hasattr(self, 'card_image'):
            self.canvas.delete(self.card_image)
        card_image = self.load_card_image(card)
        self.card_image = self.canvas.create_image(400, 400, image=card_image)
        self.canvas.image = card_image

    def load_card_image(self, card):

        """Load the image of the card from the PNG-cards-1.3 folder.
           Images taken from https://opengameart.org/content/playing-cards-vector-png
        """

        if card.rank == 'Black Joker':
            card_filename = "black_joker.png"
        elif card.rank == 'Red Joker':
            card_filename = "red_joker.png"
        card_filename = f"{card.rank}_of_{card.suit}.png".replace(' ', '_')
        card_path = os.path.join(os.path.dirname(__file__), "..", "PNG-cards-1.3", card_filename)
        image = Image.open(card_path)
        return ImageTk.PhotoImage(image)     

    # Function to toggle jokers, Joker is considered as higher than Ace
    def toggle_jokers(self):
        """Toggle the inclusion of jokers in the deck."""

        global include_jokers
        include_jokers = self.joker_var.get()
        if include_jokers:
            if 'Black Joker' not in ranks:
                ranks.append('Black Joker')
            if 'Red Joker' not in ranks:
                ranks.append('Red Joker')
        else:

            if 'Black Joker' in ranks:
                ranks.remove('Black Joker')
            if 'Red Joker' in ranks:
                ranks.remove('Red Joker')



if __name__ == "__main__":
    
    root = tk.Tk()  
    game_screen = GameScreen(root)
    root.protocol("WM_DELETE_WINDOW", root.quit)
    root.mainloop()
    root = tk.Tk()

    







