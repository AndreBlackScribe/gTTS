import sys, os
from gtts import gTTS

from io import BytesIO
import pygame

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout  # <2>
from PyQt5.QtWidgets import QWidget  # <1>
from PyQt5.QtWidgets import (
	QMainWindow,
	QApplication,
	QLineEdit,
	QPushButton,
	)


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Widgets App")
		layout = QVBoxLayout()


		self.textbox = QLineEdit()
		self.textbox.setObjectName("textbox")
		self.textbox.setText("Salut. Numele meu este Mihai")

		button = QPushButton("Smash!")
		button.clicked.connect(self.button_click)

		layout.addWidget(self.textbox)
		layout.addWidget(button)

		widget = QWidget()

		widget.setLayout(layout)
		self.setCentralWidget(widget)

	def button_click(self):
		sayit(self.textbox.text())
        
def sayit(text):
	#text = "Salut. Numele meu este Mihai"
    with BytesIO() as f:
    	gTTS(text, lang='ro').write_to_fp(f)
    	f.seek(0)
    	pygame.mixer.init()
    	pygame.mixer.music.load(f)
    	pygame.mixer.music.play()
    	while pygame.mixer.music.get_busy():
    		continue


	#tts.save("hi.mp3")
	#os.system("hi.mp3")

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
