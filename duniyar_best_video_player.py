from PyQt5.QtWidgets import QApplication , QWidget , QPushButton,QHBoxLayout,QVBoxLayout,QLabel,QSlider,QStyle,QSizePolicy,QFileDialog

import sys
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("amar player onek joss")
        self.setGeometry(350, 100,700,500)
        self.setWindowIcon(QIcon('player.png'))

        p=self.palette()
        p.setColor(QPalette.Window,Qt.black)
        self.setPalette(p)

        self.init_ui()

        self.show()

    def init_ui(self):

         #media_player_object
         self.mediaPlayer=QMediaPlayer(None,QMediaPlayer.VideoSurface)
        #video_widget_object
         videowidget=QVideoWidget()
        #open_button
         openbtn = QPushButton('open video')
         openbtn.clicked.connect(self.open_file)

        #play_button
         self.playbtn=QPushButton()
         self.playbtn.setEnabled(False)
         self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
         self.playbtn.clicked.connect(self.play_video)
        #ending_cng_btn
         cng_btn=QPushButton('change')

        #slider
         self.slider=QSlider(Qt.Horizontal)
         self.slider.setRange(0,0)
         self.slider.sliderMoved.connect(self.set_position)

        #label
         self.label=QLabel()
         self.label.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Maximum)

        #hbox_layout
         hboxlayout=QHBoxLayout()
         hboxlayout.setContentsMargins(0,0,0,0)

        #set_widgets_hbox
         hboxlayout.addWidget(openbtn)
         hboxlayout.addWidget(self.playbtn)
         hboxlayout.addWidget(self.slider)
         hboxlayout.addWidget(cng_btn)

        #vbox_layout
         vboxlayout=QVBoxLayout()
         vboxlayout.addWidget(videowidget)
         vboxlayout.addLayout(hboxlayout)
         vboxlayout.addWidget(self.label)

         self.setLayout(vboxlayout)
         self.mediaPlayer.setVideoOutput(videowidget)

         #signals_of_mediaplayer
         self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
         self.mediaPlayer.positionChanged.connect(self.position_changed)
         self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def open_file(self):
         filename, _ = QFileDialog.getOpenFileName(self,"open video")
         if filename !='':
             self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
             self.playbtn.setEnabled(True)

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playbtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause)
            )
        else:
            self.playbtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)
            )

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def handle_errors(self):
        self.playbtn.setEnabled(False)
        self.label.setText("error"+ self.mediaPlayer.errorString())


app=QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

