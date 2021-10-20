prenom="Absa"
if type(prenom)==str:
    resultat="Première vérification réussie."
    print(resultat)
prenom=0
if isinstance(prenom,str):
    resultat="Deuxième vérification réussie."
    print(resultat)
else:
    print("Deuxième vérification échouée.")