from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QDialog, QVBoxLayout, QScrollArea, QHBoxLayout
from PySide6.QtGui import QPixmap
import requests 
import os
from PySide6.QtCore import Qt # type: ignore

class SearchWindow(QWidget):

    def button( self, x):
        x.setStyleSheet("""
            QPushButton {
                background-color: dark-grey;
                color: white;
                border: 1px solid #BA263E;
                font: bold 16px;
                text-align: center;
                border-radius: 10px;
            }
            QMainWindow {
                background-color: black;
            }
            QLabel {
                font-size: 32px;
            }
            QPushButton:hover {
                background-color: #BA263E;
                color: dark-grey;
            }
        """)
    
    def __init__(self):
        super().__init__()

        self.setFixedSize(850, 500)
        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(50, 50, 280, 40)
        self.textbox.setStyleSheet("background-color: #3d3d3d; border-radius: 10px; padding: 10px;")
        
       
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 850, 500)
        self.pixmap = QPixmap('../assets/landing.jpg')
        self.background_label.setPixmap(self.pixmap) 
        self.background_label.setScaledContents(True)
        self.background_label.lower() 


        

        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        self.button(enter_button)
        enter_button.clicked.connect(self.pokemon)

        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        self.button(capture_button)
        capture_button.clicked.connect(self.capture)
        

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        self.button(display_button)
        display_button.clicked.connect(self.open_new_window)
        
        

        self.result = QLabel(self)
        self.result.setGeometry(450, 120, 500, 500)
        self.result.setStyleSheet("color: white; font-size: 17px;")
        self.result.setWordWrap(True)

        self.image = QLabel(self)
        self.image.setGeometry(480, 25, 250, 250)


    def pokemon(self):
        name = self.textbox.text()
        
        self.background_label.hide()  
        self.setStyleSheet("background-color: #282828;")
        self.textbox.raise_() 
        
        url = f"https://pokeapi.co/api/v2/pokemon/{name}/"
        try:
            response = requests.get(url)
            response.raise_for_status() 
            data = response.json() 
            
            self.data = data


            pokename = data["species"]['name']
            pokeimage= data['sprites']['other']['official-artwork']['front_default']
            abilities = ", ".join(p['ability']['name'] for p in data['abilities'])
            types = ", ".join(t['type']['name'] for t in data['types'])
            k=[]
            for i in data['stats']:
                name = i["stat"]["name"].capitalize()
                stat = i["base_stat"]
                k.append(f"{name}: {stat}")
            stats = "\n     ".join(k)

            self.result.setText(
                f"Name: {pokename}\n"
                f"Abilities: {abilities}\n"
                f"Types: {types}\n"
                f"Stats:\n     {stats}"
            )

            
            pixmap = QPixmap() 
            pixmap.loadFromData(requests.get(pokeimage).content)
            self.image.setPixmap(pixmap)
            self.image.setScaledContents(True)
        
        except requests.exceptions.HTTPError as p:
            QMessageBox.critical(self, "Error", f"HTTP error occurred: {p}")

    def capture(self):
        
        if not os.path.exists("captured_images"):
            os.mkdir("captured_images")


        image_url = self.data['sprites']['other']['official-artwork']['front_default']
        save_as = f"captured_images/{self.data['species']['name']}.png"

        response = requests.get(image_url)
        with open(save_as, 'wb') as file:
            file.write(response.content)
        if os.path.exists(save_as):
            QMessageBox.information(self, "Success", "Image captured successfully")


    def open_new_window(self):
        self.new_window = Display()
        self.new_window.show()
        
class Display(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(380,500)

        self.imagelable = QLabel(self)
        self.imagelable.setGeometry(50, 50, 280, 350)

        self.name= QLabel(self)
        self.name.setGeometry(30, 20, 300, 40)
        self.name.setStyleSheet("color: white; font-size: 32px; font: bold 16px ;")

        next = QPushButton("Next", self)
        next.setGeometry(210, 440, 150, 43)
        self.button(next)
        next.clicked.connect(self.next)
        
        
        previous = QPushButton("Previous", self)
        previous.setGeometry(20, 440, 150, 43)
        self.button(previous)
        previous.clicked.connect(self.previous)


        
        self.images = os.listdir("captured_images")
        

        
        
        self.i=0
        self.printing()

    def printing(self):
        
        
        self.name.setText(self.images[self.i].capitalize().replace(".png", ""))
        pixmap = QPixmap(f"captured_images/{self.images[self.i]}")
        self.imagelable.setPixmap(pixmap)
        self.imagelable.setScaledContents(True)


    def next(self):
        
        if 0<=self.i<=len(self.images)-1:
            self.i+=1
            self.printing()
        elif self.i>len(self.images)-1:
            self.i=len(self.images)-self.i
            self.printing()


    def previous(self):
        
        if 0<=self.i<=len(self.images)-1:
            self.i-=1
            self.printing()
        elif self.i<0:
            self.i=len(self.images)-1
            self.printing()



        
        

    
    def button( self, x):
        x.setStyleSheet("""
            QPushButton {
                background-color: dark-grey;
                color: white;
                border: 1px solid #BA263E;
                font: bold 16px;
                text-align: center;
                border-radius: 10px;
            }
            QMainWindow {
                background-color: black;
            }
            QLabel {
                font-size: 32px;
            }
            QPushButton:hover {
                background-color: #BA263E;
                color: dark-grey;
            }
        """)





if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication # type: ignore

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
