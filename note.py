from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("window")
        self.setFixedSize(383, 456)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.setWindowIcon(QtGui.QIcon(os.path.join(os.getcwd(), 'notes.ico')))
        #font
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.setFont(font)
        #centralwidget
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        #textEdit
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 383, 420))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setTabStopWidth(33)
        font.setPointSize(12)
        self.textEdit.setFont(font)
        #button to bold
        self.bold_button = QtWidgets.QPushButton(self.centralwidget)
        self.bold_button.setGeometry(QtCore.QRect(0, 420, 41, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bold_button.setFont(font)
        self.bold_button.setCheckable(True)
        self.bold_button.setObjectName("bold_button")
        self.bold_button.setToolTip('Bold')
        #button to italicize
        self.italic_button = QtWidgets.QPushButton(self.centralwidget)
        self.italic_button.setGeometry(QtCore.QRect(40, 420, 41, 31))
        font = QtGui.QFont()
        font.setItalic(True)
        self.italic_button.setFont(font)
        self.italic_button.setCheckable(True)
        self.italic_button.setObjectName("italic_button")
        self.italic_button.setToolTip('Italic')
        #underline button
        self.under_button = QtWidgets.QPushButton(self.centralwidget)
        self.under_button.setGeometry(QtCore.QRect(80, 420, 41, 31))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.under_button.setFont(font)
        self.under_button.setCheckable(True)
        self.under_button.setObjectName("under_button")
        self.under_button.setToolTip('Underline')
        #listbutton
        self.list_button = QtWidgets.QPushButton(self.centralwidget)
        self.list_button.setGeometry(QtCore.QRect(120, 420, 41, 31))
        self.list_button.setCheckable(True)
        self.list_button.setObjectName("list_button")
        self.list_button.setToolTip('Add list')
        #image button
        self.image_button = QtWidgets.QPushButton(self.centralwidget)
        self.image_button.setGeometry(QtCore.QRect(160, 420, 41, 31))
        self.image_button.setObjectName("image_button")
        self.image_button.setToolTip('Add image (Not implemented yet)')
        
        self.post_button = QtWidgets.QPushButton(self.centralwidget)
        self.post_button.setGeometry(QtCore.QRect(330, 420, 51, 31))
        self.post_button.setObjectName("post_button")
        self.setCentralWidget(self.centralwidget)

        self.bold_button.clicked.connect(self.bold)
        self.italic_button.clicked.connect(self.italic)
        self.under_button.clicked.connect(self.underline)
        self.list_button.clicked.connect(self.list)
        self.image_button.clicked.connect(self.add_image)
        self.post_button.clicked.connect(self.post)

        #styling the window
        with open('style.css', 'r') as file:
            self.setStyleSheet(file.read())

        self.initUI()
        QtCore.QMetaObject.connectSlotsByName(self)

    def initUI(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Post it note"))
        self.bold_button.setText(_translate("self", "B"))
        self.italic_button.setText(_translate("self", "I"))
        self.under_button.setText(_translate("self", "U"))
        self.list_button.setIcon(QtGui.QIcon('bullet.svg'))
        self.image_button.setIcon(QtGui.QIcon('img.svg'))
        self.post_button.setText(_translate("self", "Post"))

    def bold(self):
        if self.textEdit.fontWeight() > QtGui.QFont.Normal:
            self.textEdit.setFontWeight(QtGui.QFont.Normal)
        else:
            self.textEdit.setFontWeight(QtGui.QFont.Bold)
        self.textEdit.setFocus()

    def italic(self):
        self.textEdit.setFontItalic(not self.textEdit.fontItalic())
        self.textEdit.setFocus()

    def underline(self):
        self.textEdit.setFontUnderline(not self.textEdit.fontUnderline())
        self.textEdit.setFocus()

    def list(self):
        cursor = self.textEdit.textCursor()
        text_list = QtGui.QTextListFormat()
        text_list.setIndent(5)
        cursor.insertList(text_list.ListDisc)
        self.textEdit.setFocus()

    def add_image(self):
        pass
        # file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'F:\\', 'Image files (*.jpg, *.png, *.jpeg)')
        # pixmap = QtGui.QPixmap(file_name[0])
        # self.textEdit
        # self.textEdit.setFocus()

    def post(self):
        self.nd = Note()
        self.nd.show()

class Note(Window):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
