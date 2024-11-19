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
                   

class GameCardGUI:
    def __init__(self, root, player):
        
        self.player = player

        self.canvas = tk.Canvas(root, width=800, height=800)
        self.canvas.pack()

        self.card_image = None
        self.display_card(player.hand[-1])

        self.higher_button = tk.Button(root, text="Higher", command=self.higher)
        self.higher_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.lower_button = tk.Button(root, text="Lower", command=self.lower)
        self.lower_button.pack(side=tk.RIGHT, padx=20, pady=20)

    def display_card(self, card):
        if self.card_image:
            self.canvas.delete(self.card_image)
        card_image = self.load_card_image(card)
        self.card_image = self.canvas.create_image(400, 400, image=card_image)
        self.canvas.image = card_image

    def higher(self):
        # Logic for higher button
        self.player.guess = True
        self.root.quit()


    def lower(self):
        # Logic for lower button
        self.player.guess = False
        self.root.quit()
       
      
    
    def load_card_image(self, card):
        if card.rank == 'Black Joker':
            card_filename = "black_joker.png"
        elif card.rank == 'Red Joker':
            card_filename = "red_joker.png"
        card_filename = f"{card.rank}_of_{card.suit}.png".replace(' ', '_')
        card_path = os.path.join("PNG-cards-1.3", card_filename)
        image = Image.open(card_path)
        return ImageTk.PhotoImage(image)
    

    
class ResultScreen:
    def __init__(self, root, player, dealer, result):
        self.player = player
        self.dealer = dealer
        
        self.frame = tk.Frame(root)
        self.frame.pack()

        self.canvas = tk.Canvas(self.frame, width=800, height=800)
        self.canvas.pack()

        self.card_image = None
        self.display_card(dealer.hand[-1])

        self.result_label = tk.Label(self.frame, text=result)
        self.result_label.pack()

        self.play_again_button = tk.Button(self.frame, text="Play Again?", command=self.play_again)
        self.play_again_button.pack()
    
    def play_again(self):
        self.frame.destroy()    
        return True
    
    def load_card_image(self, card):
        if card.rank == 'Black Joker':
            card_filename = "black_joker.png"
        elif card.rank == 'Red Joker':
            card_filename = "red_joker.png"
        card_filename = f"{card.rank}_of_{card.suit}.png".replace(' ', '_')
        card_path = os.path.join("PNG-cards-1.3", card_filename)
        image = Image.open(card_path)
        return ImageTk.PhotoImage(image)
    
    def display_card(self, card):
        if self.card_image:
            self.canvas.delete(self.card_image)
        card_image = self.load_card_image(card)
        self.card_image = self.canvas.create_image(400, 400, image=card_image)
        self.canvas.image = card_image



class GameScreen:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.pack()
        

        with open("instructions.txt", "r") as file:
            instructions = file.read()
        self.description_label = tk.Label(self.frame, text=instructions)
        self.root.geometry("800x800")  
        self.description_label.pack()

        self.start_button = tk.Button(self.frame, text="Start", command=self.start_game)
        self.start_button.pack(pady=80)

        self.joker_var = tk.BooleanVar(value=include_jokers)
        self.joker_checkbutton = tk.Checkbutton(self.frame, text="Include Jokers", variable=self.joker_var, command=self.toggle_jokers)
        self.joker_checkbutton.pack()

    def start_game(self):
        self.frame.destroy()
        self.root.title("Card Game")
        deck = Deck()
        player1 = Player("Player 1")
        dealer = Player("Dealer")
        play = True
        while play is True:

            # Deal a card to the player and dealer each
            player1.draw(deck)
            dealer.draw(deck)

            # Display the player's hand and ask for a guess
            player1_guess = GameCardGUI(self.root, player1, dealer)
            
            # Evaluate result, display dealer's hand and ask if player wants to play again
            result = self.evaluate_result(player1, dealer, player1_guess)
            play = ResultScreen(self.root, player1, dealer, result)
        
        self.root.quit()

            

    def evaluate_result(self, player, dealer, player_guess):
        player_card = player.hand[-1]
        dealer_card = dealer.hand[-1]
        if player_guess is None:
            return
        if player_guess == (ranks.index(player_card.rank) < ranks.index(dealer_card.rank)):
            result = "You Win"
        else:
            result = "You Lose"
        return result

    def toggle_jokers(self):
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
    






