# ♟️ Chess-CLI

A clean, zero-dependency command-line interface for playing two-player turn-based chess in your terminal.

---

## ✨ Features

- **Pure Python**: Zero third-party dependencies required (runs with standard Python 3.10+).
- **Turn-Based Local Multiplayer**: Alternates between White and Black turns.
- **Rule Enforcement & Move Validation**:
  - Full movement patterns for Pawns, Rooks, Knights, Bishops, Queens, and Kings.
  - Path obstruction collision checks.
  - Coordinate-based input validation.
- **Capture Detection & Win Conditions**: Capturing the opponent's King or resign commands (`r`).

---

## 🚀 How to Run

Ensure you have Python 3 installed. Then simply clone and run:

```bash
python main.py
```

---

## 🎮 How to Play

The game is played by entering the coordinates of the piece you want to move and its destination square.

### Making a Move
When prompted, enter your move in two steps:
1. **Initial**: The coordinate of the piece you want to move (e.g., `e2`).
2. **Final**: The coordinate of the target square (e.g., `e4`).

```text
Enter your move (r for resign):-
Initial: e2
Final: e4
```

### Resigning
If you wish to resign the game, enter `r` when prompted for the initial move.

---

## 🧭 Coordinates & Piece Reference

- **Files (Columns)**: `a` through `h`
- **Ranks (Rows)**: `1` through `8`

| Symbol | Piece | Color |
| :---: | :---: | :---: |
| `K` / `♚` | King | White |
| `Q` / `♛` | Queen | White |
| `R` / `♜` | Rook | White |
| `B` / `♝` | Bishop | White |
| `N` / `♞` | Knight | White |
| `P` / `♟` | Pawn | White |
| `k` | King | Black |
| `q` | Queen | Black |
| `r` | Rook | Black |
| `b` | Bishop | Black |
| `n` | Knight | Black |
| `p` | Pawn | Black |
| `.` | Empty | - |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
