import __init__
from PyQt5.QtWidgets import QApplication
 
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWindow = __init__.Ui_Minaco()
    #mainWindow = __init__.MainDantA()
    mainWindow.show()
    sys.exit(app.exec_())
