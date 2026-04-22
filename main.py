from config.settings import Assistant_name
from config.settings import version
print(f'système {Assistant_name}, version {version}')
print(f"initialisation du système en cours ...Prêt")

nom_du_user = input('quel est votre nom ?: ')
print(f'''Bonjour monsieur {nom_du_user}, comment
 allez-vous aujourd'hui?''')
print('Système en attente de commandes')

from skills import date_skill
date_skill.afficher_heure()
