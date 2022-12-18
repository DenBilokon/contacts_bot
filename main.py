from phone_bot import *


def main():
    checking = True
    bye_list = ['.', 'bye', 'good bye', 'close', 'exit']

    while checking:
        user_input = str(input(">>>> "))
        if user_input.strip().lower() in bye_list:
            print('Good bye!')
            checking = False
        elif user_input.lower() == 'help':
            print(help_user)
        else:
            run_bot(user_input)


if __name__ == "__main__":

    main()