email = input("Email : ")

username = email[0 : email.index("@")]
domain = email[email.index("@") : -1]

print(f"username : {username}")
print(f"domain : {domain}")
