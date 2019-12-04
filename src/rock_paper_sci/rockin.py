import random

choices = ['r', 'p', 's']

wins = 0
losses = 0
ties = 0

while True: # Loop
    cmd = input("-> ")

    cpu_choice = random.choice(choices)

    print(f"CPU chooses {cpu_choice}")
    if cmd == "r":
        if cpu_choice == "s":
            wins += 1
            print("You win!")
        elif cpu_choice == "r":
            ties += 1
            print("You tie.")
        elif cpu_choice == "p":
            losses += 1
            print("You lose...")
    elif cmd == "p":
        if cpu_choice == "r":
            wins += 1
            print("You win!")
        elif cpu_choice == "p":
            ties += 1
            print("You tie.")
        elif cpu_choice == "s":
            losses += 1
            print("You lose...")
    elif cmd == "s":
        if cpu_choice == "p":
            wins += 1
            print("You win!")
        elif cpu_choice == "s":
            ties += 1
            print("You tie.")
        elif cpu_choice == "r":
            losses += 1
            print("You lose...")
    elif cmd == "q":
        print("Goodbye!")
        break
    
    print(f"{wins} / {losses} / {ties}")

