
def bhash(password):
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
 #END
