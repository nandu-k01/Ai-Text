import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import openai
import time

openai.api_key = "" # replace with your actual API key

class TextGenerationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Generation App")
        self.setGeometry(100, 100, 800, 600)

        # set up fonts
        self.title_font = QFont()
        self.title_font.setPointSize(24)
        self.subtitle_font = QFont()
        self.subtitle_font.setPointSize(16)

        # set up layout
        self.main_layout = QVBoxLayout()

        # create title label
        self.title_label = QLabel("Text Generation App")
        self.title_label.setFont(self.title_font)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.title_label)

        # create subtitle label
        self.subtitle_label = QLabel("Enter a question, topic or prompt:")
        self.subtitle_label.setFont(self.subtitle_font)
        self.subtitle_label.setAlignment(Qt.AlignLeft)
        self.main_layout.addWidget(self.subtitle_label)

        # create input box
        self.input_box = QLineEdit()
        self.input_box.setFont(self.subtitle_font)
        self.main_layout.addWidget(self.input_box)

        # create generate button
        self.generate_button = QPushButton("Generate")
        self.generate_button.setFont(self.subtitle_font)
        self.generate_button.clicked.connect(self.generate_text)
        self.main_layout.addWidget(self.generate_button)

        # create output box
        self.output_box = QTextEdit()
        self.output_box.setFont(self.subtitle_font)
        self.output_box.setReadOnly(True)
        self.main_layout.addWidget(self.output_box)

        self.setLayout(self.main_layout)

    def generate_text(self):
        prompt = self.input_box.text().strip()
        if prompt == "":
            self.output_box.setText("Please enter a valid prompt")
            return
        self.output_box.setText("Generating text...")
        response = self.call_openai_api(prompt)
        if "An error occurred" in response:
            self.output_box.setText(response)
        else:
            self.output_box.setText(response)

    def call_openai_api(self, prompt):
        try:
            response = openai.Completion.create(
              engine="text-davinci-003",
              prompt=prompt,
              max_tokens=1024,
              n=1,
              stop=None,
              temperature=0.7,
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"An error occurred: {e}"

def main():
    app = QApplication(sys.argv)
    text_generation_app = TextGenerationApp()
    text_generation_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
