# 🃏 Uno Card Game Simulator

A functional Python implementation of a simplified Uno card game, built from scratch using core Python principles — no external libraries required.

---

## 📌 What It Does

Simulates a complete Uno card game between multiple players. The game deals cards, matches by color or number, handles draws when no match exists, and runs until one player empties their hand.

Each card is a 2-character string: **digit (1–9)** + **color (r/g/b/y)**. For example, `5r` = 5 red, `9y` = 9 yellow.

---

## 🗂️ Project Structure

```
uno-card-game/
├── cardgame.py       # All game logic + built-in tests
├── requirements.txt
└── README.md
```

---

## ⚙️ Functions

| Function | Description |
|----------|-------------|
| `makeDeck()` | Creates a 36-card deck (9 numbers × 4 colors) |
| `deal(deck, players, cards)` | Deals cards round-robin, sets up discard pile |
| `draw(deck, playerHand)` | Draws a card from deck into player's hand |
| `discard(pile, playerHand, playerCard)` | Moves a card from hand to discard pile |
| `match(pile, playerHand)` | Finds a matching card by value or color |
| `play(deck, pile, playerHand)` | Runs one full turn — match/discard or draw |
| `supervisor(deck, pile, hands)` | Game loop — runs until a player wins |
| `initialize(nPlayers, nCards)` | Sets up a full game ready to play |

---

## 🚀 How to Run

```bash
# Run the built-in tests
python cardgame.py
```

To run a full game simulation, uncomment the simulation block at the bottom of `cardgame.py`:

```python
deck, pile, hands = initialize(2, 3)
winner = supervisor(deck, pile, hands, pause=False)
```

---

## 🧪 Tests

All functions include built-in assertion tests that run automatically. Expected output:

```
makeDeck() tests passed!
deal() tests passed!
match() tests passed!
discard() tests passed!
draw() tests passed!
play() tests passed!
All tests passed!
```

---

## 🛠️ Tech Stack

`Python 3` · `random` (shuffle) · No external dependencies

---

## ⚙️ Installation

```bash
git clone https://github.com/yoganand97/uno-card-game.git
cd uno-card-game
python cardgame.py
```
