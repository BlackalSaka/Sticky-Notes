# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Sigsh\Documents\testPyQt5\HelloPyQt\myNote.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Note(object):
    def setupUi(self, Note):
        Note.setObjectName("Note")
        Note.resize(396, 400)
        Note.setStyleSheet("#frame_buttom{\n"
"    background-color: rgb(255, 247, 209);\n"
"}\n"
"QTextBrowser{\n"
"border:none;\n"
"font: 14pt \"MingLiU-ExtB\";\n"
"background-color: rgb(255, 247, 209);\n"
"}\n"
"#frame_title{\n"
"    background-color: rgb(255, 242, 171);\n"
"}\n"
"#frame{\n"
"    border: none;\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:hover, QPushButton:checked{\n"
"background: rgb(237, 230, 194);\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Note)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_outer = QtWidgets.QFrame(Note)
        self.frame_outer.setStyleSheet("")
        self.frame_outer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_outer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_outer.setObjectName("frame_outer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_outer)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_title = QtWidgets.QFrame(self.frame_outer)
        self.frame_title.setStyleSheet("")
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_add = QtWidgets.QPushButton(self.frame_title)
        self.pushButton_add.setMinimumSize(QtCore.QSize(38, 38))
        self.pushButton_add.setStyleSheet("")
        self.pushButton_add.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_add.setIcon(icon)
        self.pushButton_add.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_2.addWidget(self.pushButton_add, 0, QtCore.Qt.AlignLeft)
        self.frame = QtWidgets.QFrame(self.frame_title)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_menu = QtWidgets.QPushButton(self.frame)
        self.pushButton_menu.setMinimumSize(QtCore.QSize(38, 38))
        self.pushButton_menu.setStyleSheet("")
        self.pushButton_menu.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resources/more-horizontal.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_menu.setIcon(icon1)
        self.pushButton_menu.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.horizontalLayout.addWidget(self.pushButton_menu)
        self.pushButton_close = QtWidgets.QPushButton(self.frame)
        self.pushButton_close.setMinimumSize(QtCore.QSize(38, 38))
        self.pushButton_close.setStyleSheet("")
        self.pushButton_close.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/resources/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close.setIcon(icon2)
        self.pushButton_close.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.horizontalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.frame_title, 0, QtCore.Qt.AlignTop)
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_outer)
        font = QtGui.QFont()
        font.setFamily("MingLiU-ExtB")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.frame_buttom = QtWidgets.QFrame(self.frame_outer)
        self.frame_buttom.setMinimumSize(QtCore.QSize(0, 48))
        self.frame_buttom.setStyleSheet("\n"
"")
        self.frame_buttom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttom.setObjectName("frame_buttom")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_buttom)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(11)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_bold = QtWidgets.QPushButton(self.frame_buttom)
        self.pushButton_bold.setMinimumSize(QtCore.QSize(38, 38))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_bold.setFont(font)
        self.pushButton_bold.setStyleSheet("")
        self.pushButton_bold.setIconSize(QtCore.QSize(36, 36))
        self.pushButton_bold.setCheckable(True)
        self.pushButton_bold.setChecked(False)
        self.pushButton_bold.setObjectName("pushButton_bold")
        self.horizontalLayout_3.addWidget(self.pushButton_bold)
        self.pushButton_italic = QtWidgets.QPushButton(self.frame_buttom)
        self.pushButton_italic.setMinimumSize(QtCore.QSize(38, 38))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.pushButton_italic.setFont(font)
        self.pushButton_italic.setStyleSheet("")
        self.pushButton_italic.setIconSize(QtCore.QSize(36, 36))
        self.pushButton_italic.setCheckable(True)
        self.pushButton_italic.setObjectName("pushButton_italic")
        self.horizontalLayout_3.addWidget(self.pushButton_italic)
        self.pushButton_underscore = QtWidgets.QPushButton(self.frame_buttom)
        self.pushButton_underscore.setMinimumSize(QtCore.QSize(38, 38))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.pushButton_underscore.setFont(font)
        self.pushButton_underscore.setStyleSheet("")
        self.pushButton_underscore.setIconSize(QtCore.QSize(36, 36))
        self.pushButton_underscore.setCheckable(True)
        self.pushButton_underscore.setObjectName("pushButton_underscore")
        self.horizontalLayout_3.addWidget(self.pushButton_underscore)
        self.pushButton_strikethrough = QtWidgets.QPushButton(self.frame_buttom)
        self.pushButton_strikethrough.setMinimumSize(QtCore.QSize(38, 38))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(True)
        self.pushButton_strikethrough.setFont(font)
        self.pushButton_strikethrough.setStyleSheet("")
        self.pushButton_strikethrough.setIconSize(QtCore.QSize(36, 36))
        self.pushButton_strikethrough.setCheckable(True)
        self.pushButton_strikethrough.setObjectName("pushButton_strikethrough")
        self.horizontalLayout_3.addWidget(self.pushButton_strikethrough)
        self.pushButton_list = QtWidgets.QPushButton(self.frame_buttom)
        self.pushButton_list.setMinimumSize(QtCore.QSize(38, 38))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(True)
        self.pushButton_list.setFont(font)
        self.pushButton_list.setStyleSheet("")
        self.pushButton_list.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/resources/list.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_list.setIcon(icon3)
        self.pushButton_list.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_list.setCheckable(True)
        self.pushButton_list.setObjectName("pushButton_list")
        self.horizontalLayout_3.addWidget(self.pushButton_list)
        self.pushButton_picture = QtWidgets.QPushButton(self.frame_buttom)
        self.pushButton_picture.setMinimumSize(QtCore.QSize(38, 38))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(True)
        self.pushButton_picture.setFont(font)
        self.pushButton_picture.setStyleSheet("")
        self.pushButton_picture.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/resources/image.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_picture.setIcon(icon4)
        self.pushButton_picture.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_picture.setObjectName("pushButton_picture")
        self.horizontalLayout_3.addWidget(self.pushButton_picture)
        spacerItem = QtWidgets.QSpacerItem(76, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.frame_grip = QtWidgets.QFrame(self.frame_buttom)
        self.frame_grip.setMinimumSize(QtCore.QSize(10, 10))
        self.frame_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.horizontalLayout_3.addWidget(self.frame_grip, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.frame_buttom)
        self.verticalLayout.addWidget(self.frame_outer)

        self.retranslateUi(Note)
        QtCore.QMetaObject.connectSlotsByName(Note)

    def retranslateUi(self, Note):
        _translate = QtCore.QCoreApplication.translate
        Note.setWindowTitle(_translate("Note", "Form"))
        self.textBrowser.setHtml(_translate("Note", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MingLiU-ExtB\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser.setPlaceholderText(_translate("Note", "记笔记..."))
        self.pushButton_bold.setText(_translate("Note", "B"))
        self.pushButton_italic.setText(_translate("Note", "I"))
        self.pushButton_underscore.setText(_translate("Note", "U"))
        self.pushButton_strikethrough.setText(_translate("Note", "ab"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Note = QtWidgets.QWidget()
    ui = Ui_Note()
    ui.setupUi(Note)
    Note.show()
    sys.exit(app.exec_())
