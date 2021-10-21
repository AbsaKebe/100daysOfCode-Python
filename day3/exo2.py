chaine = "Mame, Aminata, Fallou, Zidane, Salimata"
print(chaine)
#Séparer par , méthode split
step1=chaine.split(', ')
#Trier par ordre alpha méthode sort ou sorted
sorted(chaine.split(', '))
#Regrouper les mots méthode join
chaine_en_ordre=' '.join(sorted(chaine.split(', ')))
print(chaine_en_ordre)
