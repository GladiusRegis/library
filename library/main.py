import sqlite3

action = input('What do you want to do? [p]rint, [a]dd: ')
if action == 'p':
    with sqlite3.connect('library.db') as connection:
        cursor = connection.cursor()
        for book in cursor.execute('SELECT book_id, title, author FROM books'):
            # print(book)
            book_id, title, author = book
            print(f'ID: {book_id}, title: {title}, author: {author}')
elif action == 'a':
    with sqlite3.connect('library.db') as connection:
        cursor = connection.cursor()
        title = input('Title: ')
        author = input('Author: ')
        cursor.execute('INSERT INTO books(title, author) VALUES(?, ?)', (title, author))
        connection.commit()
else:
    print('Select [p] or [a]')
