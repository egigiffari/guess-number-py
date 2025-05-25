import random

def main():
    print("========================")
    print("====GUESS THE NUMBER====")
    print("========================")

    low_num = 1
    high_num = 100
    print(f"Select a number between {low_num} and {high_num}")
    
    attempt = 0
    secret_number = random.randint(low_num, high_num)
    is_running = True

    while is_running:
        answer = input("Please input your guess: ")
        
        if not answer.isdigit():
            print(f"Please input the valid number between ({low_num},{high_num})")
            continue

        answer = int(answer)
        attempt += 1

        if answer < secret_number:
            print("Too low, Try again")
            continue

        if answer > secret_number:
            print("Too High, Try again")
            continue

        print(f"Correct!, the number is {secret_number}")
        print("Attempt: ", attempt)
        is_running = False


if __name__ == "__main__":
    main()