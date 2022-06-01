from email import message
from tkinter import Y
from funciones import *
import datetime


class UserAccount():
    def __init__(self,alias,email,tweets,followers,timeline,):
        if str(alias): #Comprobamos si el alias es una string
            self.alias = alias
        if es_correo_valido(email) == True: #Comprobamos si el correo es válido
            self.email = email
        if tweets == list: #Los tweets serán una lista donde cada elemento será un tweet
            self.tweets = tweets
        if followers == list: #Los followers serán una lista donde cada elemento es uno de los seguidores
            self.followers = followers
        if timeline == list: #El timeline será una lista donde cada elemento será un tweet que alguien habrá publicado con el momento de publicación
            self.timeline = timeline
        self.tweets = []
        self.followers = []
        self.timeline = []
user1 = UserAccount("pepe","pepe@gmail.com", [], [], [])
user2 = UserAccount("llucia","llucia@gmail.com", [], [], [])

def follow(user2):
    user2.followers.append(user1.alias) #Añadimos el alias del user1 a la lista de followers de user2
def tweet_user1(tweet1):
    user1.tweets.append(tweet1) #Añadimos el tweet a la lista de tweets de user1
    if user2.alias in user1.followers: #Si user2 sigue a user1 el tweet se añadirá al timeline junto con la fecha de publicación
        user2.timeline.append(datetime.now() + tweet1)
def tweet_user2(tweet1):
    user2.tweets.append(tweet1) #Añadimos el tweet a la lista de tweets de user1
    if user1.alias in user2.followers: #Si user2 sigue a user1 el tweet se añadirá al timeline junto con la fecha de publicación
        user1.timeline.append(datetime.now() + tweet1)



class Tweet:
    def __init__
    
    
    
    
    
    #Hacemos globales las variables que usaremos en otras clases
    global sender
    global tweet1_time
    global tweet1
    entrada = input("¿Quién va a escribir el mensaje, user1 o user2?") #Preguntamos quien va a escribir el mensaje
    if entrada == user1:
        sender = user1.alias
    elif entrada == user2:
        sender = user2.alias
    message = input("Introduzca el mensaje que quiere publicar o enviar.") #Hacemos que escriba el mensaje
    if len(message) > 140: # Comprobamos que el mensaje es inferior a 140 carácteres
        print("El texto es demasiado largo")
    else:
        tweet1_time = datetime.now() #Guardamos el momento del mensaje
        pass
    
    class Retweet():
        if sender == user1.alias:
            anw = input("¿user2 quieres hacer retweet, si o no?")
            if anw == "si":
                retweet_time = datetime.now()
                user2.tweets.append(message) #Añadimos el tweet a la lista de tweets de user2
                if user1.alias in user2.followers: #Si user1 sigue a user2 el tweet se añadirá al timeline junto con la fecha de publicación del tweet original más la fecha del retweet
                    user1.timeline.append(tweet1_time + message + retweet_time)
        elif sender == user2.alias:
            anw = input("¿user1 quieres hacer retweet, si o no?")
            if anw == "si":
                retweet_time = datetime.now()
                user1.tweets.append(message) #Añadimos el tweet a la lista de tweets de user1
                if user2.alias in user1.followers: #Si user2 sigue a user1 el tweet se añadirá al timeline junto con la fecha de publicación del tweet original más la fecha del retweet
                    user2.timeline.append(tweet1_time + message + retweet_time)

    class DirectMessage():



               



            
