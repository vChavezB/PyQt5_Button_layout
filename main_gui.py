from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,\
							QVBoxLayout,\
							QLineEdit,\
							QPushButton
from PyQt5 import QtCore
from PyQt5.uic import loadUi
import sys 


class MyWidget(QWidget):
	def __init__(self,parent):
		super(MyWidget, self).__init__()
		self.start=QPushButton("Start",parent)
		self.pause=QPushButton("Pause",parent)
		self.end=QPushButton("End",parent)
		self.line=QLineEdit()
		
		self.start.pressed.connect(self.OnStart)
		self.pause.clicked.connect(self.OnPause)
		self.end.clicked.connect(self.OnEnd)
		
		self.layout=QVBoxLayout()
		self.layout.addWidget(self.start)
		self.layout.addWidget(self.pause)
		self.layout.addWidget(self.end)
		self.layout.addWidget(self.line)
		self.line.textChanged.connect(self.doSomething)

	def doSomething(self):
		print("do")

	def OnStart(self):
		print("start")
	def OnPause(self):
		print("pause")
	def OnEnd(self):
		print("end")

class TheWindow(QMainWindow):
	def __init__(self):
		super(TheWindow, self).__init__()
		self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
		loadUi('template.ui', self)		
		the_widget=MyWidget(self)
		self.horizontalLayout.addLayout(the_widget.layout)



QApplication.setAttribute(QtCore.Qt.AA_Use96Dpi)
app = QApplication([])
app.aboutToQuit.connect(app.deleteLater)
widget = TheWindow()
widget.show()
sys.exit(app.exec_())