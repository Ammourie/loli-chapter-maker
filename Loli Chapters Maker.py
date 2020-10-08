from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QBoxLayout ,QLabel,QSlider,QStyle,QSizePolicy,QHBoxLayout,QVBoxLayout,QFileDialog,QLineEdit
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon   ,QPalette
from PyQt5.QtCore import Qt,QUrl
import sys
import time
import os
import  mimetypes
mimetypes.init()
def get_extensions_for_type(general_type):
    for ext in mimetypes.types_map:
        if mimetypes.types_map[ext].split('/')[0] == general_type:
            yield ext
def vidtypes():
    VIDEO = tuple(get_extensions_for_type('video'))
    tmp=""
    for i in VIDEO:
        tmp+="*"+str(i)+" "
    return tmp
def fix(n,flen):
    x=str(n)
    y=x
    if(x.find('.')!=-1):
        x=x[:x.find('.')]
    m=flen-len(x)
    r=""
    for i in range(0,m):
        r=r+"0"
    return r+y
def fix2(n,flen):
    x=str(n)
    y=x
    if(x.find('.')!=-1):
        x=x[:x.find('.')]
    m=flen-len(x)
    r=""
    for i in range(0,m):
        r=r+" "
    return y+r
def trans(millis):
    
    millis = int(millis)
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=int(millis/(1000*60*60))%24
    m=millis-(seconds*1000+minutes*60*1000+hours*60*60*1000)

    return fix(hours,2)+":"+ fix(minutes,2)+":"+ fix(seconds,2)+"."+fix(m,3)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1135, 837)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ch.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setMinimumSize(QtCore.QSize(1135, 837))
        MainWindow.setMaximumSize(QtCore.QSize(1135, 837))
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("MainWindow{background-color:rgb(255, 255, 255);    }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("centlarwidget{background:rgb(255, 255, 255);    }")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 10, 1091, 801))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(50, 50))
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 1061, 741))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 340, 151, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 30, 95, 20))
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 50, 95, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.frame_1_create = QtWidgets.QFrame(self.tab_3)
        self.frame_1_create.setGeometry(QtCore.QRect(230, 30, 201, 31))
        self.frame_1_create.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_1_create.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1_create.setObjectName("frame_1_create")
        self.Hour_Begin_create = QtWidgets.QLineEdit(self.frame_1_create)
        self.Hour_Begin_create.setGeometry(QtCore.QRect(10, 10, 31, 16))
        self.Hour_Begin_create.setFrame(False)
        self.Hour_Begin_create.setObjectName("Hour_Begin_create")
        self.Minute_Begin_create = QtWidgets.QLineEdit(self.frame_1_create)
        self.Minute_Begin_create.setGeometry(QtCore.QRect(60, 10, 31, 16))
        self.Minute_Begin_create.setFrame(False)
        self.Minute_Begin_create.setObjectName("Minute_Begin_create")
        self.Second_begin_create = QtWidgets.QLineEdit(self.frame_1_create)
        self.Second_begin_create.setGeometry(QtCore.QRect(110, 10, 31, 16))
        self.Second_begin_create.setFrame(False)
        self.Second_begin_create.setObjectName("Second_begin_create")
        self.Mellisecond_Begin_create = QtWidgets.QLineEdit(self.frame_1_create)
        self.Mellisecond_Begin_create.setGeometry(QtCore.QRect(160, 10, 31, 16))
        self.Mellisecond_Begin_create.setFrame(False)
        self.Mellisecond_Begin_create.setObjectName("Mellisecond_Begin_create")
        self.label = QtWidgets.QLabel(self.frame_1_create)
        self.label.setGeometry(QtCore.QRect(40, 10, 16, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_1_create)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 16, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_1_create)
        self.label_3.setGeometry(QtCore.QRect(140, 10, 16, 16))
        self.label_3.setObjectName("label_3")
        self.Finish_button_Create = QtWidgets.QPushButton(self.tab_3)
        self.Finish_button_Create.setGeometry(QtCore.QRect(320, 390, 93, 28))
        self.Finish_button_Create.setObjectName("Finish_button_Create")
        self.chapter_name_create = QtWidgets.QLineEdit(self.tab_3)
        self.chapter_name_create.setGeometry(QtCore.QRect(230, 120, 171, 31))
        self.chapter_name_create.setObjectName("chapter_name_create")
        self.listWidget_create = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_create.setGeometry(QtCore.QRect(60, 430, 581, 221))
        self.listWidget_create.setObjectName("listWidget_create")
        self.browse_lineedit_create = QtWidgets.QLineEdit(self.tab_3)
        self.browse_lineedit_create.setGeometry(QtCore.QRect(230, 210, 371, 31))
        self.browse_lineedit_create.setObjectName("browse_lineedit_create")
        self.Browse_button_create = QtWidgets.QPushButton(self.tab_3)
        self.Browse_button_create.setGeometry(QtCore.QRect(90, 210, 101, 31))
        self.Browse_button_create.setWhatsThis("")
        self.Browse_button_create.setObjectName("Browse_button_create")
        self.label_49 = QtWidgets.QLabel(self.tab_3)
        self.label_49.setGeometry(QtCore.QRect(750, 80, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Mikadan")
        font.setPointSize(16)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.Append_button = QtWidgets.QPushButton(self.tab_3)
        self.Append_button.setGeometry(QtCore.QRect(320, 340, 93, 28))
        self.Append_button.setObjectName("Append_button")
        self.label_48 = QtWidgets.QLabel(self.tab_3)
        self.label_48.setGeometry(QtCore.QRect(540, 210, 681, 481))
        self.label_48.setAutoFillBackground(False)
        self.label_48.setText("")
        self.label_48.setPixmap(QtGui.QPixmap("./photo.png"))
        self.label_48.setScaledContents(True)
        self.label_48.setObjectName("label_48")
        self.groupBox_2.raise_()
        self.frame_1_create.raise_()
        self.Finish_button_Create.raise_()
        self.chapter_name_create.raise_()
        self.Browse_button_create.raise_()
        self.label_49.raise_()
        self.Append_button.raise_()
        self.label_48.raise_()
        self.listWidget_create.raise_()
        self.browse_lineedit_create.raise_()
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_47 = QtWidgets.QLabel(self.tab_4)
        self.label_47.setGeometry(QtCore.QRect(540, 210, 681, 481))
        self.label_47.setAutoFillBackground(False)
        self.label_47.setText("")
        self.label_47.setPixmap(QtGui.QPixmap("./photo.png"))
        self.label_47.setScaledContents(True)
        self.label_47.setObjectName("label_47")
        self.label_51 = QtWidgets.QLabel(self.tab_4)
        self.label_51.setGeometry(QtCore.QRect(750, 80, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Mikadan")
        font.setPointSize(16)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.frame = QtWidgets.QFrame(self.tab_4)
        self.frame.setGeometry(QtCore.QRect(60, 20, 581, 301))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.listWidget_create_Vid = QtWidgets.QListWidget(self.tab_4)
        self.listWidget_create_Vid.setGeometry(QtCore.QRect(60, 430, 581, 221))
        self.listWidget_create_Vid.setObjectName("listWidget_create_Vid")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_3.setGeometry(QtCore.QRect(60, 340, 151, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 30, 95, 20))
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 50, 95, 20))
        self.radioButton_6.setObjectName("radioButton_6")
        self.Append_button_vid = QtWidgets.QPushButton(self.tab_4)
        self.Append_button_vid.setGeometry(QtCore.QRect(390, 390, 93, 28))
        self.Append_button_vid.setObjectName("Append_button_vid")
        self.Finish_button_Create_vid = QtWidgets.QPushButton(self.tab_4)
        self.Finish_button_Create_vid.setGeometry(QtCore.QRect(250, 390, 93, 28))
        self.Finish_button_Create_vid.setObjectName("Finish_button_Create_vid")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.browse_Button_modify = QtWidgets.QPushButton(self.tab_2)
        self.browse_Button_modify.setGeometry(QtCore.QRect(102, 245, 101, 31))
        self.browse_Button_modify.setObjectName("browse_Button_modify")
        self.browse_lineedit_modify = QtWidgets.QLineEdit(self.tab_2)
        self.browse_lineedit_modify.setGeometry(QtCore.QRect(242, 245, 371, 31))
        self.browse_lineedit_modify.setObjectName("browse_lineedit_modify")
        self.frame_1_Modify = QtWidgets.QFrame(self.tab_2)
        self.frame_1_Modify.setGeometry(QtCore.QRect(242, 65, 201, 31))
        self.frame_1_Modify.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_1_Modify.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1_Modify.setObjectName("frame_1_Modify")
        self.Hour_Begin_Modify = QtWidgets.QLineEdit(self.frame_1_Modify)
        self.Hour_Begin_Modify.setGeometry(QtCore.QRect(10, 10, 31, 16))
        self.Hour_Begin_Modify.setFrame(False)
        self.Hour_Begin_Modify.setObjectName("Hour_Begin_Modify")
        self.Minute_Begin_modify = QtWidgets.QLineEdit(self.frame_1_Modify)
        self.Minute_Begin_modify.setGeometry(QtCore.QRect(60, 10, 31, 16))
        self.Minute_Begin_modify.setFrame(False)
        self.Minute_Begin_modify.setObjectName("Minute_Begin_modify")
        self.Second_begin_Modify = QtWidgets.QLineEdit(self.frame_1_Modify)
        self.Second_begin_Modify.setGeometry(QtCore.QRect(110, 10, 31, 16))
        self.Second_begin_Modify.setFrame(False)
        self.Second_begin_Modify.setObjectName("Second_begin_Modify")
        self.Mellisecond_Begin_modify = QtWidgets.QLineEdit(self.frame_1_Modify)
        self.Mellisecond_Begin_modify.setGeometry(QtCore.QRect(160, 10, 31, 16))
        self.Mellisecond_Begin_modify.setFrame(False)
        self.Mellisecond_Begin_modify.setObjectName("Mellisecond_Begin_modify")
        self.label_15 = QtWidgets.QLabel(self.frame_1_Modify)
        self.label_15.setGeometry(QtCore.QRect(40, 10, 16, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_1_Modify)
        self.label_16.setGeometry(QtCore.QRect(90, 10, 16, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_1_Modify)
        self.label_17.setGeometry(QtCore.QRect(140, 10, 16, 16))
        self.label_17.setObjectName("label_17")
        self.chapter_name_Modify = QtWidgets.QLineEdit(self.tab_2)
        self.chapter_name_Modify.setGeometry(QtCore.QRect(242, 155, 171, 31))
        self.chapter_name_Modify.setObjectName("chapter_name_Modify")
        self.Finish_button_Modify = QtWidgets.QPushButton(self.tab_2)
        self.Finish_button_Modify.setGeometry(QtCore.QRect(332, 425, 93, 28))
        self.Finish_button_Modify.setObjectName("Finish_button_Modify")
        self.Edit_button = QtWidgets.QPushButton(self.tab_2)
        self.Edit_button.setGeometry(QtCore.QRect(230, 375, 93, 28))
        self.Edit_button.setObjectName("Edit_button")
        self.Delete_button = QtWidgets.QPushButton(self.tab_2)
        self.Delete_button.setGeometry(QtCore.QRect(434, 375, 93, 28))
        self.Delete_button.setObjectName("Delete_button")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(72, 375, 151, 80))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 95, 20))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 50, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.Append_button_modify = QtWidgets.QPushButton(self.tab_2)
        self.Append_button_modify.setGeometry(QtCore.QRect(332, 375, 93, 28))
        self.Append_button_modify.setObjectName("Append_button_modify")
        self.listWidget_modify = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_modify.setGeometry(QtCore.QRect(72, 465, 581, 221))
        self.listWidget_modify.setObjectName("listWidget_modify")
        self.label_52 = QtWidgets.QLabel(self.tab_2)
        self.label_52.setGeometry(QtCore.QRect(762, 115, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Mikadan")
        font.setPointSize(16)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.label_50 = QtWidgets.QLabel(self.tab_2)
        self.label_50.setGeometry(QtCore.QRect(552, 245, 681, 481))
        self.label_50.setAutoFillBackground(False)
        self.label_50.setText("")
        self.label_50.setPixmap(QtGui.QPixmap("./photo.png"))
        self.label_50.setScaledContents(True)
        self.label_50.setObjectName("label_50")
        self.label_50.raise_()
        self.browse_Button_modify.raise_()
        self.browse_lineedit_modify.raise_()
        self.frame_1_Modify.raise_()
        self.chapter_name_Modify.raise_()
        self.Finish_button_Modify.raise_()
        self.Edit_button.raise_()
        self.Delete_button.raise_()
        self.groupBox.raise_()
        self.Append_button_modify.raise_()
        self.label_52.raise_()
        self.listWidget_modify.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.chapter_name_create_vid = QtWidgets.QLineEdit(self.tab_4)
        self.chapter_name_create_vid.setGeometry(QtCore.QRect(270, 340, 171, 31))
        self.chapter_name_create_vid.setObjectName("chapter_name_create_vid")

        self.mediaplayer=QMediaPlayer(None,QMediaPlayer.VideoSurface)
        self.videowid=QVideoWidget()      
        self.mediaplayer.setVolume(10)  
        self.openBTN=QPushButton('Browse')
        self.close_vid=QPushButton('close')
        self.playBTN=QPushButton()
        self.playBTN.setEnabled(False)
        self.close_vid.setEnabled(False)
        self.playBTN.setIcon(self.playBTN.style().standardIcon(QStyle.SP_MediaPlay))
        self.slider=QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.lineedit_vid=QLineEdit()
        self.lineedit_vid.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Maximum)
        self.lineedit_vid.setText("00:00:00.000")
        self.lineedit_vid.setReadOnly(True)
        self.forward_btn_long=QPushButton(">>")
        self.forward_btn_short=QPushButton(">")
        self.backward_btn_long=QPushButton("<<")
        self.backward_btn_short=QPushButton("<")
        self.forward_btn_long.setEnabled(False)
        self.backward_btn_long.setEnabled(False)
        self.forward_btn_short.setEnabled(False)
        self.backward_btn_short.setEnabled(False)
        self.Finish_button_Create_vid.setEnabled(False)
        self.hboxlayout=QHBoxLayout()
        self.hboxlayout.setContentsMargins(0,0,0,0)
        self.hboxlayout2=QHBoxLayout()
        self.hboxlayout2.setContentsMargins(0,0,0,0)
        self.hboxlayout.addWidget(self.openBTN)
        self.hboxlayout.addWidget(self.close_vid)
        self.hboxlayout.addWidget(self.playBTN)
        self.hboxlayout.addWidget(self.slider)
        self.hboxlayout2.addWidget(self.backward_btn_long)
        self.hboxlayout2.addWidget(self.backward_btn_short)
        self.hboxlayout2.addWidget(self.lineedit_vid)
        self.hboxlayout2.addWidget(self.forward_btn_short)
        self.hboxlayout2.addWidget(self.forward_btn_long)
        self.vboxlayout=QVBoxLayout()
        self.vboxlayout.addWidget(self.videowid)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.vboxlayout.addLayout(self.hboxlayout2)
        self.frame.setLayout(self.vboxlayout)
        self.mediaplayer.setVideoOutput(self.videowid)
        self.Append_button_vid.setEnabled(False)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.openBTN.clicked.connect(self.file_name)
        self.playBTN.clicked.connect(self.play_video)
        self.mediaplayer.positionChanged.connect(self.position_changed)
        self.mediaplayer.durationChanged.connect(self.duration_changed)
        self.slider.sliderMoved.connect(self.set_positin)
        self.Append_button.clicked.connect(lambda : self.append(self.chapter_name_create.text(),self.Hour_Begin_create.text(),self.Minute_Begin_create.text(),self.Second_begin_create.text(),self.Mellisecond_Begin_create.text()))
        self.Browse_button_create.clicked.connect(self.handle_browse_create)
        self.Finish_button_Create.clicked.connect(self.finish_create)
        self.browse_Button_modify.clicked.connect(self.handle_browse_modify)
        self.Delete_button.clicked.connect(self.Delete_modify)
        self.Edit_button.clicked.connect(lambda : self.edit_modify(self.chapter_name_Modify.text(),self.Hour_Begin_Modify.text(),self.Minute_Begin_modify.text(),self.Second_begin_Modify.text(),self.Mellisecond_Begin_modify.text()))
        self.Finish_button_Modify.clicked.connect(self.finish_modify)
        self.Append_button_modify.clicked.connect(lambda : self.append_modify(self.chapter_name_Modify.text(),self.Hour_Begin_Modify.text(),self.Minute_Begin_modify.text(),self.Second_begin_Modify.text(),self.Mellisecond_Begin_modify.text()))
        self.listWidget_modify.itemClicked.connect(self.singleClick)
        self.forward_btn_long.clicked.connect(self.forward_fun_long)
        self.backward_btn_long.clicked.connect(self.backward_fun_long)
        self.forward_btn_short.clicked.connect(self.forward_fun_short)
        self.backward_btn_short.clicked.connect(self.backward_fun_short)
        self.Append_button_vid.clicked.connect(lambda : self.append_vid(self.chapter_name_create_vid.text(),self.lineedit_vid.text()))
        self.Finish_button_Create_vid.clicked.connect(self.finish_create_vid)
        self.close_vid.clicked.connect(self.closeVideo)
        self.save_location=""
        self.save_location_modify=""
        self.nodes=[]
        self.indexcreate=1
        self.fileNameVid=""
        self.indexcreate_vid=1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Loli Chapters Maker V 0.4"))
        self.tabWidget.setStatusTip(_translate("MainWindow", "Open A chapter File to Modify It"))
        self.groupBox_2.setStatusTip(_translate("MainWindow", "Chapter Language"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Chapter Language"))
        self.radioButton_3.setStatusTip(_translate("MainWindow", "English"))
        self.radioButton_3.setText(_translate("MainWindow", "English"))
        self.radioButton_4.setStatusTip(_translate("MainWindow", "Arabic"))
        self.radioButton_4.setText(_translate("MainWindow", "Arabic"))
        self.Hour_Begin_create.setStatusTip(_translate("MainWindow", "Hour_Begin"))
        self.Hour_Begin_create.setPlaceholderText(_translate("MainWindow", "00"))
        self.Minute_Begin_create.setStatusTip(_translate("MainWindow", "Minute_Begin"))
        self.Minute_Begin_create.setPlaceholderText(_translate("MainWindow", "00"))
        self.Second_begin_create.setStatusTip(_translate("MainWindow", "Second_Begin"))
        self.Second_begin_create.setPlaceholderText(_translate("MainWindow", "00"))
        self.Mellisecond_Begin_create.setStatusTip(_translate("MainWindow", "Mellisecond_Begin"))
        self.Mellisecond_Begin_create.setPlaceholderText(_translate("MainWindow", "00"))
        self.label.setText(_translate("MainWindow", ":"))
        self.label_2.setText(_translate("MainWindow", ":"))
        self.label_3.setText(_translate("MainWindow", ":"))
        self.Finish_button_Create.setStatusTip(_translate("MainWindow", "Save The Chapter"))
        self.Finish_button_Create.setText(_translate("MainWindow", "Finish"))
        self.chapter_name_create.setStatusTip(_translate("MainWindow", "Chapter Name"))
        self.chapter_name_create.setPlaceholderText(_translate("MainWindow", "Chapter Name"))
        self.chapter_name_create_vid.setStatusTip(_translate("MainWindow", "Chapter Name"))
        self.chapter_name_create_vid.setPlaceholderText(_translate("MainWindow", "Chapter Name"))
        self.browse_lineedit_create.setStatusTip(_translate("MainWindow", "Where To save Your Chapter File!!"))
        self.browse_lineedit_create.setPlaceholderText(_translate("MainWindow", "Where To save Your Chapter File!!"))
        self.Browse_button_create.setStatusTip(_translate("MainWindow", "Browse"))
        self.Browse_button_create.setText(_translate("MainWindow", "Browse"))
        self.label_49.setStatusTip(_translate("MainWindow", "Loli Chapter Maker And Modifier V 0.4"))
        self.label_49.setText(_translate("MainWindow", "Loli Chapter Maker"))
        self.Append_button.setStatusTip(_translate("MainWindow", "Apend to Chapters"))
        self.Append_button.setText(_translate("MainWindow", "Append"))
        self.label_48.setStatusTip(_translate("MainWindow", "Loli Chapter Maker And Modifier V 0.4"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Create a new Chapter"))
        self.label_47.setStatusTip(_translate("MainWindow", "Loli Chapter Maker And Modifier V 0.4"))
        self.label_51.setStatusTip(_translate("MainWindow", "Loli Chapter Maker And Modifier V 0.4"))
        self.label_51.setText(_translate("MainWindow", "Loli Chapter Maker"))
        self.frame.setStatusTip(_translate("MainWindow", "video player"))
        self.groupBox_3.setStatusTip(_translate("MainWindow", "Chapter Language"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Chapter Language"))
        self.radioButton_5.setStatusTip(_translate("MainWindow", "English"))
        self.radioButton_5.setText(_translate("MainWindow", "English"))
        self.radioButton_6.setStatusTip(_translate("MainWindow", "Arabic"))
        self.radioButton_6.setText(_translate("MainWindow", "Arabic"))
        self.Append_button_vid.setStatusTip(_translate("MainWindow", "Apend to Chapters"))
        self.Append_button_vid.setText(_translate("MainWindow", "Append"))
        self.Finish_button_Create_vid.setStatusTip(_translate("MainWindow", "Save The Chapter"))
        self.Finish_button_Create_vid.setText(_translate("MainWindow", "Finish"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Create a new Chapter on video"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Create A New Chapter File"))
        self.browse_Button_modify.setStatusTip(_translate("MainWindow", "Browse"))
        self.browse_Button_modify.setText(_translate("MainWindow", "Browse"))
        self.browse_lineedit_modify.setStatusTip(_translate("MainWindow", "Open A Chapter File To Modify It"))
        self.browse_lineedit_modify.setPlaceholderText(_translate("MainWindow", "Open A Chapter File To Modify It"))
        self.Hour_Begin_Modify.setStatusTip(_translate("MainWindow", "Hour_Begin"))
        self.Hour_Begin_Modify.setPlaceholderText(_translate("MainWindow", "00"))
        self.Minute_Begin_modify.setStatusTip(_translate("MainWindow", "Minute_Begin"))
        self.Minute_Begin_modify.setPlaceholderText(_translate("MainWindow", "00"))
        self.Second_begin_Modify.setStatusTip(_translate("MainWindow", "Second_Begin"))
        self.Second_begin_Modify.setPlaceholderText(_translate("MainWindow", "00"))
        self.Mellisecond_Begin_modify.setStatusTip(_translate("MainWindow", "Mellisecond_Begin"))
        self.Mellisecond_Begin_modify.setPlaceholderText(_translate("MainWindow", "00"))
        self.label_15.setText(_translate("MainWindow", ":"))
        self.label_16.setText(_translate("MainWindow", ":"))
        self.label_17.setText(_translate("MainWindow", ":"))
        self.chapter_name_Modify.setStatusTip(_translate("MainWindow", "Chapter Name"))
        self.chapter_name_Modify.setPlaceholderText(_translate("MainWindow", "Chapter Name"))
        self.Finish_button_Modify.setStatusTip(_translate("MainWindow", "Save The Chapter"))
        self.Finish_button_Modify.setText(_translate("MainWindow", "Finish"))
        self.Edit_button.setStatusTip(_translate("MainWindow", "Apend to Chapters"))
        self.Edit_button.setText(_translate("MainWindow", "Edit"))
        self.Delete_button.setStatusTip(_translate("MainWindow", "Apend to Chapters"))
        self.Delete_button.setText(_translate("MainWindow", "Delete"))
        self.groupBox.setStatusTip(_translate("MainWindow", "Chapter Language"))
        self.groupBox.setTitle(_translate("MainWindow", "Chapter Language"))
        self.radioButton.setStatusTip(_translate("MainWindow", "English"))
        self.radioButton.setText(_translate("MainWindow", "English"))
        self.radioButton_2.setStatusTip(_translate("MainWindow", "Arabic"))
        self.radioButton_2.setText(_translate("MainWindow", "Arabic"))
        self.Append_button_modify.setStatusTip(_translate("MainWindow", "Apend to Chapters"))
        self.Append_button_modify.setText(_translate("MainWindow", "Append"))
        self.label_52.setStatusTip(_translate("MainWindow", "Loli Chapter Maker And Modifier V 0.4"))
        self.label_52.setText(_translate("MainWindow", "Loli Chapter Maker"))
        self.label_50.setStatusTip(_translate("MainWindow", "Loli Chapter Maker And Modifier V 0.4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Modify An Exsisted Chapter File"))
    def file_name(self):
        fileName,_=QFileDialog.getOpenFileName(self.openBTN,"Open Video",filter="Video Files ("+vidtypes()+")")
        self.fileNameVid=str(fileName)[:str(fileName).rfind(".")]+".xml"
        try:
            if(self.fileNameVid!=".xml"):
                file=open(self.fileNameVid,"w",encoding="utf-8")
                file.write("<?xml version=\"1.0\"?>\n<!-- <!DOCTYPE Chapters SYSTEM \"matroskachapters.dtd\"> -->\n<Chapters>\n\t<EditionEntry>\n\t\t")
                file.close()
        except:
            pass        
        if(fileName!=""):
            self.mediaplayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playBTN.setEnabled(True)
            self.backward_btn_long.setEnabled(True)
            self.forward_btn_long.setEnabled(True)
            self.backward_btn_short.setEnabled(True)
            self.forward_btn_short.setEnabled(True)
            self.openBTN.setEnabled(False)
            self.close_vid.setEnabled(True)
            self.Append_button_vid.setEnabled(True)
    def append_vid(self,chapter_name,chapter_time):
        if(self.radioButton_5.isChecked()==True):
            lang="English"
            lan="eng"
        if(self.radioButton_6.isChecked()==True):
            lang="Arabic"  
            lan='ara'   
        if(chapter_name==""):
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("Critical!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("you cant appened ,please fill the chapter name !!")
            x=msg.exec_()
        elif  (chapter_time=="00:00:00.000" and self.openBTN.isEnabled()==True):
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("Critical!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("you cant appened ,please browse for a video first !!")
            x=msg.exec_()
        
        else :  
            try :
                t=str(chapter_time).split(":")
                H=int(t[0])
                M=int(t[1])
                t=t[2].split(".")
                S=int(t[0])
                MS=int(t[1])
                tmp="Index: "+str(self.indexcreate_vid)+"    -->    Name: "+str(chapter_name)+"    -->    Lang: "+lan+"    -->    Time: "+str(chapter_time)
                self.listWidget_create_Vid.addItem(tmp)
                self.indexcreate_vid+=1
                file=open(self.fileNameVid,"a",encoding="utf-8")
                file.write("<ChapterAtom>\n\t\t\t")
                file.write("<ChapterUID>"+str((24*60*1000*int(fix(H,2)))+(60*1000*int(fix(M,2)))+(1000*int(fix(S,2)))+int(fix(MS,3)))+"</ChapterUID>\n\t\t\t")
                file.write("<ChapterFlagHidden>0</ChapterFlagHidden>\n\t\t\t<ChapterFlagEnabled>1</ChapterFlagEnabled>\n\t\t\t")
                file.write("<ChapterTimeStart>"+str(chapter_time)+"</ChapterTimeStart>\n\t\t\t")
                file.write("<ChapterDisplay>\n\t\t\t\t")
                file.write("<ChapterString>")
                file.write(chapter_name)
                file.write("</ChapterString>\n\t\t\t\t")
                file.write("<ChapterLanguage>"+lan+"</ChapterLanguage>\n\t\t\t")
                file.write("</ChapterDisplay>\n\t")
                file.write("</ChapterAtom>\n\t")
                file.close()
                self.chapter_name_create_vid.setText("")
                self.Finish_button_Create_vid.setEnabled(True)
                self.close_vid.setEnabled(False)
            except:
                
                msg=QtWidgets.QMessageBox()
                msg.setWindowTitle("Critical!")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("please full  all spaces with integer !!")
                self.Hour_Begin_create.setText("")
                self.Minute_Begin_create.setText("")
                self.Second_begin_create.setText("")
                self.Mellisecond_Begin_create.setText("")
                x=msg.exec_()
    def closeVideo(self):
        os.remove(self.fileNameVid)
        self.fileNameVid=""
        self.mediaplayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.fileNameVid)))
        self.chapter_name_create_vid.setText("")
        self.openBTN.setEnabled(True)
        self.playBTN.setEnabled(False)
        self.close_vid.setEnabled(False)
        self.Append_button_vid.setEnabled(False)
        self.backward_btn_long.setEnabled(False)
        self.forward_btn_long.setEnabled(False)
        self.backward_btn_short.setEnabled(False)
        self.forward_btn_short.setEnabled(False)
        self.listWidget_create_Vid.clear()
        self.indexcreate_vid=1

    def finish_create_vid(self):
        self.Finish_button_Create_vid.setEnabled(False)
        file=open(self.fileNameVid,"a",encoding='utf-8')
        file.write("</EditionEntry>\n</Chapters>\n")
        self.chapter_name_create_vid.setText("")
        self.openBTN.setEnabled(True)
        self.playBTN.setEnabled(False)
        self.backward_btn_long.setEnabled(False)
        self.forward_btn_long.setEnabled(False)
        self.backward_btn_short.setEnabled(False)
        self.forward_btn_short.setEnabled(False)
        self.Append_button_vid.setEnabled(False)
        self.listWidget_create_Vid.clear()
        self.indexcreate_vid=1
        msg=QtWidgets.QMessageBox()
        msg.setWindowTitle("information!")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Done!!")
        x=msg.exec_()
        self.fileNameVid=""
        self.mediaplayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.fileNameVid)))
        
    def play_video(self):
        if self.mediaplayer.state()==QMediaPlayer.PlayingState:
            self.mediaplayer.pause()
            self.playBTN.setIcon(self.playBTN.style().standardIcon(QStyle.SP_MediaPlay))

        else :
            self.mediaplayer.play()
            self.playBTN.setIcon(self.playBTN.style().standardIcon(QStyle.SP_MediaPause))
    def position_changed(self,position):
        self.slider.setValue(position)
        self.lineedit_vid.setText(trans(position))
    def duration_changed(self,duration):
        self.slider.setRange(0,duration)
    def set_positin(self,position):
        self.mediaplayer.setPosition(position)
    def forward_fun_long(self):
        try:
            p=self.mediaplayer.position()
            self.mediaplayer.setPosition(p+500)
        except:
            pass
    def backward_fun_long(self):
        try:
            p=self.mediaplayer.position()
            self.mediaplayer.setPosition(p-500)
        except:
            pass
    def forward_fun_short(self):
        try:
            p=self.mediaplayer.position()
            self.mediaplayer.setPosition(p+250)
        except:
            pass
    def backward_fun_short(self):
        try:
            p=self.mediaplayer.position()
            self.mediaplayer.setPosition(p-250)
        except:
            pass

    def append(self,chapter_name,Hour_begin,Minute_Begin,Second_Begin,Mellisecond_Begin):
        if(self.radioButton_3.isChecked()==True):
            lang="English"
            lan="eng"
        if(self.radioButton_4.isChecked()==True):
            lang="Arabic"  
            lan='ara'   
        if(chapter_name==""):
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("Critical!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("you cant appened ,please fill the chapter name !!")
            x=msg.exec_()
        elif  (Hour_begin=="" and Minute_Begin=="" and Second_Begin=="" and Mellisecond_Begin==""):
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("Critical!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("you cant appened ,please fill the chapter point time !!")
            x=msg.exec_()
        elif self.browse_lineedit_create.text()=="":
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("Critical!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("you cant appened ,please choose where to save your chapter file !!")
            x=msg.exec_()
        
        else :  
            try :
                hour_begin=int(Hour_begin)
                Minute_Begin=int(Minute_Begin)
                Second_Begin=int(Second_Begin)
                Mellisecond_Begin=int(Mellisecond_Begin)
                if int(fix(Minute_Begin,2))>=60  or int(fix(Minute_Begin,2))<0 :
                    msg=QtWidgets.QMessageBox()
                    msg.setWindowTitle("Critical!")
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setText("you cant appened ,notice that minutes must be in range [0,59] !!")
                    x=msg.exec_()
                    self.Minute_Begin_create.setText("")
                elif int(fix(Second_Begin,2))>=60  or int(fix(Second_Begin,2))<0 :
                    msg=QtWidgets.QMessageBox()
                    msg.setWindowTitle("Critical!")
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setText("you cant appened ,notice that seconds must be in range [0,59] !!")
                    x=msg.exec_()
                    self.Second_begin_create.setText("")
                elif int(fix(Mellisecond_Begin,3))>=1000  or int(fix(Mellisecond_Begin,3))<0 :
                    msg=QtWidgets.QMessageBox()
                    msg.setWindowTitle("Critical!")
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setText("you cant appened ,notice that melliseconds must be in range [0,999] !!")
                    x=msg.exec_()
                    self.Mellisecond_Begin_create.setText("")
                else:
                    tmp="Index: "+str(self.indexcreate)+"    -->    Name: "+str(chapter_name)+"    -->    Lang: "+lan+"    -->    Time: "+Hour_begin+":"+fix( Minute_Begin ,2)+":"+fix( Second_Begin ,2)+"."+fix( Mellisecond_Begin ,3)
                    self.listWidget_create.addItem(tmp)
                    self.indexcreate+=1
                    file=open(self.save_location,"a",encoding="utf-8")
                    file.write("<ChapterAtom>\n\t\t\t")
                    file.write("<ChapterUID>"+str((24*60*1000*int(fix(Hour_begin,2)))+(60*1000*int(fix(Minute_Begin,2)))+(1000*int(fix(Second_Begin,2)))+int(fix(Mellisecond_Begin,3)))+"</ChapterUID>\n\t\t\t")
                    file.write("<ChapterFlagHidden>0</ChapterFlagHidden>\n\t\t\t<ChapterFlagEnabled>1</ChapterFlagEnabled>\n\t\t\t")
                    file.write("<ChapterTimeStart>"+fix( Hour_begin ,2)+":"+fix( Minute_Begin ,2)+":"+fix( Second_Begin ,2)+"."+fix( Mellisecond_Begin ,3)+"</ChapterTimeStart>\n\t\t\t")
                    file.write("<ChapterDisplay>\n\t\t\t\t")
                    file.write("<ChapterString>")
                    file.write(chapter_name)
                    file.write("</ChapterString>\n\t\t\t\t")
                    file.write("<ChapterLanguage>"+lan+"</ChapterLanguage>\n\t\t\t")
                    file.write("</ChapterDisplay>\n\t")
                    file.write("</ChapterAtom>\n\t")
                    file.close()
                    self.Hour_Begin_create.setText("")
                    self.Minute_Begin_create.setText("")
                    self.Second_begin_create.setText("")
                    self.Mellisecond_Begin_create.setText("")
                    self.chapter_name_create.setText("")
            except:
                
                msg=QtWidgets.QMessageBox()
                msg.setWindowTitle("Critical!")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("please full  all spaces with integer !!")
                self.Hour_Begin_create.setText("")
                self.Minute_Begin_create.setText("")
                self.Second_begin_create.setText("")
                self.Mellisecond_Begin_create.setText("")
                x=msg.exec_()

    def handle_browse_create(self):
        save_location_tuble=QtWidgets.QFileDialog.getSaveFileName(self.browse_lineedit_create,caption="Save as",directory=".",filter="XML Files (*.xml)")
        self.save_location=str(save_location_tuble[0])
        self.browse_lineedit_create.setText(self.save_location)
        try:
            file=open(self.save_location,"w",encoding="utf-8")
            file.write("<?xml version=\"1.0\"?>\n<!-- <!DOCTYPE Chapters SYSTEM \"matroskachapters.dtd\"> -->\n<Chapters>\n\t<EditionEntry>\n\t\t")
            file.close()
        except:
            pass
    def finish_create(self):
        try:
            file=open(self.save_location,"a")
            file.write("</EditionEntry>\n</Chapters>\n")
            self.browse_lineedit_create.setText("")
            self.Hour_Begin_create.setText("")
            self.Minute_Begin_create.setText("")
            self.Second_begin_create.setText("")
            self.Mellisecond_Begin_create.setText("")
            self.chapter_name_create.setText("")
            self.listWidget_create.clear()
            self.indexcreate=1
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("information!")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Done!!")
            x=msg.exec_()
            self.save_location=""
        except:
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("Information!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("browse for a chapter file first!!")
            x=msg.exec_()
    def handle_browse_modify(self):
        save_location_tuble=QtWidgets.QFileDialog.getOpenFileName(self.browse_lineedit_modify,caption="Open",directory=".",filter="XML Files (*.xml)")
        self.save_location_modify=str(save_location_tuble[0])
        self.browse_lineedit_modify.setText(self.save_location_modify)
        try:
            file=open(self.save_location_modify,'r',encoding="utf-8")
            x=file.readlines()
            file.close()

            tmp=""
            flag=0
            for i in x:
                if i.find("<ChapterAtom>")!=-1:
                    flag=1
                if i.find("</ChapterAtom>")!=-1:
                    tmp+=i
                    self.nodes.append(tmp)
                    tmp=""
                    flag=0
                if(flag==1):
                    tmp+=i
            c=1
            for i in self.nodes:
                tmp="Index: "+str(c)+"     -->    Name: "+i[i.find('<ChapterString>')+len("<ChapterString>"):i.find('</ChapterString>')]+"     -->    Lang: "+i[i.find('<ChapterLanguage>')+len("<ChapterLanguage>"):i.find('</ChapterLanguage>')]+"     -->    Time: "+i[i.find('<ChapterTimeStart>')+len("<ChapterTimeStart>"):i.find('</ChapterTimeStart>')]
                self.listWidget_modify.addItem(tmp)
                c+=1
        except:
            pass
    def Delete_modify(self):
        if(len(self.nodes)==0 ):
            
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("There is no chapter to delete !!")
            
            x=msg.exec_()
        elif(self.listWidget_modify.currentItem()==None ):
            
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("select a chapter to delete !!")
            
            x=msg.exec_()

        
        else:
            indstr=self.listWidget_modify.currentItem().text()
            indstr=str(indstr).split(" ")

            ind=int(indstr[1])-1
            self.nodes.pop(ind)
            self.listWidget_modify.clear()
            c=1
            for i in self.nodes:
                tmp="Index: "+str(c)+"     -->    Name: "+i[i.find('<ChapterString>')+len("<ChapterString>"):i.find('</ChapterString>')]+"     -->    Lang: "+i[i.find('<ChapterLanguage>')+len("<ChapterLanguage>"):i.find('</ChapterLanguage>')]+"     -->    Time: "+i[i.find('<ChapterTimeStart>')+len("<ChapterTimeStart>"):i.find('</ChapterTimeStart>')]
                self.listWidget_modify.addItem(tmp)
                c+=1
            self.Hour_Begin_Modify.setText("")
            self.Minute_Begin_modify.setText("")
            self.Second_begin_Modify.setText("")
            self.Mellisecond_Begin_modify.setText("")
            self.chapter_name_Modify.setText("")

    def edit_modify(self,chapter_name,Hour_begin,Minute_Begin,Second_Begin,Mellisecond_Begin):
        if self.browse_lineedit_modify.text()=="":
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("please browse for a chapter to edit!!")
            x=msg.exec_()
        elif(self.listWidget_modify.currentItem()==None ):
            
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("select a chapter to edit !!")
            
            x=msg.exec_()
        
        else:
            indstr=self.listWidget_modify.currentItem().text()
            indstr=str(indstr).split(" ")

            ind=int(indstr[1])-1
            if(self.radioButton.isChecked()==True):
                lang="English"
                lan="eng"
            elif(self.radioButton_2.isChecked()==True):
                lang="Arabic"  
                lan='ara'  
            self.nodes[ind]=self.nodes[ind][0:self.nodes[ind].find("<ChapterLanguage>")+len("<ChapterLanguage>")]+str(lan)+self.nodes[ind][self.nodes[ind].find("</ChapterLanguage>"):]
            
            if chapter_name!="":
                self.nodes[ind]=self.nodes[ind][0:self.nodes[ind].find("<ChapterString>")+len("<ChapterString>")]+str(chapter_name)+self.nodes[ind][self.nodes[ind].find("</ChapterString>"):]
                self.listWidget_modify.clear()
                c=1
            for i in self.nodes:
                tmp="Index: "+str(c)+"     -->    Name: "+i[i.find('<ChapterString>')+len("<ChapterString>"):i.find('</ChapterString>')]+"     -->    Lang: "+i[i.find('<ChapterLanguage>')+len("<ChapterLanguage>"):i.find('</ChapterLanguage>')]+"     -->    Time: "+i[i.find('<ChapterTimeStart>')+len("<ChapterTimeStart>"):i.find('</ChapterTimeStart>')]
                self.listWidget_modify.addItem(tmp)
                c+=1

                
            if Hour_begin!="" or Minute_Begin!="" or Second_Begin!="" or Mellisecond_Begin!="":
                try:
                    hour_begin=int(Hour_begin)
                    Minute_Begin=int(Minute_Begin)
                    Second_Begin=int(Second_Begin)
                    Mellisecond_Begin=int(Mellisecond_Begin)
                    if int(fix(Minute_Begin,2))>=60  or int(fix(Minute_Begin,2))<0 :
                        msg=QtWidgets.QMessageBox()
                        msg.setWindowTitle("Critical!")
                        msg.setIcon(QtWidgets.QMessageBox.Critical)
                        msg.setText("you cant appened ,notice that minutes must be in range [0,59] !!")
                        x=msg.exec_()
                        self.Minute_Begin_create.setText("")
                    elif int(fix(Second_Begin,2))>=60  or int(fix(Second_Begin,2))<0 :
                        msg=QtWidgets.QMessageBox()
                        msg.setWindowTitle("Critical!")
                        msg.setIcon(QtWidgets.QMessageBox.Critical)
                        msg.setText("you cant appened ,notice that seconds must be in range [0,59] !!")
                        x=msg.exec_()
                        self.Second_begin_create.setText("")
                    elif int(fix(Mellisecond_Begin,3))>=1000  or int(fix(Mellisecond_Begin,3))<0 :
                        msg=QtWidgets.QMessageBox()
                        msg.setWindowTitle("Critical!")
                        msg.setIcon(QtWidgets.QMessageBox.Critical)
                        msg.setText("you cant appened ,notice that melliseconds must be in range [0,999] !!")
                        x=msg.exec_()
                        self.Mellisecond_Begin_create.setText("")
                    else:

                        self.nodes[ind]=self.nodes[ind][0:self.nodes[ind].find("<ChapterTimeStart>")+len("<ChapterTimeStart>")]+str(str(fix(Hour_begin,2))+":"+str(fix(Minute_Begin,2))+":"+str(fix(Second_Begin,2))+"."+str(fix(Mellisecond_Begin,3)))+self.nodes[ind][self.nodes[ind].find("</ChapterTimeStart>"):]
                        
                        self.listWidget_modify.clear()
                        c=1
                        for i in self.nodes:
                            tmp="Index: "+str(c)+"     -->    Name: "+i[i.find('<ChapterString>')+len("<ChapterString>"):i.find('</ChapterString>')]+"     -->    Lang: "+i[i.find('<ChapterLanguage>')+len("<ChapterLanguage>"):i.find('</ChapterLanguage>')]+"     -->    Time: "+i[i.find('<ChapterTimeStart>')+len("<ChapterTimeStart>"):i.find('</ChapterTimeStart>')]
                            self.listWidget_modify.addItem(tmp)
                            c+=1
                        
                        self.nodes[ind]=self.nodes[ind][0:self.nodes[ind].find("<ChapterUID>")+len("<ChapterUID>")]+str((24*60*1000*int(fix(Hour_begin,2)))+(60*1000*int(fix(Minute_Begin,2)))+(1000*int(fix(Second_Begin,2)))+int(fix(Mellisecond_Begin,3)))   +self.nodes[ind][self.nodes[ind].find("</ChapterUID>"):]
                        self.Hour_Begin_Modify.setText("")
                        self.Minute_Begin_modify.setText("")
                        self.Second_begin_Modify.setText("")
                        self.Mellisecond_Begin_modify.setText("")
                        self.chapter_name_Modify.setText("")
                except:
                    msg=QtWidgets.QMessageBox()
                    msg.setWindowTitle("Critical!")
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setText("you cant enter letters !!")
                    self.Hour_Begin_Modify.setText("")
                    self.Minute_Begin_modify.setText("")
                    self.Second_begin_Modify.setText("")
                    self.Mellisecond_Begin_modify.setText("")
                    x=msg.exec_()

            
    def finish_modify(self):
        try:
            file=open(self.save_location_modify,'w',encoding="utf-8")
            file.write("<?xml version=\"1.0\"?>\n")
            file.write("<!-- <!DOCTYPE Chapters SYSTEM \"matroskachapters.dtd\"> -->\n")
            file.write("<Chapters>\n")
            file.write("\t<EditionEntry>\n")
            for i in self.nodes:
                file.write(i)
            file.write("\t</EditionEntry>\n")
            file.write("</Chapters>")
            file.close()
            self.browse_lineedit_modify.setText("")
            self.Hour_Begin_Modify.setText("")
            self.Minute_Begin_modify.setText("")
            self.Second_begin_Modify.setText("")
            self.Mellisecond_Begin_modify.setText("")
            self.listWidget_modify.clear()
            self.chapter_name_Modify.setText("")
            self.nodes.clear()
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("Information!")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Done!!")
            x=msg.exec_()
            self.save_location_modify=""
        except:
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("Information!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("browse for capter file first!!")
            x=msg.exec_()
            pass
    def append_modify(self,chapter_name,Hour_begin,Minute_Begin,Second_Begin,Mellisecond_Begin):
        if(self.radioButton.isChecked()==True):
            lang="English"
            lan="eng"
        elif(self.radioButton_2.isChecked()==True):
            lang="Arabic"  
            lan='ara'   
        if(chapter_name==""):
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("Critical!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("you cant appened ,please fill the chapter name !!")
            x=msg.exec_()
        elif  (Hour_begin=="" and Minute_Begin=="" and Second_Begin=="" and Mellisecond_Begin==""):
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("Critical!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("you cant appened ,please fill the chapter point time !!")
            x=msg.exec_()
        elif self.browse_lineedit_modify.text()=="":
            msg=QtWidgets.QMessageBox()
            msg.setWindowTitle("Critical!")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("you cant appened ,please open a achapter file first !!")
            x=msg.exec_()
        
        else :  
            try:
                hour_begin=int(Hour_begin)
                Minute_Begin=int(Minute_Begin)
                Second_Begin=int(Second_Begin)
                Mellisecond_Begin=int(Mellisecond_Begin)
                if int(fix(Minute_Begin,2))>=60  or int(fix(Minute_Begin,2))<0 :
                    msg=QtWidgets.QMessageBox()
                    msg.setWindowTitle("Critical!")
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setText("you cant appened ,notice that minutes must be in range [0,59] !!")
                    x=msg.exec_()
                    self.Minute_Begin_create.setText("")
                elif int(fix(Second_Begin,2))>=60  or int(fix(Second_Begin,2))<0 :
                    msg=QtWidgets.QMessageBox()
                    msg.setWindowTitle("Critical!")
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setText("you cant appened ,notice that seconds must be in range [0,59] !!")
                    x=msg.exec_()
                    self.Second_begin_create.setText("")
                elif int(fix(Mellisecond_Begin,3))>=1000  or int(fix(Mellisecond_Begin,3))<0 :
                    msg=QtWidgets.QMessageBox()
                    msg.setWindowTitle("Critical!")
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setText("you cant appened ,notice that melliseconds must be in range [0,999] !!")
                    x=msg.exec_()
                    self.Mellisecond_Begin_create.setText("")
                else:
                
                    tmp=""
                    tmp+="<ChapterAtom>\n\t\t\t"
                    tmp+="<ChapterUID>"+str((24*60*1000*int(fix(Hour_begin,2)))+(60*1000*int(fix(Minute_Begin,2)))+(1000*int(fix(Second_Begin,2)))+int(fix(Mellisecond_Begin,3)))+"</ChapterUID>\n\t\t\t"
                    tmp+"<ChapterFlagHidden>0</ChapterFlagHidden>\n\t\t\t<ChapterFlagEnabled>1</ChapterFlagEnabled>\n\t\t\t"
                    tmp+="<ChapterTimeStart>"+fix( Hour_begin ,2)+":"+fix( Minute_Begin ,2)+":"+fix( Second_Begin ,2)+"."+fix( Mellisecond_Begin ,3)+"</ChapterTimeStart>\n\t\t\t"
                    tmp+="<ChapterDisplay>\n\t\t\t\t"+"<ChapterString>"+chapter_name+"</ChapterString>\n\t\t\t\t"+"<ChapterLanguage>"+lan+"</ChapterLanguage>\n\t\t\t"+"</ChapterDisplay>\n\t"+"</ChapterAtom>\n\t"
                    self.nodes.append(tmp)
                    self.listWidget_modify.clear()
                    c=0
                    for i in self.nodes:
                        tmp="Index: "+str(c)+"     -->    Name: "+i[i.find('<ChapterString>')+len("<ChapterString>"):i.find('</ChapterString>')]+"     -->    Lang: "+i[i.find('<ChapterLanguage>')+len("<ChapterLanguage>"):i.find('</ChapterLanguage>')]+"     -->    Time: "+i[i.find('<ChapterTimeStart>')+len("<ChapterTimeStart>"):i.find('</ChapterTimeStart>')]
                        self.listWidget_modify.addItem(tmp)
                        c+=1
                    self.Hour_Begin_Modify.setText("")
                    self.Minute_Begin_modify.setText("")
                    self.Second_begin_Modify.setText("")
                    self.Mellisecond_Begin_modify.setText("")
                    self.chapter_name_Modify.setText("")
            except:
                msg=QtWidgets.QMessageBox()
                msg.setWindowTitle("Critical!")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("you cant enter letters !!")
                self.Hour_Begin_Modify.setText("")
                self.Minute_Begin_modify.setText("")
                self.Second_begin_Modify.setText("")
                self.Mellisecond_Begin_modify.setText("")
                x=msg.exec_()
    def singleClick(self):
        indstr=self.listWidget_modify.currentItem().text()
        indstr=str(indstr).split(" ")

        ind=int(indstr[1])-1
        tm=str(self.nodes[ind][self.nodes[ind].find('<ChapterTimeStart>')+len("<ChapterTimeStart>"):self.nodes[ind].find('</ChapterTimeStart>')])
        tm=tm.split(":")
        self.chapter_name_Modify.setText(str(self.nodes[ind][self.nodes[ind].find('<ChapterString>')+len("<ChapterString>"):self.nodes[ind].find('</ChapterString>')]))
        lan=self.nodes[ind][self.nodes[ind].find('<ChapterLanguage>')+len("<ChapterLanguage>"):self.nodes[ind].find('</ChapterLanguage>')]
        if(lan=="eng"):
            self.radioButton.setChecked(True)
        else :
            self.radioButton_2.setChecked(True)
        self.Hour_Begin_Modify.setText(tm[0])        
        self.Minute_Begin_modify.setText(tm[1])
        tm=tm[2].split(".")
        self.Second_begin_Modify.setText(tm[0])
        self.Mellisecond_Begin_modify.setText(tm[1])       
        





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyle(QtWidgets.QStyleFactory.create("gtk2"))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
