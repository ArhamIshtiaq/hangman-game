# hangman-game
Interactive web-based Hangman game built with React and TypeScript
## Features

- **Interactive Gameplay**: Classic hangman experience with visual hangman drawing
- **Statistics Tracking**: Persistent game statistics including win rate and streaks
- **Word Categories**: Fruits and technology-themed words
- **Visual ASCII Art**: Dynamic hangman drawing that updates with each wrong guess
- **Hint System**: Built-in hints for each word to help players
- **Game Commands**: 
  - `quit` - Exit the game
  - `stats` - View game statistics
  - `hint` - Get a hint for the current word
- **Error Handling**: Robust input validation and file handling
- **Persistent Data**: Game statistics saved between sessions

## How to Run

```bash
python hangman.py
```

## Game Rules

1. **Objective**: Guess the hidden word letter by letter
2. **Lives**: You have 6 incorrect guesses before losing
3. **Input**: Enter single letters (case insensitive)
4. **Winning**: Guess all letters in the word before running out of tries
5. **Commands**: Use special commands for additional features

## Programming Concepts Demonstrated

- **Object-Oriented Programming**: Complete class-based implementation
- **File I/O Operations**: JSON-based statistics persistence
- **Error Handling**: Try-catch blocks for robust user experience
- **Data Structures**: Sets for efficient letter tracking, dictionaries for statistics
- **String Manipulation**: Word display and input processing
- **Control Flow**: Complex game state management with loops and conditionals
- **Random Selection**: Dynamic word selection for gameplay variety
- **JSON Handling**: Structured data storage and retrieval

## Game Statistics

The game tracks comprehensive statistics:
- **Games Played**: Total number of games
- **Games Won**: Number of victories
- **Win Rate**: Percentage of games won
- **Current Streak**: Consecutive wins
- **Best Streak**: Highest consecutive win count

Statistics are automatically saved to `game_stats.json` and persist between sessions.

## Word Categories

### Fruits
- Apple, Banana, Cherry, Mango, Grapes
- Orange, Lemon, Peach, Berry, Melon

### Technology
- Python, Programming, Computer, Software, Technology

## Example Gameplay

```
==================================================
HANGMAN GAME
==================================================
               ┌───┐
               │   │
               O   │
              /│   │
                   │
                   │
            =========

Word: P _ _ _ _ N
Tries left: 3
Category: Fruits & Tech
Correct guesses: N, P
Incorrect guesses: A, E, I

Enter a letter (or command): t
Great! 'T' is in the word!

Word: P _ T _ _ N
```

## Code Structure

### Main Components

- **`HangmanGame` Class**: Core game logic and state management
- **`reset_game()`**: Initialize new game state
- **`load_stats()` / `save_stats()`**: Statistics persistence
- **`display_hangman()`**: ASCII art rendering
- **`guess_letter()`**: Input processing and game logic
- **`give_hint()`**: Hint system implementation
- **`play_game()`**: Main game loop

### Key Features Implementation

- **Visual Feedback**: 7-stage ASCII hangman drawing
- **Input Validation**: Comprehensive error checking
- **Game State Management**: Clean separation of game phases
- **Data Persistence**: JSON-based statistics storage

## Technical Highlights

- **Modular Design**: Well-organized class structure
- **Error Resilience**: Graceful handling of file operations
- **User Experience**: Clear feedback and intuitive commands
- **Code Documentation**: Comprehensive docstrings and comments
- **Scalability**: Easy to add new words and categories

## Requirements

- Python 3.x (no external dependencies required)
- Works on Windows
- Automatic creation of statistics file

## Educational Value

This project demonstrates:
- **Advanced Python Programming**: Classes, methods, and data structures
- **File Handling**: Reading, writing, and error management
- **Game Development**: State management and user interaction
- **Data Persistence**: JSON storage and retrieval
- **User Interface Design**: Console-based interactive experience
- **Software Architecture**: Clean, maintainable code organization

## Future Enhancements

Potential improvements could include:
- Multiple difficulty levels
- Expanded word categories
- Multiplayer functionality
- GUI implementation
- Online word database integration

## Author

**Arham Ishtiaq** - 

*This project showcases object-oriented programming, file I/O, data persistence, and interactive console application development in Python.*
