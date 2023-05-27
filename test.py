with open('test.txt', 'r+', encoding='utf-8') as file:
    data = file.readlines()

print(data)

data[1] = 'New line! \n'

with open('test.txt', 'w', encoding='utf-8') as file:
    file.writelines(data)
