import sqlite3


def connect_database():
    """Connects to the database and checks if its tables exist
    
    Return:
    connection(sqlite3.Connection): SQLite3 connection to a database
    """
    connection = sqlite3.connect("assets/UsersInfo.db")
    set_database(connection)

    return connection


def set_database(connection: sqlite3.Connection) -> None:
    """If the tables of the database dont exist, sets them up
    
    Parameters:
    connection(sqlite3.Connection): SQLite3 connection to a database
    """
    cursor = connection.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nickname VARCHAR NOT NULL,
                      username VARCHAR UNIQUE NOT NULL,
                      salt NOT NULL,
                      hashed_password VARCHAR NOT NULL,
                      login_tries INTEGER NOT NULL,
                      last_try DATE,
                      timeout_until DATE)""")
    
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


def register_new_user(nickname: str, username: str, salt: bytes, password: str, login_tries: int, connection: sqlite3.Connection):
    """Registers a new user to the database
    
    Parameters:
    nickname(str): nickname of the user
    username(str): username of the user
    salt(bytes): salt used to hash the user password
    password(str): hashed password of the user
    connection(slite3.Connection):
    """
    cursor = connection.cursor()

    cursor.execute("INSERT INTO users (nickname, username, salt, hashed_password, login_tries) VALUES (?, ?, ?, ?, ?)", (nickname, username, salt, password, login_tries))
    connection.commit()

    cursor.close()

    return


def update_password(user_id: int, salt: bytes, password: bytes, connection: sqlite3.Connection):
    """Updates the salt and hashed password of a user"""
    cursor = connection.cursor()

    cursor.execute("UPDATE users SET salt = ?, hashed_password = ? WHERE id = ?", (salt, password, user_id))
    connection.commit()

    cursor.close()

    return


def delete_user(user_id: int, connection: sqlite3.Connection) -> None:
    """Deletes a user and all accounts linked to him"""
    cursor = connection.cursor()

    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    cursor.execute("DELETE FROM accounts WHERE user_id = ?", (user_id,))
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


def save_account(account: list, connection: sqlite3.Connection):
    """Saves a new encrypted user account to the database
    
    Parameters:
    Account(list): List with the information from the account
    connection(sqlite3.Connection): Connection to the database
    """
    cursor = connection.cursor()

    cursor.execute("INSERT INTO accounts (plataform, login, password, logo, user_id) VALUES (?, ?, ?, ?, ?)", (account))
    connection.commit()

    cursor.close()

    return


def update_logo(logo_bytes: bytes, account_id: int, connection: sqlite3.Connection):
    """Updates the logo of a account in the database
    
    Parameters:
    logo_bytes(bytes): The bytes blob of the image
    account_id(int): The id of the account in the database
    connection(sqlite3.Connection): Connection to the database
    """
    cursor = connection.cursor()

    cursor.execute("UPDATE accounts SET logo = ? WHERE id = ?", (logo_bytes, account_id))
    connection.commit()

    cursor.close()

    return


def update_account(account: list, connection: sqlite3.Connection) -> None:
    """Updates an account information
    
    Parameters:
    account(list): List with updated info of the account
    connection(sqlite3.Connection): Connection to the database
    """
    cursor = connection.cursor()

    cursor.execute("UPDATE accounts SET plataform = ?, login = ?, password = ? WHERE id = ?", (account))
    connection.commit()

    cursor.close()

    return


def update_account_info(account: list, connection: sqlite3.Connection) -> None:
    """Updates the login and password of a account"""
    cursor = connection.cursor()

    cursor.execute("UPDATE accounts SET login = ?, password = ? WHERE id = ?", (account))
    connection.commit()

    cursor.close()

    return


def delete_account(account_id: int, connection: sqlite3.Connection):
    """Deletes the account from the database
    
    Parameters:
    account_id(int): The id of the account in the database
    connection(sqlite3.Connection): Connection to the database
    """
    cursor = connection.cursor()

    cursor.execute("DELETE FROM accounts WHERE id = ?", (account_id,))
    connection.commit()

    cursor.close()

    return


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


def get_accounts_info(user_id: int, connection: sqlite3.Connection) -> tuple:
    """Gets only the id, login and password of a account"""
    cursor = connection.cursor()

    cursor.execute("SELECT id, login, password FROM accounts WHERE user_id = ?", (user_id,))
    accounts = cursor.fetchall()
    
    cursor.close()

    return accounts


def update_login_tries(user_id: int, login_tries: int, last_try, connection: sqlite3.Connection) -> None:
    cursor = connection.cursor()

    cursor.execute("UPDATE users SET login_tries = ?, last_try = ? WHERE id = ?", (login_tries, last_try, user_id))
    connection.commit()

    cursor.close()
    
    return


def timeout_user(user_id: int, timeout, connection: sqlite3.Connection) -> None:
    cursor = connection.cursor()

    cursor.execute("UPDATE users SET login_tries = ?, timeout_until = ? WHERE id = ?", (0, timeout, user_id))
    connection.commit()

    cursor.close()
    
    return


def remove_timeout(user_id: int, connection: sqlite3.Connection) -> None:
    cursor = connection.cursor()

    cursor.execute("UPDATE users SET timeout_until = ? WHERE id = ?", (None, user_id))
    connection.commit()

    cursor.close()
    
    return
