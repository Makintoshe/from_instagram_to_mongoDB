from selenium import webdriver
from bs4 import BeautifulSoup
from numpy import asarray
from PIL import Image
from bs4 import BeautifulSoup
from selenium import webdriver
from pymongo.errors import ConnectionFailure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import numpy as np
import blosc

def lever_exception(f):
    '''
    Cette fonction lève des exceptions
    '''
    raise Exception('Erreur au niveau de ::: ',f)

    
def io_image_bin(img):
    '''
    l'objectif de cette méthode est de compresser sous forme de bloc, l'image dans un tableau numpy d'octet. 
    Ceci n'est qu'une alternative technique à la façon conventionnelle de sauvegarder une image 
    sous un format binaire dans une base de données. Il faudrait just eprévoir un moyen de resize la taille 
    de l'image en sauvegardant par exemple ses dimensions, ce pendant le contenu de l'image reste intact.
    '''
    image_array = asarray(img) # Conversion de l'image en tableau numpy
    compressed_bytes = blosc.pack_array(image_array) # Compression
    return compressed_bytes
    
    
    
def get_io_img(compressed_bytes):
    '''
    Cette fonction permet de reconvertir l'image au moment de sa récupération.
    '''
    decompressed_array = blosc.unpack_array(compressed_bytes)
    image_dec = Image.fromarray(decompressed_array)
    image_dec.save("image_dec.png", qualité = 95)
    return image_dec

def connexion(browser, votre_username_insta, votre_passsword_insta):
    
    # connection au compte
    username = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    username.clear()
    username.send_keys(votre_username_insta)
    password.clear()
    password.send_keys(votre_passsword_insta)

    #bouton de connexion automatique
    button = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    return browser

def instagram_scrapping():
    # Ouverture du navigateur

    # linux : chromedriver
    # windows : chromedriver.exe#target username
    # # mac : chromedriver_mac
    #fic = os.path.join("browser/", "chromedriver")
    browser = webdriver.Chrome("browser/chromedriver")

    #Ouverture d'instagram
    browser.get("http://www.instagram.com")

    # accepter les coockies
    button = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/button[2]"))).click()

    browser = connexion(browser)

    return browser

def get_datas_by_scrapp(browser, url):
    
    # on se rassure d'être connecté!
    browser = connexion(browser)

    # ouverture d'une page spécifique
    browser.get(url)

    # récupération de l'image du post
    images = browser.find_elements_by_tag_name('img')
    images = [image.get_attribute('src') for image in images]
    images = images[:-2]
    photo_p = images[0] # à modifier, à 1 vous récupérer la photo d'un post

    # récupération de l'image du post
    txts = browser.find_elements_by_tag_name('span')
    texts = [txt.text for txt in txts]
    texts = texts[:-2]
    post_txt = texts[13] # à modifier
    reviews = texts[15:]
    r = []
    for i in range(0,len(reviews),4):
        r.append(reviews[i])

    return photo, post_txt, r

