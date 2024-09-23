import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton # type: ignore

class MyForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ma'lumot Formasi")

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Ism:"))
        self.ism_entry = QLineEdit()
        layout.addWidget(self.ism_entry)

        layout.addWidget(QLabel("Elektron Pochta:"))
        self.email_entry = QLineEdit()
        layout.addWidget(self.email_entry)

        layout.addWidget(QLabel("Qisqacha Tarjimai Hol:"))
        self.tajimai_hol_text = QTextEdit()
        layout.addWidget(self.tajimai_hol_text)

        self.submit_button = QPushButton("Yuborish")
        self.submit_button.clicked.connect(self.submit_form)
        layout.addWidget(self.submit_button)

        layout.addWidget(QLabel("Olingan Ma'lumotlar:"))
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        self.setLayout(layout)

    def submit_form(self):
        ism = self.ism_entry.text()
        elektron_pochta = self.email_entry.text()
        tarjimai_hol = self.tajimai_hol_text.toPlainText()

        self.output_text.clear()
        self.output_text.append(f"Ism: {ism}\n")
        self.output_text.append(f"Elektron Pochta: {elektron_pochta}\n")
        self.output_text.append(f"Tarjimai Hol:\n{tarjimai_hol}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())