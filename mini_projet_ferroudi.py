from sqlite3.dbapi2 import Cursor
from tkinter import *
import tkinter.messagebox as MessageBox

import sqlite3

root = Tk()
root.geometry("980x695")
root.title("Système de gestion des étudiants")
root.config(background="slateblue4")

conn = sqlite3.connect("mini_projet")
cursor = conn.cursor()

#Création de la table filiere

cursor.execute("""Create TABLE IF NOT EXISTS Filiere(
idFiliere INT(30) NOT NULL PRIMARY KEY ,
nomFiliere TEXT NOT NULL);""")



#Création de la table Etudiants

cursor.execute("""CREATE TABLE IF NOT EXISTS Etudiants(
idEtudiant INT(20) PRIMARY KEY,
nom  TEXT NOT NULL,
prenom TEXT NOT NULL,
idFiliere INT(30) NOT NULL,
Age INT(2) NOT NULL,
FOREIGN KEY (idFiliere)
REFERENCES Filiere (idFiliere)
ON DELETE NO ACTION
ON UPDATE NO ACTION);""")


def AjouterEtudiant():
    idEtudiant = e_idEtudiant.get()
    Nom = e_Nom.get()
    Prenom = e_Prenom.get()
    idFiliereFK = e_idFiliereFK.get()
    Age=e_Age.get()
    if (idEtudiant == "" or Nom == "" or Prenom == "" or idFiliereFK == "" or Age==""):
        MessageBox.showinfo("l'ajout d'un etudiant","Remplissez tous les champs")
    else:
        connection = sqlite3.connect(database="mini_projet")
        cursor = connection.cursor()
        cursor.execute("insert into Etudiants values('"+idEtudiant +"','"+Age+"','"+Nom+"','"+Prenom+"','"+idFiliereFK+"')")
        cursor.execute("commit")
        e_idEtudiant.delete(0, "end")
        e_Nom.delete(0, "end")
        e_Age.delete(0, "end")
        e_Prenom.delete(0, "end")
        e_idFiliereFK.delete(0, "end")
        AfficherEtudiant()
        MessageBox.showinfo("Le statut d'ajout", "Ajout réussi")
        connection.close()


def SupprimerEtudiant():
    if (e_idEtudiant.get() == ""):
        MessageBox.showinfo("Le statut de la suppression ","L'idEtudiant est essentiel")
    else:
        connection = sqlite3.connect(database="mini_projet")
        cursor = connection.cursor()
        cursor.execute("Delete from Etudiants where idEtudiant='"+e_idEtudiant.get()+"'")
        cursor.execute("commit")
        e_idEtudiant.delete(0, "end")
        e_Nom.delete(0, "end")
        e_Prenom.delete(0, "end")
        e_Age.delete(0, "end")
        e_idFiliereFK.delete(0, "end")
        AfficherEtudiant()
        MessageBox.showinfo("Le statut de la suppression", "Suppression réussie")
        connection.close()


def ModifierEtudiant():
    if (e_idEtudiant.get() == "" or e_Nom.get() == "" or e_Prenom.get() == "" or e_idFiliereFK.get() == "" or e_Age.get()==""):
        MessageBox.showinfo("Le statut de la modification ","Remplissez tous les champs")
    else:
        connection = sqlite3.connect(database="mini_projet")
        cursor = connection.cursor()
        cursor.execute("Update Etudiants set nom='"+e_Nom.get()+"',prenom='"+e_Prenom.get() + "',Age='" +e_Age.get() + "',idFiliereFK='"+e_idFiliereFK.get()+"' where idEtudiant='"+e_idEtudiant.get()+"'")
        cursor.execute("commit")
        e_idEtudiant.delete(0, "end")
        e_Nom.delete(0, "end")
        e_Age.delete(0, "end")
        e_Prenom.delete(0, "end")
        e_idFiliereFK.delete(0, "end")
        AfficherEtudiant()
        MessageBox.showinfo("Le statut de la modification","modification réussie")
        connection.close()


def AfficherEtudiant():
    connection = sqlite3.connect(database="mini_projet")
    cursor = connection.cursor()
    cursor.execute("Select * from etudiants")
    rows = cursor.fetchall()
    list0.delete(0, list0.size())
    for row in rows:
        insertData = str(row[0])+'-'+row[1]+' '+row[2]+'-'+str(row[3])
        list0.insert(list0.size()+1, insertData)
    connection.close()


def AjouterFiliere():
    idFiliere = e_idFiliere.get()
    nomFiliere = e_nomFiliere.get()
    if (idFiliere == "" or nomFiliere == ""):
        MessageBox.showinfo("Le statut de l'ajout","Remplissez tous les champs")
    else:
        connection = sqlite3.connect(database="mini_projet")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Filiere VALUES('"+idFiliere+"','" +nomFiliere+"')")
        cursor.execute("commit")
        e_idFiliere.delete(0, "end")
        e_nomFiliere.delete(0, "end")
        AfficherFiliere()
        MessageBox.showinfo("Le statut de l'ajout", "Ajout réussi")
        connection.close()


