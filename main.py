""" File Creator Python | lucas.boistard@esme.fr """ 

#~--------------------------------------------------------------
#~ Import goes here
#~--------------------------------------------------------------
import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QSizeGrip
from PyQt5.QtCore import Qt

from View import View
from Controller import Controller

#~--------------------------------------------------------------
#~ Class Declaration / Main class
#~--------------------------------------------------------------
if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyle('Breeze')
	appView = View()
	controller = Controller(appView)
	appView.set_control(controller)
	sys.exit(app.exec_())