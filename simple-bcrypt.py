
def bhash(password):
  if len(password) > 72:
    raise Exception("Password above max length 72")
  try:
    import bcrypt
    hashed = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
    return hashed
  except:
    return None
 def verify(password,hashed):
  try:
    import bcrypt
    return bcrypt.checkpw(password.encode(),hashed)
  except:
    return None
  
 if __name__ == '__main__':
  passwd = input("Enter a password to test:")
  print(bhash(passwd))
 #END
