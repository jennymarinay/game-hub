def mathGame():
    pass

def trivia():
    print("Hello, Welcome to Pinoy's Trivia!")

    ans = input("Are you ready to play? (YES/NO): ")
    score = 0
    total_q = 4                

    if ans.lower() == 'yes':
            ans = input("1. Name the oldest Philippine city.: ")
            if ans == 'cebu':
                score += 1
                print("Correct!")
            else:
                print("Incorrect")

            ans = input("2. What place in the Philippines is also known as the “walled city”?: ")
            if ans.lower() == 'intramuros':
                score += 1
                print("Correct!")
            else:
                print("Incorrect")

            ans = input("3. What is the capital of the Republic of the Philippines?: ")
            if ans.lower() == 'manila':
                score += 1
                print("Correct!")
            else:
                print("Incorrect")

            ans = input("4. Philippines is located in which continent: ")
            if ans.lower() == 'asia':
                score += 1
                print("Correct!")
            else:
                print("Incorrect")

            ans = input("5. Philippines national food is?: ")
            if  ans.lower() == 'lechon':
                score += 1
                print("Correct!")
            else:
                print("Incorrect")

    print("Thank you for playing, you got", score, "correct answer/s!")
    mark = (score/total_q) * 100

    print("Mark:", str(mark) + '%')
    print('Goodbye')

    ans1 = input('You want to try again? (YES/NO): ')
    if ans1.lower() == 'yes' or ans1.upper() == 'yes':
        main()
    else:
        exit()
    
    
def rock_paper_scissors():
    pass

def wordGuess():
    pass

def sudoku():
    pass


def main():
    while True:
        print("1. Math Game\n2. Trivia\n3. Rock Paper Scissor\n4. Word Guessing Game\n5. Sudoku\n6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            mathGame()
        elif choice == "2":
            trivia()
        elif choice == "3":
            rock_paper_scissors()
        elif choice == "4":
            wordGuess()
        elif choice == "5":
            sudoku()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

