
PHONE_DICT = {}

HELP_TEXT = """This contact bot save your contacts 
    Global commands:
      'add' - add new contact. Input user name and phone
    Example: add User_name 095-xxx-xx-xx
      'change' - change users old phone to new phone. Input user name, old phone and new phone
    Example: change User_name 095-xxx-xx-xx 050-xxx-xx-xx
      'phone' - show contacts of input user. Input user name
    Example: phone User_name
      'show all' - show all contacts
    Example: show all
      'exit/'.'/'bye'/'good bye'/'close' - exit bot
    Example: good bye"""

# Decorator - оброблює помилки введення і виводить відповідний результат
def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return "Give me name, old phone and new phone"
        except KeyError:
            return "Enter correct username"
        except ValueError:
            return "Enter username"
        except TypeError:
            return "Not enough params for command"

    return wrapper


# Оброблює введений номер телефону до стандартного виду
def sanitize_phone_number(phone_num):
    new_phone = (
        phone_num.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def hello(*args):
    return "How can I help you?"


def bye(*args):
    return 'Bye'

def help_user(*args):
    return HELP_TEXT

# Додаємо новий номер телефону до списку
@input_error
def add(name, phone_num):
    if name in PHONE_DICT:
        PHONE_DICT[name].append(sanitize_phone_number(phone_num))
    if name not in PHONE_DICT:
        PHONE_DICT[name] = []
        PHONE_DICT[name].append(sanitize_phone_number(phone_num))
    return f"Added new contact - {name} {sanitize_phone_number(phone_num)}"


# Замінюємо старий номер телефону на новий
@input_error
def change(name: str, old_num: str, new_num):
    if name in PHONE_DICT:
        PHONE_DICT[name].remove(sanitize_phone_number(old_num))
        PHONE_DICT[name].append(sanitize_phone_number(new_num))
    return f"Changed contact {name} - number {sanitize_phone_number(old_num)} to number {sanitize_phone_number(new_num)}"


# Виводимо номер телефону по імені
@input_error
def phone(name):
    phones = ""
    for i in PHONE_DICT[name]:
        phones += i + " "
    return phones


# Виводимо всі номери телефонів
@input_error
def show_all(*args):
    text = ""
    for name_user, phone_list in PHONE_DICT.items():
        phones = ""
        for i in phone_list:
            phones += i + " "
        text += ''.join(name_user + ": " + phones + '\n')

    return text


COMMANDS = {hello: ['hello', 'hi'],
            show_all: ['show all'],
            phone: ['phone'],
            add: ['add'],
            change: ['change'],
            help_user: ['help'],
            bye: ['.', 'bye', 'good bye', 'close', 'exit']
            }


def parse_command(text: str):
    for comm, key_words in COMMANDS.items():
        for key_word in key_words:
            if text.startswith(key_word):
                return comm, text.replace(key_word, '').strip().split(' ')
    return None, None


# Функція спілкування з юзером і виконання функцій відповідно до команди
def run_bot(user_input):
    command, data = parse_command(user_input)
    if not command:
        return "Incorrect input. Try again"
    return(command(*data))
    # if user_input.strip().lower() == 'hello':
    #     print("How can I help you?")
    #
    # elif user_input.lower() == "show all":
    #     show_all()
    #
    # elif input_list[0].lower() == 'phone':
    #     phone(input_list[1])
    #
    # elif input_list[0].lower() == 'add':
    #     add(input_list[1], input_list[2])
    #
    # elif input_list[0].lower() == 'change':
    #     change(input_list[1], input_list[2], input_list[3])
    #
    # else:


if __name__ == "__main__":
    run_bot()




