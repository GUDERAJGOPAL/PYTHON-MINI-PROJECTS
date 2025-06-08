import random

def main():
    game()

def game():
    try:
        n = int(input("Enter level (1 to 3): "))
        if 1 <= n <= 3:
            start()
        else:
            print("Invalid level. Please enter a number between 1 and 3.")
            game()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        game()

def start():
    count = 10
    score = 0

    while count > 0:
        n1 = random.randint(0, 9)
        n2 = random.randint(0, 9)
        
        print(f"What is {n1} + {n2}?")
        
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == n1 + n2:
                score += 1
                print("Correct!")
            else:
                print("Incorrect!")
            
            count -= 1
            print(f"Score: {score} | Attempts left: {count}")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"Game over! Your final score is: {score}")

main()
