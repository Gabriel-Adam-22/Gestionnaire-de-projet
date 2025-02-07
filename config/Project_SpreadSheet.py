import sys

from PyQt6.QtWidgets  import (QApplication, QMainWindow, 
                             QTableWidget, QTableWidgetItem,
                             QLabel, QPushButton)
from PyQt6.QtGui import QFont, QIcon

import sqlite3 as sql


class SpreadSheet(QMainWindow):

    def __init__(self):
        super().__init__()
        
        # Connexion a la db
        self.conn = sql.connect("config\\Tasks.db")
        self.c = self.conn.cursor()
        self.conn.commit()

        # Initialiser le classement des elements
        self.Classeur()

        # Parametres de la fenetre
        self.setWindowTitle("Voir les projets")
        self.setGeometry(200, 150, 800, 630)
        self.setWindowIcon(QIcon("config\\task4.png"))

        # Créer le tableur
        self.Tableur = QTableWidget(self)
        self.initTable()

        # Créer le bouton de supression
        self.Delete_button = QPushButton("Supprimer", self)

        # Label de description
        self.Title_Description = QLabel("Description : ... ", self)
        self.Important_Label = QLabel("| Importance : ...", self)
        self.Description_Label = QLabel("...", self)
        self.init_Labels_Buttons()

        # self.contact_button = QPushButton(self)
        # self.contact_button.setText("Contact buyer")
        # self.contact_button.setStyleSheet(" background-color: #181818; border: 1px solid black; "
        #                                 ":hover: { color: yellow };")

    def Classeur(self):
        self.c.execute("SELECT * FROM Tasks")
        self.elements = self.c.fetchall()

        self.input_Task_list = []
        self.output_Task_list = []

        for i in self.elements:
            self.input_Task_list.append(i)
        
        while not self.input_Task_list == []:
            
            self.important = self.important = ("","","",0)

            for i in self.input_Task_list:
                if int(i[3]) >= self.important[3]:
                    self.important = i
            
            self.output_Task_list.append(self.important)
            self.input_Task_list.remove(self.input_Task_list[self.input_Task_list.index(self.important)])

    

    def initTable(self):
        
        self.Tableur.setColumnCount(1)
        self.Tableur.setHorizontalHeaderLabels(["Nom du projet"])
        self.Tableur.setGeometry(0, 0, 800, 400)
        # self.Tableur.setRowCount(100)
        
        # self.c.execute("SELECT name, important FROM Tasks")
        # important = self.c.fetchall()

        # self.c.execute("SELECT name, important FROM Tasks")
        # names_important = self.c.fetchall()
        self.counter = 0



        for i in self.output_Task_list:
            self.counter +=1
        self.Tableur.setRowCount(self.counter)

        self.counter = -1        
        for i in self.output_Task_list:
            
            self.Tableur.setItem(self.counter,1, QTableWidgetItem(str(i[1])))
            self.counter+=1

        self.Tableur.setColumnWidth(0, 800)

        self.Tableur.cellClicked.connect(self.CurrentCell)

    def init_Labels_Buttons(self):

        # Title Description
        self.Title_Description.setGeometry(5, 410, 390, 30)
        self.Title_Description.setFont(QFont("Tw Cen MT", 5))
        self.Title_Description.setStyleSheet("font-size: 25px;"
                                             "color: #688C7B;")
        
        # Important Label Description
        self.Important_Label.setGeometry(395, 410, 400, 30)
        self.Important_Label.setFont(QFont("Tw Cen MT", 5))
        self.Important_Label.setStyleSheet("font-size: 25px;"
                                           "color: #688C7B;")

        # Content Description
        self.Description_Label.setGeometry(5, 450, 790, 140)
        self.Description_Label.setStyleSheet("font-size: 15px;"
                                             "color: #688C7B;")
        
        # Delete Element
        self.Delete_button.setGeometry(350, 596, 120, 30)
        self.Delete_button.setFont(QFont("Tw Cen MT"))
        self.Delete_button.setStyleSheet("""
                                        QPushButton {
                                            background-color: (0,0,0); 
                                            border: None;
                                            font-size: 25px;
                                            color: #688C7B;
                                            border-radius: 5px;

                                        }
                                        QPushButton:hover {
                                            color: #1e1e1e;
                                            background-color: #e3004f;
                                        }
                                    """)
        self.Delete_button.clicked.connect(self.DeleteCell)

    def DeleteCell(self):
        if self.Tableur.currentItem():
            self.name = self.Tableur.currentItem().text()
            self.c.execute("DELETE FROM Tasks WHERE name = ?", (self.name,))     
            self.conn.commit()
            self.Tableur.removeRow(self.Tableur.currentRow())
            self.Title_Description.setText("Description : ... ")
            self.Important_Label.setText("| Importance : ...")
            self.Description_Label.setText("...")

    def CurrentCell(self):
        self.name = self.Tableur.currentItem().text()
        
        self.c.execute("SELECT important FROM Tasks WHERE name = ?", (self.name,))
        Important_level = self.c.fetchone()
        self.c.execute("SELECT description FROM Tasks WHERE name = ?", (self.name,))
        description = self.c.fetchone()
            
        # print(Important_level, description)
        if Important_level == None or description == None:
            Important_level = ('0',)
            description = ("Unkown element",)

        self.Title_Description.setText(f"Description : {self.name}")
        self.Important_Label.setText(f"| Importance : {Important_level[0]}/100")
        self.Description_Label.setText(str(description[0]))
        # print(description)

def main():
    app = QApplication(sys.argv)
    window2 = SpreadSheet()
    window2.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()