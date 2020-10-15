# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from V1 import *

# import  camera

student_info = []


class Error(Exception):
    """Base class for other exceptions"""
    pass


class IncompleteInfo(Error):
    pass


class Ui_MainWindow(object):

    def reset_btn_clicked(self):
        student_info.clear()
        self.takePhoto_btn.show()
        self.upload_btn.show()
        self.firstName_Text.clear()
        self.lastName_Text.clear()
        self.studentID_Text.clear()

    def takePhoto_btn_clicked(self):
        alert = QMessageBox()
        #alert.setWindowTitle("Error occurs")
        # alert.setIcon()
        alert.setText("Smile!")
        alert.exec_()
        self.takePhoto_btn.hide()

    def upload_photo_button_clicked(self):
        student_info.clear()
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        student_info.append(path)
        alert = QMessageBox()
        alert.setText("Photo uploaded successfully.")
        alert.exec_()
        # self.upload_confirm()

    def create_button_clicked(self):
        try:
            student_info.append(self.firstName_Text.text())
            student_info.append(self.lastName_Text.text())
            student_info.append(self.studentID_Text.text())

            if (self.comboBox_course.currentText() == "ENG_4OIB6"):
                student_info.append("101")
            elif (self.comboBox_course.currentText() == "COMPENG_4TL4"):
                student_info.append("102")

            for i in range(len(student_info)):
                if(student_info[i]=="" or len(student_info)!=5):
                    raise IncompleteInfo;

            self.takePhoto_btn.show()
            alert = QMessageBox()
            alert.setText("Account created successfully.\nYou can check on student_info.txt")
            alert.exec_()
            self.firstName_Text.clear()
            self.lastName_Text.clear()
            self.studentID_Text.clear()
            self.generate_txt()
        except:
            alert = QMessageBox()
            alert.setText("Information Missing! Please check personal information and re-upload photo.")
            alert.exec_()
            self.reset_btn_clicked()

    def generate_txt(self):
        alert = QMessageBox()
        alert.setText("See list in the txt file.")
        alert.exec_()
        with open("student_info.txt", 'w') as filehandler:
            for listitem in student_info:
                filehandler.write('%s\n' % listitem)

    def switchToPro(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setup(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(879, 766)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # -------------------------------------------------
        # label_2 is the instruction picture on the left of the login page
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(350, 650))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("image/loginLeft.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)

        # ------------------------------------------------------------
        # self.logo is the Profmate logo
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMaximumSize(QtCore.QSize(480, 111))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("image/loginProfmate.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.logo.setObjectName("logo")
        self.verticalLayout_2.addWidget(self.logo)
        spacerItem2 = QtWidgets.QSpacerItem(15, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(38, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        # takePhoto_btn initialization is here
        self.takePhoto_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.takePhoto_btn.sizePolicy().hasHeightForWidth())
        self.takePhoto_btn.setSizePolicy(sizePolicy)
        self.takePhoto_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.takePhoto_btn.setIcon(icon)
        self.takePhoto_btn.setIconSize(QtCore.QSize(65, 75))
        self.takePhoto_btn.setObjectName("takePhoto_btn")
        self.horizontalLayout.addWidget(self.takePhoto_btn)

        # upload_btn initialization is here
        self.upload_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upload_btn.sizePolicy().hasHeightForWidth())
        self.upload_btn.setSizePolicy(sizePolicy)
        self.upload_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/photo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upload_btn.setIcon(icon1)
        self.upload_btn.setIconSize(QtCore.QSize(75, 75))
        self.upload_btn.setObjectName("upload_btn")
        self.horizontalLayout.addWidget(self.upload_btn)

        # reset_btn initialization is here
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_btn.sizePolicy().hasHeightForWidth())
        self.reset_btn.setSizePolicy(sizePolicy)
        self.reset_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/reset.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_btn.setIcon(icon2)
        self.reset_btn.setIconSize(QtCore.QSize(80, 80))
        self.reset_btn.setObjectName("reset_btn")
        self.horizontalLayout.addWidget(self.reset_btn)

        # toProfessor_btn initialization is here
        self.toProfessor_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toProfessor_btn.sizePolicy().hasHeightForWidth())
        self.toProfessor_btn.setSizePolicy(sizePolicy)
        self.toProfessor_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/professor.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toProfessor_btn.setIcon(icon3)
        self.toProfessor_btn.setIconSize(QtCore.QSize(70, 70))
        self.toProfessor_btn.setObjectName("toProfessor_btn")
        self.horizontalLayout.addWidget(self.toProfessor_btn)
        spacerItem4 = QtWidgets.QSpacerItem(38, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(17, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # informations initialization is here
        self.firstName_Label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstName_Label.sizePolicy().hasHeightForWidth())
        self.firstName_Label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.firstName_Label.setFont(font)
        self.firstName_Label.setObjectName("firstName_Label")
        self.verticalLayout.addWidget(self.firstName_Label)
        self.lastName_Label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastName_Label.sizePolicy().hasHeightForWidth())
        self.lastName_Label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.lastName_Label.setFont(font)
        self.lastName_Label.setObjectName("lastName_Label")
        self.verticalLayout.addWidget(self.lastName_Label)
        self.studentID_Label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentID_Label.sizePolicy().hasHeightForWidth())
        self.studentID_Label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.studentID_Label.setFont(font)
        self.studentID_Label.setObjectName("studentID_Label")
        self.verticalLayout.addWidget(self.studentID_Label)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.firstName_Text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstName_Text.sizePolicy().hasHeightForWidth())
        self.firstName_Text.setSizePolicy(sizePolicy)
        self.firstName_Text.setText("")
        self.firstName_Text.setObjectName("firstName_Text")
        self.verticalLayout_3.addWidget(self.firstName_Text)
        self.lastName_Text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastName_Text.sizePolicy().hasHeightForWidth())
        self.lastName_Text.setSizePolicy(sizePolicy)
        self.lastName_Text.setObjectName("lastName_Text")
        self.verticalLayout_3.addWidget(self.lastName_Text)
        self.studentID_Text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentID_Text.sizePolicy().hasHeightForWidth())
        self.studentID_Text.setSizePolicy(sizePolicy)
        self.studentID_Text.setObjectName("studentID_Text")
        self.verticalLayout_3.addWidget(self.studentID_Text)
        self.comboBox_course = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.comboBox_course.sizePolicy().hasHeightForWidth())
        self.comboBox_course.setSizePolicy(sizePolicy)
        self.comboBox_course.setObjectName("comboBox_course")
        self.comboBox_course.addItem("")
        self.comboBox_course.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_course)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem8 = QtWidgets.QSpacerItem(17, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(156, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.create_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_btn.sizePolicy().hasHeightForWidth())
        self.create_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.create_btn.setFont(font)
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout_5.addWidget(self.create_btn)
        spacerItem10 = QtWidgets.QSpacerItem(125, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem11 = QtWidgets.QSpacerItem(17, 11, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem11)

        # dogs picture initialization is here
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(476, 110))
        self.label_3.setStyleSheet("")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("image/dogs.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 2, 2)
        spacerItem12 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 1, 3, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 2, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum,
                                             QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem14, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 879, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student_login"))
        self.firstName_Label.setText(_translate("MainWindow", "First Name"))
        self.lastName_Label.setText(_translate("MainWindow", "Last Name "))
        self.studentID_Label.setText(_translate("MainWindow", "Student ID"))
        self.label.setText(_translate("MainWindow", "Course code"))
        self.create_btn.setText(_translate("MainWindow", "Create"))
        self.reset_btn.clicked.connect(self.reset_btn_clicked)
        self.takePhoto_btn.clicked.connect(self.takePhoto_btn_clicked)
        self.upload_btn.clicked.connect(self.upload_photo_button_clicked)
        self.toProfessor_btn.clicked.connect(self.switchToPro)
        self.comboBox_course.setItemText(0, _translate("MainWindow", "ENG_4OIB6"))
        self.comboBox_course.setItemText(1, _translate("MainWindow", "COMPENG_4TL4"))
        self.create_btn.clicked.connect(self.create_button_clicked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
