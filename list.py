books = list()
books = []

titles = ['Книга 1', 'Книга 2', 'Книга 3', 'Книга 4']

# Друк елемента за індексом
print(titles[1])

# Додати елемент в кінець списку
titles.append('Нова книга')

# Вставляє на i-те місце елемент зі значенням x
titles.insert(1, 'Книга 1.5')

# Видалення елементу зі списку
titles.remove(titles[0])

# Друк оновленого списку
print(titles)