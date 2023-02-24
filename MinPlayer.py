from genericpath import isdir
import os
import re
import json
import time
import sched
import geopy
import shutil
import psutil
import pytube
import random
import hashlib
import pymysql
import datetime
import platform
import requests
import geocoder
import wikipedia
import pyautogui
import threading
import subprocess
import PySide2extn
import pygame as pg
from gtts import gTTS
import psutil,math,sys
import PySimpleGUI as sg
from timeit import Timer
from pytube import YouTube
from selenium import webdriver
from win10toast import ToastNotifier
from geopy.geocoders import Nominatim
from deep_translator import GoogleTranslator
from selenium.webdriver.common.keys import Keys
from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar
from lib2to3.pgen2.token import ASYNC
from playsound import *
from qt_material import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtMultimedia import *
from PySide6.QtWidgets import *
from PySide2.QtWidgets import *
from multiprocessing import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from threading import *
from datetime import*
from hashlib import *
from getpass import *
from Widgets import *
from random import *
from time import *

########################################################################
import sys
from PySide6.QtCore import QStandardPaths, Qt, Slot
from PySide6.QtGui import QAction, QIcon, QKeySequence, QScreen
from PySide6.QtWidgets import (QApplication, QDialog, QFileDialog,
    QMainWindow, QSlider, QStyle, QToolBar)
