# MONGO Fonctions
from pymongo.errors import ConnectionFailure
from bson.objectid import ObjectId
from EngineeringMethods import *
import pymongo as pm
import pandas as pd

def check_connexion(f,uri):
    '''
    Cette méthode vérifie que la connexion s'est bien effectué,
    elle ping le serveur et, renvoi le cleint.
    '''
    cli = pm.MongoClient(f''+uri)
    try:
        cli.admin.command('ping')
    except ConnectionFailure:
        return lever_exception(f)
    print('connexion réussie !')
    return cli

def create_database(Obj, db_name):
    '''
    Cette méthode crée une <base de données>
    '''
    return Obj[db_name]


def check_exist_db(CLI, db_name):
    '''
    Cette fonction vérifie l'existence d'une base de données
    '''
    dbs = CLI.list_database_names()
    if db_name in dbs:
        print(db_name+" exist !")
    else :
        print(db_name+" does not exist !")
    print("\nla liste des bd existantes est ::: ",dbs)


def create_posts_collection(db, collection_name):
    '''
    Cette méthode crée une collection et la renvoie    
    '''
    return db[collection_name]


def insert_post(posts, txt, reviews, medias, img_size):
    '''
    Cette méthode insert un document dans la collection <posts>,
    de la base de données <insta_post_db>,
    elle renvoie la clée ou l'id de chaque post afin de les conserver (facultatif)
    '''
    un_post = {'text': txt, 'commentaires': reviews, 'medias':medias, 'img_size':img_size}
    inserer_post = posts.insert_one(un_post)
    primary_key = inserer_post.inserted_id
    return primary_key # c'est un objet de type bson ajouté par défaut car non spécifié.


def get_datas(collection, post_id=None):
    '''
    Cette méthode renvoie un ou plusieurs document.
    '''
    docs = []
    if(post_id!=None):
        if (len(post_id)==1):
            # renvoi un document
            p_id = ObjectId(""+str(post_id))
            document = collection.find_one({'_id': p_id})
            return document
        elif :
            # renvoi un vecteur de document
            for doc in post_id:
                p_id = ObjectId(""+str(post_id))
                docs.append(collection.find_one({'_id': p_id}))
                return docs
        else :
            # renvoi l'ensemble des documents en dataframe
            documents = collection.find_all() 
    else :
        documents = {} # car None
    return pd.DataFrame(documents)
    
    
    
