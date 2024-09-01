import string
import secrets

# Definition des variables c'est l'alphabet
letters = string.ascii_letters
numbers = string.digits
chars_spec = string.punctuation
alphabet = letters + numbers + chars_spec

# Demande à l'utilisateur la longueur du mot de passe
lenght_user = int(input("Saisissez la longueur du mot de passe : "))

# Génération du mot de passe 
generate_passwd = ''.join(secrets.choice(alphabet) for _ in range(lenght_user))
print("Votre mot de passe sécurisé est : " + generate_passwd)