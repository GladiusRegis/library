import sqlite3


def get_books(c):
    return c.execute('SELECT book_id, title, author FROM books')


def save_book(conn, t, a):
    c = conn.cursor()
    c.execute('INSERT INTO books(title, author) VALUES(?, ?)', (t, a))
    conn.commit()


action = input('What do you want to do? [p]rint, [a]dd: ')
if action == 'p':
    with sqlite3.connect('library.db') as connection:
        cursor = connection.cursor()
        for book in get_books(cursor):
            # print(book)
            book_id, title, author = book
            print(f'ID: {book_id}, title: {title}, author: {author}')
elif action == 'a':
    with sqlite3.connect('library.db') as connection:
        title = input('Title: ')
        author = input('Author: ')
        save_book(connection, title, author)

else:
    print('Select [p] or [a]')
