import sys
from PyQt4 import QtGui, uic, QtCore
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  
import selenium
from selenium import webdriver
import openpyxl
import time

linkList = []
maxList = []
URLList = []

#GUI definitions and processes
class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        #.QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        uic.loadUi('mywindow.ui', self)
        self.setWindowTitle("Zillow Scrape")
        self.setWindowIcon(QtGui.QIcon('Hofdata.png'))
        self.home()

    def home(self):
        quit_button = QtGui.QPushButton("Quit", self)
        quit_button.clicked.connect(self.close_application)
        quit_button.move(500,270)

        self.progress = self.progressBar
        self.pushButton.clicked.connect(self.inform_user)
                  
        QtGui.qApp.setStyle('Plastique')
        self.show()

    def close_application(self):
        print('Its closed')
        sys.exit()
        
    def collect_links(self, zipcode):
        #gather links from Zillow
            URL = 'http://www.zillow.com/homes/for_sale/' + str(zipcode) + '/1_p/'
            browser = webdriver.Firefox()
            browser.maximize_window()
            browser.get(URL)
            browser.implicitly_wait(20)
            #finds the number of pages of results
            final_page = browser.find_element_by_xpath("//ol[contains(@class, 'zsg-pagination')]")
            for child in final_page.find_elements_by_xpath(".//*"):
                maxList.append(child.text)
            maxList[:] = (value for value in maxList if value != 'NEXT')
            maxList[:] = (value for value in maxList if value != '...')
            res = list(map(int, maxList))
            res2 = list(set(res))
            last_page = max(res2)
            
            logOutput = self.textEdit
            self.textEdit.moveCursor(QtGui.QTextCursor.End)
            logOutput.insertPlainText('There are ' + str(last_page) + ' pages of results to scrape.\n')
            logOutput.insertPlainText ('Please allow for at least ' + str(last_page) + ' minutes for the script to complete.\n')

            for number in res2[1::]:
                URLList.append('http://www.zillow.com/homes/for_sale/' + str(zipcode) + '/' + str(number) + '_p/')
            for address in URLList:
                browser.get(address)
                browser.implicitly_wait(20)
                elem = browser.find_elements_by_class_name('hdp-link')
                for e in elem:
                    link = e.get_attribute('href')
                    if link not in linkList:
                        linkList.append(link)
            

    def inform_user(self):
        #gather zip code and log outputs
        self.pushButton.setEnabled(False)
        zipcode = self.plainTextEdit.toPlainText()
        self.plainTextEdit.setReadOnly(True)

        logOutput = self.textEdit
        self.textEdit.moveCursor(QtGui.QTextCursor.End)
        logOutput.insertPlainText('You entered a zip code of ' + zipcode + '\n')
        logOutput.insertPlainText('Opening Firefox and gathering links to all properties in your zip code...\n')

        #progress bar
        self.completed = 0
        while self.completed < 5:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

        self.collect_links(zipcode)
        
        logOutput.insertPlainText('We found ' + str(len(linkList)) + ' properties for ' + zipcode + '.')
        while self.completed < 10:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

            
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
