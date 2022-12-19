from phone_bot import *


def main():
    # checking = True

    while True:
        user_input = str(input(">>>> "))
        # if user_input.strip().lower() in bye_list:
        #     print('Good bye!')
        #     checking = False
        # elif user_input.lower() == 'help':
        #     print(help_user)
        # else:
        result = run_bot(user_input)
        if result == 'Bye':
            print('Goodbye!')
            break
        print(result)


if __name__ == "__main__":
    main()
