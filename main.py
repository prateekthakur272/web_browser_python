from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QWidget

class WebBrowser():
    def __init__(self) -> None:
        
        self.window = QWidget()
        self.window.setWindowTitle('Web Browser')
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()
        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)
        
        self.go_button = QPushButton('Go')
        self.go_button.setMinimumHeight(30)
        
        self.back_button = QPushButton('<')
        self.back_button.setMinimumHeight(30)
        
        self.forward_button = QPushButton('>')
        self.forward_button.setMinimumHeight(30)
        
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_button)
        self.horizontal.addWidget(self.back_button)
        self.horizontal.addWidget(self.forward_button)
        
        self.bowser = QWebEngineView()
        
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.bowser)
        
        self.bowser.setUrl(QUrl('https://google.co.in'))
        self.go_button.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_button.clicked.connect(self.bowser.back)
        self.forward_button.clicked.connect(self.bowser.forward)
        
        self.window.setLayout(self.layout)
        self.window.show()
        
    def navigate(self, url):
        if not url.startswith('http'):
            url = 'http://' + url
        self.url_bar.setText(url)
        self.bowser.setUrl(QUrl(url))



app = QApplication([])
window = WebBrowser()
app.exec_()
       
                