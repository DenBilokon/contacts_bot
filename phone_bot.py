
PHONE_DICT = {}


# Decorator - оброблює помилки введення і виводить відповідний результат
def input_error(func):
    def wrapper(*args):
        try:
            func(*args)

        except IndexError:
            return print("Give me name and phone")

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
@input_error
def add(name, phone_num: str):
    if name in PHONE_DICT:
        PHONE_DICT[name].append(sanitize_phone_number(phone_num))
    if name not in PHONE_DICT:
        PHONE_DICT[name] = []
        PHONE_DICT[name].append(sanitize_phone_number(phone_num))
    return PHONE_DICT


# Замінюємо старий номер телефону на новий
@input_error
def change(name: str, old_num: str, new_num):
    if name in PHONE_DICT:
        PHONE_DICT[name].remove(sanitize_phone_number(old_num))
        PHONE_DICT[name].append(sanitize_phone_number(new_num))
    return PHONE_DICT


# Виводимо номер телефону по імені
@input_error
def phone(name):
    return print(PHONE_DICT[name])


# Виводимо всі номери телефонів

def show_all():
    text = ""
    for name_user, phone_list in PHONE_DICT.items():
        phones = ""
        for i in phone_list:
            if i[-1] == i:
                phones += i
            else:
                phones += i + ", "
        text += ''.join(name_user + ": " + phones + '\n')

    return print(text)







