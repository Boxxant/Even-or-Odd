print("Is your number even or odd?")
while True:  # Runs forever
    ask = input("What is your number?")  # Prompts the user for number
    try:  # Prevents crash and notifies user if they enter a string instead of a number
        if int(ask) % 2 == 0:
            print('The number is even.')
        else:
            print('The number is odd.')
    except:
        print('You must enter a number.')

