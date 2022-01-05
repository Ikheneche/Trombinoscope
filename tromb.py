import mysql.connector as msc # on a importé un connecteur
def recupere_liste ():#connetion a la base de données
        bdd = msc.connect(user='ISEN', password='ISEN',
                              host='127.0.0.1',port='8081',
                              database='trombinoscope')
        cursor = bdd.cursor()# on a crée un curseur
#qui = 1
#création de la requete
        query = "SELECT nom, prenom, photo FROM personnes;"
        cursor.execute(query)# exécution de la requete

        liste_personnes=[]
# création de liste à partir du résultat d'exéction de la requete
        for enregistrement in cursor :
            liste_personnes.append(enregistrement)
        cursor.close ()
        bdd.close()
        return liste_personnes

#print(liste_personnes)
    #  print(enregistrement[0])
    #  print(enregistrement[1])
    #  print(enregistrement[2])




