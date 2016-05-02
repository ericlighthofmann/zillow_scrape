import sys
from PyQt4 import QtGui, QtCore

width = 600
height = 400

class Window(QtGui.QMainWindow):

    def __init__(self):
        # initialize the window
        super(Window, self).__init__()
        self.setFixedSize(width, height)
        self.setWindowTitle("Zillow Scraper")
        self.setWindowIcon(QtGui.QIcon('Hofdata.png'))

        #allows quitting of the app
        quitAction = QtGui.QAction("Quit", self)
        quitAction.setShortcut("Ctrl+Q")
        quitAction.setStatusTip('Leave The App')
        quitAction.triggered.connect(self.close_application)

        # gives status message to use
        self.statusBar().showMessage('Please enter the zip code you wish to scrape.')

        #creates menu bar at the top
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(quitAction)

        #sets the apps style
        QtGui.qApp.setStyle('Plastique')

        self.home()

    def home(self):     
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn = QtGui.QPushButton("Download",self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)

        self.show()

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)
        
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Quit!',
                                            "Really quit?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
        
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
