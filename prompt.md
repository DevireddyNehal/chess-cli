Build **terminal chess V1** as a **turn-based local two-player game** first. Do **not** start with AI, checkmate analysis, animations, or fancy visuals.

## What V1 should do

* show an 8×8 board in terminal
* let White and Black take turns
* accept moves like `e2 e4`
* move pieces on the board
* enforce basic move rules
* reject illegal moves
* detect capture
* stop when a king is captured or a player resigns

That is enough for a strong first version.

---

## The best way to build it

## 1) Decide the board format

Use a simple 2D list.

Example idea:

* each square contains either empty or a piece
* pieces can be stored as text like:

  * `"wP"` = white pawn
  * `"bK"` = black king
  * `"--"` = empty square

This is the easiest structure to reason about.

Why this matters:

* easy to print
* easy to move
* easy to check contents

---

## 2) Print the board every turn

Do not try to make it “live” yet.

Each turn:

* clear the terminal
* print the board again
* show whose turn it is
* show last move
* ask for input

That already feels like a game.

---

## 3) Choose move input format

Use something simple like:

* `e2 e4`
* `b1 c3`
* `resign`

This is much easier than click-based movement.

You need a small function that converts:

* `e2` → board coordinates
* `e4` → board coordinates

That conversion is one of the first useful subproblems.

---

## 4) Build the game loop

Your main loop should always do this:

1. show board
2. ask current player for move
3. validate input format
4. check if the move is legal
5. update board if valid
6. switch turn
7. repeat

Keep this loop simple.

---

## 5) Build piece movement one piece at a time

Do **not** try to code all chess rules at once.

Do it in this order:

### First:

* pawns
* rooks
* knights

### Then:

* bishops
* queen
* king

Why this order:

* pawns teach direction and capture rules
* rooks/bishops teach line movement
* knights teach special movement
* queen combines rook + bishop
* king is small but important

---

## 6) Create one function per piece type

Each piece should have a “can this move happen?” check.

For example:

* pawn movement function
* rook movement function
* knight movement function
* bishop movement function
* queen movement function
* king movement function

Each function should answer only this:

> Is this move legal for this piece?

That keeps the code understandable.

---

## 7) Separate “piece rules” from “game rules”

This is important.

### Piece rules:

* can the rook move like a rook?
* can the knight move like a knight?

### Game rules:

* is it white’s turn?
* is destination occupied by own piece?
* is the path blocked?
* is the move in bounds?

Keep these separate.

That prevents the code from becoming a mess.

---

## 8) Start with basic legality only

For V1, you should **not** implement full advanced chess logic immediately.

You can postpone:

* castling
* en passant
* promotion
* check
* checkmate
* stalemate

For now, just make sure:

* pieces move correctly
* captures work
* turns alternate
* kings exist
* illegal moves are rejected

That is already a real chess engine skeleton.

---

## 9) Handle captures

If a piece moves to a square containing an enemy piece:

* remove enemy piece
* place moving piece there

If it contains your own piece:

* reject the move

That is a key part of the logic.

---

## 10) Add end conditions

For V1, easiest win condition:

* if a king is captured, game ends

That is not full chess rules, but it is enough for version 1.

Later you can replace it with true checkmate logic.

---

## 11) Keep the board readable

Use coordinates on the side, like:

* files: `a b c d e f g h`
* ranks: `8 7 6 5 4 3 2 1`

That helps you and makes it feel real.

---

## 12) Build in this exact order

Do not jump around.

### Phase A

* board setup
* display board
* print turn

### Phase B

* parse input like `e2 e4`

### Phase C

* move a knight correctly

### Phase D

* add pawn movement

### Phase E

* add rook, bishop, queen, king

### Phase F

* captures and turn switching

### Phase G

* end condition

If you try to do all pieces first, you will drown.

---

## 13) Test after every piece

After each step, test:

* legal move works
* illegal move is rejected
* turn changes correctly
* board redraws correctly

This is how you avoid getting lost.

---

## 14) Suggested file structure

Keep it in one file first if needed.

If you split later:

* `main.py` → game loop
* `board.py` → board setup/display
* `pieces.py` → move logic
* `utils.py` → coordinate parsing

But for today, one file is fine if that keeps you moving.

---

## 15) What to actually type first

Start with:

* board representation
* initial setup
* print function
* move parser

Do **not** start with checkmate.

That is premature complexity.

---

## 16) The simplest final V1 feature list

Your first working chess CLI should have:

* board display
* turn system
* move input
* piece movement
* captures
* king capture win condition
* resign command

That is a strong first build.

---

## 17) What makes this a good project for you

This is the right kind of hard because:

* it is logic-heavy
* it feels real
* it is terminal-only
* it has visible progress
* it is not boring CRUD
* it is not a fake wrapper
* it is hard enough to be proud of

---

## 18) Today’s exact order

Do this:

1. create project folder
2. create one Python file
3. define board layout
4. print board
5. parse move input
6. move knight only
7. test knight moves
8. add pawns
9. test captures
10. stop once the core loop works

Start small. Expand one piece at a time.

If you want, I can turn this into a **very exact build checklist for the first 2 hours**, still without dumping code.
