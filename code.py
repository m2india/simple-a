import sys
from PyQt4 import QtCore, QtGui
from cond import Ui_Dialog

class NaMe(QtGui.QDialog):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_Dialog()
    self.ui.setupUi(self)
    
    self.ui.pushButton.clicked.connect(self.ma)
    
    
  
	  
	  
  def ma(self):
	 
	 a = raw_input( ' ')
	 
	 print "hello", a	  
	  
	  
	  
	  
	  
   
if __name__ == '__main__':
  app = QtGui.QApplication(sys.argv)
  main = NaMe()
  main.show()
  sys.exit(app.exec_())   
    
