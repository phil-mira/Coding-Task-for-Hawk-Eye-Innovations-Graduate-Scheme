const suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'];
const ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'];

class Card {
    constructor(suit, rank) {
        this.suit = suit;
        this.rank = rank;
    }

    getValue() {
        return ranks.indexOf(this.rank) + 2;
    }

    toString() {
        return `${this.rank} of ${this.suit}`;
    }
}

class Deck {
    constructor() {
        this.cards = [];
        this.initializeDeck();
    }

    initializeDeck() {
        this.cards = [];
        for (let suit of suits) {
            for (let rank of ranks) {
                this.cards.push(new Card(suit, rank));
            }
        }
        this.shuffle();
    }

    shuffle() {
        for (let i = this.cards.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [this.cards[i], this.cards[j]] = [this.cards[j], this.cards[i]];
        }
    }

    deal() {
        return this.cards.pop();
    }
}

let deck = new Deck();
let currentCard = deck.deal();
let correctGuesses = 0; // Initialize the count of correct guesses
let totalGames = 0; // Initialize the count of total games played

$(document).ready(function() {
    // Set the initial card image when the document is ready
    $('#gameCardImage').attr('src', getCardImage(currentCard));
    // Add click event listeners to the "Higher" and "Lower" buttons
    $('#higherButton').click(guessHigher);
    $('#lowerButton').click(guessLower);
    // Update the score display
    $('#score').text(updateScore);
    console.log('Event listeners added');
});

// Function to get the image path for a given card
function getCardImage(card) {
    const rank = card.rank.toLowerCase();
    const suit = card.suit.toLowerCase();
    return `PNG-cards-1.3/${rank}_of_${suit}.png`;
}

// Function to display a message for 5 seconds
function displayMessage(message) {
    $('#message').text(message);
    setTimeout(() => {
        $('#message').text('');
    }, 5000); // Clear the message after 5 seconds
}

// Function to update the score display
function updateScore() {
    $('#score').text(`Score: ${correctGuesses}/${totalGames}`);
}

// Function to handle the "Higher" button click
function guessHigher() {
    console.log('Higher button clicked');
    let newCard = deck.deal(); // Deal a new card from the deck
    totalGames++; // Increment the total games count
    // Check if the new card's value is higher than the current card's value
    if (newCard.getValue() > currentCard.getValue()) {
        correctGuesses++; // Increment the correct guesses count
        displayMessage('Correct! The new card is higher.');
    } else {
        displayMessage('Wrong! The new card is not higher.');
    }
    currentCard = newCard; // Update the current card to the new card
    // Update the card image to the new card
    $('#gameCardImage').attr('src', getCardImage(currentCard));
    updateScore(); // Update the score display
}

// Function to handle the "Lower" button click
function guessLower() {
    console.log('Lower button clicked');
    let newCard = deck.deal(); // Deal a new card from the deck
    totalGames++; // Increment the total games count
    // Check if the new card's value is lower than the current card's value
    if (newCard.getValue() < currentCard.getValue()) {
        correctGuesses++; // Increment the correct guesses count
        displayMessage('Correct! The new card is lower.');
    } else {
        displayMessage('Wrong! The new card is not lower.');
    }
    currentCard = newCard; // Update the current card to the new card
    // Update the card image to the new card
    $('#gameCardImage').attr('src', getCardImage(currentCard));
    updateScore(); // Update the score display
}