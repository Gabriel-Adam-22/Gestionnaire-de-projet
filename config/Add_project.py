import sys

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

import sqlite3 as sql

conn = sql.connect("config\\Tasks.db")
c = conn.cursor()

conn.commit()

class Add_New_Project(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 100, 400, 550)
        # self.setMaximumSize(400, 550)
        self.setWindowTitle("Ajouter un projet")
        self.setWindowIcon(QIcon("config\\task4.png"))


        self.title = QLabel("Nouveau Projet", self)

        self.label_name = QLabel("Nom du projet : ", self)

        self.entry_project_name = QLineEdit(self)

        self.label_description = QLabel("Description du projet : ", self)

        self.Describe_project = QTextEdit(self)

        self.Important_level = QSlider(Qt.Orientation.Horizontal, self)

        self.Important_level_label = QLabel("Importance du projet : 0/100", self)

        # self.Important_project_CheckBox = QCheckBox("Projet Urgent", self)

        self.Validation = QPushButton("Valider", self)

        self.initGui()

        
    def initGui(self):

        # Define Title
        self.title.setGeometry(32, 10, 600, 50)
        self.title.setFont(QFont("Tw Cen MT",50))
        self.title.setStyleSheet("color: #688C7B;"
                                 "font-size: 55px;")

        # Define the Label Name
        self.label_name.setGeometry(10, 100, 600, 50)
        self.label_name.setFont(QFont("Tw Cen MT", 50))
        self.label_name.setStyleSheet("font-size: 30px;"
                                      "font-weight: bold;"
                                      "color: #688C7B;")

        # Define the Entry project name
        self.entry_project_name.setGeometry(210, 112, 170, 30)
        self.entry_project_name.setFont(QFont("Tw Cen MT", 20))
        self.entry_project_name.setStyleSheet("color: #688C7B;"
                                              "font-weight: bold;")
        self.entry_project_name.setPlaceholderText("Nom ...")

        # Define the Label Description
        self.label_description.setGeometry(10, 200, 600, 50)
        self.label_description.setFont(QFont("Tw Cen MT", 50))
        self.label_description.setStyleSheet("font-size: 30px;"
                                             "font-weight: bold;"
                                             "color: #688C7B;")
        
        # Define the project description
        self.Describe_project.setGeometry(10, 250, 380, 200)
        self.Describe_project.setFont(QFont("Tw Cen MT", 20))
        self.Describe_project.setStyleSheet("color: #688C7B;"
                                            "font-weight: bold;")
        self.Describe_project.setPlaceholderText("Description ...")

        # # Define the slider
        self.Important_level.setGeometry(187, 463, 200, 20)
        self.Important_level.setMinimum(0)
        self.Important_level.setMaximum(100)
        self.Important_level.valueChanged.connect(self.update_Important_level_label)

        # Define the Important Label
        self.Important_level_label.setGeometry(10, 463, 168, 20)

        
        """
        ## Define the Important project Checkbox
        # self.Important_project_CheckBox.setGeometry(50, 463, 140, 20)
        # self.Important_project_CheckBox.setFont(QFont("Tw Cen MT", 13))
        # self.Important_project_CheckBox.setStyleSheet("color: #688C7B;"
                                            #  "font-weight: bold;")
        # self.Important_project_CheckBox.stateChanged.connect(self.Checkbox_changed)
        """       
       
        # Define the Validation Button
        self.Validation.setGeometry(int(280/2), 515, 120, 26)
        self.Validation.setFont(QFont("Tw Cen MT", 13))
        self.Validation.setStyleSheet("background-color: #688C7B;"
                                      "font-weight: bold;")
        self.Validation.clicked.connect(self.Verify_informations)
        
    def update_Important_level_label(self, value):
        self.Important_level_label.setText(f"Importance du projet : {value}/100")

    def Missing_Element(self):
        self.Error = QMessageBox()
        self.Error.setWindowIcon(QIcon("task4.png"))
        self.Error.setText("Error: Name or Description are missing")
        self.Error.setFont(QFont("Tw Cen MT", 5))
        self.Error.setStyleSheet("background-color: #688C7B;"
                                 "font-size: 25px;")
        self.Error.setWindowTitle("Missing Element")
        self.Error.show()

    def Verify_informations(self):
        project_name = self.entry_project_name.text()
        project_description = self.Describe_project.toPlainText()

        # if self.Important_project_CheckBox.isChecked():
        #     Important_project = 1
        # else:
        #     Important_project = 0 

        if project_name.strip(" ") == "" or project_description.strip(" ") == "":
            self.Validation.clicked.connect(self.Missing_Element)
        else:
            # print(self.Important_level_label.setText)
            c.execute("INSERT INTO Tasks (name, description, important) VALUES (?, ?, ?)", (project_name, project_description, self.Important_level.value()))
            conn.commit()
            self.entry_project_name.setText("")
            self.Describe_project.setText("")
            self.Important_level.setValue(0)

            # self.Important_project_CheckBox.setChecked(False)
            
            

        
def main():
    app = QApplication(sys.argv)
    window = Add_New_Project()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()