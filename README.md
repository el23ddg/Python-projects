# Python-projects
A group of projects which I am learning and building to understand and grasp better concepts. 

## 1. Rock_Paper_Scissors_Game.py
#### Project Brief 📄
This is a simple command-line-based Python program where the user can play a round of the classic game Rock, Paper, Scissors against the computer. It’s a fun way to practice Python programming, especially working with user input, random number generation, and control flow.
#### Rules of the Game 📜
- Rock (✊) beats Scissors (✌).
- Scissors (✌) beat Paper (✋).
- Paper (✋) beats Rock (✊).
- If both the user and the computer choose the same item, it’s a tie.
#### Features ✨
- Allows the user to choose between Rock, Paper, and Scissors by entering a number (1, 2, or 3).
- The computer randomly selects its choice using Python's random.randint() function.
- Displays the user's choice and the computer's choice with corresponding emojis.
- Clearly determines and announces the winner or if it’s a tie.

## 2. GIF.py - Image to GIF Converter 🖼️➡️🎞️
#### Project Overview 📄
This project demonstrates how to convert multiple image files into an animated GIF using Python and the imageio library. The provided script takes a sequence of images, combines them, and saves the result as an animated GIF. It's a simple yet effective way to bring static images to life!
#### Features ✨
- Converts a sequence of 2 or more images into an animated GIF.
- Allows customization of GIF properties, such as frame duration and loop behavior.
- Lightweight and straightforward, powered by Python's imageio library.
#### Customization 🚀
You can easily tweak the script for your needs:
- Change frame duration: Modify the duration parameter to speed up or slow down the animation.
- Change loop behavior: Set loop to 1 for a single loop or 0 for infinite looping.
#### Output
![dinodancer](https://github.com/user-attachments/assets/41e19d31-a859-47ba-8206-008a9d46c0d8)

## 3. Meme_Generation_Bot.py - Build a Discord Bot with Python 🤖
#### Project Overview 📄
This project is a step-by-step guide to creating your own custom Discord bot using Python. It leverages the discord.py library to allow you to interact with Discord’s API, enabling you to build bots for moderation, automation, games, and more.
#### Features ✨
- Connects your bot to a Discord server.
- Responds to commands sent in the chat.
- Highly customizable to suit various use cases (e.g., moderation, fun commands, notifications).
#### What I Learnt 🧠
- How to set up a Discord bot application on the Discord Developer Portal.
- How to use the discord.py library to build and manage your bot.
- Sending messages, responding to commands, and handling events.
- Basic coding concepts like functions, libraries, and asynchronous programming.
#### My Bot - memeBot
![Screenshot 2025-01-17 182649](https://github.com/user-attachments/assets/d2e46a7f-cf2d-49cd-9719-0678f359974b)
#### Acknowledgments 🙌
This project was inspired by CodeDex's guide, which makes learning Discord bot development accessible and fun. 

## 4. Dice_Rolling_Simulator.py 🎲
#### Project Overview 📄
The Dice Rolling Simulator is a simple Python-based game that simulates the rolling of a six-sided die. It provides users with an interactive experience to roll a dice, view the result, and decide whether to roll again or exit the game. This project is perfect for beginners who want to learn Python concepts like loops, conditional statements, and random number generation.
#### Features ✨
- Roll a virtual six-sided die.
- Interactive gameplay with user inputs.
- Simple, lightweight, and beginner-friendly.
#### Customization 🚀
Here are some ways you can expand the project:
- Allow the user to select different types of dice (e.g., 4-sided, 8-sided, 20-sided).
- Add a scoring system to track results over multiple rolls.
- Create a graphical user interface (GUI) using libraries like tkinter or PyQt.
- Add sound effects when the dice is rolled.
#### Output looks like this
![dice game terminal](https://github.com/user-attachments/assets/a9bd72a2-1964-4427-b0a0-dc15a3fb8828)

## 5. Who_wants_to_be_a_Millionare.py
#### Project Overview 📄
This is a Python-based console game inspired by the popular TV show "Who Wants to Be a Millionaire". Players answer a series of multiple-choice questions to win increasing amounts of money, with lifelines available to help along the way.
#### Features ✨
Multiple-choice questions: Players answer questions with four options (A, B, C, or D).
Three lifelines:
- 50-50: Eliminates two incorrect options.
- Ask the Audience: Simulates audience polling with percentage-based voting.
- Phone a Friend: Simulates a friend's advice, favoring the correct answer.
- Incremental rewards: Players win money for each correct answer, with the total displayed at the end.
- Input validation: Ensures valid user input for questions and lifeline selection.
#### How the lifelines work
1. 50-50
- Eliminates two incorrect answers, leaving the correct answer and one random incorrect option.
2. Ask the Audience
- Simulates audience voting with percentages.
- The correct answer has the majority of votes.
3. Phone a Friend
- Simulates advice from a friend.
- The friend typically gives the correct answer with high confidence.

## 6. QR Code Generator project
#### Project Overview 📄
This Python program generates a QR code for a given website link and saves it as an image file (youtube_qr.png). You can scan this QR code with a smartphone or QR code reader to instantly access the encoded URL.
#### How it works
- The program uses the qrcode library to create the QR code.
- The QR code is styled with:
a) Version: 1 (determines the complexity and size of the QR code).
b) Box Size: 5 (defines the size of each square in the QR grid).
c) Border: 5 (sets the width of the border around the QR code).
- The QR code is rendered as an image with:
a) Fill Color: Black
b) Background Color: White
- Finally, the QR code is saved as a .png image file.

## 7. GEN AI projects
#### A group of beginner gen ai projects which will equip me for future projects. I am learning tokenization, text classification, spell check, machine translation and naive bayes to start with. This will help me to build the foundation for better projects.

## 8. Text Based Treasure Hunt Game Project
#### Project Overview 📄
Welcome to the Text-Based Treasure Hunt Game, a Python-based interactive game where you explore a mysterious world, face enemies, collect items, and aim to find the ultimate treasure! 💎 This project combines a fun gameplay experience with Python programming concepts such as dictionaries, loops, conditionals, and user input handling.
#### Features ✨
Explore 5 Unique Rooms:
- Traverse through a Hall, Kitchen, Dungeon, Armory, and the Treasure Room.
- Each room has its own description, items, and challenges. 🗺️
Combat System:
- Fight enemies like the Goblin and the Skeleton Warrior.
- Use weapons like the Knife to increase your damage.
- Strategic gameplay: Choose to attack or run from battles! ⚔️
Score System:
- Earn points by defeating enemies (+20 points) and collecting items (+10 points). 🏆
- Your score reflects your progress and achievements in the game.
Health System:
- Start with 100 health points, which decreases during battles.
- Collect items like the Shield to increase your health. ❤️
Treasure Hunt:
- Your ultimate goal is to find the Treasure Room and claim the glittering treasure. 🪙
- Winning the game displays your final score. 🎉









