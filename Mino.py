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
#import screem
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
from argparse import ArgumentParser, RawTextHelpFormatter
from lib2to3.pgen2.token import ASYNC
from playsound import *
from qt_material import *
from PySide6.QtSql import *
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
from ui_interface import *
from threading import *
from datetime import*
from hashlib import *
from getpass import *
from Widgets import *
from random import *
from time import *
########################################################################
platforms = {'linux' : 'Linux','linux1' : 'Linux','linux2' : 'Linux','darwin' : 'OS X','win32' : 'Windows'}
bt={'statut':True,'ct':True,'middel':True,'ps':True,'bt':True,'cg':True,'full':True,'ful':True,'a':0}
event_schedule = sched.scheduler(time, time)
geoLoc = Nominatim(user_agent="GetLoc")
os.fsdecode("utf-8")
os.fsencode("utf-8")
########################################################################7

class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)

class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

#########################################################################

    @Slot()
    def run(self):

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value,None))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done

#########################################################################
class Screenshot(QWidget):
    def __init__(self):
        super().__init__()
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
        self.screenshot_label = QLabel(self)

        self.screenshot_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.screenshot_label.setAlignment(Qt.AlignCenter)

        screen_geometry: QRect = self.screen().geometry()
        self.screenshot_label.setMinimumSize(
            screen_geometry.width() / 8, screen_geometry.height() / 8
        )

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.screenshot_label)

        options_group_box = QGroupBox("Options", self)
        self.delay_spinbox = QSpinBox(options_group_box)
        self.delay_spinbox.setSuffix(" s")
        self.delay_spinbox.setMaximum(60)

        self.delay_spinbox.valueChanged.connect(self.update_checkbox)

        self.hide_this_window_checkbox = QCheckBox("Hide This Window", options_group_box)

        options_group_box_layout = QGridLayout(options_group_box)
        options_group_box_layout.addWidget(QLabel("Screenshot Delay:", self), 0, 0)
        options_group_box_layout.addWidget(self.delay_spinbox, 0, 1)
        options_group_box_layout.addWidget(self.hide_this_window_checkbox, 1, 0, 1, 2)

        main_layout.addWidget(options_group_box)

        buttons_layout = QHBoxLayout()
        self.new_screenshot_button = QPushButton("New Screenshot")
        self.new_screenshot_button.clicked.connect(self.new_screenshot)
        buttons_layout.addWidget(self.new_screenshot_button)
        save_screenshot_button = QPushButton("Save Screenshot")
        save_screenshot_button.clicked.connect(self.save_screenshot)
        buttons_layout.addWidget(save_screenshot_button)
        quit_screenshot_button = QPushButton("Quit")
        quit_screenshot_button.setShortcut(Qt.CTRL | Qt.Key_Q)
        quit_screenshot_button.clicked.connect(self.close)
        buttons_layout.addWidget(quit_screenshot_button)
        buttons_layout.addStretch()
        main_layout.addLayout(buttons_layout)

        self.shoot_screen()
        self.delay_spinbox.setValue(5)

        self.setWindowTitle("Min-Screen")
        self.setWindowFlag(Qt.FramelessWindowHint,False)
        self.resize(300, 200)

    def resizeEvent(self, event):
        scaled_size = self.original_pixmap.size()
        scaled_size.scale(self.screenshot_label.size(), Qt.KeepAspectRatio)
        if scaled_size != self.screenshot_label.pixmap().size():
            self.update_screenshot_label()

    @Slot()
    def new_screenshot(self):
        if self.hide_this_window_checkbox.isChecked():
            self.hide()
        self.new_screenshot_button.setDisabled(True)

        QTimer.singleShot(self.delay_spinbox.value() * 1000, self.shoot_screen)

    @Slot()
    def save_screenshot(self):
        fmt = "png"  # In order to avoid shadowing built-in format
        initial_path = QStandardPaths.writableLocation(QStandardPaths.PicturesLocation)
        if not initial_path:
            initial_path = QDir.currentPath()
        initial_path += f"/untitled.{fmt}"

        fileDialog = QFileDialog(self, "Save As", initial_path)
        fileDialog.setAcceptMode(QFileDialog.AcceptSave)
        fileDialog.setFileMode(QFileDialog.AnyFile)
        fileDialog.setDirectory(initial_path)
        mime_types = []

        for bf in QImageWriter.supportedMimeTypes():
            mime_types.append(bf.data().decode("utf8"))
        fileDialog.setMimeTypeFilters(mime_types)
        fileDialog.selectMimeTypeFilter("image/" + fmt)
        fileDialog.setDefaultSuffix(fmt)
        if fileDialog.exec() != QDialog.Accepted:
            return

        file_name = fileDialog.selectedFiles()[0]
        if not self.original_pixmap.save(file_name):
            path = QDir.toNativeSeparators(file_name)
            QMessageBox.warning(
                self,
                "Save Error",
                f"The image could not be saved to {path}.",
            )

    def shoot_screen(self):
        screen = QGuiApplication.primaryScreen()
        window = self.windowHandle()
        if window:
            screen = window.screen()
        if not screen:
            return

        if self.delay_spinbox.value() != 0:
            QApplication.beep()

        self.original_pixmap = screen.grabWindow(0)
        self.update_screenshot_label()

        self.new_screenshot_button.setDisabled(False)
        if self.hide_this_window_checkbox.isChecked():
            self.show()

    @Slot()
    def update_checkbox(self):
        if self.delay_spinbox.value() == 0:
            self.hide_this_window_checkbox.setDisabled(True)
            self.hide_this_window_checkbox.setChecked(False)
        else:
            self.hide_this_window_checkbox.setDisabled(False)

    def update_screenshot_label(self):
        self.screenshot_label.setPixmap(
            self.original_pixmap.scaled(
                self.screenshot_label.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
        )

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)        
        QSizeGrip(self.ui.size_grip)
        ########################################################################
        self.user_name=os.environ['USERNAME']
        self.lang='Fr-fr'
        self.np=1
        self.c=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.threadpool = QThreadPool()
        self.psutil_thread()
        self.processes()
        self.met()
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
        self.image_file_list = []
        self.image_file_types = ('jpg', 'jpeg', 'png', 'gif','esp','psd','tif','ai','indd','svg')
        self.image_can_seek = ('jpg', 'jpeg', 'png', 'gif','esp','psd','tif','ai','indd','svg')
        
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
        self.gif_l=False
        self.ax=False
        ################################################################
        self.indexes = self.ui.treeview.selectedIndexes()
        self.ui.tabWidget.setEnabled(True)
        self.ui.tabWidget.setTabBarAutoHide(True)
        self.ui.tabWidget.setAcceptDrops(True)
        self.ui.tabWidget.setMovable(True)
        self.ui.tabWidget.setDocumentMode(True)
        self.ui.tabWidget.setTabPosition(QTabWidget.TabPosition.South)
        ########################################################################
        loadJsonStyle(self, self.ui)
        self.show()
        self.set_bg()
        ########################################################################
        self.ui.bg_.clicked.connect(self.cbg)
        self.ui.pushButton_m.clicked.connect(self.gc)
        self.ui.left_menu_btn.clicked.connect(self.ent)
        self.ui.user_btn.clicked.connect(self.start_log)
        self.ui.pushButton_d.clicked.connect(self.capture)
        self.ui.pushButton_down.clicked.connect(self.downt)
        self.ui.right_menu_toggle_btn.clicked.connect(self.ch)
        self.ui.playlist_btn.clicked.connect(lambda: self.give_path(1))
        self.ui.tabWidget.tabCloseRequested.connect(self.close_current_tab_)
        self.ui.repeat_btn.clicked.connect(self.rep)
        self.ui.pushButton_12.clicked.connect(lambda: self.ui.notification.expandMenu())
        ##hide var ###################################################
        self.ui.age.hide()
        self.ui.pseudo.hide()
        self.ui.widget_7.hide()
        self.ui.list_music.hide()
        #self.ui.right_menu.hide()
        self.ui.left_menu_toggle.hide()
        self.ui.treeview.hideColumn(2)
        self.ui.treeview.hideColumn(3)
        self.ui.treeview_iv.hideColumn(1)
        self.ui.treeview_iv.hideColumn(2)
        self.ui.treeview_iv.hideColumn(3)
        #######################################################################
        self.ui.search_icon.clicked.connect(lambda: self.newtab(self.ui.page,"icons8-logo-google-94","Browser"))
        self.ui.map_icon.clicked.connect(lambda: self.newtab(self.ui.osm_page,"icons8-marqueur-de-plan-94","OSM"))
        self.ui.facebook_icon.clicked.connect(lambda: self.newtab(self.ui.f_page,"icons8-facebook-entouré-188","Facebook"))
        self.ui.youtube_icon.clicked.connect(lambda: self.newtab(self.ui.y_page,"icons8-lecture-de-youtube-100","YouTube"))
        self.ui.cpu_icon.clicked.connect(lambda: self.newtab(self.ui.cpu_page,"cpu","Processor"))
        self.ui.instagram_icon.clicked.connect(lambda: self.newtab(self.ui.i_page,"icons8-instagram-94","Instagram"))
        self.ui.dribbble_icon.clicked.connect(lambda: self.newtab(self.ui.i_page,"dribbble","Dribbble"))
        self.ui.battery_icon.clicked.connect(lambda: self.newtab(self.ui.battery_container,"icons8-batterie-pleine-94","Battery"))
        self.ui.ram_icon.clicked.connect(lambda: self.newtab(self.ui.ram_page,"SecurityAndMaintenance","Read Memory"))
        self.ui.thrending_icon.clicked.connect(lambda: self.newtab(self.ui.process_page,"trending-up","Process Data"))
        self.ui.movie_icon.clicked.connect(lambda: self.newtab(self.ui.iv_page,"icons8-ios-photos-94","Galerie"))
        self.ui.movie_icon.clicked.connect(self.open)
        self.ui.level_sld.valueChanged.connect(self.cs)
        self.ui.play_btn.clicked.connect(self.playAudioFile)
        self.ui.stop_btn.clicked.connect(self.stop_song)
        self.ui.jfb.clicked.connect(lambda: self.change_music_postion(-5))
        self.ui.jrb.clicked.connect(lambda: self.change_music_postion(+5))
        self.ui.right_btn.clicked.connect(lambda: self.play_file(True))
        #######################################################################
        self.ui.bg_.setIcon(self.style().standardIcon(QStyle.SP_DirIcon))
        self.ui.bg_2.setObjectName("icon")
        self.ui.bg_2.setIcon(self.style().standardIcon(QStyle.SP_DirHomeIcon))
        self.ui.bg_3.setObjectName("icon")
        self.ui.bg_3.setIcon(self.style().standardIcon(QStyle.SP_DirLinkIcon))
        self.ui.bg_4.setObjectName("icon")
        self.ui.bg_4.setIcon(self.style().standardIcon(QStyle.SP_DirOpenIcon))
        self.ui.bg_5.setObjectName("icon")
        self.ui.bg_5.setIcon(self.style().standardIcon(QStyle.SP_DriveCDIcon))
        self.ui.bg_6.setObjectName("icon")
        self.ui.bg_6.setIcon(self.style().standardIcon(QStyle.SP_DriveHDIcon))
        self.ui.bg_7.setIcon(QIcon(QPixmap(u"./images/icons8-fermer-94.png")))
        self.ui.play_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.ui.left_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekBackward))
        self.ui.right_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekForward))
        self.ui.stop_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.ui.jfb.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipBackward))
        self.ui.jfb.setObjectName("icon")
        self.ui.jrb.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipForward))
        self.ui.jrb.setObjectName("icon")
        #######################################################################
        self.ni = DragButton(self.ui.home)
        self.ni.setIcon(QIcon(QPixmap(u"./images/icons8-personne-homme-94.png")))
        self.ni.setIconSize(QSize(30, 30))
        self.ui.icon_list.addWidget(self.ni,0,0)

        self.ni21 = DragButton(self.ui.home)
        self.ni21.setIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))
        self.ni21.setIconSize(QSize(30, 30))
        self.ui.icon_list.addWidget(self.ni21,2,0)


        self.ni2 = DragButton(self.ui.home)
        self.ni2.setIcon(self.style().standardIcon(QStyle.SP_TrashIcon))
        self.ni2.setIconSize(QSize(30, 30))
        self.ui.icon_list.addWidget(self.ni2,1,0)

        self.ni.setContentsMargins(0, 0, 0, 0)


        self.ni23 = DragButton(self.ui.home)
        self.ni23.setIcon(self.style().standardIcon(QStyle.SP_DirIcon))
        self.ni23.setIconSize(QSize(30, 30))
        self.ui.icon_list.addWidget(self.ni23,3,0)

        #######################################################################
        self.ni23.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ni23.connect(self.ni23,QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), self.mi)


        self.ui.playlist_btn.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.playlist_btn.connect(self.ui.playlist_btn,QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), self.plmn)

        self.ui._scroll_area.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui._scroll_area.connect(self.ui._scroll_area,QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), self.sem)

        self.ui.cmdList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.cmdList.connect(self.ui.cmdList,QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), self.RC_CMDLIST)

        self.ui.img_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.img_list.connect(self.ui.img_list,QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), self.iv_menu)

        self.ui.home.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.home.connect(self.ui.home,QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), self.RC_DESK)

        self.ui.treeview.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.treeview.connect(self.ui.treeview,QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), self.RC_TV)

        self.ui.treeview_iv.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.treeview_iv.connect(self.ui.treeview_iv,QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), self.iv_trf)

        ########################################################################
        

        self.ui.img_list.setMovement(QListView.Free)
        self.ui.treeview_iv.doubleClicked.connect(self.select)
        self.ui.img_list.clicked.connect(lambda: self.load_ivfile(self.give_path(4)))
        self.ui.img_list.itemSelectionChanged.connect(lambda: self.load_ivfile(self.give_path(4)))
        self.ui.list_music.itemDoubleClicked.connect(lambda: self.play_file(song_ind=False,song=self.give_path(2)))

        ########################################################################
        self.ui.star_menu.setStyleSheet("color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));")

        self.ui.process_page.setStyleSheet(
u"*{\n"
"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"}\n"
"QLabel,QFrame,QLineEdit{\n"
"background-color: transparent;"
"border: None;"
"}\n"
"QLineEdit{\n"
"border: 1px solid cyan;"
"border-radius: 5px;"
"}\n"
"QCustomSlideMenu{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"}\n"
)

        
        self.ui.cpu_page.setStyleSheet(
u"*{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"}\n"
"QLabel,QFrame{\n"
"background-color: transparent;"
"border: None;"
"}\n"
                )

        self.ui.ram_page.setStyleSheet(
u"*{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"border: 1px solid cyan;"
"}\n"
"QLabel,QFrame{\n"
"background-color: transparent;"
"border: None;"
"}\n"
"QLabel{\n"
"border: 1px solid cyan;"
"border-radius: 5px;"
"}\n"
"#llr{\n"
"border: None;"
"border-color: None;"
"}\n"
                )

        self.ui.notifications_widget.setStyleSheet(
u"QCustomSlideMenu{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"}\n"
"QLabel,QFrame{\n"
"background-color: transparent;"
"border: None;"
"}\n"
            )


        self.ui.iv_page.setStyleSheet(
u"*{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"border: 1px solid cyan;"
"}\n"
"QLabel,QFrame{\n"
"background-color: transparent;"
"border: None;"
"}\n"
"QLabel{\n"
"border: 1px solid cyan;"
"border-radius: 5px;"
"}\n"
"#llr,#lp{\n"
"border: None;"
"border-color: None;"
"}\n"
                )

        
        self.ui.frame_16.setStyleSheet(u"color: white;")

        self.ui.battery_container.setStyleSheet(
u"*{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"}\n"
"QLabel,QFrame{\n"
"background-color: transparent;"
"border: None;"
"}\n"
)
        self.ui.home.setStyleSheet(
u"QToolTip{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"}\n")
########################################################################

        self.TimeGetUsers = QTimer(self)
        self.TimeGetUsers.timeout.connect(self.users)


        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        timer2 = QTimer(self)
        timer2.timeout.connect(lambda: self.batteri)
        timer2.start(100)


        cbg_timer = QTimer(self)
        cbg_timer.timeout.connect(self.cbg)
        cbg_timer.start(1000*60*5)



        timer3 = QTimer(self)
        timer3.timeout.connect(self.get_news)
        timer3.start(1000*60*60)
        self.get_news()


        self.play_song_timer = QTimer(self)
        self.play_song_timer.timeout.connect(self.auto_play_next)
        

        self.adt = QTimer(self)
        self.adt.timeout.connect(self.cpg)
        


        
        ########################################################################
        self.installEventFilter(self)


        # creating a tab widget
        self.tabs = QTabWidget(self.ui.page)

        # making document mode true
        self.tabs.setDocumentMode(True)

        # adding action when double clicked
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

        # adding action when tab is changed
        self.tabs.currentChanged.connect(self.current_tab_changed)

        # making tabs closeable
        self.tabs.setTabsClosable(True)

        # adding action when tab close is requested
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        

        # making tabs as central widget

        # creating a tool bar for navigation
        self.fb= QFrame(self.ui.page)
        self.h_tool_bar_l = QHBoxLayout(self.fb)

        # adding tool bar tot he main window
        self.ui.verticalLayout_8.addWidget(self.fb,0,Qt.AlignTop)
        self.ui.verticalLayout_8.addWidget(self.tabs)
        # creating back action
        back_btn = QPushButton()
        back_btn.setStatusTip("Back to previous page")
        back_btn.clicked.connect(lambda: self.tabs.currentWidget().back())
        back_btn.setObjectName('icon2')
        back_btn.setIcon(QIcon(QPixmap(u":/icons/icons/arrow-left-circle.svg")))
        self.h_tool_bar_l.addWidget(back_btn)

        # similarly adding next button
        next_btn = QPushButton()
        next_btn.setObjectName('icon2')
        next_btn.setIcon(QIcon(QPixmap(u":/icons/icons/arrow-right-circle.svg")))
        next_btn.setStatusTip("Forward to next page")
        next_btn.clicked.connect(lambda: self.tabs.currentWidget().forward())
        self.h_tool_bar_l.addWidget(next_btn)

        # similarly adding reload button
        reload_btn = QPushButton()
        reload_btn.setStatusTip("Reload page")
        reload_btn.clicked.connect(lambda: self.tabs.currentWidget().reload())
        self.h_tool_bar_l.addWidget(reload_btn)
        reload_btn.setObjectName('icon2')
        reload_btn.setIcon(QIcon(QPixmap(u":/icons/icons/refresh-cw.svg")))

        # creating home action
        home_btn = QPushButton()
        home_btn.setStatusTip("Go To home")
        home_btn.setObjectName('icon2')
        home_btn.setIcon(QIcon(QPixmap(u":/icons/icons/home.svg")))

        # adding action to home button
        home_btn.clicked.connect(self.navigate_home)
        self.h_tool_bar_l.addWidget(home_btn)

        # creating a line edit widget for URL
        self.urlbar = QLineEdit()
        self.urlbar.setClearButtonEnabled(True)
        self.urlbar.setStyleSheet("height: 25px;")

        # adding action to line edit when return key is pressed
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        # adding line edit to tool bar
        self.h_tool_bar_l.addWidget(self.urlbar)

        # similarly adding stop action
        stop_btn = QPushButton()
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.clicked.connect(lambda: self.tabs.currentWidget().stop())
        self.h_tool_bar_l.addWidget(stop_btn)
        stop_btn.setObjectName('icon2')
        stop_btn.setIcon(QIcon(QPixmap(u":/icons/icons/x-circle.svg")))

        # creating first tab
        self.add_new_tab(QUrl('http://www.google.com'), 'Homepage')

        self.change_style()
        self.rv = False