def ModifierFiliere():
    if (e_idFiliere.get() == "" or e_nomFiliere.get() == ""):
        MessageBox.showinfo("Le statut de la modification ","Remplissez tous les champs")
    else:
        connection = sqlite3.connect(database="mini_projet")
        cursor = connection.cursor()
        cursor.execute("Update Filiere set nomFiliere='" +e_nomFiliere.get()+"' where idFiliere='"+e_idFiliere.get()+"'")
        cursor.execute("commit")
        e_nomFiliere.delete(0, "end")
        e_idFiliere.delete(0, "end")
        AfficherFiliere()
        MessageBox.showinfo("Le statut de la modification","modification réussie")
        connection.close()


def SupprimerFiliere():
    if (e_idFiliere.get() == ""):
        MessageBox.showinfo("Le statut de la suppression ","L'idFiliere est essentiel")
    else:
        connection = sqlite3.connect(database="mini_projet")
        cursor = connection.cursor()
        cursor.execute("Delete from Filiere where idFiliere='" +e_idFiliere.get()+"'")
        cursor.execute("commit")
        e_nomFiliere.delete(0, "end")
        e_idFiliere.delete(0, "end")
        AfficherFiliere()
        MessageBox.showinfo("Le statut de la suppression","Suppression réussie")
        connection.close()


def AfficherFiliere():
    connection = sqlite3.connect(database="mini_projet")
    cursor = connection.cursor()
    cursor.execute("Select * from Filiere")
    rows = cursor.fetchall()
    list.delete(0, list.size())
    for row in rows:
        insertData = str(row[0])+'-'+row[1]
        list.insert(list.size() + 1, insertData)
    connection.close()


label_title = Label(root, text="Bienvenue sur l'application de gestion ", font=("Courrier", 20), bg="slateblue4", fg="white")
label_title.pack()
label_title = Label(root, text="ETUDIANTS", font=("Courrier", 20), bg="slateblue4", fg="white")
label_title.place(x=60, y=50)
idEtudiant = Label(root, text='idEtudiant', font=("bold", 10))
idEtudiant.place(x=20, y=100)
Nom = Label(root, text='Nom', font=("bold", 10))
Nom.place(x=20, y=140)
Prenom = Label(root, text='Prénom', font=("bold", 10))
Prenom.place(x=20, y=180)
Age = Label(root, text='Age', font=("bold", 10))
Age.place(x=20, y=220)
idFiliereFK = Label(root, text='idFilière', font=("bold", 10))
idFiliereFK.place(x=20, y=260)

Ajouter = Button(root, text="Ajouter", font=("italic", 14), bg='green', fg="white", command=AjouterEtudiant)
Ajouter.place(x=10, y=310)
Modifier = Button(root, text="Modifier", font=("italic", 14), bg='darkorange2',fg="white", command=ModifierEtudiant)
Modifier.place(x=95, y=310)
Supprimer = Button(root, text="Supprimer", font=("italic", 14), bg='red',fg="white", command=SupprimerEtudiant)
Supprimer.place(x=188, y=310)
list0 = Listbox(root, width=100, height=15)
list0.place(x=350, y=85)

e_idEtudiant = Entry()
e_idEtudiant.place(x=100, y=100)
e_Nom = Entry()
e_Nom.place(x=100, y=140)
e_Age = Entry()
e_Age.place(x=100, y=220)
e_Prenom = Entry()
e_Prenom.place(x=100, y=180)
e_idFiliereFK = Entry()
e_idFiliereFK.place(x=100, y=260)


label_title = Label(root, text="FILIERES", font=("bold", 20), bg="slateblue4", fg="white")
label_title.place(x=60, y=450)
idFiliere = Label(root, text='idFilière', font=("bold", 10))
idFiliere.place(x=20, y=500)
nomFiliere = Label(root, text='Nom de la filière', font=("bold", 10))
nomFiliere.place(x=20, y=540)

Ajouter = Button(root, text="Ajouter", font=("italic", 14), bg='green',fg="white", command=AjouterFiliere)
Ajouter.place(x=10, y=590)
Modifier = Button(root, text="Modifier", font=("italic", 14), bg='darkorange2',fg="white", command=ModifierFiliere)
Modifier.place(x=95, y=590)
Supprimer = Button(root, text="Supprimer", font=("italic", 14), bg='red',fg="white", command=SupprimerFiliere)
Supprimer.place(x=188, y=590)

e_idFiliere = Entry()
e_idFiliere.place(x=140, y=500)
e_nomFiliere = Entry()
e_nomFiliere.place(x=140, y=540)
list = Listbox(root, width=100, height=15)
list.place(x=350, y=400)


def quitter_logiciel():
    root.destroy()

close = Button(root , text="Fermer" ,font=("italic","14"), bg="slateblue4" , fg="white" , command=quitter_logiciel)
close.place(x=870 , y=650)

barremenu = Menu(root)
root.config(menu=barremenu)

fichier_menu = Menu(barremenu, tearoff=0)
barremenu.add_cascade(label="Menu", menu=fichier_menu)
fichier_menu.add_command(label="Afficher la liste des étudiants", command=AfficherEtudiant)
fichier_menu.add_command(label="Afficher la liste des filières ", command=AfficherFiliere)
fichier_menu.add_separator()
fichier_menu.add_command(label="Quitter ", command=quitter_logiciel)

conn.commit()
cursor.close()

root.mainloop()
