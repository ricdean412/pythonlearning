#-----------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A,B,C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)

#-----------------------
def check_answer(answer, guess):

    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0
#-----------------------
def display_score(correct_guesses, guesses):
    print("----------------------")
    print("RESULTS")
    print("----------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

#-----------------------
def play_again():

    response = input("Do you want to play again?: (yes or no): ")
    response = response.upper()

    if response  == "YES":
        return True
    else:
        return False

#-----------------------

# Dictionary:
questions = {
    "Who wields the Master Sword?: ":"B",
    "What color is Super Saiyan God?: ":"D",
    "What is Frieza's catchphrase?: ":"A",
    "What does BMW stand for?: ":"D"
}

options = [["A. Mario", "B. Link", "C. Sonic", "D. Gohan"],
           ["A. Yellow/Gold", "B. Blue", "C. Pink", "D. Red"],
           ["A. Hello, Monkeys!", "B. Hello, Apes!", "C. Hello, Dinos!", "D. Hello, Ducks!"],
           ["A. Break My Windows", "B. Black Man's Wish", "C. British Motor Works", "D. Bayerische Motoren Werke"]]

new_game()

while play_again():
    new_game()

print("Byeeee, thanks for playing!")