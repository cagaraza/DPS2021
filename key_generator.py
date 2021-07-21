import pyotp

key = "cagaraza@gmail.comDPSCHALLENGE"
#   T0: 120,\
#   X: 0,\
#   algorithm: sha512,\
#   digits: 10,\
totp = pyotp.totp.TOTP(key, digits=10, digest='openssl_sha512', interval= 120)
totp.now()

