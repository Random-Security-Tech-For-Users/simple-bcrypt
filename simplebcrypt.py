def bhash(password):
    if type(password) == bytes:
        password = password.decode()
    if type(password) != str:
        raise Exception("Wrong password type: Expected string")
    if len(password) > 72:
        raise Exception("Password above max length of 72")
    try:
        import bcrypt
        hashed = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
        return hashed.decode()
    except:
        return None
def verify(password,hashed):
    if type(password) == bytes:
        password = password.decode()
    if type(hashed) == bytes:
        hashed = hashed.decode()
    if type(password) != str or type(hashed) != str:
        raise Exception("Wrong password type: Expected string")
    if len(password) > 72:
        raise Exception("Password is above max length of 72")
    try:
        import bcrypt
        return bcrypt.checkpw(password.encode(),hashed.encode())
    except:
        return None
  
if __name__ == '__main__':
    passwd = input("Enter a password to test:")
    print(bhash(passwd))
    print(verify(passwd,bhash(passwd)))
#END
