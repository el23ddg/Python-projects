# who wants to be a millionare game in python
import random

questions = [{"question":"What is the capital of Italy?",
              "options":["A. Paris", "B. London", "C. Rome", "D. Berlin"],
              "answer":"C",
              "prize": 10000
},
{   "question":"What is the square of 16?",
    "options":["A. 144", "B. 256", "C. 324", "D. 386"],
    "answer":"B",
    "prize": 20000
},
{
    "question":"Who wrote the Merchant of Venice?",
    "options":["A. Shakespeare", "B. Dickens", "C. J.K.Rowling", "D. Scott Fitzgerald"],
    "answer":"A",
    "prize": 30000
},
{
    "question":"Who is the father of Machine Learning?",
    "options":["A. Aristotle", "B. Archimedes", "C. Euclid", "D. Arthur Samuel"],
    "answer":"D",
    "prize": 40000
}]

total_prize_money = 0
lifelines_used = {
    "50-50":False,
    "Ask the Audience":False,
    "Phone a friend":False
}

print("Welcome to 'Who Wants to Be a Millionaire'!")
print("Answer the questions correctly to win money. Lets see who can take the most amount today!!\n")
print("You can also use the available lifeline: 50-50, Ask the Audience, Phone a friend\n")

# Functions for the 3 lifelines 

# function for the 50-50 lifeline 
def use_50_50(correct_answer, options):
    wrong_answers = [opt[0] for opt in options if opt[0]!=correct_answer]
    wrong_answers_to_keep = random.choice(wrong_answers)
    final_options = [opt for opt in options if opt[0] in (correct_answer, wrong_answers_to_keep)]
    return final_options

# function for the Ask the Audience lifeline
def use_ask_the_audience(correct_answer, options):
    votes = {opt[0]: random.randint(5, 25) for opt in options}
    votes[correct_answer] += random.randint(30, 50)  # Correct answer gets the majority votes
    print("\nAudience Poll:")
    for opt, vote in votes.items():
        print(f"{opt}: {vote}%")
    print()

# function for the Phone a friend lifeline 
def use_phone_a_friend(correct_answer):
    confidence = random.choice(["I'm 100 percent sure", "I'm pretty sure", "I think", "I'm not sure, but my guess is"])
    print(f"\nYour friend says: \"{confidence} the answer is {correct_answer}.\"\n")

# looping through every question
for i,j in enumerate(questions):
    print(f"Question {i+1}:{j['question']}")
    for option in j['options']:
        print(option)
    
    # lifelines displaying and choosing options for the player 
    while True:
        use_lifeline = input("Do you want to use a lifeline? (yes/no): ").strip().lower()
        if use_lifeline == 'yes':
            print("Available lifelines: ")
            for lifeline, used in lifelines_used.items():
                if not used:
                    print(f"{lifeline}")
            chosen_lifeline = input("Choose a lifeline (50-50, Ask the Audience, Phone a Friend): ").strip()

            if chosen_lifeline == '50-50' and not lifelines_used == '50-50':
                lifelines_used['50-50'] = True
                j["options"]=use_50_50(j['answer'], j["options"])
                print("\nOptions after 50-50:")
                for option in j['options']:
                    print(option)
            elif chosen_lifeline == "Ask the Audience" and not lifelines_used["Ask the Audience"]:
                lifelines_used["Ask the Audience"] = True
                use_ask_the_audience(j['answer'], j['options'])
            elif chosen_lifeline == "Phone a friend" and not lifelines_used["Phone a friend"]:
                lifelines_used["Phone a friend"] = True
                use_phone_a_friend(j['answer'])
            else:
                print("Invalid choice or lifeline already used. Try again.")
                continue
        break

    player_answer = input('Enter your choice (A,B,C or D): ').strip().upper() # player's input for the choices 

    if player_answer == j['answer']:
        total_prize_money = total_prize_money + j['prize']
        print(f"Correct! you have won {j['prize']} rupees. The total prize is : {total_prize_money} rupees\n")
    else:
        print(f"Wrong anwer! The correct option was {j['answer']}")
        print(f"Game over the total prize you won is: {total_prize_money} rupees")
        break
else:
    print(f"Congrats you have done well and won a prize of : {total_prize_money} rupees")

print("Thank you for playing")






