FILENAMEPASSWD = "passwd.txt"
FILENAMEUSER = "user.txt"

listOfPasswd = ["123456",
                "12345",
                "123456789",
                "password",
                "admin",
                "1234567",
                "12345678",
                "abc123",
                "qwerty"
               ]
listOfUsers = ["adm", 
                "admin", 
                "administrator", 
                "anon", 
                "anonymous", 
                "bitnami",
                "guest",
                "root",
                "ROOT",
                "rooty",
                "rpc",
                "rpcuser",
                "system_admin",
                "www-data",
                "xpdb",
                "xpopr",
                "zabbix"
              ]

with open(FILENAMEPASSWD, "w", encoding="UTF-8") as file:
    for passwd in listOfPasswd:
        file.write(passwd + "\n")
        
with open(FILENAMEUSER, "w", encoding="UTF-8") as file:
    for user in listOfUsers:
        file.write(user + "\n")
