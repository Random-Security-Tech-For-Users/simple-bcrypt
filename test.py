import simplebcrypt
hash1 = simplebcrypt.bhash("password")
testhash = simplebcrypt.bhash("password".encode())
if simplebcrypt.verify("password",hash1) != True:
  raise Exception("Verification error")
if simplebcrypt.verify("fakepassword",hash1) != False:
  raise Exception("Allowed another password to be accepted")
