import bcrypt

def hash(password:str):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

if __name__ == "__main__":
    hash()