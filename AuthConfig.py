# MONGO AUTHENTIFICATION

# Pour <<pymongo>>, plusieurs alternative dsont possible; voir la librairie : https://github.com/mongodb/mongo-python-driver

username = ''
password = ''
cluster = ''

def get_uri(usr,pwd,clst):
    '''
    - Cette fonction construit et renvoie une uri
    - Elle attend en paramètre le <username>, le <mot de passe> et,
      le chemin vers le <cluster> de la base de données
    '''
    return 'mongodb+srv://'+usr+':'+pwd+'@'+clst+'.mongodb.net/'
    
