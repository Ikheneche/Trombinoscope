import tkinter as tk
import Trombi as tb
import tromb as tr #importation du fichier tromb, 
#recuperation de la liste personnes
from PIL import Image, ImageTk
personnes=tr.recupere_liste()# la recupération de la liste des personnes
fenetre =tk.Tk()# creation de la fenetre 
fenetre.title("Trombinoscope") # titre
fenetre.geometry ("400x400")  # la taille de la fenetre
fenetre.configure(bg='#856ff8') # mettre une couleur
i=0 # initialiser la variable globale
def changer_droite():
    global i
    personne=personnes[i] # recuperer la ieme personne
    #constitution du chemin vers la photo
    chemin="Trombi\\" +personne[2] + ".jpg"
    img = Image.open(chemin) # ouverture de la photo qui se trouve ici
    newsize=(200,200) # redimensionner l'image
    img=img.resize(newsize)
    photo = ImageTk.PhotoImage(img) #affichage de la photo
    #modifier le contenu du label nom(prenom) avec le nom(prenom) de la ieme personne
    string_nom.set(personne[0]) #modifier le contenu du label
    string_prenom.set(personne[1])
    i=i+1 # incrementation
    print(len(personnes))
    # control sur la valeur de i
    if i==len(personnes):
        i=0
    #configure() change l'état d'un composant
    photo_affich.configure(image=photo)
    fenetre.mainloop()
def changer_gauche():
    global i
    personne=personnes[i] # personnes c'est toute la liste des personnes
    chemin="Trombi\\" +personne[2] + ".jpg"
    img = Image.open(chemin)
    newsize=(200,200)
    img=img.resize(newsize)
    photo = ImageTk.PhotoImage(img)
    #modifiction de string nom et prenom, set=modifier=affecter
    string_nom.set(personne[0])
    string_prenom.set(personne[1])
    i=i-1
    if i == -1 :
        i=len(personnes)-1
    #configure() change l'état d'un composant
    photo_affich.configure(image=photo)
    fenetre.mainloop()
#bouton_gauche.pack() #ajouter  le bouton
p = tk.PanedWindow(fenetre, orient=tk.HORIZONTAL)
bouton_droite=tk.Button(p,text="Droite",command=changer_droite) # créer un bouton
bouton_gauche=tk.Button(p,text="Gauche",command=changer_gauche) # créer un bouton
p.add(bouton_droite)
p.add(bouton_gauche)
#**********************************************************************************
img = Image.open("Trombi\Loic_Coroller.jpg") 
newsize=(200,200)
img=img.resize(newsize)   
photo = ImageTk.PhotoImage(img)
photo_affich = tk.Label(fenetre,image=photo)
#Variable de type chaine de charac qu on initiaise au vide
string_nom=tk.StringVar(value="") 
string_prenom=tk.StringVar(value="")
#creation de label dans la fentre, couleur bleu, le texte dedans=sting nom, et sa position
nom=tk.Label(fenetre,bg='#856ff8', textvariable=string_nom).place(x=100,y=250)
prenom=tk.Label(fenetre,bg='#856ff8', textvariable=string_prenom).place(x=200,y=250)
p.pack()
photo_affich.pack()
fenetre.mainloop()#ouverture de la fenetre
