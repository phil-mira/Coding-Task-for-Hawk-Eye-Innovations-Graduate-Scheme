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

$(document).ready(function() {
    $('#gameCardImage').attr('src', getCardImage(currentCard));
    $('#higherButton').click(guessHigher);
    $('#lowerButton').click(guessLower);
    console.log('Event listeners added');
});

function getCardImage(card) {
    const rank = card.rank.toLowerCase();
    const suit = card.suit.toLowerCase();
    return `PNG-cards-1.3/${rank}_of_${suit}.png`;
}

function displayMessage(message) {
    $('#message').text(message);
    setTimeout(() => {
        $('#message').text('');
    }, 3000); // Clear the message after 5 seconds
}

function guessHigher() {
    console.log('Higher button clicked');
    let newCard = deck.deal();
    if (newCard.getValue() > currentCard.getValue()) {
        displayMessage('Correct! The new card is higher.');
    } else {
        displayMessage('Wrong! The new card is not higher.');
    }
    currentCard = newCard;
    $('#gameCardImage').attr('src', getCardImage(currentCard));
}

function guessLower() {
    console.log('Lower button clicked');
    let newCard = deck.deal();
    if (newCard.getValue() < currentCard.getValue()) {
        $('#message').text('Correct! The new card is lower.');
    } else {
        $('#message').text('Wrong! The new card is not lower.');
    }
    currentCard = newCard;
    $('#gameCardImage').attr('src', getCardImage(currentCard));
}