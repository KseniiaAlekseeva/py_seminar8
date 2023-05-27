def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input("Enter FIO: ")
    phone_num = input("Enter phone number: ")

    with open('book.txt', 'a', encoding='utf-8') as book:
        book.write(f"\n{fio} | {phone_num}")


def find_data() -> int:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()

    find_info = input('Enter what do you want to find: ')
    data = data.split('\n')
    result = search(data, find_info)
    print(result)

    while len(result) > 1:
        find_info = input('Enter what do you want to find: ')
        result = search(result, find_info)
        print(result)

    return [i for i in range(len(data)) if data[i] == result[0]][0]


def search(book: str, info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    # return [contact for contact in book if info.lower() in contact.lower()]
    return list(filter(lambda contact: info.lower() in contact.lower(), book))


def edit_data(delet: bool) -> None:
    find_index = find_data()

    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()

    if not delet:
        fio = input("Enter new FIO: ")
        phone_num = input("Enter new phone number: ")
        data[find_index] = fio+" | "+phone_num+"\n"
    else:
        data.pop(find_index)
        data[len(data)-1] = data[len(data)-1][:len(data[len(data)-1])-1]

    with open('book.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)
