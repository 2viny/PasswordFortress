import random
import pickle
import hashlib

class userInfo:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.accounts = dict()

    def getAccounts (self):
        return self.accounts()

    def getUsername (self):
        return self.username

    def lookUser (self):
        print(f"user: {self.username} \npassword: {self.password}")

class usersTable:
    def __init__ (self) :
        self.tableSize = 100
        self.users = [[] for i in range(self.tableSize)]

    def getAllUsers(self):
        for i in range(self.tableSize):
            if len(self.users[i]) == 0:
                pass
            else:
                print(f"\nIndexKey: {i}")
                for j, registerUser in enumerate(self.users[i]):
                    print(f"{self.users[i][j].getUsername()}", end = "")
                    if j != (len(self.users[i])-1):
                        print(", ", end = "")

    def hashIndex (self, username):
        index = 0
        for char in username:
            index += ord(char)
        return index % self.tableSize
    
    def getUser (self, search):       
        i = self.hashIndex(search)
        for registeredUser in self.users[i]:
            if registeredUser.getUsername() == search:
                return registeredUser
    
    def setUser (self, user):
        username = user.getUsername()
        i = self.hashIndex(username)
        found = False
        for j, registerUser in enumerate(self.users[i]):
            if registerUser.getUsername() == username:
                self.users[i][j] = (user)
                found = True
                break
        if found == False:
            self.users[i].append((user))
    
    def deleteUser (self, user):
        username = user.getUsername()
        i = self.hashIndex(username)
        for j, registerUser in enumerate(self.users[i]):
            if registerUser.getUsername() == username:
                del self.users[i][j]
                break

users = usersTable()

try: 
    with open("SavedUsers.users", "rb") as file:
        for line in file.readlines():
            serializedUser = line.rstrip()
            user = pickle.loads(serializedUser)
            users.setUser(user)
except FileNotFoundError:
    pass

while True:
    action = input("\nQue ação deseja realizar?\
                   \n\"Registrar\": Registra um novo usuário.\
                   \n\"Entrar\": Entra com um usuário existente.\
                   \n\"Sair\": Fecha o programa.\n").lower()
    
    if action == "sair":
        quit()
    
    elif action == "registrar":
        username = input("Informe um usuário: ")
        existe = False
        for i in range(users.tableSize):
            for j, registerUser in enumerate(users.users[i]):
                if users.users[i][j].getUsername() == username:
                    print("Esse usuário existe!")
                    existe = True
                    break
            if existe == True:
                break

        if existe == False:
            password = hashlib.md5(input("Informe uma senha: ").encode()).hexdigest()
            user = userInfo(username, password)
            users.setUser(user)
            serializedUser = pickle.dumps(user) + b"\n"
            with open("SavedUsers.users", "ab") as file:
                file.write(serializedUser)
            print("usuário salvo!")
    
    elif action == "entrar":
        search = input("Informe seu usuário: ")
        user = users.getUser(search)
        if user == None:
            print("Usuário inexistente.")
        else:
            password = hashlib.md5(input("Informe sua senha: ").encode()).hexdigest()
            if password != user.password:
                print("Acesso negado.")
            else:
                while True:
                    action = input("\nQue ação deseja realizar?\
                                    \n\"Ler\": Ver suas contas.\
                                    \n\"Adicionar\": Adiciona uma nova conta.\
                                    \n\"Remover\": Remove uma conta existente.\
                                    \n\"Apagar\": Apaga seu usuário.\
                                    \n\"Sair\": Sai do seu usuário e renorna ao início.\n").lower()
                    
                    if action == "ler":
                        for plataform, plataformPassword in user.accounts.items():
                            print(f"{plataform}: {plataformPassword}")

                    if action == "adicionar":
                        plataform = input("Informe a plataforma: ")
                        plataformPassword = input("Informe a senha: ")
                        user.accounts[plataform] = plataformPassword

                    if action == "remover":
                        plataform = input("Informe a plataforma que deseja remover: ")
                        if plataform in user.accounts:
                            del user.accounts[plataform]
                        else:
                            print("Conta inexistente.")

                    if action == "apagar":
                        # apagar o user salvo no txt tbm
                        password = hashlib.md5(input("Informe sua senha para confirmar: ").encode()).hexdigest()
                        if password == user.password:
                            users.deleteUser(user)
                            print("Seu usuário foi deletado.")
                            break
                        else:
                            print("Senha incorreta.")

                    if action == "sair":
                        userLine = 0
                        with open("SavedUsers.users", "rb") as file:
                            for line in (editUser := file.readlines()):
                                serializedUser = line.rstrip()
                                lookingForUser = pickle.loads(serializedUser)
                                if lookingForUser.getUsername() == user.getUsername():
                                    serializedUser = pickle.dumps(user)
                                    break
                                userLine +=1
                        with open("SavedUsers.users", "wb") as file:
                            editUser[userLine] = serializedUser + b"\n"
                            file.writelines(editUser)
                        break
    
    elif action == "devtools":
        while True:
            action = input("\nEstá é uma ferramenta para testes, que função deseja realizar?\
                            \n\"Gerar\": Gera alguma quantidade de usuários aleatórios.\
                            \n\"Visualizar\": Vizualiza todos os usuários existentes.\
                            \n\"Sair\": Sai das ferramentas de testes e renorna ao início.\n").lower()

            if action == "sair":
                break

            if action == "gerar":
                lower_abc = "abcdefghijklmnopqrstuvwxyz"
                upper_ABC = lower_abc.upper()
                letters = lower_abc + upper_ABC
                generatedUsers = int(input("Quantos usuários aleatórios você deseja gerar? "))
                for i in range(generatedUsers):
                    username = "".join(random.sample(letters, random.randint(3, 8)))
                    user = userInfo(username, "randomUser")
                    users.setUser(user)
            
            if action == "visualizar":
                users.getAllUsers()