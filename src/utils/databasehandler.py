import sqlite3


def connect_database():
    """Connects to the database and checks if its tables exist
    
    Return:
    connection(sqlite3.Connection): SQLite3 connection to a database
    """
    connection = sqlite3.connect("src/UsersInfo.db")
    set_database(connection)

    return connection


def set_database(connection: sqlite3.Connection) -> None:
    """If the tables of the database dont exist, sets them up
    
    Parameters:
    connection(sqlite3.Connection): SQLite3 connection to a database
    """
    cursor = connection.cursor()
    cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table'")
    result = cursor.fetchone()

    if result[0] == 0:
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nickname VARCHAR NOT NULL,
                       username VARCHAR UNIQUE NOT NULL,
                       salt NOT NULL,
                       hashed_password VARCHAR NOT NULL)""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS accounts (
                       id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       plataform VARCHAR NOT NULL,
                       login VARCHAR NOT NULL,
                       password VARCHAR NOT NULL,
                       logo BLOB,
                       user_id INTEGER,
                       FOREIGN KEY (user_id) REFERENCES users(id))""")
        
        connection.commit()
    
    cursor.close()
    return


def register_new_user(nickname: str, username: str, salt: bytes, password: str, connection: sqlite3.Connection):
    """Registers a new user to the database
    
    Parameters:
    nickname(str): nickname of the user
    username(str): username of the user
    salt(bytes): salt used to hash the user password
    password(str): hashed password of the user
    connection(slite3.Connection):
    """
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (nickname, username, salt, hashed_password) VALUES (?, ?, ?, ?)", (nickname, username, salt, password))
    connection.commit()
    cursor.close()
    return


def user_exists(search: str, connection: sqlite3.Connection) -> tuple or False:
    """Checks if a user exists on the database based on its username
    
    Parameters:
    search(str): User to be searched for in the database
    connection(sqlite3.Connection): Database that will be searched

    Returns:
    False(bool): If the user doesnt exist
    result(tuple): A tuple with the user information
    """
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (search,))
    result = cursor.fetchone()

    cursor.close()

    if result == None:
        return False
    
    return result


def get_accounts(user_id: int, connection: sqlite3.Connection) -> tuple:
    """Gets all the accounts of a given user

    Parameters:
    UserId(int): Id of the user in the database
    connection(sqlite3.Connection): Database that will be searched

    returns:
    accounts(tuple): All the accounts from the user in a tuple
    """
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM accounts WHERE user_id = ?", (user_id,))
    accounts = cursor.fetchall()
    
    cursor.close()

    return accounts