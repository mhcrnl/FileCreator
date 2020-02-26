""" File Creator Python | lucas.boistard@esme.fr """ 

#~--------------------------------------------------------------
#~ Import goes here
#~--------------------------------------------------------------
import sys
import os
import shutil

#~--------------------------------------------------------------
#~ Variables Declarations
#~--------------------------------------------------------------
file_extensions = ['py','java','html']

#~--------------------------------------------------------------
#~ Class Declaration / View class
#~--------------------------------------------------------------
class Controller(object):

    #~----------------------------------------------------------
    #~ Init method
    #~----------------------------------------------------------
    def __init__(self, view):
    	self.view = view

   	#~----------------------------------------------------------
    #~ Create File
    #~----------------------------------------------------------
    def format_File(self,language,filename):
        extension = self.checkExtension(language.lower())
        self.formated_Filename = self.addExtension(filename, extension)
        print(self.formated_Filename)

        self.createFile(self.formated_Filename)

    #~----------------------------------------------------------
    #~ Check extension depends on the language selected
    #~----------------------------------------------------------
    def checkExtension(self,language):
        self.extension = ""
        if language == "python":
            self.extension = ".py"
        elif language == "java":
            self.extension = ".java"
        elif language == "html":
            self.extension = ".html"

        return self.extension

    #~----------------------------------------------------------
    #~ Add extension to the filename
    #~----------------------------------------------------------
    def addExtension(self,filename, extension):
        filename = filename + extension
        return filename

    #~----------------------------------------------------------
    #~ Add extension to the filename
    #~----------------------------------------------------------
    def createFile(self, formated_Filename):
        for extenion in file_extensions:
            if extenion == 'py':
                shutil.copy('Ressources/Python.txt', formated_Filename)











   
