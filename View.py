""" File Creator Python | lucas.boistard@esme.fr """ 
#~--------------------------------------------------------------
#~ Import goes here
#~--------------------------------------------------------------
import sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QPushButton
from PyQt5.uic import loadUi
from PyQt5 import QtCore


from Controller import Controller

#~--------------------------------------------------------------
#~ Class Declaration / View class
#~--------------------------------------------------------------
class View(QMainWindow):

    #~----------------------------------------------------------
    #~ Init method
    #~----------------------------------------------------------
    def __init__(self):
    	super(View, self).__init__()   # Call the inherited classes __init__ method
    	loadUi('view.ui', self)	       #Load UI
    	self.show()	                   #Show the UI
    	self.control = None            #Controller
    	self.ui_initialization()
    	
    #~----------------------------------------------------------
    #~ Initialize components
    #~----------------------------------------------------------
    def ui_initialization(self):
        self.text_Preview.setEnabled(True)
        self.text_Preview.setReadOnly(True)
        self.fillPreview()
        
    #~----------------------------------------------------------
    #~ Define the controller
    #~----------------------------------------------------------
    def set_control(self, controller):
    	self.control = controller
    	self.slot_initialization()

    #~----------------------------------------------------------
    #~ Initialize each object of the GUI
    #~----------------------------------------------------------
    def slot_initialization(self):
    	self.button_cancel.clicked.connect(self.quit_Application)
    	self.button_createFile.clicked.connect(self.getData)

    #~----------------------------------------------------------
    #~ When clicking on "Cancel", quit the application
    #~----------------------------------------------------------
    def quit_Application(self):
    	QtCore.QCoreApplication.instance().quit()

    #~----------------------------------------------------------
    #~ Get Data from GUI depends on what user choose
    #~----------------------------------------------------------
    def getData(self):
        self.language = str(self.comboBox_language.currentText())
        self.filename = self.text_filename.toPlainText()
        self.control.format_File(self.language,self.filename)

    #~----------------------------------------------------------
    #~ Get Data from GUI depends on what user choose
    #~----------------------------------------------------------
    def fillPreview(self):
        
        language = self.comboBox_language.currentText()
        print(language)
        print(language.lower())
        if language.lower() == "python":
            pythonFile = open("Ressources/Python.txt" , "r")
            self.text_Preview.append(pythonFile.read())
        elif language.lower() == "java":
            print("helooe")
        elif language.lower() == "html":
            print("html Fill Preview")
            

    
  



