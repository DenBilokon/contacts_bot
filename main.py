import time
from phone_bot import *


def main():
    checking = True
    bye_list = ['.', 'bye', 'good bye', 'close', 'exit']

    while checking:
        user_input = str(input())
        input_list = user_input.split(" ")
        if user_input.strip() == 'hello':
            print("How can I help you?")

        elif user_input.strip() in bye_list:
            print('Good bye')
            time.sleep(2)
            checking = False

        elif user_input == "show all":
            show_all()

        elif input_list[0] == 'phone':
            phone(input_list[1])

        elif input_list[0] == 'add':
            add(input_list[1], input_list[2])

        elif input_list[0] == 'change':
            change(input_list[1], input_list[2], input_list[3])

        else:
            print("Incorrect input. Try again")


if __name__ == "__main__":
    main()