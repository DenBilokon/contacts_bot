
PHONE_DICT = {}


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

    if len(new_phone) == 12:
        new_phone = "".join("+" + new_phone)
    else:
        new_phone = "".join("+38" + new_phone)
    return new_phone


# Додаємо новий номер телефону до списку

def add(name, phone_num):
    if name in PHONE_DICT:
        PHONE_DICT[name].append(sanitize_phone_number(phone_num))
    if name not in PHONE_DICT:
        PHONE_DICT[name] = []
        PHONE_DICT[name].append(sanitize_phone_number(phone_num))
    return PHONE_DICT


# Замінюємо старий номер телефону на новий

def change(name: str, old_num: str, new_num):
    if name in PHONE_DICT:
        PHONE_DICT[name].remove(sanitize_phone_number(old_num))
        PHONE_DICT[name].append(sanitize_phone_number(new_num))
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
    if user_input.strip() == 'hello':
        print("How can I help you?")

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




