from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QBoxLayout ,QLabel,QSlider,QStyle,QSizePolicy,QHBoxLayout,QVBoxLayout,QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon   ,QPalette
from PyQt5.QtCore import Qt,QUrl
import sys
import time
def trans(millis):
    
    millis = int(millis)
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=int(millis/(1000*60*60))%24
    m=millis-(seconds*1000+minutes*60*1000+hours*60*60*1000)

    return str(hours)+":"+ str(minutes)+":"+ str(seconds)+"."+str(m)
class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Player")
        self.setGeometry(200,200,1000,700)
        
        self.initUI()

        self.show()
        self.openBTN.clicked.connect(self.file_name)
        self.playBTN.clicked.connect(self.play_video)
        self.mediaplayer.positionChanged.connect(self.position_changed)
        self.mediaplayer.durationChanged.connect(self.duration_changed)
        self.slider.sliderMoved.connect(self.set_positin)
    def initUI(self):
        self.mediaplayer=QMediaPlayer(None,QMediaPlayer.VideoSurface)
        
        self.videowid=QVideoWidget()
        
        self.openBTN=QPushButton('open video')

        self.playBTN=QPushButton("play")
        self.playBTN.setEnabled(False)
        self.playBTN.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))



        self.slider=QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)

        self.label=QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Maximum)
        self.label.setText("0:0:0.0")


        self.hboxlayout=QHBoxLayout()
        self.hboxlayout.setContentsMargins(0,0,0,0)
        self.hboxlayout.addWidget(self.openBTN)
        self.hboxlayout.addWidget(self.playBTN)
        self.hboxlayout.addWidget(self.label)
        self.hboxlayout.addWidget(self.slider)




        self.vboxlayout=QVBoxLayout()
        self.vboxlayout.addWidget(self.videowid)
        self.vboxlayout.addLayout(self.hboxlayout)
        


        self.setLayout(self.vboxlayout)
        self.mediaplayer.setVideoOutput(self.videowid)
    def file_name(self):
        fileName,_=QFileDialog.getOpenFileName(self,"Open Video")
        if(fileName!=""):
            self.mediaplayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playBTN.setEnabled(True)
    def play_video(self):
        if self.mediaplayer.state()==QMediaPlayer.PlayingState:
            self.mediaplayer.pause()
            self.playBTN.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.playBTN.setText("Play")

        else :
            self.mediaplayer.play()
            self.playBTN.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
            self.playBTN.setText("Pause")
    def position_changed(self,position):
        self.slider.setValue(position)
        self.label.setText(trans(position))
    def duration_changed(self,duration):
        self.slider.setRange(0,duration)
    def set_positin(self,position):
        self.mediaplayer.setPosition(position)
        
        





app=QApplication(sys.argv)
window=window()
sys.exit(app.exec_())
