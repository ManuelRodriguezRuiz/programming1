oldpassword = str(input("Geef het oude wachtwoord:"))
newpassword = str(input("Geef het nieuwe wachtwoord:"))

def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        return "true"
    else:
        return "false"

print(new_password(oldpassword, newpassword))