
def encodage(msg, decal):
  sortie = ""
  for car in msg :
    code = ord(car)
    code = code + decal
    sortie += chr(code)
  return sortie


entree = input("Texte à encoder : ")
cle = input("Valeur de la clé : ")
print(encodage(entree, int(cle)))


def decodage(msg, decal):
  sortie = ""
  for car in msg :
    code = ord(car)
    code = code - decal
    sortie += chr(code)
  return sortie


entree = input("Texte à decoder : ")
cle = input("Valeur de la clé : ")
print(decodage(entree, int(cle)))
