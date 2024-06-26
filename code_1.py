# THIS IS A QUIZ PROGRAM

def score_function(content, tag, user_points):
    """
    This function takes as a parameter content, tag and user_points.
    content: quiz is read by lines.
    tag: answer for each question.
    user_points: user's score.
    """
    print(content)  # prints the quiz read by lines

    options = ['a', 'b', 'c', 'd']  # options that the user has to answer each question.

    for i in range(2):  # this loop makes the user have 2 chances to enter an answer between "options".
        user_input = input('Enter your choice (a, b, c, or d): ')
        if user_input in options:
            if user_input == tag:
                print('Correct answer!')
                # if the user's answer is right, the 'correct answer!' message will appear.
                user_points += 1
            else:
                print('Wrong answer :/')
                # if the user's answer is wrong, the 'wrong answer :/' message will appear.
            break
        else:
            print('This option is not valid.')
            # if the user input is not between "options" the 'This option is not valid.'
            # message will appear and give the user another chance
    else:
        print('Sorry, you have run out of chances.')
        # this message will appear after the user runs out of the 2 chances and the program will
        # automatically continue to the next question.

    return user_points


def quiz_function(fname):
    """
    This function takes fname as a parameter.
    fname: each text file that will be opened.
    The score function is called where:
    content[] : corresponds to lines for each question.
    'a, b, c, or d': varies depending on the correct answer for each question.
    user_points: keeps track of the score.
    """
    zero_width_space = '\u200b'
    
    with open(fname, encoding="utf8") as file:  # opens the file
        content = file.readlines()  # reads the file line by line
        content = [line.strip() for line in content] # removes the new line characters ('\n') from the questions and answers
        content = [line.replace(zero_width_space, '') for line in content] # removes the zero width ('\u200b')space when opening the text file

    user_points = 0  # user score starts at 0

    user_points = score_function(content[0:5], 'c', user_points)
    user_points = score_function(content[6:11], 'c', user_points)
    user_points = score_function(content[12:17], 'b', user_points)
    user_points = score_function(content[18:23], 'd', user_points)
    user_points = score_function(content[24:29], 'a', user_points)

    print(f'The quiz is over! Your score is: {user_points}/5.')  # final score for the quiz.


def main():
    # this function opens the program
    print("Welcome to quiz.program, choose your favorite topic's number: ")  # this message welcomes the user.
    user_choice = input('Type [1] for sports quiz, [2] for geography quiz, [3] for animals quiz, '
                        '[4] for internet quiz, or [5] for "who said it?" history quiz: ')
    # user_choice prompts the user to choose a quiz.

    options_quiz = ['1', '2', '3', '4', '5']  # options that the user has to guess
    if user_choice in options_quiz:  # this if statement calls the quiz_function to open each quiz.
        if user_choice == '1':
            quiz_function('sport_quiz.txt')
        elif user_choice == '2':
            quiz_function('geography_quiz.txt')
        elif user_choice == '3':
            quiz_function('animals_quiz.txt')
        elif user_choice == '4':
            quiz_function('internet_technology_quiz.txt')
        elif user_choice == '5':
            quiz_function('who_said_it_history_quiz.txt')
    else:
        print('Invalid option, try again.')
        return main()  # if the user's answer is not between the option, the invalid option message will appear and the main function will start again


main()

for i in range(10):  # this loop is to prompt the user to choose between playing again or not.
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again == 'yes':  # if the user's input is yes, the main function is called to start the quiz again.
        main()
    elif play_again == 'no':  # if the user's input is no, the "Thank you for playing!" message will appear.
        print("Thank you for playing!")
        break
    else:
        print('Invalid option, please try again.')  # if the answer is not yes or no, the user has to answer the question again.
