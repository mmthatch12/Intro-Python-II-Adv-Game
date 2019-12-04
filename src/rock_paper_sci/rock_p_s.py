import random

choices = ['r', 'p', 's']

wins = 0
losses = 0
ties = 0

def check_inputs(cmd, cpu_cmd):
    if cmd == cpu_cmd:
        return 0
    elif cmd == "r" and cpu_cmd == "s" \
        or cmd == "p" and cpu_cmd == "r" \
        or cmd == "s" and cpu_cmd == "p":
        return 1
    else:
        return -1


# Create a REPL loop to process commands
while True: # Loop
    # Read
    cmd = input("-> ")

    # CPU will pick a random choice
    cpu_choice = random.choice(choices)

    # REPL should accept 'r', 'p', 's' commands
    # 'q' to quit
    # Eval
    if cmd in choices:
        result = check_inputs(cmd, cpu_choice)
        if result == 1:
            wins += 1
            print(f"CPU chooses {cpu_choice}. You win!")
        elif result == 0:
            ties += 1
            print(f"CPU chooses {cpu_choice}. You tie.")
        elif result == -1:
            losses += 1
            print(f"CPU chooses {cpu_choice}. You lose...")
    elif cmd == "q":
        # Break out of the loop
        print("Goodbye!")
        break
    else:
        print("Invalid command.")

    # Print out the score and loop
    print(f"\n\n{wins} / {losses} / {ties}")