#================================================================Video==========================================================
#================================================================================================================================
#================================================================================================================================

    def capture(self):
        self.screenshot = Screenshot()
        
        self.screenshot.move(self.screenshot.screen().availableGeometry().topLeft() + QPoint(20, 20))
        self.screenshot.show()



    def add_ivfile(self,filename):
        if filename.rpartition(".")[2].lower() not in self.image_file_types:
            if os.path.isdir(os.path.abspath(filename)):
                try:
                    self.tr[filename] = threading.Thread(target = lambda: self.iv_list(os.path.abspath(filename)))
                    self.tr[filename].start()
                except Exception as e:
                    return False
        elif os.path.exists(filename):
            self.image_file_list.append(filename)
            self.cind_iv +=1
            self.ui.img_list.addItem(str(str(self.cind_iv)+" > ")+str(filename.rpartition("\\")[2]))
        elif os.path.exists(os.path.join(self.main_dir, filename)):
            self.image_file_list.append(os.path.join(self.main_dir, filename))
            self.cind_iv +=1
            self.ui.img_list.addItem(str(str(self.cind_iv)+" > ")+str(filename.rpartition("\\")[2]))
        elif os.path.exists(os.path.join(self.data_dir, filename)):
            self.image_file_list.append(os.path.join(self.data_dir, filename))
            self.cind_iv +=1
            self.ui.img_list.addItem(str(str(self.cind_iv)+" > ")+str(filename.rpartition("\\")[2]))
        else:
            if os.path.isdir(os.path.abspath(filename)):
                try:
                    self.tr[filename+'_'] = threading.Thread(target = lambda: self.iv_list(os.path.abspath(filename)))
                    self.tr[filename+'_'].start()
                except Exception as e:
                    return False

        if self.first_loard and len(self.image_file_list)>0:
            self.load_ivfile(self.image_file_list[-1])
            self.first_loard = False
        elif self.ui.lp.isHidden():
            self.ui.lp.setText(f"Total Images Files ({self.cind_iv})")
            self.ui.lp.show()
            self.rv = True
        else:
            if self.rv:
                self.ui.lp.setText(f"Total Images Files ({self.cind_iv})")




    def load_ivfile(self,filename=None):

        if filename != None:
            try:
                if filename.endswith('.gif'):
                    self.gif_content = QMovie(filename)
                    self.ui.current_view.setMovie(self.gif_content)
                    self.gif_content.start()
                    self.gif_l = True
                else:
                    self.ui.current_view.setPixmap(QPixmap.fromImage(filename))
                    if self.gif_l:
                        self.gif_content.stop()
                        self.gif_l = False
                self._fit_to_window()
            except:
                self.image_file_list.remove(filename)

            if filename.rpartition(".")[2].lower() in self.image_can_seek:
                self.ui.img_list.setFocus()
            else:
                print("file does not support seeking")




    def iv_list(self,_path=None):
        if _path is None:
            if os.path.isdir(self.give_path(3)):
                files = os.listdir(self.give_path(3))
                for item in files:
                    if f'{self.give_path(3)}\\{item}' not in self.image_file_list:
                        self.add_ivfile(f'{self.give_path(3)}\\{item}')
            else:
                if _path not in self.image_file_list:
                    self.add_ivfile(_path)
        else:
            if os.path.isdir(_path):
                files = os.listdir(_path)
                for item in files:
                    if f'{_path}\\{item}' not in self.image_file_list:
                        self.add_ivfile(f'{_path}\\{item}')
            else:
                if _path not in self.image_file_list:
                    self.add_ivfile(_path)



    def load_iv0(self,_path=None):
        self.first_loard = True
        self.ui.lp.show()
        self.cls_f()
        if True:
            self.last_ivlen = len(self.image_file_list)
            if _path is None:
                print('>none')
                if os.path.isdir(self.give_path(3)):
                    files = os.listdir(self.give_path(3))
                    print(files)
                    for item in files:
                        if f'{self.give_path(3)}\\{item}' not in self.image_file_list:
                            filename=f'{self.give_path(3)}\\{item}'
                            print(filename)

                            if os.path.exists(filename) and (filename.rpartition(".")[2].lower() in self.image_can_seek):
                                self.image_file_list.append(filename)
                                self.cind_iv +=1
                                self.ui.img_list.addItem(str(str(self.cind_iv)+" > ")+str(filename.rpartition("\\")[2]))
                            elif os.path.exists(os.path.join(self.main_dir, filename)) and (filename.rpartition(".")[2].lower() in self.image_can_seek):
                                self.image_file_list.append(os.path.join(self.main_dir, filename))
                                self.cind_iv +=1
                                self.ui.img_list.addItem(str(str(self.cind_iv)+" > ")+str(filename.rpartition("\\")[2]))
                            elif os.path.exists(os.path.join(self.data_dir, filename)) and (filename.rpartition(".")[2].lower() in self.image_can_seek):
                                self.image_file_list.append(os.path.join(self.data_dir, filename))
                                self.cind_iv +=1
                                self.ui.img_list.addItem(str(str(self.cind_iv)+" > ")+str(filename.rpartition("\\")[2]))
                            else:
                                pass
            else:
                print(_path+" is not none")
                _path = str(_path)
                if os.path.isdir(_path):
                    files = os.listdir(_path)
                    for item in files:
                        if f'{_path}\\{item}' not in self.image_file_list:
                            filename=f'{_path}\\{item}'
                            if os.path.exists(filename) and (filename.rpartition(".")[2].lower() in self.image_can_seek):
                                self.image_file_list.append(filename)
                                self.cind_iv +=1
                                self.ui.img_list.addItem(str(str(self.cind_iv)+" > ")+str(filename.rpartition("\\")[2]))
                            elif os.path.exists(os.path.join(self.main_dir, filename)) and (filename.rpartition(".")[2].lower() in self.image_can_seek):
                                self.image_file_list.append(os.path.join(self.main_dir, filename))
                                self.cind_iv +=1
                                self.ui.img_list.addItem(str(str(self.cind_iv)+" > ")+str(filename.rpartition("\\")[2]))
                            elif os.path.exists(os.path.join(self.data_dir, filename)) and (filename.rpartition(".")[2].lower() in self.image_can_seek):
                                self.image_file_list.append(os.path.join(self.data_dir, filename))
                                self.cind_iv +=1
                                self.ui.img_list.addItem(str(str(self.cind_iv)+" > ")+str(filename.rpartition("\\")[2]))
                            else:
                                pass




            if len(self.image_file_list) != self.last_ivlen:
                playsound("./Themes/Halo 4 He/windows ding.wav",block=False)
            else:
                self.ui.img_list.addItem("No Images Detect!")
            self.ui.lp.hide()  




    def load_iv(self,_path=None):
        self.first_loard = True
        self.cls_f()
        self.ui.lp.show() 

        try:

            if self.give_path(3):
                self.last_ivlen = len(self.image_file_list)
                if _path is None:
                    try:
                        if os.path.isdir(self.give_path(3)):
                            files = os.listdir(self.give_path(3))
                            for item in files:
                                if f'{self.give_path(3)}\\{item}' not in self.image_file_list:
                                    self.add_ivfile(f'{self.give_path(3)}\\{item}')
                        else:
                            if _path not in self.image_file_list:
                                self.add_ivfile(_path)

                    except Exception as e:
                        pass
                else:
                    if os.path.isdir(_path):
                        files = os.listdir(_path)
                        for item in files:
                            if f'{_path}\\{item}' not in self.image_file_list:
                                self.add_ivfile(f'{_path}\\{item}')
                    else:
                        if _path not in self.image_file_list:
                            self.add_ivfile(_path)

        except Exception as e:
            pass
        finally:
            if len(self.image_file_list) != self.last_ivlen:
                playsound("./Themes/Halo 4 He/windows ding.wav",block=False)
                self.ui.lp.setObjectName("lp")
                self.ui.lp.hide()

    @Slot()
    def _zoom_in(self):
        self._scale_image(1.25)

    @Slot()
    def _zoom_out(self):
        self._scale_image(0.8)

    @Slot()
    def _normal_size(self):
        self.ui.current_view.adjustSize()
        self._scale_factor = 1.0


    def _scale_image(self, factor):
        self._scale_factor *= factor
        new_size = self._scale_factor * self.ui.current_view.pixmap().size()
        self.ui.current_view.resize(new_size)

        self._adjust_scrollbar(self.ui._scroll_area.horizontalScrollBar(), factor)
        self._adjust_scrollbar(self.ui._scroll_area.verticalScrollBar(), factor)

    def _adjust_scrollbar(self, scrollBar, factor):
        pos = int(factor * scrollBar.value()
                  + ((factor - 1) * scrollBar.pageStep() / 2))
        scrollBar.setValue(pos)













    def init_widget(w, name):
        """Init a widget for the gallery, give it a tooltip showing the
           class name"""
        w.setObjectName(name)
        w.setToolTip(class_name(w))

    def change_style(self, style_name="fusion"):
        QApplication.setStyle(QStyleFactory.create(style_name))

    def embed_into_hbox_layout(w, margin=5):
        """Embed a widget into a layout to give it a frame"""
        result = QWidget()
        layout = QHBoxLayout(result)
        layout.setContentsMargins(margin, margin, margin, margin)
        layout.addWidget(w)
        return result


    def stop_song(self):
        self.player.stop()
        self.stop = True


    def ent(self):
        if self.windowToast:
            self.ui.left_menu_toggle.setStyleSheet("color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));")
            self.ui.left_menu_toggle.show()
            self.ui.left_lineEdit.setStyleSheet(u"background-color: white;color: black;height: 40px;")
            self.ui.left_menu_btn.setIconSize(QSize(22, 22))
            self.ui.left_lineEdit.setMinimumSize(QSize(250, 5))
            self.ui.left_lineEdit.setFocus()
            self.windowToast = False
        else:
            self.ui.left_menu_toggle.hide()
            self.ui.left_lineEdit.setStyleSheet(u"background-color: transparent;color: white;border-bottom: none")
            self.ui.left_menu_btn.setIconSize(QSize(18, 18))
            self.windowToast = True



    def cpg(self):
        self.ui.sp.rpb_setValue(int(self.player.get_pos() / 100))






    def cs(self):
        self.volume=self.ui.level_sld.value()/100
        print(self.volume)
        self.player.set_volume(self.volume)


    def playAudioFile(self):
        if self.pause:
            self.player.unpause()
            self.stop = False
            self.ui.play_btn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause)
            )
            self.pause=False
        else:
            self.player.pause()
            self.ui.play_btn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)
            )
            self.pause=True







    def add_file(self,filename):

        if filename.rpartition(".")[2].lower() not in self.music_file_types:
            if os.path.isdir(os.path.abspath(filename)):
                try:
                    self.tr[filename] = threading.Thread(target = lambda: self.uplaylist(os.path.abspath(filename)))
                    self.tr[filename].start()
                except Exception as e:
                    return False
        elif os.path.exists(filename):
            self.music_file_list.append(filename)
            self.cind +=1
            self.ui.list_music.addItem(str(str(self.cind)+" > ")+str(filename.rpartition("\\")[2]))
        elif os.path.exists(os.path.join(self.main_dir, filename)):
            self.music_file_list.append(os.path.join(self.main_dir, filename))
            self.cind +=1
            self.ui.list_music.addItem(str(str(self.cind)+" > ")+str(filename.rpartition("\\")[2]))
        elif os.path.exists(os.path.join(self.data_dir, filename)):
            self.music_file_list.append(os.path.join(self.data_dir, filename))
            self.cind +=1
            self.ui.list_music.addItem(str(str(self.cind)+" > ")+str(filename.rpartition("\\")[2]))
        else:
            if os.path.isdir(os.path.abspath(filename)):
                try:
                    self.tr[filename+'_'] = threading.Thread(target = lambda: self.uplaylist(os.path.abspath(filename)))
                    self.tr[filename+'_'].start()
                except Exception as e:
                    return False
        print("{} invalid file".format(filename))
        self.ui.titre_playlist.setText(f"PlayList::({len(self.music_file_list)} Songs) ")
        return True



    def rep(self):
        if self.ax:
            self.ax = False
        else:
            self.ax = True



    def auto_play_next(self):
        if self.player.get_pos() not in self.prog:
            self.prog.append(self.player.get_pos())
        else:
            self.prog.clear()
            self.ui.play_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.ui.mv2.stop()
            if self.stop is False:
                if self.ax:
                    self.player.rewind()
                else:
                    self.play_file(True)
                self.ui.mv2.start()


    def play_file(self,song_ind=False,song=None):

        for filename in self.music_file_list:
            if self.player.get_busy() and ( (song_ind is False) and song is None ):
                pass
            else:
                if song_ind:
                    self.song_nbr+=1
                    if self.song_nbr >= len(self.music_file_list):
                        self.song_nbr=0
                    filename = self.music_file_list[self.song_nbr]

                elif song != None:
                    for i in range(len(self.music_file_list)):
                        if song is self.music_file_list[i]:
                            self.song_nbr=i

                    self.player.stop()
                    filename = song
                else:
                    filename = self.music_file_list[self.song_nbr]
                
                try:
                    self.player.load(filename)
                except:
                    self.music_file_list.remove(filename)
                    print(self.music_file_list)

                if filename.rpartition(".")[2].lower() in self.music_can_seek:
                    print(f"{self.song_nbr} ::{filename}")
                    self.ui.list_music.setFocus()
                    self.ui.list_music.setCurrentRow(self.song_nbr)
                    self.player.play(fade_ms=4000)
                    self.player.set_volume(self.volume)
                    self.ui.pgf.show()
                    self.adt.start(1000)
                    self.ui.play_btn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
                    self.starting_pos = 0
                else:
                    speak("file does not support seeking")
                    self.starting_pos = -1
                self.player.set_endevent(self.MUSIC_DONE)

            if self.player.get_busy() and (len(self.prog)==0):
                self.play_song_timer.start(2000)
                self.ui.lp2.show()
                self.ui.mv2.start()
            else:
                self.ui.mv2.start()
            break




    def uplaylist(self,_path=None):
        if _path is None:
            if os.path.isdir(self.give_path()):
                files = os.listdir(self.give_path())
                print(f"md========{self.main_dir}=============")
                print(f"dtd========{self.data_dir}==========")
                print(files)
                print("=================================")
                for item in files:
                    if f'{self.give_path()}\\{item}' not in self.music_file_list:
                        self.add_file(f'{self.give_path()}\\{item}')
            else:
                if _path not in self.music_file_list:
                    self.add_file(_path)
        else:
            if os.path.isdir(_path):
                files = os.listdir(_path)
                for item in files:
                    if f'{_path}\\{item}' not in self.music_file_list:
                        self.add_file(f'{_path}\\{item}')
            else:
                if _path not in self.music_file_list:
                    self.add_file(_path)








    def playlist(self,_path=None,ss=None):
        self.last_len = len(self.music_file_list)
        playsound("./Themes/Halo 4 He/windows fax sent.wav",block=False)
        if _path is None:
            if os.path.isdir(self.give_path()):
                files = os.listdir(self.give_path())
                for item in files:
                    if f'{self.give_path()}\\{item}' not in self.music_file_list:
                        self.add_file(f'{self.give_path()}\\{item}')
            else:
                if _path not in self.music_file_list:
                    self.add_file(_path)
        else:
            if os.path.isdir(_path):
                files = os.listdir(_path)
                for item in files:
                    if f'{_path}\\{item}' not in self.music_file_list:
                        self.add_file(f'{_path}\\{item}')
            else:
                if _path not in self.music_file_list:
                    self.add_file(_path)

            if ss != None:
                self.play_file(song=ss)

        if len(self.music_file_list) != self.last_len:
            self.speak(f"Your playlist has been update at {len(self.music_file_list)} musics")

        if len(self.music_file_list) >0 and self.ui.list_music.isHidden():
            self.ui.list_music.show()
            self.play_file()
        self.ui.list_music.show()







    def change_music_postion(self,amount):
        """
        Changes current playback postition by amount seconds.
        This only works with OGG and MP3 files.
        music.get_pos() returns how many milliseconds the song has played, not
        the current postion in the file. We must track the starting postion
        ourselves. music.set_pos() will set the position in seconds.
        """
        if self.starting_pos >= 0:  # will be -1 unless play_file() was OGG or MP3
            played_for = self.player.get_pos() / 1000.0
            old_pos = self.starting_pos + played_for
            self.starting_pos = old_pos + amount
            self.player.play(start=self.starting_pos)
            print("jumped from {} to {}".format(old_pos, self.starting_pos))




























    def close_current_tab_(self, i):

        # if there is only one tab
        if self.ui.tabWidget.count() < 2:
            # do nothing
            return
        else:
            playsound("./Themes/Halo 4 He/halo4_windows_trash_03.wav",block=False)
            self.ui.tabWidget.removeTab(i)
        


    # method for adding new tab
    def add_new_tab(self, qurl = None, label ="Blank"):

        # if url is blank
        if qurl is None:
            # creating a google url
            qurl = QUrl('http://www.google.com')

        # creating a QWebEngineView object
        browser = QWebEngineView()

        # setting url to browser
        browser.setUrl(qurl)

        # setting tab index
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        # adding action to the browser when url is changed
        # update the url
        browser.urlChanged.connect(lambda qurl, browser = browser:
                                self.update_urlbar(qurl, browser))

        # adding action to the browser when loading is finished
        # set the tab title
        browser.loadFinished.connect(lambda _, i = i, browser = browser:
                                    self.tabs.setTabText(i, browser.page().title()))

    # when double clicked is pressed on tabs
    def tab_open_doubleclick(self, i):

        # checking index i.e
        # No tab under the click
        if i == -1:
            # creating a new tab
            self.add_new_tab()

    # when tab is changed
    def current_tab_changed(self, i):

        # get the curl
        qurl = self.tabs.currentWidget().url()

        # update the url
        self.update_urlbar(qurl, self.tabs.currentWidget())

        # update the title
        self.update_title(self.tabs.currentWidget())

    # when tab is closed
    def close_current_tab(self, i):

        # if there is only one tab
        if self.tabs.count() < 2:
            # do nothing
            return

        # else remove the tab
        self.tabs.removeTab(i)

    # method for updating the title
    def update_title(self, browser):

        # if signal is not from the current tab
        if browser != self.tabs.currentWidget():
            # do nothing
            return

        # get the page title
        title = self.tabs.currentWidget().page().title()

    # action to go to home
    def navigate_home(self):

        # go to google
        self.tabs.currentWidget().setUrl(QUrl("http://www.google.com"))

    # method for navigate to url
    def navigate_to_url(self):

        # get the line edit text
        # convert it to QUrl object
        q = QUrl(self.urlbar.text())

        # if scheme is blank
        if q.scheme() == "":
            # set scheme
            q.setScheme("http")

        # set the url
        self.tabs.currentWidget().setUrl(q)

    # method to update the url
    def update_urlbar(self, q, browser = None):

        # If this signal is not from the current tab, ignore
        if browser != self.tabs.currentWidget():

            return

        # set text to the url bar
        self.urlbar.setText(q.toString())

        # set cursor position
        self.urlbar.setCursorPosition(0)






    def mi(self, QPos): 
        self.menu_icon= QMenu()
        self.menu_icon.setStyleSheet("color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));")
        
        nf = self.menu_icon.addAction(QPixmap(u":/icons/icons/folder-plus.svg"),"Open Folder")
        self.connect(nf, SIGNAL("triggered()"), self.nf)

        NF = self.menu_icon.addAction(QPixmap(u":/icons/icons/file-plus.svg"),"New File")
        self.connect(NF, SIGNAL("triggered()"), self.NF)

        NF4 = self.menu_icon.addAction(QPixmap(u":/icons/icons/tool.svg"),"Add to Playlist..")
        self.connect(NF4, SIGNAL("triggered()"), self.playlist)

        menu_item2 = self.menu_icon.addAction(QPixmap(u":/icons/icons/copy.svg"),"Copy")
        self.connect(menu_item2, SIGNAL("triggered()"), self.ROW_ITEM_TV)

        nf2 = self.menu_icon.addAction(QPixmap(u":/icons/icons/droplet.svg"),"Cut")
        self.connect(nf2, SIGNAL("triggered()"), self.nf)

        NF2 = self.menu_icon.addAction(QPixmap(u":/icons/icons/paperclip.svg"),"Paste")
        self.connect(NF2, SIGNAL("triggered()"), self.NF)

        nf3 = self.menu_icon.addAction(QPixmap(u":/icons/icons/delete.svg"),"Delete")
        self.connect(nf3, SIGNAL("triggered()"), self.nf)

        nf4 = self.menu_icon.addAction(QPixmap(u":/icons/icons/edit.svg"),"Rename")
        self.connect(nf4, SIGNAL("triggered()"), self.RENAME_TV)

        nf5 = self.menu_icon.addAction(QPixmap(u":/icons/icons/copy.svg"),"Copy Path")
        self.connect(nf5, SIGNAL("triggered()"), self.give_path())

        go_to3 = self.menu_icon.addAction(QPixmap(u":/icons/icons/eye-off.svg"),"Mask")
        self.connect(go_to3, SIGNAL("triggered()"), self.GO_TO)

        nf5 = self.menu_icon.addAction(QPixmap(u":/icons/icons/navigation.svg"),"View in Explorer")
        self.connect(nf5, SIGNAL("triggered()"), self.nf)

        go_to6 = self.menu_icon.addAction(QPixmap(u":/icons/icons/terminal.svg"),"Open in Command Promt")
        self.connect(go_to6, SIGNAL("triggered()"), self.GO_TO)


        parentPosition = self.ni23.mapToGlobal(QPoint(0, 0))        
        self.menu_icon.move(parentPosition + QPos)
        self.menu_icon.show() 


    def pop(self):
        self.popup = QDialog(self.ui.home)
        self.popup.setWindowTitle("Mino::Themes")
        self.popup.setModal(True)
        self.popup.setText('test')


    def tbg(self):
        items = tuple(self.themes_names)
        item, ok = QInputDialog.getItem(self.ui.centralwidget, "Mino::Themes",
                "Select theme:", items, 0, False)
        if ok and item:
            self.cbg(item)


    def RC_DESK(self, QPos): 
        self.ML_DESK= QMenu()
        self.ML_DESK.setStyleSheet("color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));")
        
        nf = self.ML_DESK.addAction(QPixmap(u":/icons/icons/folder-plus.svg"),"New Folder")
        self.connect(nf, SIGNAL("triggered()"), self.nf)

        NF = self.ML_DESK.addAction(QPixmap(u":/icons/icons/file-plus.svg"),"New File")
        self.connect(NF, SIGNAL("triggered()"), self.NF)
        
        nbg = self.ML_DESK.addAction(QPixmap(u":/icons/icons/arrow-right-circle.svg"),"Another background")
        self.connect(nbg, SIGNAL("triggered()"), self.cbg)

        ab = self.ML_DESK.addAction(QPixmap(u"./images/@BackgroundAccessToastIcon.png"),"Themes background")
        self.connect(ab, SIGNAL("triggered()"), self.tbg)

        parentPosition = self.ui.home.mapToGlobal(QPoint(0, 0))        
        self.ML_DESK.move(parentPosition + QPos)
        self.ML_DESK.show() 






    def plmn(self, QPos): 
        self.plmn_f= QMenu()
        self.plmn_f.setStyleSheet("color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));")
        
        nf2 = self.plmn_f.addAction(QPixmap(u":/icons/icons/folder-plus.svg"),"Open Folder")
        self.connect(nf2, SIGNAL("triggered()"), self.nf)

        NF2 = self.plmn_f.addAction(QPixmap(u":/icons/icons/file-plus.svg"),"Open File")
        self.connect(NF2, SIGNAL("triggered()"), self.NF)

        parentPosition = self.ui.playlist_btn.mapToGlobal(QPoint(0, 0))        
        self.plmn_f.move(parentPosition + QPos)
        self.plmn_f.show() 






    def nf(self):
        item = QFileDialog.getExistingDirectory(None, "Select Directory")
        if item != None:
            self.playlist(str(item.replace('/',"\\")))
        
    def NF(self):
        item = QFileDialog.getOpenFileName(None, "Select File","","Fichiers multimédias (*.mp3 *.ogg *.mid *.mod *.it *.xm *.wav *.wav*. *.3gp*. *.m3u*. *.wma *.au);;All Files (*)")

        if item != None:
            self.playlist(str(item[0].replace('/',"\\")))

    def RC_CMDLIST(self, QPos): 
        self.listMenu= QMenu()
        self.listMenu.setStyleSheet("color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));")
        
        menu_item = self.listMenu.addAction("Remove Item")
        self.connect(menu_item, SIGNAL("triggered()"), self.ROW_ITEM)

        go_to = self.listMenu.addAction("Go To")
        self.connect(go_to, SIGNAL("triggered()"), self.GO_TO)


        parentPosition = self.ui.cmdList.mapToGlobal(QPoint(0, 0))        
        self.listMenu.move(parentPosition + QPos)
        self.listMenu.show() 

    def ROW_ITEM(self):
        currentItemName=str(self.ui.cmdList.currentItem())
        print(currentItemName)




    def iv_trf(self, QPos): 
        self.iv_tr= QMenu()
        self.iv_tr.setStyleSheet("color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));")
        self._exit_act = self.iv_tr.addAction("&Fast Scan")
        self._exit_act.triggered.connect(lambda: threading.Thread(target=self.select).start())
        self._exit_act.setShortcut("Ctrl+Q")

        self.fs = self.iv_tr.addAction("&Full Scan")
        self.fs.triggered.connect(lambda: threading.Thread(target= lambda: self.select(1)).start())
        self.fs.setShortcut("Ctrl+Q")

        menu_item3 = self.iv_tr.addAction(QPixmap(u":/icons/icons/eye.svg"),"Open")
        self.connect(menu_item3, SIGNAL("triggered()"), lambda: self.Open_TV(3))

        NF4 = self.iv_tr.addAction(QPixmap(u":/icons/icons/tool.svg"),"Add to Playlist..")
        self.connect(NF4, SIGNAL("triggered()"), lambda: self.playlist(self.give_path(3)))


        s = self.iv_tr.addAction(QPixmap(u":/icons/icons/tool.svg"),"collapsed Width")
        self.connect(s, SIGNAL("triggered()"), lambda: self.ui.treeview_iv.setMinimumWidth(150))

        s2 = self.iv_tr.addAction(QPixmap(u":/icons/icons/tool.svg"),"expanded Width")
        self.connect(s2, SIGNAL("triggered()"), lambda: self.ui.treeview_iv.setMinimumWidth(400))

        parentPosition = self.ui.treeview_iv.mapToGlobal(QPoint(0, 0))        
        self.iv_tr.move(parentPosition + QPos)
        self.iv_tr.show() 


    def cls_f(self):
        self.ui.img_list.clear()
        self.image_file_list.clear()
        self.cind_iv = 0

    def rmt(self):
        self.ui.img_list.removeItemWidget(self.ui.img_list.currentItem())


    def iv_menu(self, QPos):
        self.iv_main_menu= QMenu()
        self.iv_main_menu.setStyleSheet("color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));")
        
        self.cls = self.iv_main_menu.addAction("&Clear")
        self.cls.triggered.connect(self.cls_f)

        self.rmv_it = self.iv_main_menu.addAction("&Remove")
        self.rmv_it.triggered.connect(self.rmt)

        self.about_act = self.iv_main_menu.addAction("&About")
        self.about_act.triggered.connect(self._about)

        parentPosition = self.ui.img_list.mapToGlobal(QPoint(0, 0))        
        self.iv_main_menu.move(parentPosition + QPos)
        self.iv_main_menu.show() 



    def fscreem(self):
        self.ui.p_left_frame_for_iv.hide()
        self._fit_to_window()


    def nofscreem(self):
        self.ui.p_left_frame_for_iv.show()



    def sem(self, QPos): 
        self.sem_= QMenu()
        self.sem_.setStyleSheet("color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));")
        self.a1 = self.sem_.addAction("&Open...")
        self.a1.triggered.connect(self._open)
        self.a1.setShortcut(QKeySequence.Open)

        self.a2 = self.sem_.addAction("&Save As...")
        self.a2.triggered.connect(self._save_as)

        self.a3 = self.sem_.addAction("&Print...")
        self.a3.triggered.connect(self._print_)
        self.a3.setShortcut(QKeySequence.Print)

        self.a4 = self.sem_.addAction("&Copy")
        self.a4.triggered.connect(self._copy)
        self.a4.setShortcut(QKeySequence.Copy)

        self.a5 = self.sem_.addAction("&Paste")
        self.a5.triggered.connect(self._paste)
        self.a5.setShortcut(QKeySequence.Paste)

        s3 = self.sem_.addAction(QPixmap(u":/icons/icons/tool.svg"),"Normal Screen")
        self.connect(s3, SIGNAL("triggered()"), self.nofscreem )

        s4 = self.sem_.addAction(QPixmap(u":/icons/icons/tool.svg"),"FullScreen")
        self.connect(s4, SIGNAL("triggered()"), self.fscreem ) 

        self._newbg2 = self.sem_.addAction("&Set as background")
        bg = self.give_path(4)

        if bg is not None:
            bg = bg.replace('/',"\\")
            bg = bg.replace('\\\\',"\\")
            bg = bg.replace('\\','/')

        self._newbg2.triggered.connect(lambda: threading.Thread(target=lambda: self.ui.m_m.setStyleSheet(f"background-image: url({str(bg)});")).start())
        self._newbg2.setShortcut("Ctrl+G")

        self.a7 = self.sem_.addAction("Zoom &In (25%)")
        self.a7.setShortcut(QKeySequence.ZoomIn)
        self.a7.triggered.connect(self._zoom_in)

        self.a8 = self.sem_.addAction("Zoom &Out (25%)")
        self.a8.triggered.connect(self._zoom_out)
        self.a8.setShortcut(QKeySequence.ZoomOut)

        self.a9 = self.sem_.addAction("&Normal Size")
        self.a9.triggered.connect(self._normal_size)
        self.a9.setShortcut("Ctrl+S")

        parentPosition = self.ui._scroll_area.mapToGlobal(QPoint(0, 0))        
        self.sem_.move(parentPosition + QPos)
        self.sem_.show() 



    def _update_actions(self):
        pass


    def _initialize_image_filedialog(self, dialog, acceptMode):
        if self._first_file_dialog:
            self._first_file_dialog = False
            locations = QStandardPaths.standardLocations(QStandardPaths.PicturesLocation)
            directory = locations[-1] if locations else QDir.currentPath()
            dialog.setDirectory(directory)

        mime_types = [m.data().decode('utf-8') for m in QImageWriter.supportedMimeTypes()]
        mime_types.sort()

        dialog.setMimeTypeFilters(mime_types)
        dialog.selectMimeTypeFilter("image/jpeg")
        dialog.setAcceptMode(acceptMode)
        if acceptMode == QFileDialog.AcceptSave:
            dialog.setDefaultSuffix("jpg")




    def _save_file(self, fileName):
        self._image = self.give_path(4)
        writer = QImageWriter(fileName)

        native_filename = QDir.toNativeSeparators(fileName)
        if not writer.write(self._image):
            error = writer.errorString()
            message = f"Cannot write {native_filename}: {error}"
            QMessageBox.information(self, QGuiApplication.applicationDisplayName(),
                                    message)
            return False
        self.speak(f'Wrote "{native_filename}"')
        return True

    @Slot()
    def _open(self):
        dialog = QFileDialog(self, "Open File")
        self._initialize_image_filedialog(dialog, QFileDialog.AcceptOpen)
        while (dialog.exec() == QDialog.Accepted
               and not self.load_ivfile(dialog.selectedFiles()[0])):
            pass

    @Slot()
    def _save_as(self):
        dialog = QFileDialog(self, "Save File As")
        self._initialize_image_filedialog(dialog, QFileDialog.AcceptSave)
        while (dialog.exec() == QDialog.Accepted
               and not self._save_file(dialog.selectedFiles()[0])):
            pass

    @Slot()
    def _print_(self):
        printer = QPrinter()
        dialog = QPrintDialog(printer, self)
        if dialog.exec() == QDialog.Accepted:
            with QPainter(printer) as painter:
                pixmap = self.ui.current_view.pixmap()
                rect = painter.viewport()
                size = pixmap.size()
                size.scale(rect.size(), Qt.KeepAspectRatio)
                painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
                painter.setWindow(pixmap.rect())
                painter.drawPixmap(0, 0, pixmap)

    @Slot()
    def _copy(self):
        pass

    @Slot()
    def _paste(self):
        new_image = QGuiApplication.clipboard().image()
        if new_image.isNull():
            self.speak("No image in clipboard")
        else:
            self._set_image(new_image)
            self.setWindowFilePath('')








    def _fit_to_window(self):
        self.ui._scroll_area.setWidgetResizable(True)
        self._update_actions()

    @Slot()
    def _about(self):
        self.speak("MInView Images version 1.1")








    def RC_TV(self, QPos): 
        self.LM_TV= QMenu(self.ui.treeview)
        self.LM_TV.setStyleSheet("color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));")
        
        menu_item3 = self.LM_TV.addAction(QPixmap(u":/icons/icons/eye.svg"),"Open")
        self.connect(menu_item3, SIGNAL("triggered()"), self.Open_TV)

        NF4 = self.LM_TV.addAction(QPixmap(u":/icons/icons/tool.svg"),"Add to Playlist..")
        self.connect(NF4, SIGNAL("triggered()"), self.playlist)

        menu_item2 = self.LM_TV.addAction(QPixmap(u":/icons/icons/copy.svg"),"Copy")
        self.connect(menu_item2, SIGNAL("triggered()"), self.ROW_ITEM_TV)

        nf2 = self.LM_TV.addAction(QPixmap(u":/icons/icons/droplet.svg"),"Cut")
        self.connect(nf2, SIGNAL("triggered()"), self.nf)

        NF2 = self.LM_TV.addAction(QPixmap(u":/icons/icons/paperclip.svg"),"Paste")
        self.connect(NF2, SIGNAL("triggered()"), self.NF)

        nf3 = self.LM_TV.addAction(QPixmap(u":/icons/icons/delete.svg"),"Delete")
        self.connect(nf3, SIGNAL("triggered()"), self.nf)

        nf4 = self.LM_TV.addAction(QPixmap(u":/icons/icons/edit.svg"),"Rename")
        self.connect(nf4, SIGNAL("triggered()"), self.RENAME_TV)

        nf5 = self.LM_TV.addAction(QPixmap(u":/icons/icons/copy.svg"),"Copy Path")
        self.connect(nf5, SIGNAL("triggered()"), self.give_path)

        go_to3 = self.LM_TV.addAction(QPixmap(u":/icons/icons/eye-off.svg"),"Mask")
        self.connect(go_to3, SIGNAL("triggered()"), self.GO_TO)

        nf5 = self.LM_TV.addAction(QPixmap(u":/icons/icons/navigation.svg"),"View in Explorer")
        self.connect(nf5, SIGNAL("triggered()"), self.nf)

        go_to6 = self.LM_TV.addAction(QPixmap(u":/icons/icons/terminal.svg"),"Open in Command Promt")
        self.connect(go_to6, SIGNAL("triggered()"), self.GO_TO)

        parentPosition7 = self.ui.treeview.mapToGlobal(QPoint(0, 0))        
        self.LM_TV.move(parentPosition7 + QPos)
        self.LM_TV.show() 

    def ROW_ITEM_TV(self):
        for index in self.ui.treeview.selectedIndexes():
            item = self.ui.treemodel.filePath(index)
            item = str(item.replace('/',"\\"))
            command = f"start {item}"
            threading.Thread(target = lambda: subprocess.getoutput(command)).start()
            break


    def Open_TV(self,a=0):
        if a==0:
            for index in self.ui.treeview.selectedIndexes():
                item = self.ui.treemodel.filePath(index)

                ex = item.split('.')
                item = str(item.replace('/',"\\"))

                audio_ex = ["mp3", "ogg", "mid", "mod", "it", "xm", "wav", 'wav', '3gp', 'm3u','wma','au']

                if ex[len(ex)-1] in audio_ex:
                    print("ok")
                    self.playlist(item,item)
                else:
                    command = f"start {item}"
                    threading.Thread(target = lambda: subprocess.getoutput(command)).start()
                    break
        else:
            for index in self.ui.treeview_iv.selectedIndexes():
                item = self.ui.treemodel_iv.filePath(index)

                ex = item.split('.')
                item = str(item.replace('/',"\\"))

                audio_ex = ["mp3", "ogg", "mid", "mod", "it", "xm", "wav", 'wav', '3gp', 'm3u','wma','au']

                if ex[len(ex)-1] in audio_ex:
                    print("ok")
                    self.playlist(item,item)
                else:
                    command = f"start {item}"
                    threading.Thread(target = lambda: subprocess.getoutput(command)).start()
                    break


    def give_path(self,a=0):
        if a == 1:
            item = QFileDialog.getExistingDirectory(None, "Select Directory")
            self.playlist(str(item.replace('/',"\\")))
            
        elif a == 2:
            path = str((self.ui.list_music.selectedItems()[0]).text())
            path = path.rpartition(' > ')[2]
            for song in self.music_file_list:
                if song.rpartition(path)[1] is path:
                    return song
        elif a == 3:
            for index in self.ui.treeview_iv.selectedIndexes():
                item = self.ui.treemodel_iv.filePath(index)
                item = str(item.replace('/',"\\"))
                return str(item)

        elif a == 4:
            if len(self.ui.img_list.selectedItems())>0:
                path = str((self.ui.img_list.selectedItems()[0]).text())
                path = path.rpartition(' > ')[2]
                for img in self.image_file_list:
                    if img.rpartition(path)[1] is path:
                        return img
            else:
                return None
        else:
            for index in self.ui.treeview.selectedIndexes():
                item = self.ui.treemodel.filePath(index)
                print(item.replace('/',"\\"))
                return str(item.replace('/',"\\"))


    def RENAME_TV(self):
        for index in self.ui.treeview.selectedIndexes():
            item = self.ui.treemodel.filePath(index)
            item = str(item.replace('/',"\\"))
            threading.Thread(target = lambda: os.rename(item,str(self.ui.cmd.text())) ).start()
            break



    def select(self,a=0):
        if a==0:
            for index in self.ui.treeview_iv.selectedIndexes():
                item = self.ui.treemodel_iv.filePath(index)
                item = str(item.replace('/',"\\"))
                self.load_iv0(_path=item)
                pass
        else:
            for index in self.ui.treeview_iv.selectedIndexes():
                item = self.ui.treemodel_iv.filePath(index)
                item = str(item.replace('/',"\\"))
                self.load_iv(_path=item)
                pass

    def GO_TO(self):
        print(self.ui.cmdList.currentItem().text())

    def eventFilter(self, QObject, event):
        if event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.RightButton:

                if self.valid_log is None:
                    playsound("./Themes/Halo 4 He/windows ding.wav",block=False)

                print("Right button clicked")
                if self.valid_log is False:
                    if self.lineEdit_3.displayText() is not None:
                        self.login()
                        self.valid_log = None

            elif event.button() == Qt.LeftButton:
                if self.valid_log:
                    print('show')
                    self.ui.label_5.setPixmap(QPixmap(u"./images/icons8-utilisateur-94.png"))
                    self.lineEdit_3 = QLineEdit(self.ui.frame_16)
                    self.lineEdit_3.setEchoMode(QLineEdit.Password)
                    self.lineEdit_3.setClearButtonEnabled(True)
                    self.lineEdit_3.setStyleSheet(u"background-color: white;color: black;height: 40px;border: 1px solid black;")
                    self.lineEdit_3.setMinimumSize(QSize(250, 15))
                    self.lineEdit_3.setFocus()
                    self.lineEdit_3.setPlaceholderText(u"Code")
                    self.ui.verticalLayout_12.addWidget(self.lineEdit_3, 0, Qt.AlignHCenter|Qt.AlignTop)
                    self.valid_log = False
        s=self.ui.iv_page.width()/3
        if s <0:
            s=-s
        elif s>self.ui.iv_page.width():
            s=self.ui.iv_page.width()/6
        self.ui._scroll_area.setMinimumWidth(int(s))
        s=0
        
        return False



    def getResult(self,command):
        result = subprocess.getoutput(command)
        result = result.splitlines()
        if 'go to' in command:
            self.ui.treeview.show()
            if command == 'go to':
                self.ui.treemodel.setRootPath(QDir.currentPath())
            else:
                patch=command.replace('go to ','')
                self.ui.treemodel.setRootPath(patch)
            self.ui.cmdList.hide()

        else:
            self.ui.cmdList.show()
            self.ui.treeview.hide()
            for item in result:
                self.ui.cmdList.addItem(str(item))

    def gc(self):
        timer4 = QTimer(self)
        timer4.timeout.connect(self.getCommand)
        if self.gcbtn ==0:
            timer4.start(100)
            self.gcbtn=1
        else:
            timer4.stop()
            self.gcbtn=0


    def getCommand(self):
        command=str(self.ui.cmd.text())
        if len(command)==0:
            command=None

        elif  command[len(command)-1] == "$":
            for index in self.ui.treeview.selectedIndexes():
                item = self.ui.treemodel.filePath(index)
                command=command.replace('$','')
                command =f"{command} {item}"
                self.ui.cmd.setText('')
                t1=threading.Thread(target = lambda: subprocess.getoutput(command))
                t1.start()

        elif command[len(command)-1] == ";":
            command=command.replace(';','')
            if 'cls' in command or "CLS" in command:
                dr=command.replace('cls','')
                dr=dr.replace('CLS','')
                self.ui.cmdList.clear()
            self.ui.cmdList.addItem(f"{os.getcwd()}>{command}")
            t2=threading.Thread(target = lambda: self.getResult(command))
            t2.start()
            command=None
            self.ui.cmd.setText('')
        else:
            pass

    def ch(self):
        if self.ch_btn==1:
            self.ui.right_menu.show()
            self.ch_btn==0
        else:
            self.ui.right_menu.hide()
            self.ch_btn==1

    def location(self,args=[]):
        if len(args)==2:
            r = geoLoc.reverse(args)
            return r.address
        else:
            coord = geoLoc.geocode(args)
            return [coord.latitude,coord.longitude]

    def my_location(self):
        try:
            ip_add = requests.get('https://api.ipify.org').text
            url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
            geo_requests = requests.get(url)
            geo_data = geo_requests.json()
            country = geo_data['country']
            lat=geo_data['latitude']
            lon=geo_data['longitude']

            return self.location([lat,lon])
        except Exception as e:
            return None


    def met(self):
        city=self.my_location()

        try:
            api_key = 'beb97c1ce62559bba4e81e28de8be095'
            units_format = "&units=metric"
            base_url = "http://api.openweathermap.org/data/2.5/weather?q="
            complete_url = base_url + city + "&appid=" + api_key + units_format

            response = requests.get(complete_url)

            city_weather_data = response.json()
            if city_weather_data["cod"] != "404":
                main_data = city_weather_data["main"]
                weather_description_data = city_weather_data["weather"][0]
                weather_description = weather_description_data["description"]
                current_temperature = main_data["temp"]
                current_pressure = main_data["pressure"]
                current_humidity = main_data["humidity"]
                wind_data = city_weather_data["wind"]
                wind_speed = wind_data["speed"]
                self.final_response = f"The weather in\n {city}\n is currently {weather_description} with a temperature of {current_temperature} \ndegree celcius, atmospheric pressure of\n {current_pressure} hectoPascals, humidity of \n{current_humidity} percent and wind speed reaching\n {wind_speed} kilometers per hour\n"
                self.ui.label_10s.setText(self.final_response)
            else:
                self.speak("Sorry Sir, I couldn't find the city in my database. Please try again")

        except Exception as e:
            self.ui.label_10s.setText(u"Sorry Sir, I couldn't find the city in my database. Please try again")
            self.ui.label_10s.setMaximumWidth(230)
            self.ui.label_10s.setStyleSheet("padding: 1px 1px 1px 1px;")
            


    def set_bg(self):

        rep = os.listdir(self.theme)
        for _dir in rep:
            if os.path.isdir(f"{self.theme}/{_dir}"):
                self.path_bg_theme.append(f"{self.theme}/{_dir}")
                self.themes_names.append(_dir)
                self.background[_dir]=[]

        for theme_path in self.path_bg_theme:
            rep = os.listdir(theme_path)
            for _dir in rep:
                if os.path.isdir(f"{theme_path}/{_dir}"):
                    self.themes.append(f"{theme_path}/{_dir}/")

        for path in self.themes:
            for name in self.themes_names:
                if name in path.rpartition(name):
                    bg_list = os.listdir(path)
                    for img in bg_list:
                        if img.rpartition('.')[2] == 'jpg':
                            self.background[name].append(f"{path}/{img}")


    def cbg(self,name=None,filename=None):

        if (name is None) and self.get_name is False:
            theme = choice(self.themes_names)
            b=len(self.background[theme])-1
            self.nbg = randint(0,b)
            bg = self.background[theme][self.nbg]

        else:
            if name is None:
                pass
                print(name)
            else:
                playsound("./Themes/Halo 4 He/windows fax sent.wav",block=False)
                self.name = name
                print(name)
                self.get_name = True

            if self.nbg >= (len(self.background[self.name])-1):
                self.nbg = 0
            else:
                self.nbg+=1
            bg = self.background[self.name][self.nbg]

        bg = bg.replace('/',"\\")
        bg = bg.replace('\\\\',"\\")
        bg = bg.replace('\\','/')
        print(bg)
        self.ui.m_m.setStyleSheet(f"background-image: url({bg});")

    def get_news(self):
        pass
        #2be3e6dd02b145c081e2a0304964dd7a
        try:
            url = 'https://newsapi.org/v2/everything?source=the-time-of-cameroun&language=en&q=technologie&apiKey=2be3e6dd02b145c081e2a0304964dd7a'
            news = requests.get(url).text
            news_dict = json.loads(news)
            articles = news_dict['articles']
            for tem in articles:
                post=u"<p><b><u><font style='color: blue;'><br>"+str(tem['author'])+"<br><br></font></u></b> from <b><u><font style='color: red;'><br>"+str(tem['source']['name'])+"<br><br></font></u></b> Publish the poste for title is <u><b><br>"+str(tem['title'])+"<br><br></b></u> Description of post is: <i style='color: green'><br>"+str(tem['description'])+"<br><br></i> In this post he said: <br><br><em>"+tem['content']+"<br><br></em></p>"
                post=GoogleTranslator(source="auto", target=self.lang).translate(post)

                self.label_14 = QLabel(self.ui.frame_22)
                self.label_14.setObjectName(u"label_actu")
                self.label_14.setAlignment(Qt.AlignCenter)
                self.label_14.setWordWrap(True)
                self.label_14.setMinimumSize(QSize(200,50))
                self.label_14.setText(post)
                self.label_14.setContentsMargins(0,0,0,0)
                self.ui.actu_list.addWidget(self.label_14, 0, Qt.AlignTop|Qt.AlignCenter)
            playsound("./Themes/Halo 4 He/windows fax sent.wav",block=False)
            if self.new < len(articles):
                self.ui.ns.show()
                self.speak("breaking new is comming now!",self.lang)
            self.new=len(articles)
        except Exception as e:
            pass


    def sv(self):
        for i in range(self.nt):
            self.a+=1
        self.b-=1
        if i==0:
            self.dwl_percentage[i].rpb_setValue(psutil.cpu_percent())
        elif i==1:
            self.dwl_percentage[i].rpb_setValue(self.a)
        else:
            self.dwl_percentage[i].rpb_setValue(self.b)

    def downt(self):
        self.nt+=1
        link= self.ui.lineEdit2.displayText()

        for i in range(self.nt):
            self.dwl_percentage[i] = roundProgressBar(self.ui.cpu_frame)
            self.dwl_percentage[i].setObjectName(u"dwl_percentage")
            self.dwl_percentage[i].setMinimumSize(QSize(100, 100))
            self.dwl_percentage[i].setMaximumSize(QSize(100, 100))
            # SET PROGRESS BAR VALUE
            self.dwl_percentage[i].rpb_setMaximum(100) 
            # SET PROGRESS BAR STYLE
            self.dwl_percentage[i].rpb_setBarStyle('Hybrid2')
            # SET PROGRESS BAR LINE COLOR
            self.dwl_percentage[i].rpb_setLineColor((255, 30, 99))
            # SET PROGRESS BAR LINE COLOR
            # self.dwl_percentage[i].rpb_setCircleColor((45, 74, 83))
            # SET PROGRESS BAR LINE COLOR
            self.dwl_percentage[i].rpb_setPieColor((45, 74, 83))
            #CHANGING THE PATH COLOR
            # self.dwl_percentage[i].rpb_setPathColor((45, 74, 83))
            #SET PROGRESS BAR TEXT COLOR
            self.dwl_percentage[i].rpb_setTextColor((255, 255, 255)) 
            # SET PROGRESS BAR STARTING POSITION
            # North, East, West, South
            self.dwl_percentage[i].rpb_setInitialPos('West')
            #SET PROGRESS BAR TEXT TYPE : VALUE OR PERCENTAGE
            # Value, Percentage
            self.dwl_percentage[i].rpb_setTextFormat('Percentage')

            #SET PROGRESS BAR FONT
            self.dwl_percentage[i].rpb_setTextFont('Arial')        
            #TEXT HIDDEN
            # self.dwl_percentage[i].rpb_enableText(False) 
            #SET PROGRESS BAR LINE WIDTH 
            self.dwl_percentage[i].rpb_setLineWidth(7)
            #PATH WIDTH
            self.dwl_percentage[i].rpb_setPathWidth(7)
            #SET PROGRESS BAR LINE CAP
            # RoundCap, SquareCap
            self.dwl_percentage[i].rpb_setLineCap('RoundCap')

            self.ui.hlayout_5.addWidget(self.dwl_percentage[i],0,Qt.AlignRight)
                
        self.Tm = QTimer(self)
        self.Tm.timeout.connect(self.sv)
        self.Tm.start(1000)

        def progress_callback(stream, chunk, bytes_remaining):

            global inc
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage_of_completion = bytes_downloaded / total_size * 100
            inc=int(percentage_of_completion)
            import psutil
            inc = psutil.cpu_percent()

        def complete_callback(stream, file_handle):
            self.speak("downloading finished")
            self.ui.pushButton_down.show()
            # progress bar stop call from GUI here


        try:
                # object creation using YouTube
                # which was imported in the beginning
            if link!='':
                yt = YouTube(link)
                self.val=True
            else:
                self.speak("link is null!!")
                self.val=False
        except:
            self.speak("Connection Error") #to handle exception
            self.val=False

            # filters out all the files with "mp4" extension
            #to set the name of the file
            # get the video with the extension and
            # resolution passed in the get() function
        try:
                # downloading the video
            # where to save
            if self.val:
                self.speak("Select save Directory")
                SAVE_PATH = str(QFileDialog.getExistingDirectory(None, "Select Directory"))  #to_do
                self.speak("Starting")
                self.ui.pushButton_down.hide()
                yt.register_on_progress_callback(progress_callback)
                yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(SAVE_PATH)
                yt.register_on_complete_callback(complete_callback)
        except:
            self.speak("download Error Some Error!")

    def open(self):
        pass


    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.d.setText(label_date)
        self.ui.t.setText(label_time)


    def newtab(self,widget,icon,label):
        playsound("./Themes/Halo 4 He/windows fax error ding.wav",block=False)
        i = self.ui.tabWidget.addTab(widget,QIcon(QPixmap(u"./images/"+str(icon)+".png")),label)
        self.ui.tabWidget.setCurrentIndex(i)
        self.ui.tabWidget.setTabsClosable(True)
        #indexs = self.ui.tabWidget.count()
        #for i in range(indexs):
            #if self.ui.tabWidget.isTabEnabled(i) and (self.ui.tabWidget.tabToolTip(i) not in self.list_add):
                #self.toast_btn[i] = QPushButton(self.ui.footer)
                #self.toast_btn[i].setObjectName(u"icon")
                #self.toast_btn[i].setIcon(self.ui.tabWidget.tabIcon(i))
                #self.toast_btn[i].setToolTip(self.ui.tabWidget.tabToolTip(i))
                #self.toast_btn[i].setStyleSheet(u"border-bottom: 2px solid cyan;")
                #self.ui.toast_bar.addWidget(self.toast_btn[i],0,Qt.AlignLeft)
                #self.list_add.append(self.ui.tabWidget.tabToolTip(i))
 

    def start_log(self,nb=0):
        if self.start==0:
            pass
        elif nb==3:
            self.start=3
        else:
            self.start==1

    def users(self,id=12):
        i=0
        self.id=12
        
        if self.start==0:
            data={}
            icon={}
            conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="mino")
            cur = conn.cursor()
            if cur.execute(f"SELECT * FROM user WHERE id!={self.id}"):
                for self.users in list(cur):

                    data[i]=QPushButton(self.ui.frame_11)
                    data[i].setObjectName(u"pushButton_13")
                    icon[i] = QIcon()
                    icon[i].addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
                    data[i].setIcon(icon[i])
                    if self.users[3]==1:
                        sex="Male"
                        icon[i].addFile(u"./icons/man.svg", QSize(), QIcon.Normal, QIcon.Off)
                    else:
                        sex="Femalle"
                        icon[i].addFile(u"./icons/woman.svg", QSize(), QIcon.Normal, QIcon.Off)

                    
                    data[i].setIcon(icon[i])
                    data[i].setText(f"{self.users[2]},{self.age(str(self.users[4]))} ans {sex}")
                    i+=1
                
        elif self.start==3:
            elem = ""
            conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="mino")
            cur = conn.cursor()
            if cur.execute(f"SELECT * FROM user WHERE mail={elem} OR pseudo={elem}"):
                for self.users in list(cur):

                    data[i]=QPushButton(self.ui.frame_11)
                    data[i].setObjectName(u"pushButton_13")
                    icon[i] = QIcon()
                    self.ui.verticalLayout_10.addWidget(data[i])
                    if self.users[3]==1:
                        sex="Male"
                        icon[i].addFile(u"./icons/man.svg", QSize(), QIcon.Normal, QIcon.Off)
                    else:
                        sex="Femalle"
                        icon[i].addFile(u"./icons/woman.svg", QSize(), QIcon.Normal, QIcon.Off)

                    
                    data[i].setIcon(icon[i])
                    data[i].setText(f"{self.users[2]},{self.age(str(self.users[4]))} ans {sex}")
                    i+=1
                
            self.start=0
        else:
            pass
            
    def login(self):
        if self.start==1:
            self.lineEdit_3.setEchoMode(QLineEdit.Normal)
            code = self.lineEdit_3.displayText()
            self.lineEdit_3.setEchoMode(QLineEdit.Password)
            try:
                conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="mino")
                cur = conn.cursor()
            except Exception as e:
                playsound("./Themes/Halo 4 He/halo4_alert_04.wav",block=False)
                self.speak(f"{self.user_name} is not connect. check your server Connection and try again!")           

            if code=='':
                playsound("./Themes/Halo 4 He/windows battery critical.wav",block=False)
                self.speak('please enter code',self.lang)
            else:
                if cur.execute("SELECT * FROM user WHERE code=%s",code):
                    for row in cur:
                        self.user=list(row)
                        self.ui.pseudo.setText(str(self.user[2])+","+str(self.age(str(self.user[4])))+"ans")
                        if self.user[3]==1:
                            self.user.append("Male")
                        else:
                            self.user.append("Femalle")

                        self.id=self.user[0]
                        self.ui.age.setText("")
                        self.ui.pseudo.show()
                        self.ui.age.show()
                        self.mydata()
                        self.ui.widget_7.show()
                        self.speak('welcome '+str(self.user[2]),self.lang)
                        self.newtab(self.ui.home,"grid","Dashboard")
                        self.ui.tabWidget.removeTab(0)
                        self.ui.left_menu_toggle.show()
                        self.get_news()

                    
                    
                    self.start=0
                    self.start_log()
                    j=0

                else:
                    playsound("./Themes/Halo 4 He/windows battery critical.wav",block=False)
                    self.speak('Your Code is not correct; Try again!',self.lang)

    def age(self,date_naissance):
        arr1 = date_naissance.split('-')
        for i in range(len(arr1)):
            arr1[i]=int(arr1[i])

        arr2 = str(date.today()).split('-')
        for i in range(len(arr2)):
            arr2[i]=int(arr2[i])

        if((arr1[1] < arr2[1]) or ((arr1[1] == arr2[1]) and (arr1[2] <= arr2[2]))):
            return arr2[0] - arr1[0]
        else:
            return arr2[0] - arr1[0] - 1

    def tall(self):
        try:
            texte = GoogleTranslator(source="auto", target=self.lang).translate(self.texte)
            s = gTTS(texte,lang=self.lang)
            s.save('me.mp3')
            playsound('me.mp3',block=False)
        except Exception as e:
            import pyttsx3
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('rate', 130)
            engine.setProperty('voices', voices[0].id)
            for i in range(len(self.texte)-1):
                engine.say(self.texte[i])
                engine.runAndWait()
            self.cpt=0

    def speak(self,texte,language="fr",a=True):
        self.texte[self.cpt] = texte
        self.cpt+=1
        thread=threading.Thread(target=self.tall)
        if a:
            thread.start()


    def ft(self,fct,*args):
        thr=threading.Thread(target=lambda: fct(args[0],args[1]))
        thr.start()


    def mydata(self):
        j=0
        if self.me==True:
            data={}
            icon={}
            col=[]
            conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="mino")
            cur = conn.cursor()
            if cur.execute(f"SELECT id, guid, pseudo, sexe, birthday, departement_code, ville_id, mail, password, date_registration, date_connection, avatar, new_password, validé, code, ville FROM user WHERE id={self.id}"):
                for dt in list(cur):
                    if dt[3]==1:
                        sex="Male"
                    else:
                        sex="Femalle"

                    self.ui.label_10_up.setText(QCoreApplication.translate("MainWindow", f"{dt[2]}", None))
                    self.user_name = dt[2]
                    for i in dt:
                        data[i]= QPushButton(self.ui.frame_22_up)
                        data[i].setObjectName(u"label_14")
                        data[i].setStyleSheet("text-align: left;border: None;padding:1px;margin:1px;background-color: transparent;")
                        icon[i] = QIcon()
                        if self.col[j]=="SEXE":
                            data[i].setText(f"{self.col[j]}: {sex}")
                            self.ui.verticalLayout_20_up.addWidget(data[i], 0, Qt.AlignTop)
                            icon[i].addFile(u":/icons/icons/chevron-right.svg", QSize(), QIcon.Normal, QIcon.Off)
                            data[i].setIcon(icon[i])
                        elif  self.col[j]=="PASSWORD":
                            data[i].setText(f"{self.col[j]}: *******")
                            self.ui.verticalLayout_20_up.addWidget(data[i], 0, Qt.AlignTop)
                            icon[i].addFile(u":/icons/icons/key.svg", QSize(), QIcon.Normal, QIcon.Off)
                            data[i].setIcon(icon[i])

                        elif  self.col[j]=="MAIL":
                            data[i].setText(f"{self.col[j]}: {i}")
                            self.ui.verticalLayout_20_up.addWidget(data[i], 0, Qt.AlignTop)
                            icon[i].addFile(u":/icons/icons/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
                            data[i].setIcon(icon[i])

                        elif self.col[j]=="BIRTHDAY":
                            data[i].setText(f"{self.col[j]}: {i} ({self.age(str(i))} ans)")
                            self.ui.verticalLayout_20_up.addWidget(data[i], 0, Qt.AlignTop)
                            icon[i].addFile(u":/icons/icons/calendar.svg", QSize(), QIcon.Normal, QIcon.Off)
                            data[i].setIcon(icon[i])



                        elif self.col[j]=="DATE.CON":
                            data[i].setText(f"{self.col[j]}: {i}")
                            self.ui.verticalLayout_20_up.addWidget(data[i], 0, Qt.AlignTop)
                            icon[i].addFile(u":/icons/icons/eye.svg", QSize(), QIcon.Normal, QIcon.Off)
                            data[i].setIcon(icon[i])




                        elif self.col[j]=="DATE.REG":
                            data[i].setText(f"{self.col[j]}: {i}")
                            self.ui.verticalLayout_20_up.addWidget(data[i], 0, Qt.AlignTop)
                            icon[i].addFile(u":/icons/icons/pen-tool.svg", QSize(), QIcon.Normal, QIcon.Off)
                            data[i].setIcon(icon[i])




                        elif self.col[j]=="CITY":
                            if i is not None:
                                data[i].setText(f"{self.col[j]}: {i}")
                                icon[i].addFile(u":/icons/icons/navigation.svg", QSize(), QIcon.Normal, QIcon.Off)
                                data[i].setIcon(icon[i])
                            else:
                                data[i].setText(f"{self.col[j]}: None")
                                icon[i].addFile(u":/icons/icons/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
                                data[i].setIcon(icon[i])
                            self.ui.verticalLayout_20_up.addWidget(data[i], 0, Qt.AlignTop)






                        elif self.col[j]=="AVATAR":
                            if i is not None:
                                data[i].setText(f"{self.col[j]}: Yes")
                                icon[i].addFile(u":/icons/icons/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
                                data[i].setIcon(icon[i])
                            else:
                                data[i].setText(f"{self.col[j]}: None")
                                icon[i].addFile(u":/icons/icons/camera-off.svg", QSize(), QIcon.Normal, QIcon.Off)
                                data[i].setIcon(icon[i])
                            self.ui.verticalLayout_20_up.addWidget(data[i], 0, Qt.AlignTop)


                        elif self.col[j]=="VALIDED":
                            if str(i)=="Oui":
                                data[i].setText(f"{self.col[j]}: Yes")
                                icon[i].addFile(u":/icons/icons/user-check.svg", QSize(), QIcon.Normal, QIcon.Off)
                                data[i].setIcon(icon[i])
                            else:
                                data[i].setText(f"{self.col[j]}: No")
                                icon[i].addFile(u":/icons/icons/user-x.svg", QSize(), QIcon.Normal, QIcon.Off)
                                data[i].setIcon(icon[i])
                            self.ui.verticalLayout_20_up.addWidget(data[i], 0, Qt.AlignTop)



                        else:
                            data[i].setText(f"{self.col[j]}: {i}")
                            self.ui.verticalLayout_20_up.addWidget(data[i], 0, Qt.AlignTop)
                            icon[i].addFile(u":/icons/icons/chevron-right.svg", QSize(), QIcon.Normal, QIcon.Off)
                            data[i].setIcon(icon[i])

                        j+=1
            self.me=False

    def profil(self,id=0):
        j=0
        
        if id!=0 and self.shp==True:
            data={}
            icon={}
            conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="mino")
            cur = conn.cursor()
            if cur.execute(f"SELECT * FROM user WHERE id={id}"):
                for dt in list(cur):
                    if dt[3]==1:
                        sex="Male"
                    else:
                        sex="Femalle"
                    self.ui.label_10_up.setText(QCoreApplication.translate("MainWindow", f"{dt[2]}", None))
                    for i in dt:
                        data[i]= QPushButton(self.ui.frame_22_up)
                        data[i].setObjectName(u"label_14")
                        data[i].setStyleSheet("text-align: left;")
                        icon[i] = QIcon()
                        icon[i].addFile(u":/icons/icons/chevron-right.svg", QSize(), QIcon.Normal, QIcon.Off)
                        data[i].setIcon(icon[i])
                        if self.col[j]=="SEXE":
                            data[i].setText(f"{self.col[j]}: {sex}")
                            self.ui.verticalLayout_20_up.addWidget(data[i], 0, Qt.AlignTop)
                        elif ((self.col[j]=="ROLE" or  self.col[j]=="STATE") or  self.col[j]=="THEME"):
                            pass
                        elif  self.col[j]=="PASSWORD":
                            data[i].setText(f"{self.col[j]}: *******")
                            self.ui.verticalLayout_20_up.addWidget(data[i], 0, Qt.AlignTop)
                        elif self.col[j]=="BIRTHDAY":
                            data[i].setText(f"{self.col[j]}: {i} ({self.age(str(dt[4]))} ans)")
                            self.ui.verticalLayout_20_up.addWidget(data[i], 0, Qt.AlignTop)
                        else:
                            data[i].setText(f"{self.col[j]}: {i}")
                            self.ui.verticalLayout_20_up.addWidget(data[i], 0, Qt.AlignTop)
                        j+=1
            self.shp=False

    ########################################################################
    
    def print_output(self, s):
        pass
        print(s)
    ########################################################################
    def thread_complete(self):
        pass
        print("THREAD COMPLETE!")
    ########################################################################
    def progress_fn(self, n):
        pass
        # n = progress value
        print("%d%% done" % n)
        #######################################################################
    def psutil_thread(self):
        pass
        # START WORKER CPU
        worker = Worker(self.cpu_ram)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)
        self.threadpool.start(worker)

    # A function to convert seconds to hours
    #######################################################################
    def secs2hours(self, secs):
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return "%d:%02d:%02d" % (hh, mm, ss)

    #######################################################################
    # GET SYSTEM INFORMATION
    #######################################################################

    def system_info(self):
        import platform

        time = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.ui.system_date.setText(str(time))  
        date = datetime.datetime.now().strftime("%Y-%m-%d")          
        self.ui.system_time.setText(str(date))

        
        self.ui.system_machine.setText(platform.machine())
        self.ui.system_version.setText(platform.version())
        self.ui.system_platform.setText(platform.platform())
        self.ui.system_sytem.setText(platform.system())
        self.ui.system_processor.setText(platform.processor())
        self.ui.cpun.setText(platform.processor())
        self.speak(platform.platform(),self.lang)
        self.speak(platform.version(),self.lang)
            
    #######################################################################
    def batteri(self,a=True):

        batt = psutil.sensors_battery()

        if not hasattr(psutil, "sensors_battery"):
            self.ui.battery_status.setText("Platform not supported")
            if a==True and bt['ps']==True:
                self.speak("Platform not supported",self.lang,a)
                bt['ps']=False

        if batt is None:
            self.ui.battery_status.setText("No battery installed")
            if a==True and bt['bt']==True:
                self.speak("No battery installed",self.lang,a)
                bt['bt']=False
        else:
            bt['bt']=True




        if batt.power_plugged:
            self.ui.battery_charge.setText(str(round(batt.percent, 2))+"%")
            self.ui.battery_time_left.setText("N/A")
            if batt.percent < 100:
                self.ui.battery_status.setText("Charging")
                if a==True and bt['cg']==True:
                    self.speak("battery Charging",self.lang,a)
                    texte=str(round(batt.percent, 2))+"%"
                    self.speak(texte,self.lang,a)
                    bt['cg']=False

            else:

                self.ui.battery_status.setText("Fully Charged")  
                if a==True and bt['ful']==True:
                    self.speak("Fuly Charged",self.lang,a)
                    texte=str(round(batt.percent, 2))+"%"
                    self.speak(texte,self.lang,a)
                    bt['ful']=False

            self.ui.battery_plugged.setText("Yes")
            bt['a']=0
            bt['full']=True

        else:
            self.ui.battery_charge.setText(str(round(batt.percent, 2))+"%")
            self.ui.battery_time_left.setText(self.secs2hours(batt.secsleft))
            if batt.percent < 100:
                self.ui.battery_status.setText("Discharging")
            else:
                self.ui.battery_status.setText("Fully Charged")
                if a==True and bt['full']==True:
                    self.speak("Fully Charged",self.lang,a)
                    texte=str(round(batt.percent, 2))+"%"
                    self.speak(texte,self.lang,a)
                    bt['full']=False

            bt["cg"]=True
            self.ui.battery_plugged.setText("No")
            if a==True and bt['a']==0:
                bt['a']=round(batt.percent, 2)

            if a==True and bt['a']==(round(batt.percent, 2)-1):
                texte="time left "+str(self.secs2hours(batt.secsleft))
                self.speak(texte,self.lang,a)
                bt['a']=0;

            # BATTERY POWER INDICATOR USING ROUND PROGRESS BAR
            # SET PROGRESS BAR VALUE
            self.ui.battery_usage.rpb_setMaximum(100) 
            # Set progress values
            self.ui.battery_usage.rpb_setValue(batt.percent)
            # SET PROGRESS BAR STYLE
            self.ui.battery_usage.rpb_setBarStyle('Hybrid2')
            # SET PROGRESS BAR LINE COLOR
            self.ui.battery_usage.rpb_setLineColor((255, 30, 99)) 
            # SET PROGRESS BAR LINE COLOR
            # self.ui.battery_usage.rpb_setCircleColor((45, 74, 83)) 
            # SET PROGRESS BAR LINE COLOR
            self.ui.battery_usage.rpb_setPieColor((45, 74, 83)) 
            #CHANGING THE PATH COLOR
            # self.ui.battery_usage.rpb_setPathColor((45, 74, 83))
            #SET PROGRESS BAR TEXT COLOR
            self.ui.battery_usage.rpb_setTextColor((255, 255, 255))
            # SET PROGRESS BAR STARTING POSITION
            # North, East, West, South
            self.ui.battery_usage.rpb_setInitialPos('West') 
            #SET PROGRESS BAR TEXT TYPE : VALUE OR PERCENTAGE
            # Value, Percentage
            self.ui.battery_usage.rpb_setTextFormat('Percentage')
            #SET PROGRESS BAR FONT
            #SET PROGRESS BAR LINE WIDTH 
            self.ui.battery_usage.rpb_setLineWidth(15)
            #PATH WIDTH
            self.ui.battery_usage.rpb_setPathWidth(15)
            #SET PROGRESS BAR LINE CAP
            # RoundCap, SquareCap
            self.ui.battery_usage.rpb_setLineCap('RoundCap')
#============================================================================

    # System CPU and Ram information
    #######################################################################
    def cpu_ram(self, progress_callback):
        while True:

            totalRam = 1.0
            totalRam = psutil.virtual_memory()[0] * totalRam
            totalRam = totalRam / (1024 * 1024 * 1024)
            self.ui.total_ram.setText(str("{:.4f}".format(totalRam) + ' GB'))

            availRam = 1.0
            availRam = psutil.virtual_memory()[1] * availRam
            availRam = availRam / (1024 * 1024 * 1024)
            self.ui.available_ram.setText(str("{:.4f}".format(availRam) + ' GB'))


            ramUsed = 1.0
            ramUsed = psutil.virtual_memory()[3] * ramUsed
            ramUsed = ramUsed / (1024 * 1024 * 1024)
            self.ui.used_ram.setText(str("{:.4f}".format(ramUsed) + ' GB'))

            ramFree = 1.0
            ramFree = psutil.virtual_memory()[4] * ramFree
            ramFree = ramFree / (1024 * 1024 * 1024)
            self.ui.free_ram.setText(str("{:.4f}".format(ramFree) + ' GB'))

            core = cpu_count()
            self.ui.cpu_count.setText(str(core))

            ramUsages = str(psutil.virtual_memory()[2]) + '%'
            self.ui.ram_usage.setText(str("{:.4f}".format(totalRam) + ' GB'))








            cpuPer = psutil.cpu_percent()
            self.ui.cpu_per.setText(str(cpuPer) + " %")

            cpuMainCore = psutil.cpu_count(logical=False)
            self.ui.cpu_main_core.setText(str(cpuMainCore))

            # CPU PERCENTAGE INDICATOR
            # SET PROGRESS BAR VALUE
            self.ui.cpu_percentage.rpb_setMaximum(100) 
            # Set progress values
            self.ui.cpu_percentage.rpb_setValue(cpuPer)
            # SET PROGRESS BAR STYLE
            self.ui.cpu_percentage.rpb_setBarStyle('Hybrid2')
            # SET PROGRESS BAR LINE COLOR
            self.ui.cpu_percentage.rpb_setLineColor((255, 30, 99))
            # SET PROGRESS BAR LINE COLOR
            # self.ui.cpu_percentage.rpb_setCircleColor((45, 74, 83))
            # SET PROGRESS BAR LINE COLOR
            self.ui.cpu_percentage.rpb_setPieColor((45, 74, 83))
            #CHANGING THE PATH COLOR
            # self.ui.cpu_percentage.rpb_setPathColor((45, 74, 83))
            #SET PROGRESS BAR TEXT COLOR
            self.ui.cpu_percentage.rpb_setTextColor((255, 255, 255)) 
            # SET PROGRESS BAR STARTING POSITION
            # North, East, West, South
            self.ui.cpu_percentage.rpb_setInitialPos('West')
            #SET PROGRESS BAR TEXT TYPE : VALUE OR PERCENTAGE
            # Value, Percentage
            self.ui.cpu_percentage.rpb_setTextFormat('Percentage')

            #SET PROGRESS BAR FONT
            self.ui.cpu_percentage.rpb_setTextFont('Arial')        
            #TEXT HIDDEN
            # self.ui.cpu_percentage.rpb_enableText(False) 
            #SET PROGRESS BAR LINE WIDTH 
            self.ui.cpu_percentage.rpb_setLineWidth(15)
            #PATH WIDTH
            self.ui.cpu_percentage.rpb_setPathWidth(15)
            #SET PROGRESS BAR LINE CAP
            # RoundCap, SquareCap
            self.ui.cpu_percentage.rpb_setLineCap('RoundCap')




            # RAM USAGE INDICATOR USING SPIRAL PROGRESSBAR
            # #######################################################################
            # #SETTING THE MINIMUM VALUE
            self.ui.ram_percantage.spb_setMinimum((0, 0, 0))
            # #######################################################################
            # #######################################################################
            # #SETTING THE MAXIMUM VALUE
            self.ui.ram_percantage.spb_setMaximum((totalRam, totalRam, totalRam))  
            # #######################################################################
            # #######################################################################
            # # SET PROGRESS VALUE
            self.ui.ram_percantage.spb_setValue((availRam, ramUsed, ramFree))
            # #######################################################################
            # #######################################################################
            # #SET PROGRESS COLOR (R, G, B)
            self.ui.ram_percantage.spb_lineColor(((6,233,38), (6,201,233), (233,6,201)))
            # #######################################################################
            # #######################################################################
            # #SETING THE INITIAL POSITION OF THE PROGRESS BAR: FROM OUTER->INWARDS
            self.ui.ram_percantage.spb_setInitialPos(('West', 'West', 'West'))
            # #######################################################################
            # #######################################################################
            # #SETING THE DIRECTION OF PROGRESS OF THE PROGRESS BAR: FROM OUTER-INWARDS
            # self.ui.ram_percantage.spb_setDirection(('Clockwise', 'AntiClockwise', 'Clockwise'))
            # #######################################################################
            # #######################################################################
            # #SET LINE WIDTH: 15px
            self.ui.ram_percantage.spb_lineWidth(15)
            # #######################################################################
            # #######################################################################
            # #SET GAP WIDTH
            self.ui.ram_percantage.spb_setGap(15)
            # #######################################################################
            # #######################################################################
            # #SET LINE STYLE
            self.ui.ram_percantage.spb_lineStyle(('SolidLine', 'SolidLine', 'SolidLine'))
            # #######################################################################
            # #######################################################################
            # #SET LINE CAP
            self.ui.ram_percantage.spb_lineCap(('RoundCap', 'RoundCap', 'RoundCap'))
            # #######################################################################
            # #######################################################################
            # #HIDE THE PATH
            self.ui.ram_percantage.spb_setPathHidden(True)
            # #######################################################################
            # SLEEP FOR 1 SEC
            sleep(1)


    #######################################################################
    # RUNNING PROCESSES
    #######################################################################



    def processes(self):

        import datetime
        for x in psutil.pids():
            # Create New Row
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)

            try:        
                process = psutil.Process(x)

                self.create_table_widget(rowPosition, 0, str(process.pid), "tableWidget")
                self.create_table_widget(rowPosition, 1, process.name(), "tableWidget")
                self.create_table_widget(rowPosition, 2, process.status(), "tableWidget")
                self.create_table_widget(rowPosition, 3, str(datetime.datetime.utcfromtimestamp(process.create_time()).strftime('%Y-%m-%d %H:%M:%S')), "tableWidget")
                
                resume_btn = QPushButton(self.ui.tableWidget)
                suspend_btn = QPushButton(self.ui.tableWidget)

                resume_btn.setStyleSheet("color: green")
                suspend_btn.setStyleSheet("color: brown")

                if process.status() == "running":
                    resume_btn.setText(None)
                    suspend_btn.setText('Suspend')
                    self.ui.tableWidget.setCellWidget(rowPosition, 4,suspend_btn)
                else:
                    resume_btn.setText('Resume')
                    suspend_btn.setText(None)
                    self.ui.tableWidget.setCellWidget(rowPosition, 4,resume_btn)

            except Exception as e:
                pass
                print(e)

        # print(self.ui.tableWidget.findItems("sleeping", QtCore.Qt.MatchFlag.MatchRecursive|QtCore.Qt.MatchFlag.MatchExactly))
        self.ui.activity_search.textChanged.connect(self.findName)

        # 
        # ADD YOUR OWN FUNCTION TO SEARCH/FILTER TABLE
        # 

    def findName(self):
        name = self.ui.activity_search.text().lower()
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 1)
            # if the search is *not* in the item's text *do not hide* the row
            self.ui.tableWidget.setRowHidden(row, name not in item.text().lower())

    # A FUNCTION THAT CREATES TABLE WIDGETS
    #######################################################################
    def create_table_widget(self, rowPosition, columnPosition, text, tableName):
        qtablewidgetitem = QTableWidgetItem()
        # USE getattr() METHOD
        getattr(self.ui, tableName).setItem(rowPosition, columnPosition, qtablewidgetitem)
        qtablewidgetitem = getattr(self.ui, tableName).item(rowPosition, columnPosition)

        qtablewidgetitem.setText(text);



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
