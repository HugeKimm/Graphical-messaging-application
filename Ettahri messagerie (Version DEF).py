
import tkinter
from tkinter import *
from tkinter import messagebox
import paho.mqtt.client as mqtt
from tkinter.scrolledtext import ScrolledText
import datetime



"""client,userdata,result"""



client = mqtt.Client()


#Connexion au serveur MQTT
client=mqtt.Client()
client.on_connexion=client.connect
client.on_recevoir=client
#broker_address="192.168.1.10"
client.connect("broker.hivemq.com", 1883)
client.publish("SNIR2/Hakim","test")



#Pubblication d'un messsage
def publierMessage():

    if label_Message["text"]!="":
       message=Publication_Entry.get()
       client.publish("messageS",message,0,True)
       skt.insert(END, message+"\n")
       skt.insert('insert', f"Heure actuelle: {now}\n")
       Publication_Entry.delete(0,"end")
    else:
        messagebox.showinfo("INFORMATION","merci de saisir un message")




#souscription de topic
def souscription():
    topic=linEdit_1.get()
    print(topic)
    client.subscribe("SNIR2/"+topic)


#traitement d'un message avec la fonction Callback
def traiterMessage(client,userdata,message):
    print("In on_traiterMessage callback")
    loop_flag=0




#souscription et abonne à quelqu'un
def souscription():
    topic = Souscription_Entry.get()
    if topic:
        if topic not in label_Abonne["text"]:
            client.subscribe("SNIR2/" + topic, 0)
            #connectionTopicSave("Hakim", topic)
            if label_Abonne["text"] == "Aucun abonnement pour le moment.":
                label_Abonne["text"] = topic
            else:
                label_Abonne["text"] += ", " + topic
            Souscription_Entry.delete(0, "end")
        else:
            #Messagebox d'ivertissement, pour dire que il est deja abonné
            messagebox.showwarning("INFORMATION", message="Vous vous êtes déjà abonné(e)")
    else:
        #Messagebox d'ivertissement
        messagebox.showwarning("INFORMATION", message="Vous n'avez rien saisie dans le topic")




#Desuscription de nom topic
def desouscription():
    if label_Abonne["text"]!="":
        topic=label_Abonne["text"]
        if label_Abonne["text"]=="Aucun abonnement pour le moment.":
            messagebox.showinfo("INFORMATION","Vous n'avez souscrit à aucun topic")
        else:
            listeTopic=label_Abonne["text"].split(",")
            if (topic in listeTopic) == True:
                client.unsubscribe("SNIR2/"+topic,0)
                chaine =""
                indice=0
                while indice <(len(listeTopic)-1):
                    if listeTopic[indice]!=topic:
                        chaine+=listeTopic[indice]+","
                    indice+=1
                label_Abonne["text"]=chaine
            else:#sinon(le client Mqtt a deja souscrit à un topic)
                  messagebox.showinfo("INFORMATION","Vous n'etes pas abonné à ce topic")
    else:
        messagebox.shoinfo("INFORMATION","Merci de saisir un nom de topic")




#Création de fenetre
fen=tkinter.Tk()
fen.geometry("950x800")
fen.title("Application messagerie V2")

#Label pour le titre dans la fenetre
label_ApplicationMessage=tkinter.Label(fen,text="Application de messagerie V2 (protocole MQTT)", font=("times",25))
label_ApplicationMessage.pack()


#s'inscrire au Topic
#Frame Souscription
Souscription=tkinter.Frame(fen,width=900,height=100,bg="lightblue")
Souscription.place(x=20,y=50)

#Label Souscription à pour un topic
label_Souscription=tkinter.Label(Souscription,text="Souscription à un topic:",bg="lightblue",fg="blue")
label_Souscription.place(x=1,y=1)

#Label_1 pour saisir le nom du topic
label_1=tkinter.Label(Souscription,text="Saisir le nom du topic:",bg="lightblue",)
label_1.place(x=130,y=40)

#Label pour l' Abonnement(s)
label_2=tkinter.Label(Souscription,text="Abonnement(s) en cours au(x) topic(s):",bg="lightblue",)
label_2.place(x=3,y=70)

#Label pour mettre en affichage les Abonnement(s)
label_Abonne=tkinter.Label(Souscription,text="Aucun abonnement pour le moment.",bg="lightblue",fg="red")
label_Abonne.place(x=310,y=70)


#Zone de saisie Souscription Topic
Souscription_Entry = tkinter.Entry(Souscription)
Souscription_Entry.place (x=310,y=45, width=250,height=20)

#Bouton pour s'inscrire ou pour s'abonner
Souscription_Bouton=tkinter.Button(Souscription, text="S'abonner", bg="lightgreen",command=souscription)
Souscription_Bouton.place(x=570,y=40, width=155,height=30)

#Bouton pour desinscrire de topic
desouscription_Bouton=tkinter.Button(Souscription, text="Se désabonner", bg="lightgreen",command=desouscription)
desouscription_Bouton.place(x=730,y=40, width=150,height=30)



#Zones de publication
Publication=tkinter.Frame(fen,width=900,height=100,bg="orange")
Publication.place(x=20,y=160)

#Label pour publier dans le topic
label_Publication=tkinter.Label(Publication,text='Publication dans mon topic " Hakim ":',bg="orange",fg="blue",)
label_Publication.place(x=1,y=1)

#Bouton pour publier dans message
Publication_Bouton=tkinter.Button(Publication, text="Publier un message :", bg="lightgreen",command=publierMessage)
Publication_Bouton.place(x=130,y=50, width=180,height=30)

#Zone de saisie Publication Message
Publication_Entry = tkinter.Entry(Publication)
Publication_Entry.place (x=350,y=55, width=350,height=20)



#zone de message
Message=tkinter.Frame(fen,width=900,height=50,bg="lightgreen")
Message.place(x=20,y=270)

#Label pour  reçevoir des messages
label_3=tkinter.Label(Message,text="Message reçu:",bg="lightgreen",fg="blue")
label_3.place(x=1,y=1)

#Label pour Affiché les messages
label_Message=tkinter.Label(Message,text="Aucun message à afficher...",bg="lightgreen",fg="red",)
label_Message.place(x=170,y=5)



#Création de ScrolledText
SKForm=tkinter.Label(Message,text="Messagerie",bg="lightgreen",fg="red",)
SKForm=tkinter.Frame(fen,width=900,height=50,)
SKForm.place(x=70,y=400)
#SKForm = Tk()


skt = ScrolledText(SKForm)
skt.config(width = 100, height = 10)


def  publierMessage():
    # Récupérer le contenu du LineEdit
    messageS = Publication_Entry.get()
    # Insérer le contenu dans le ScrolledText
    skt.insert(tkinter.END, messageS + "\n")


# Obtenir l'heure actuelle
now = datetime.datetime.now()
# Insérer l'heure dans le widget ScrolledText
skt.insert('insert', f"Heure actuelle: {now}\n")

#Fin de fenetre pour ScrolledText
skt.pack()

#fermeture de fenetre et d'application
fen.mainloop()
