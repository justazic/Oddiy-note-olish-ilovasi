import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit # type: ignore

class NoteApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Oddiy Note Olish Ilovasi")

        self.layout = QVBoxLayout()

        self.note_entry = QLineEdit(self)
        self.note_entry.setPlaceholderText("Yozmoqchi bo'lgan notangizni kiriting...")
        self.layout.addWidget(self.note_entry)

        self.save_button = QPushButton("Saqlash", self)
        self.save_button.clicked.connect(self.note_qoshish)
        self.layout.addWidget(self.save_button)

        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)
        self.layout.addWidget(self.text_area)

        self.setLayout(self.layout)

    def note_qoshish(self):
        note = self.note_entry.text()
        if note:
            self.text_area.append(note)
            self.note_entry.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NoteApp()
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec_())