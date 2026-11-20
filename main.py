import sys
from PyQt6 import uic
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('lab1.ui', self)
        self.setFixedSize(self.size())

        self.pushButton.clicked.connect(self.textOut)
        self.pushButton_2.clicked.connect(self.open_form2)
        self.pushButton_3.clicked.connect(self.close)
        self.radioButton.toggled.connect(self.update_style)
        self.radioButton_2.toggled.connect(self.update_style)
        self.radioButton_3.toggled.connect(self.update_style)
        self.radioButton_4.toggled.connect(self.update_style)
        self.radioButton_5.toggled.connect(self.update_style)
        self.checkBox.stateChanged.connect(self.update_style)
        self.checkBox_2.stateChanged.connect(self.update_style)
        self.checkBox_3.stateChanged.connect(self.update_style)
        self.checkBox_4.stateChanged.connect(self.update_style)

    def open_form2(self):
        self.form2 = Form2(self)
        self.form2.show()

    def textOut(self):
        text_from_field = self.textEdit.toPlainText().strip()
        self.listWidget.clear()
        self.listWidget.addItem(text_from_field)
        self.update_style()

    # метод, отвечающий за смену цветов и шрифтов
    def update_style(self):
        # кортеж кнопка-цвет
        colors = (
            (self.radioButton, QColor("red")),
            (self.radioButton_2, QColor("blue")),
            (self.radioButton_3, QColor("green")),
            (self.radioButton_4, QColor("yellow")),
            (self.radioButton_5, QColor("black")),
        )
        # перебор по кортежу выше
        for radio_button, color in colors:
            if radio_button.isChecked(): # если соотв. кнопка отмечена то ставится её цвет
                self.listWidget.setStyleSheet(f"color: {color.name()};")
                break

        font = QFont("Arial", 14)
        font.setBold(self.checkBox.isChecked()) # методы объекта QFont принимают bool аргумент
        font.setItalic(self.checkBox_2.isChecked()) # если соотв. кнопка отмечена, то ставится соотв. ей шрифт
        font.setUnderline(self.checkBox_3.isChecked())
        font.setStrikeOut(self.checkBox_4.isChecked())
        self.listWidget.setFont(font)


class Form2(QWidget):
    def __init__(self, parent_form):
        super().__init__()
        uic.loadUi('lab1_form2.ui', self)
        self.setFixedSize(self.size())
        self.parent_form = parent_form
        self.pushButton.clicked.connect(self.close_form)

    def close_form(self):
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
