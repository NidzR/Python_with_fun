 #((2. Dice Rolling Simulator))

# import random

# def roll_dice():
#     print(f"🎲 You rolled a {random.randint(1, 6)}!")

# while True:
#     input("Press Enter to roll the dice or type 'exit' to quit: ")
#     if input().lower() == "exit":
#         break
#     roll_dice()

#(3. Joke Generator)

# import pyjokes

# print("Here's a joke for you:")
# print(pyjokes.get_joke())

#(4. Guess the Number)

# import random

# number = random.randint(1, 100)
# print("Guess a number between 1 and 100!")

# while True:
#     guess = int(input("Your guess: "))
#     if guess < number:
#         print("Too low! Try again.")
#     elif guess > number:
#         print("Too high! Try again.")
#     else:
#         print("🎉 Correct! You guessed it!")
#         break

#(5. Emoji Translator)

# def emoji_translator(text):
#     words = text.split()
#     emojis = {
#         "happy": "😊",
#         "sad": "😢",
#         "love": "❤️",
#         "angry": "😡",
#         "laugh": "😂",
#         "wow": "😲",
#         "cool": "😎",
#         "cry": "😭",
#         "confused": "😕",
#         "party": "🥳",
#         "tired": "😴",
#         "sleepy": "😪",
#         "hungry": "🍔",
#         "food": "🍕",
#         "heart": "💖",
#         "fire": "🔥",
#         "thumbs_up": "👍",
#         "thumbs_down": "👎",
#         "ok": "👌",
#         "star": "⭐",
#         "clap": "👏",
#         "strong": "💪",
#         "money": "💵",
#         "idea": "💡",
#         "robot": "🤖",
#     }
#     return " ".join([emojis.get(word, word) for word in words])

# # Input sentence
# text = input("Type a sentence: ")
# print(emoji_translator(text))

#(6. Magic 8-Ball)

# import random

# answers = [
#     "Yes, definitely!",
#     "No way!",
#     "Maybe.",
#     "Ask again later.",
#     "It is certain.",
#     "Very doubtful.",
# ]

# question = input("Ask the Magic 8-Ball a question: 🎱 ")
# print("Thinking...")
# print(random.choice(answers))

#(7. Password Strength Checker)

# import re

# password = input("Enter a password: ")

# if len(password) < 8:
#     print("Weak: Password should be at least 8 characters long.")
# elif not re.search("[A-Z]", password):
#     print("Weak: Add an uppercase letter.")
# elif not re.search("[0-9]", password):
#     print("Weak: Add a number.")
# elif not re.search("[@#$%&*!]", password):
#     print("Weak: Add a special character.")
# else:
#     print("Strong Password! 💪")

#(8. ASCII Art Generator)

from art import *

text = input("Enter your text: ")
print(art(text))
