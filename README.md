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
Eliminates two incorrect answers, leaving the correct answer and one random incorrect option.
2. Ask the Audience
Simulates audience voting with percentages.
The correct answer has the majority of votes.
3. Phone a Friend
Simulates advice from a friend.
The friend typically gives the correct answer with high confidence.















