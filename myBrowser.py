# -pip install PyQt5
# -pip install PyQtWebEngine


#imports
from imp import reload
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


#Class def (duh)
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://youtube.com/si1az0'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

#navbar
        #navigation bar/ url search
        navigateBar1 = QToolBar()
        self.addToolBar(navigateBar1)

        backButton = QAction('Back', self)
        backButton.triggered.connect(self.browser.back)
        navigateBar1.addAction(backButton)

        forwardButton = QAction('Forward', self)
        forwardButton.triggered.connect(self.browser.forward)
        navigateBar1.addAction(forwardButton)

        reloadButton = QAction('Reload', self)
        reloadButton.triggered.connect(self.browser.reload)
        navigateBar1.addAction(reloadButton)

        homeButton = QAction('home', self)
        homeButton.triggered.connect(self.goHome)
        navigateBar1.addAction(homeButton)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigateURL)
        navigateBar1.addWidget(self.url_bar)
        
        self.browser.urlChanged.connect(self.updateURL)

#function defs being used on navbar
    def goHome(self):
        self.browser.setUrl(QUrl('https://github.com/si1az'))

    def navigateURL(self):
        preURL = 'https://'
        if preURL in self.url_bar.text():
            url = self.url_bar.text()
        else:
            url = preURL + self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def updateURL(self, q):
        self.url_bar.setText(q.toString())

#makes da ting run
app = QApplication(sys.argv)
QApplication.setApplicationName('Insecure Browser1')
window = MainWindow()
app.exec()

# subscribe to si1az on youtube