user_name="manivardhan"
user_password="secret_123"

def login(name,password):
    if user_name==name and user_password==password:
           print("login successful")
    else:
          print("invalid credentials")
