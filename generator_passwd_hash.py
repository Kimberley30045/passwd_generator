import string
import secrets
import hashlib

# Definition des variables pour l'alphabet
letters = string.ascii_letters
numbers = string.digits
chars_spec = string.punctuation
alphabet = letters + numbers + chars_spec

# Demande à l'utilisateur la longueur du mot de passe
lenght_user = int(input("Saisissez la longueur du mot de passe : "))

# Génération du mot de passe 
generate_passwd = ''.join(secrets.choice(alphabet) for _ in range(lenght_user))
print("Votre mot de passe sécurisé est : " + generate_passwd)

# Hachage du mot de passe
hashed_passwd = hashlib.sha256(generate_passwd.encode()).hexdigest()

# Demander le nom du fichier à l'utilisateur 
file_name = input("Nous allons inscrire votre mot de passe dans un fichier .txt Donnez un nom à ce fichier " )

# Verif s'il ya le format txt sinon il ajoute. 
if not file_name.endswith('.txt'):
    file_name += '.txt'

# On ecrit le mot de passe sur le fichier
with open(file_name, 'w') as file:
    file.write(hashed_passwd)

print(f"Le mot de passe a été enregistré dans le fichier {file_name}.")
