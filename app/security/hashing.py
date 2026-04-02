import bcrypt


def hash_password(password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed
def verify_password(password,hashed_password):
    dehash = bcrypt.checkpw(password.encode(), hashed_password)
    return dehash