from PySide6.QtMultimedia import (QAudio, QAudioOutput, QMediaFormat,
                                  QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget


AVI = "video/x-msvideo"  # AVI


MP4 = 'video/mp4'


def get_supported_mime_types():
    result = []
    for f in QMediaFormat().supportedFileFormats(QMediaFormat.Decode):
        mime_type = QMediaFormat(f).mimeType()
        result.append(mime_type.name())
    print(result)
    return result

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)     
        ########################################################################
        self.user_name=os.environ['USERNAME']
        self.lang='Fr-fr'
        self.np=1
        self.c=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        pg.init()
        pg.mixer.init()
        self.VOLUME_CHANGE_AMOUNT = 0.02
        self.MUSIC_DONE = pg.event.custom_type()  # event to be set as mixer.music.set_endevent()
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        self.data_dir = os.path.join(self.main_dir, "data")
        self.toast_btn = {}
        self.list_add = []
        self.starting_pos = 0  # needed to fast forward and rewind
        self.volume = 0.75
        self.music_file_list = []
        self.music_file_types = ("mp3", "ogg", "mid", "mod", "it", "xm", "wav", 'wav', '3gp', 'm3u','wma','au')
        self.music_can_seek = ("mp3", "ogg", "mid", "mod", "it", "xm", "wav", 'wav', '3gp', 'm3u','wma','au')
        self.pause = False
        self.player = pg.mixer.music
        ########################################################################
        self.start=1
        self.texte=[0,0]
        self.cpt=0
        self.shp=True
        self.me=True
        self.col=["ID","GUID","PSEUDO","SEXE","BIRTHDAY","DEPT.CODE","CITY.CODE","MAIL","PASSWORD","DATE.REG","DATE.CON","AVATAR","NEW.PASS","VALIDED","CODE","CITY"]
        self.dwl_percentage={}
        self.b=self.a=50
        self.nt=0
        self.new=0
        self.nbg=0
        self.ch_btn=1
        self.gcbtn=0
        self.windowToast = True
        self.valid_log = True
        self.song_nbr=0
        self.prog = []
        self.tr = {}
        self.cind=0
        self.theme ="./Themes"
        self.path_bg_theme = []
        self.themes=[]
        self.background={}
        self.themes_names=[]
        self.bg_action={}
        self.get_name = False
        self.stop = False
        self.resize(1024,512)
        self.setStyleSheet(
"QDialog,QInputDialog,QListView,QMessageBox,QToolTip{\n"
"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"border: none;"
"}\n"
"*{\n"
"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"border: none;"
"}\n"
"QLabel,QComboBox{\n"
"background-color: transparent;"
"}\n"
"QMenu,QToolTip{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"border: 1px double cyan;border-radius: 5px;\n"
"}\n"
"QAction{\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(238,174,202,1), stop:1 rgba(148,187,233,1));\n"
"   border: 1px solid rgb(9, 5, 13);\n"
"   padding: 5px 5px 5px 5px;\n"
"   border-radius: 5px;\n"
"   text-align: center;\n"
"}\n"
"QAction:hover{\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(238,174,202,1), stop:1 rgba(148,187,233,1));\n"
"   border: 2px solid cyan;\n"
"   text-align: center;\n"
"}\n"
                )
        ########################################################################
        self.show()
        self._playlist = []  # FIXME 6.3: Replace by QMediaPlaylist?
        self._playlist_index = -1
        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)

        self._player.errorOccurred.connect(self._player_error)

        tool_bar = QToolBar()

        file_menu = self.menuBar().addMenu("&File")
        icon = QIcon.fromTheme("document-open")
        open_action = QAction(icon, "&Open...", self,
                              shortcut=QKeySequence.Open, triggered=self.open)
        file_menu.addAction(open_action)
        tool_bar.addAction(open_action)
        icon = QIcon.fromTheme("application-exit")
        exit_action = QAction(icon, "E&xit", self,
                              shortcut="Ctrl+Q", triggered=self.close)
        file_menu.addAction(exit_action)

        play_menu = self.menuBar().addMenu("&Play")
        style = self.style()
        icon = QIcon.fromTheme("media-playback-start.png",
                               style.standardIcon(QStyle.SP_MediaPlay))
        self._play_action = tool_bar.addAction(icon, "Play")
        self._play_action.triggered.connect(self._player.play)
        play_menu.addAction(self._play_action)

        icon = QIcon.fromTheme("media-skip-backward-symbolic.svg",
                               style.standardIcon(QStyle.SP_MediaSkipBackward))
        self._previous_action = tool_bar.addAction(icon, "Previous")
        self._previous_action.triggered.connect(self.previous_clicked)
        play_menu.addAction(self._previous_action)

        icon = QIcon.fromTheme("media-playback-pause.png",
                               style.standardIcon(QStyle.SP_MediaPause))
        self._pause_action = tool_bar.addAction(icon, "Pause")
        self._pause_action.triggered.connect(self._player.pause)
        play_menu.addAction(self._pause_action)

        icon = QIcon.fromTheme("media-skip-forward-symbolic.svg",
                               style.standardIcon(QStyle.SP_MediaSkipForward))
        self._next_action = tool_bar.addAction(icon, "Next")
        self._next_action.triggered.connect(self.next_clicked)
        play_menu.addAction(self._next_action)

        icon = QIcon.fromTheme("media-playback-stop.png",
                               style.standardIcon(QStyle.SP_MediaStop))
        self._stop_action = tool_bar.addAction(icon, "Stop")
        self._stop_action.triggered.connect(self._ensure_stopped)
        play_menu.addAction(self._stop_action)

        self._volume_slider = QSlider()
        self._volume_slider.setOrientation(Qt.Horizontal)
        self._volume_slider.setMinimum(0)
        self._volume_slider.setMaximum(100)
        available_width = self.screen().availableGeometry().width()
        self._volume_slider.setFixedWidth(available_width / 10)
        self._volume_slider.setValue(self._audio_output.volume())
        self._volume_slider.setTickInterval(10)
        self._volume_slider.setTickPosition(QSlider.TicksBelow)
        self._volume_slider.setToolTip("Volume")
        self._volume_slider.valueChanged.connect(self._audio_output.setVolume)
        tool_bar.addWidget(self._volume_slider)

        about_menu = self.menuBar().addMenu("&About")
        about_qt_act = QAction("About &Qt", self, triggered=qApp.aboutQt)
        about_menu.addAction(about_qt_act)

        self._video_widget = QVideoWidget()
        self._player.playbackStateChanged.connect(self.update_buttons)
        self._player.setVideoOutput(self._video_widget)
        self.setCentralWidget(self._video_widget)
        self.addToolBar(tool_bar)

        self.update_buttons(self._player.playbackState())
        self._mime_types = []

    @Slot()
    def open(self):
        self._ensure_stopped()
        file_dialog = QFileDialog(self)

        is_windows = sys.platform == 'win32'
        if not self._mime_types:
            self._mime_types = get_supported_mime_types()
            if (is_windows and AVI not in self._mime_types):
                self._mime_types.append(AVI)
            elif MP4 not in self._mime_types:
                self._mime_types.append(MP4)

        file_dialog.setMimeTypeFilters(self._mime_types)

        default_mimetype = AVI if is_windows else MP4
        if default_mimetype in self._mime_types:
            file_dialog.selectMimeTypeFilter(default_mimetype)

        movies_location = QStandardPaths.writableLocation(QStandardPaths.MoviesLocation)
        file_dialog.setDirectory(movies_location)
        if file_dialog.exec() == QDialog.Accepted:
            url = file_dialog.selectedUrls()[0]
            self._playlist.append(url)
            self._playlist_index = len(self._playlist) - 1
            self._player.setSource(url)
            self._player.play()

    @Slot()
    def _ensure_stopped(self):
        if self._player.playbackState() != QMediaPlayer.StoppedState:
            self._player.stop()

    @Slot()
    def previous_clicked(self):
        # Go to previous track if we are within the first 5 seconds of playback
        # Otherwise, seek to the beginning.
        if self._player.position() <= 5000 and self._playlist_index > 0:
            self._playlist_index -= 1
            self._playlist.previous()
            self._player.setSource(self._playlist[self._playlist_index])
        else:
            self._player.setPosition(0)

    @Slot()
    def next_clicked(self):
        if self._playlist_index < len(self._playlist) - 1:
            self._playlist_index += 1
            self._player.setSource(self._playlist[self._playlist_index])

    @Slot("QMediaPlayer::PlaybackState")
    def update_buttons(self, state):
        media_count = len(self._playlist)
        self._play_action.setEnabled(media_count > 0
            and state != QMediaPlayer.PlayingState)
        self._pause_action.setEnabled(state == QMediaPlayer.PlayingState)
        self._stop_action.setEnabled(state != QMediaPlayer.StoppedState)
        self._previous_action.setEnabled(self._player.position() > 0)
        self._next_action.setEnabled(media_count > 1)

    def show_status_message(self, message):
        self.statusBar().showMessage(message, 5000)

    @Slot("QMediaPlayer::Error", str)
    def _player_error(self, error, error_string):
        print(error_string, file=sys.stderr)
        self.show_status_message(error_string)


    def closeEvent(self, event: QCloseEvent) ->None:
        reply = QMessageBox.question(self.ui.m_m,"MIno","Are you sure to quit?",QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.speak(f"Good bye {self.user_name}!")
            event.accept()
        else:
            event.ignore()

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
