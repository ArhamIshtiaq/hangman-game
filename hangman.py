#!/usr/bin/env python3
"""
Hangman Game - Python Implementation
A complete command-line hangman game with statistics tracking
Author: Arham Ishtiaq
"""

import random
import json
import os


class HangmanGame:
    """A complete Hangman game implementation with statistics tracking"""
    
    def __init__(self):
        self.words = [
            "apple", "banana", "cherry", "mango", "grapes", 
            "orange", "lemon", "peach", "berry", "melon",
            "python", "programming", "computer", "software", "technology"
        ]
        self.max_tries = 6
        self.stats_file = "game_stats.json"
        self.reset_game()
        self.load_stats()
    
    def reset_game(self):
        """Reset game state for a new game"""
        self.current_word = random.choice(self.words).upper()
        self.guessed_letters = set()
        self.tries_left = self.max_tries
        self.game_status = "playing"
        self.incorrect_guesses = set()
        self.correct_guesses = set()
    
    def load_stats(self):
        """Load game statistics from file"""
        try:
            if os.path.exists(self.stats_file):
                with open(self.stats_file, 'r') as f:
                    self.stats = json.load(f)
            else:
                self.stats = {
                    "games_played": 0,
                    "games_won": 0,
                    "current_streak": 0,
                    "best_streak": 0
                }
        except (json.JSONDecodeError, FileNotFoundError):
            self.stats = {
                "games_played": 0,
                "games_won": 0,
                "current_streak": 0,
                "best_streak": 0
            }
    
    def save_stats(self):
        """Save game statistics to file"""
        try:
            with open(self.stats_file, 'w') as f:
                json.dump(self.stats, f, indent=2)
        except IOError:
            print("Warning: Could not save statistics")
    
    def display_hangman(self):
        """Return hangman drawing based on incorrect guesses"""
        stages = [
            """
               ┌───┐
               │   │
                   │
                   │
                   │
                   │
            =========
            """,
            """
               ┌───┐
               │   │
               O   │
                   │
                   │
                   │
            =========
            """,
            """
               ┌───┐
               │   │
               O   │
               │   │
                   │
                   │
            =========
            """,
            """
               ┌───┐
               │   │
               O   │
              /│   │
                   │
                   │
            =========
            """,
            """
               ┌───┐
               │   │
               O   │
              /│\  │
                   │
                   │
            =========
            """,
            """
               ┌───┐
               │   │
               O   │
              /│\  │
              /    │
                   │
            =========
            """,
            """
               ┌───┐
               │   │
               O   │
              /│\  │
              / \  │
                   │
            =========
            """
        ]
        return stages[self.max_tries - self.tries_left]
    
    def display_word(self):
        """Display the current state of the word"""
        display = ""
        for letter in self.current_word:
            if letter in self.correct_guesses:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()
    
    def is_word_complete(self):
        """Check if the word has been completely guessed"""
        return all(letter in self.correct_guesses for letter in self.current_word)
    
    def guess_letter(self, letter):
        """Process a letter guess"""
        letter = letter.upper()
        
        if not letter.isalpha() or len(letter) != 1:
            return False, "Please enter a single letter!"
        
        if letter in self.guessed_letters:
            return False, f"You already guessed '{letter}'. Try a different letter!"
        
        self.guessed_letters.add(letter)
        
        if letter in self.current_word:
            self.correct_guesses.add(letter)
            message = f"Great! '{letter}' is in the word!"
            
            if self.is_word_complete():
                self.game_status = "won"
                self.stats["games_won"] += 1
                self.stats["current_streak"] += 1
                if self.stats["current_streak"] > self.stats["best_streak"]:
                    self.stats["best_streak"] = self.stats["current_streak"]
                message += f"\nCongratulations! You won! The word was '{self.current_word}'"
            
            return True, message
        else:
            self.incorrect_guesses.add(letter)
            self.tries_left -= 1
            message = f"Sorry, '{letter}' is not in the word. Tries left: {self.tries_left}"
            
            if self.tries_left == 0:
                self.game_status = "lost"
                self.stats["current_streak"] = 0
                message += f"\nGame Over! The word was '{self.current_word}'"
            
            return False, message
    
    def display_game_state(self):
        """Display the current game state"""
        print("\n" + "="*50)
        print("HANGMAN GAME")
        print("="*50)
        print(self.display_hangman())
        print(f"Word: {self.display_word()}")
        print(f"Tries left: {self.tries_left}")
        print(f"Category: Fruits & Tech")
        
        if self.correct_guesses:
            print(f"Correct guesses: {', '.join(sorted(self.correct_guesses))}")
        if self.incorrect_guesses:
            print(f"Incorrect guesses: {', '.join(sorted(self.incorrect_guesses))}")
        
        print("-" * 50)
    
    def display_stats(self):
        """Display game statistics"""
        win_rate = (self.stats["games_won"] / max(self.stats["games_played"], 1)) * 100
        
        print("\nGAME STATISTICS")
        print("=" * 30)
        print(f"Games Played: {self.stats['games_played']}")
        print(f"Games Won: {self.stats['games_won']}")
        print(f"Win Rate: {win_rate:.1f}%")
        print(f"Current Streak: {self.stats['current_streak']}")
        print(f"Best Streak: {self.stats['best_streak']}")
        print("=" * 30)
    
    def play_game(self):
        """Main game loop"""
        print("\nWelcome to Hangman!")
        print("Guess the word letter by letter. You have 6 tries!")
        print("Type 'quit' to exit, 'stats' to see statistics, 'hint' for a hint")
        
        while self.game_status == "playing":
            self.display_game_state()
            
            guess = input("\nEnter a letter (or command): ").strip().lower()
            
            if guess == 'quit':
                print("Thanks for playing!")
                return
            elif guess == 'stats':
                self.display_stats()
                continue
            elif guess == 'hint':
                self.give_hint()
                continue
            
            success, message = self.guess_letter(guess)
            print(f"\n{message}")
        
        # Game ended
        self.stats["games_played"] += 1
        self.save_stats()
        self.display_game_state()
        
        if self.game_status == "won":
            print("\nExcellent work! You're a word master!")
        else:
            print("\nBetter luck next time! Keep practicing!")
        
        self.display_stats()
    
    def give_hint(self):
        """Provide a hint to the player"""
        hints = {
            "APPLE": "A red or green fruit that keeps doctors away",
            "BANANA": "A yellow curved fruit loved by monkeys",
            "CHERRY": "Small red fruit often used in desserts",
            "MANGO": "Sweet tropical fruit with orange flesh",
            "GRAPES": "Small fruits that grow in bunches",
            "ORANGE": "Citrus fruit that shares its name with a color",
            "LEMON": "Sour yellow citrus fruit",
            "PEACH": "Fuzzy fruit with a pit in the center",
            "BERRY": "Small, round fruit often found in pies",
            "MELON": "Large, round fruit with sweet flesh",
            "PYTHON": "A programming language named after a snake",
            "PROGRAMMING": "The art of writing code",
            "COMPUTER": "Electronic device for processing data",
            "SOFTWARE": "Programs and applications for computers",
            "TECHNOLOGY": "Modern tools and digital innovations"
        }
        
        hint = hints.get(self.current_word, "It's a word with letters!")
        print(f"\nHint: {hint}")


def main():
    """Main function to run the hangman game"""
    while True:
        game = HangmanGame()
        game.play_game()
        
        while True:
            play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
            if play_again in ['y', 'yes']:
                break
            elif play_again in ['n', 'no']:
                print("\nThanks for playing Hangman!")
                print("Game statistics have been saved.")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")


if __name__ == "__main__":
    main()