ss DataBase:
    __instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")

    def __new__(cls, *args, **kwargs):                                                                                          if cls.__instance is None:                                                                                                  cls.__instance = super().__new__(cls)                
        return cls.__instance

db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)
print(db is db2)
