import sys

from config.Add_project import Add_New_Project
from config.Project_SpreadSheet import SpreadSheet

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont

import sqlite3 as sql

conn = sql.connect("config\\Tasks.db")
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS Tasks(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    important INTEGER
)
''')

conn.commit()


class GestionProjet(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 180, 901, 550)
        self.setWindowIcon(QIcon('config\\task4.png'))
        self.setWindowTitle("Gestionnaire de projets")

        self.buttons_layout = QHBoxLayout()
        self.color_layout = QHBoxLayout()

        # self.setStyleSheet("background-color: #68c8c8")
        
        self.title = QLabel("Gestionnaire de projets", self)
        self.Labels()

        self.separator = QLabel("|\n|\n|\n|\n|\n|\n|\n|", self)
        self.separate()

        self.See = QPushButton("Voir les projets\n en cours", self)
        self.See_project_button()

        self.Add = QPushButton("Ajouter un projet", self)
        self.Add_project_button()

        # self.Remove = QPushButton("Terminer un projet\n(Enfin ...)", self)
        # self.Remove_project_button()


    def Labels(self):
        self.title.setGeometry(200, 0, 600, 100)
        self.title.setFont(QFont("Tw Cen MT",50))
        self.title.setStyleSheet("font-size: 50px;"
                                 "color: #688C7B;")

        # "background-color: red;"
        # "border-radius: 5px;"

    def separate(self):
        self.separator.setGeometry(445, 70, 30, 470)
        self.separator.setFont(QFont("Arial", 5))
        self.separator.setStyleSheet("font-size: 50px;")

    # def See_project_button(self):
    #     self.See.setGeometry(80, 180, 300, 90)
    #     self.See.setFont(QFont("Tw Cen MT", 5))
    #     self.See.setStyleSheet("font-size: 32px;"
    #                            "background-color: #688C7B;"
    #                            "font-weight: bold;")
    #     self.See.clicked.connect(self.See_project_button)

    def Add_project_button(self):
        self.Add.setGeometry(533, 260, 300, 90)
        self.Add.setFont(QFont("Tw Cen MT", 5))
        self.Add.setStyleSheet("font-size: 35px;"
                               "background-color: #688C7B;"
                               "font-weight: bold;")
        self.Add.clicked.connect(self.Add_projects)

    def See_project_button(self):
        self.See.setGeometry(80, 260, 300, 90)
        self.See.setFont(QFont("Tw Cen MT", 5))
        self.See.setStyleSheet("font-size: 35px;"
                               "background-color: #688C7B;"
                               "font-weight: bold;")
        self.See.clicked.connect(self.See_projects)

    # def Remove_project_button(self):
    #     self.Remove.setGeometry(300, 400, 300, 90)
    #     self.Remove.setFont(QFont("Tw Cen MT", 5))
    #     self.Remove.setStyleSheet("font-size: 30px;"
    #                               "background-color: #688C7B;"
    #                               "font-weight: bold;") 
    #     # self.Remove.

    def See_projects(self):
        self.New_win2 = SpreadSheet()
        self.New_win2.show()

    def Add_projects(self):
        self.New_win = Add_New_Project()
        self.New_win.show()

def main():
    app = QApplication(sys.argv)
    window = GestionProjet()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()