
PHONE_DICT = {}

help_user = """This contact bot save your contacts 
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
            func(*args)

        except IndexError:
            return print("Give me name, old phone and new phone")

        except KeyError:
            return print("Enter correct user name")

        except ValueError:
            return print("Enter user name")

        else:
            return func

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


# Додаємо новий номер телефону до списку

def add(name, phone_num):
    if name in PHONE_DICT:
        PHONE_DICT[name].append(sanitize_phone_number(phone_num))
    if name not in PHONE_DICT:
        PHONE_DICT[name] = []
        PHONE_DICT[name].append(sanitize_phone_number(phone_num))
    print(f"Added new contact - {name} {sanitize_phone_number(phone_num)}")
    return PHONE_DICT


# Замінюємо старий номер телефону на новий

def change(name: str, old_num: str, new_num):
    if name in PHONE_DICT:
        PHONE_DICT[name].remove(sanitize_phone_number(old_num))
        PHONE_DICT[name].append(sanitize_phone_number(new_num))
    print(f"Changed contact {name} - number {sanitize_phone_number(old_num)} to number {sanitize_phone_number(new_num)}")
    return PHONE_DICT


# Виводимо номер телефону по імені

def phone(name):
    phones = ""
    for i in PHONE_DICT[name]:
        phones += i + " "
    return print(phones)


# Виводимо всі номери телефонів
def show_all():
    text = ""
    for name_user, phone_list in PHONE_DICT.items():
        phones = ""
        for i in phone_list:
            phones += i + " "
        text += ''.join(name_user + ": " + phones + '\n')

    return print(text)


# Функція спілкування з юзером і виконання функцій відповідно до команди
@input_error
def run_bot(user_input):

    input_list = user_input.split(" ")
    if user_input.strip().lower() == 'hello':
        print("How can I help you?")

    elif user_input.lower() == "show all":
        show_all()

    elif input_list[0].lower() == 'phone':
        phone(input_list[1])

    elif input_list[0].lower() == 'add':
        add(input_list[1], input_list[2])

    elif input_list[0].lower() == 'change':
        change(input_list[1], input_list[2], input_list[3])

    else:
        print("Incorrect input. Try again")




