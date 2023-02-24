import sys
from PySide6.QtCore import QStandardPaths, Qt, Slot
from PySide6.QtGui import QAction, QIcon, QKeySequence, QScreen
from PySide6.QtWidgets import (QApplication, QDialog, QFileDialog,
    QMainWindow, QSlider, QStyle, QToolBar)
from PySide6.QtMultimedia import (QAudio, QAudioOutput, QMediaFormat,
                                  QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar
from PySide2.QtWebEngineWidgets import QWebEngineView
import Widgets
from Widgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 724)
        MainWindow.setStyleSheet(u"*{\n"
"color: white;\n"
"padding: 0;\n"
"margin: 0;\n"
"border: none;\n"
"}\n"
"#centralwidget{\n"
"background-color: black;\n"
"color: white;"
"}\n"
"#frame_16{\n"
"background-image: url(./images/img103.png);background-position: center;background-repeat: no-repeat;\n"
"padding: 0;\n"
"margin: 0;\n"
"border: none;\n"
"}\n"
"#home{\n"
"background-image: url(./images/5_halo4.jpg);background-position: center;background-repeat: no-repeat;\n"
"padding: 0;\n"
"margin: 0;\n"
"border: none;\n"
"}\n"
"#pushButton{\n"
"border: 1px double rgb(7 ,98 ,160);"
"border-radius: 20px;"
"}\n"
"#header{\n"
"background-color: rgb(28, 37, 49);text-align: left; margin:0px;\n"
"}\n"
"#footer{\n"
"background-color: black;text-align: left; margin:0px;\n"
"}\n"
"#label_actu{\n"
"   background-color: rgba(14, 14, 22, 100);\n"
"   border: 1px solid rgb(9, 5, 13);\n"
"   padding: 5px 5px;\n"
"   margin: 5px 5px;\n"
"   border-radius: 5px;\n"
"   text-align: left;\n"
"color: white;\n"
"}\n"
"QTabWidget::pane {"
"    border: 1px solid black;"
"    background: black;"
"    border-top-left-radius: 10px;"
"    border-bottom-right-radius: 10px;"
"}\n"

"QTabWidget::tab-bar:top {"
"    top: 1px;"
"}\n"

"QTabWidget::tab-bar:bottom {"
"    bottom: 1px;"
"}\n"

"QTabWidget::tab-bar:left {"
"    right: 1px;"
"}\n"

"QTabWidget::tab-bar:right {"
"    left: 1px;"
"}\n"

"QTabBar::tab {"
"    border: 1px solid black;"
"    background-color: black;"
"    border-top-left-radius: 10px;"
"    border-bottom-right-radius: 10px;"
"    font-family: Roboto;"
"}\n"

"QTabBar::tab:selected {"
"    border: 1px double cyan;"
"    color: black;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(238,174,202,1), stop:1 rgba(148,187,233,1));"
"}\n"

"QTabBar::tab:!selected {"
"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"}\n"

"QTabBar::tab:!selected:hover {"
"color: black;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(238,174,202,1), stop:1 rgba(148,187,233,1));"
"}\n"
"QTabBar::tab:top:!selected {"
"    margin-top: 3px;"
"}\n"

"QTabBar::tab:bottom:!selected {"
"    margin-bottom: 3px;"
"}\n"

"QTabBar::tab:top, QTabBar::tab:bottom {"
"    min-width: 8ex;"
"    margin-right: -1px;"
"    padding: 5px 10px 5px 10px;"
"}\n"

"QTabBar::tab:top:selected {"
"    border-bottom-color: none;"
"}\n"

"QTabBar::tab:bottom:selected {"
"    border-top-color: none;"
"}\n"

"QTabBar::tab:top:last, QTabBar::tab:bottom:last,"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {"
"    margin-right: 0;"
"}\n"

"QTabBar::tab:left:!selected {"
"    margin-right: 3px;"
"}\n"

"QTabBar::tab:right:!selected {"
"    margin-left: 3px;"
"}\n"

"QTabBar::tab:left, QTabBar::tab:right {"
"    min-height: 8ex;"
"    margin-bottom: -1px;"
"    padding: 10px 5px 10px 5px;"
"}\n"

"QTabBar::tab:left:selected {"
"    border-left-color: none;"
"}\n"

"QTabBar::tab:right:selected {"
"    border-right-color: none;"
"}\n"

"QTabBar::tab:left:last, QTabBar::tab:right:last,"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {"
"    margin-bottom: 0;"
"}\n"
"#label_14:hover{\n"
"   border: 1px solid cyan;\n"
"}\n"
"QFileSystemModel{\n"
"color: black;"
"}\n"
)
     
#==================================================================bigin=========
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(
u"QDialog,QInputDialog,QListView,QMessageBox,QToolTip{\n"
"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"border: none;"
"}\n"
"*{\n"
"color: white;\n"
"}\n"
"QLabel,QComboBox{\n"
"background-color: transparent;"
"}\n"
"QMenu,QToolTip{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"border: 1px double cyan;border-radius: 5px;\n"
"}\n"
"QCustomSlideMenu{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"}\n"
                )
#==========================================Vertical==BoxLayout==and attributes======
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
#==========================================header widget=========
        self.header = QWidget(self.centralwidget)
        self.header.setMaximumHeight(0)
        self.header.setMinimumHeight(0)
        self.header.setObjectName(u"header")
#=========================horizontal boxlayout==in header= and attributes=============
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
#===========================toggle_button zone for menu= in header=======

        self.widget_6 = QWidget(self.header)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")



























        self.toggle_button = QPushButton(self.header)
        self.toggle_button.setObjectName(u"toggle_button")
        self.toggle_button.setMinimumSize(QSize(10, 0))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.toggle_button.setFont(font)
#====================Icon for toggle button=========
        icon = QIcon()
        icon.addFile(u":/icons/icons/grid.svg", QSize(), QIcon.Normal, QIcon.Off)
#====================setIcon=========
        self.toggle_button.setIcon(icon)
#===============Icon size=======
        self.toggle_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.toggle_button, 0, Qt.AlignLeft)
#=================add toggle contain in toggle zone=========







        self.frame = QFrame(self.widget_6)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        #===================================================================================
        self.user_btn = QPushButton(self.frame)
        self.user_btn.setObjectName(u"pushButton_8")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.user_btn.setIcon(icon1)
        self.user_btn.setIconSize(QSize(18, 18))
        self.horizontalLayout_7.addWidget(self.user_btn, 0, Qt.AlignHCenter)

        self.pseudo=QLabel(self.frame)
        self.pseudo.setObjectName(u"pseudo")
        self.pseudo.setStyleSheet(u"background-color: transparent;color: white;")

        self.age=QLabel(self.frame)
        self.age.setObjectName(u"age")
        self.age.setStyleSheet(u"background-color: transparent;color: white;")
        self.horizontalLayout_7.addWidget(self.pseudo, 0, Qt.AlignHCenter)
        self.horizontalLayout_7.addWidget(self.age, 0, Qt.AlignHCenter)

        #===================================================================================
        self.bell_btn = QPushButton(self.frame)
        self.bell_btn.setObjectName(u"pushButton_8")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bell_btn.setIcon(icon1)
        self.bell_btn.setIconSize(QSize(18, 18))
        self.horizontalLayout_7.addWidget(self.bell_btn, 0, Qt.AlignHCenter)
        #===================================================================================
        self.message_btn = QPushButton(self.frame)
        self.message_btn.setObjectName(u"pushButton_8")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/message-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.message_btn.setIcon(icon1)
        self.message_btn.setIconSize(QSize(18, 18))
        self.horizontalLayout_7.addWidget(self.message_btn, 0, Qt.AlignHCenter)
        #===================================================================================
        self.wifi_btn = QPushButton(self.frame)
        self.wifi_btn.setObjectName(u"pushButton_8")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/wifi.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.wifi_btn.setIcon(icon1)
        self.wifi_btn.setIconSize(QSize(18, 18))
        self.horizontalLayout_7.addWidget(self.wifi_btn, 0, Qt.AlignHCenter)
        #===================================================================================





        self.horizontalLayout_6.addWidget(self.frame, 0, Qt.AlignHCenter)




        self.frame_3 = QFrame(self.widget_6)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_12 = QPushButton(self.frame_3)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon2)

        self.horizontalLayout_8.addWidget(self.pushButton_12)


        self.minimizeWindow = QPushButton(self.frame_3)
        self.minimizeWindow.setObjectName(u"minimizeWindow")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/minus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeWindow.setIcon(icon4)
        self.minimizeWindow.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.minimizeWindow)




        self.restoreWindow = QPushButton(self.frame_3)
        self.restoreWindow.setObjectName(u"restoreWindow")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreWindow.setIcon(icon3)
        self.restoreWindow.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.restoreWindow)


        self.closeWindow = QPushButton(self.frame_3)
        self.closeWindow.setObjectName(u"closeWindow")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeWindow.setIcon(icon5)
        self.closeWindow.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.closeWindow)

        self.horizontalLayout_6.addWidget(self.frame_3, 0, Qt.AlignRight)

        self.horizontalLayout_3.addWidget(self.widget_6)

        self.verticalLayout.addWidget(self.header)
#============================End of Header=========



        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(15)
        font3.setPixelSize(17)

        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(5)
        font4.setPixelSize(11)






        self.notifications_widget = QCustomSlideMenu()
        self.notifications_widget.setObjectName(u"notifications_widget")
        self.notifications_widget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));")
        
        self.vblnw = QVBoxLayout(self.notifications_widget)
        self.vblnw.setObjectName(u"verticalLayout_19")
        self.vblnw.setContentsMargins(0, 0, 0, 0)



        self.frame_22 = QFrame(self.notifications_widget)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(150, 433))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.frame_22.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));")

        self.vblf22 = QVBoxLayout(self.frame_22)
        self.vblf22.setObjectName(u"verticalLayout_20")


        self.frame_15 = QFrame(self.frame_22)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.frame_15.setStyleSheet(u"background-color: transparent;color: white;")

        self.horizontalLayout_16 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_8 = QLabel(self.frame_15)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u":/icons/icons/sun.svg"))
        self.label_8.setStyleSheet(u"background-color: transparent;color: white;")

        self.horizontalLayout_16.addWidget(self.label_8, 0, Qt.AlignLeft)

        font2 = QFont()
        font2.setPointSize(40)
        font2.setBold(True)
        font2.setWeight(40)

        fontd = QFont()
        fontd.setPointSize(30)
        fontd.setWeight(30)

        self.label_10s = QLabel(self.frame_15)
        self.label_10s.setObjectName(u"label_10")
        self.label_10s.setWordWrap(True)
        self.label_10s.setStyleSheet(u"background-color: transparent;color: white;")

        self.horizontalLayout_16.addWidget(self.label_10s, 0, Qt.AlignRight)

        self.frame_tb = QFrame(self.frame_22 )
        self.frame_tb.setStyleSheet(u"background-color: transparent;color: white;")
        self.frame_tb.setObjectName(u"frame_2")
        self.frame_tb.setFrameShape(QFrame.StyledPanel)
        self.frame_tb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6_tb = QVBoxLayout(self.frame_tb)
        self.verticalLayout_6_tb.setSpacing(5)
        self.verticalLayout_6_tb.setObjectName(u"verticalLayout_5")
        self.verticalLayout_6_tb.setContentsMargins(0, 0, 0, 0)

        self.d = QLabel(self.frame_tb)
        self.d.setObjectName(u"messages_btn")

        self.t = QLabel(self.frame_tb)
        self.t.setObjectName(u"messages_btn")
        self.t.setFont(font2)
        
        self.verticalLayout_6_tb.addWidget(self.t,0, Qt.AlignVCenter)
        self.verticalLayout_6_tb.addWidget(self.d,0, Qt.AlignJustify)
        

        self.vblf22.addWidget(self.frame_tb, 0, Qt.AlignCenter|Qt.AlignTop)
        self.vblf22.addWidget(self.frame_15, 1, Qt.AlignCenter|Qt.AlignTop)



        self.actu_page = QWidget()
        self.actu_page.setObjectName(u"page")
        self.actu_list = QVBoxLayout(self.actu_page)
        self.actu_list.setObjectName(u"verticalLayout_8")
        self.actu_page.setStyleSheet(u"background-color: transparent;color: white;")


        self.ns = QScrollArea()
        self.ns.setObjectName(u"scrollArea")
        self.ns.setWidgetResizable(True)
        self.ns.setMinimumSize(220,200)
        self.ns.setStyleSheet(u"background-color: transparent;color: white;")

        self.ns.setWidget(self.actu_page)
        
        self.vblf22.addWidget(self.ns, 0, Qt.AlignCenter|Qt.AlignTop)
        self.vblnw.addWidget(self.frame_22,0,Qt.AlignTop)


#=========================================================================================

        self.battery_container = QWidget()
        self.battery_container.setObjectName('battery')
        self.vb_battery_container = QVBoxLayout(self.battery_container)
        self.vb_battery_container.setSpacing(0)
        self.vb_battery_container.setObjectName(u"vb_battery_container")
        self.vb_battery_container.setContentsMargins(0, 0, 0, 0)




        self.battery_info = QFrame(self.battery_container)
        self.battery_info.setObjectName(u"battery_info")
        self.gridLayout_8 = QGridLayout(self.battery_info)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(20, 20, 20, 20)
        self.frame_5 = QFrame(self.battery_info)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_7.addWidget(self.label_10, 6, 0, 1, 1)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_7.addWidget(self.label_7, 3, 0, 1, 1)

        self.battery_status = QLabel(self.frame_5)
        self.battery_status.setObjectName(u"battery_status")

        self.gridLayout_7.addWidget(self.battery_status, 3, 1, 1, 1)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_7.addWidget(self.label_8, 4, 0, 1, 1)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_7.addWidget(self.label_9, 5, 0, 1, 1)

        self.battery_time_left = QLabel(self.frame_5)
        self.battery_time_left.setObjectName(u"battery_time_left")

        self.gridLayout_7.addWidget(self.battery_time_left, 5, 1, 1, 1)

        self.battery_plugged = QLabel(self.frame_5)
        self.battery_plugged.setObjectName(u"battery_plugged")

        self.gridLayout_7.addWidget(self.battery_plugged, 6, 1, 1, 1)

        self.battery_charge = QLabel(self.frame_5)
        self.battery_charge.setObjectName(u"battery_charge")

        self.gridLayout_7.addWidget(self.battery_charge, 4, 1, 1, 1)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout_7.addWidget(self.label_6, 2, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_5, 0, 0, 0, 0)






        self.battery_usage = roundProgressBar(self.battery_info)
        self.battery_usage.setObjectName(u"battery_usage")
        self.battery_usage.setMinimumSize(QSize(230, 230))
        self.battery_usage.setMaximumSize(QSize(250, 250))
        self.gridLayout_8.addWidget(self.battery_usage,0,Qt.AlignRight)



        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Plugged In", None))
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_10.setMargin(20)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_7.setMargin(20)
        self.battery_status.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.battery_status.setFont(font4)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_8.setMargin(20)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Time Left", None))
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_9.setMargin(20)
        self.battery_time_left.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.battery_time_left.setFont(font4)
        self.battery_plugged.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.battery_plugged.setFont(font4)
        self.battery_charge.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.battery_charge.setFont(font4)





        self.battery_gauche = QHBoxLayout()
        self.battery_gauche.setSpacing(0)
        self.battery_gauche.setObjectName(u"gauche")
        self.battery_gauche.setContentsMargins(10, 10, 10, 10)
#================================ldbattery=========================================================
        self.ldbattery = QLabel(self.battery_container)
        self.ldbattery.setObjectName(u"ldbattery")
        self.ldbattery.setPixmap(QPixmap(u":/icons/icons/battery-charging.svg"))
        self.ldbattery.setBaseSize(80,80)
        self.ldbattery.setMargin(10)
#================================nbattery=========================================================
        self.nbattery = QLabel(self.battery_container)
        self.nbattery.setObjectName(u"nbattery")
        font2 = QFont()
        font2.setPointSize(30)
        font2.setBold(True)
        font2.setWeight(120)
        self.nbattery.setFont(font2)
        self.nbattery.setWordWrap(True)
        self.nbattery.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:rgb(230, 5, 64);\"> BATTERY DATA</span></p></body></html>", None))
        self.nbattery.setGeometry(QRect(102, 8, 400, 100))
        self.ldbattery.setGeometry(QRect(50,19,80,80))
        self.battery_gauche.addWidget(self.ldbattery,0,Qt.AlignLeft)
        self.battery_gauche.addWidget(self.nbattery,0,Qt.AlignRight)
        self.vb_battery_container.addWidget(self.battery_info)













        fontl = QFont()
        fontl.setPointSize(20)
        fontl.setBold(True)
        fontl.setWeight(20)


        self.bottom_menu = QCustomSlideMenu()
        self.bottom_menu.setObjectName(u"bottom_menu")

        self.verticalLayout_13 = QVBoxLayout(self.bottom_menu)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)





        self.up = QCustomSlideMenu(self.bottom_menu)
        self.up.setObjectName(u"up")
        self.up.setMinimumSize(QSize(0, 0))
        self.up.setStyleSheet("color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));border: 1px double cyan;border-radius: 5px;")
        self.verticalLayout_19_up = QVBoxLayout(self.up)
        self.verticalLayout_19_up.setSpacing(0)
        self.verticalLayout_19_up.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19_up.setContentsMargins(0, 0, 0, 0)
        self.frame_22_up = QFrame(self.up)
        self.frame_22_up.setObjectName(u"frame_22")
        self.frame_22_up.setMinimumSize(QSize(212, 433))
        self.frame_22_up.setFrameShape(QFrame.StyledPanel)
        self.frame_22_up.setFrameShadow(QFrame.Raised)
        self.frame_22_up.setStyleSheet(u"color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));")
        self.verticalLayout_20_up = QVBoxLayout(self.frame_22_up)
        self.verticalLayout_20_up.setObjectName(u"verticalLayout_20")


        self.label_10_up = QLabel(self.frame_22_up)
        self.label_10_up.setObjectName(u"label_10")
        self.label_10_up.setFont(font2)
        self.label_10_up.setWordWrap(True)
        self.label_10_up.setStyleSheet("font-weight:600;")
        self.label_10_up.setStyleSheet(u"background-color: transparent;border: none;")


        self.label_8_up = QLabel(self.frame_22_up)
        self.label_8_up.setObjectName(u"label_8")
        self.label_8_up.setMinimumSize(QSize(220, 100))
        self.label_8_up.setMaximumSize(QSize(220, 120))
        self.label_8_up.setScaledContents(True)
        self.label_8_up.setStyleSheet(f"background-image: url(./icons/man.svg);\n"
"background-repeat: none;\n"
"background-position: center;\n"
"padding-left: -2px;\n"
"border: none;\n"
)

        self.verticalLayout_20_up.addWidget(self.label_8_up, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_20_up.addWidget(self.label_10_up, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_19_up.addWidget(self.frame_22_up, 0, Qt.AlignHCenter)

        self.verticalLayout_13.addWidget(self.up,0,Qt.AlignVCenter|Qt.AlignTop)




        self.terminal = QCustomSlideMenu(self.bottom_menu)
        self.terminal.setStyleSheet("color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));border: 1px double cyan;border-radius: 5px;")
        self.terminal.setObjectName(u"terminal")
        self.terminal.setMinimumSize(QSize(0, 0))
        self.verticalLayout_19_tl = QVBoxLayout(self.terminal)
        self.verticalLayout_19_tl.setSpacing(0)
        self.verticalLayout_19_tl.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19_tl.setContentsMargins(0, 0, 0, 0)

        self.cmd = QLineEdit(self.terminal)
        self.cmd.setObjectName(u"cmd")
        self.cmd.setEchoMode(QLineEdit.Normal)
        self.cmd.setStyleSheet(u"border-bottom: 3px solid rgb(7 ,98 ,160);border: 1px solid rgb(7 ,98 ,160);background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));color: white;border-radius: 5px;height: 25px;")
        self.cmd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Command Line..", None))
        self.cmd.setClearButtonEnabled(True)
        self.cmdList = QListWidget(self.terminal)
        self.cmdList.setObjectName('listOutput')
        self.cmdList.setMinimumSize(QSize(400, 500))
        self.cmdList.setStyleSheet("color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));")

        self.treemodel = QFileSystemModel()
        self.treemodel.setObjectName('treeview')
        self.treeview = QTreeView()
        self.treeview.setModel(self.treemodel)
        self.treeview.setMinimumSize(QSize(400, 500))
        self.treeview.setStyleSheet("color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));")

        self.treeview.hide()
        self.verticalLayout_19_tl.addWidget(self.treeview,0,Qt.AlignVCenter)
        self.verticalLayout_19_tl.addWidget(self.cmdList,0,Qt.AlignVCenter)
        self.verticalLayout_19_tl.addWidget(self.cmd,0,Qt.AlignBottom)







        self.verticalLayout_13.addWidget(self.terminal,0,Qt.AlignVCenter|Qt.AlignTop)



        icon20 = QIcon()
        icon20.addFile(u":/icons/icons/more-vertical.svg", QSize(), QIcon.Normal, QIcon.Off)

        self.frame_5 = QFrame(self.bottom_menu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(
u"#frame_5{\n"
"   background-color: transparent;\n"
"   border: none;\n"
"}\n"
"#icon4{\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(238,174,202,1), stop:1 rgba(148,187,233,1));\n"
"   border: 1px solid rgb(9, 5, 13);\n"
"   padding: 5px 5px 5px 5px;\n"
"   border-radius: 5px;\n"
"   text-align: center;\n"
"}\n"
"#icon4:hover{\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(238,174,202,1), stop:1 rgba(148,187,233,1));\n"
"   border: 2px solid cyan;\n"
"   text-align: center;\n"
"}\n"
                )

        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_15.setSpacing(20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(5, 5, 5, 5)



        self.pushButton_g = QPushButton(self.frame_5)
        self.pushButton_g.setObjectName("icon4")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_g.setIcon(icon15)
        self.horizontalLayout_15.addWidget(self.pushButton_g,0,Qt.AlignLeft)



        self.pushButton_m = QPushButton(self.frame_5)
        self.pushButton_m.setObjectName("icon4")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/terminal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_m.setIcon(icon15)
        self.horizontalLayout_15.addWidget(self.pushButton_m,0,Qt.AlignCenter)




        self.pushButton_d = QPushButton(self.frame_5)
        self.pushButton_d.setObjectName("icon4")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/image.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_d.setIcon(icon15)
        self.horizontalLayout_15.addWidget(self.pushButton_d,0,Qt.AlignRight)




        self.verticalLayout_13.addWidget(self.frame_5,0,Qt.AlignBottom)



        self.frame_16 = QWidget()
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(300, 0))
        self.verticalLayout_12 = QVBoxLayout(self.frame_16)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_16)
        self.label_5.setStyleSheet(u"background-color: transparent;")
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(75, 75))
        self.label_5.setMaximumSize(QSize(150, 150))
        self.label_5.setPixmap(QPixmap(u":/icons/icons/grid.svg"))
        self.label_5.setAlignment(Qt.AlignCenter)
        self.verticalLayout_12.addWidget(self.label_5,0,Qt.AlignCenter)


        





























        self.cpu_page = QWidget()
        self.cpu_page.setStyleSheet(
u"*{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"}\n"
"QLabel,QFrame{\n"
"background-color: transparent;"
"border: None;"
"}\n"
)
        self.cpu_page.setObjectName(u"cpu_page")
        self.gridLayout_2 = QGridLayout(self.cpu_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")






        self.cpu_frame = QFrame(self.cpu_page)
        self.cpu_frame.setObjectName(u"cpu_frame")
        self.cpu_frame.setFrameShape(QFrame.StyledPanel)
        self.cpu_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_5 = QGridLayout(self.cpu_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.cpu_count = QLabel(self.cpu_frame)
        self.cpu_count.setObjectName(u"cpu_count")
        self.gridLayout_5.addWidget(self.cpu_count, 1, 1, 1, 1)

        
        self.cpu_per = QLabel(self.cpu_frame)
        self.cpu_per.setObjectName(u"cpu_per")
        self.gridLayout_5.addWidget(self.cpu_per, 2, 1, 1, 1)
        self.cpu_main_core = QLabel(self.cpu_frame)
        self.cpu_main_core.setObjectName(u"cpu_main_core")
        self.gridLayout_5.addWidget(self.cpu_main_core, 3, 1, 1, 1)
        self.cpun = QLabel(self.cpu_frame)
        self.cpun.setObjectName(u"cpu_main_core")
        self.gridLayout_5.addWidget(self.cpun, 4, 1, 1, 1)
        self.label_18 = QLabel(self.cpu_frame)
        self.label_18.setObjectName(u"label_18")
        self.gridLayout_5.addWidget(self.label_18, 2, 0, 1, 1)
        self.label_4 = QLabel(self.cpu_frame)
        self.label_4.setObjectName(u"label_4")
        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_22 = QLabel(self.cpu_frame)
        self.label_22.setObjectName(u"label_22")
        self.gridLayout_5.addWidget(self.label_22, 3, 0, 1, 1)
        self.label_222 = QLabel(self.cpu_frame)
        self.label_222.setObjectName(u"label_22")
        self.gridLayout_5.addWidget(self.label_222, 4, 0, 1, 1)









#================================ncpu=========================================================
        self.ncpu = QLabel(self.cpu_page)
        font2 = QFont()
        font2.setPointSize(30)
        font2.setBold(True)
        font2.setWeight(120)
        self.ncpu.setFont(font2)
        self.ncpu.setWordWrap(True)
        self.ncpu.setObjectName('llr')
        self.ncpu.setText('CPU DATA')













        self.gridLayout_2.addWidget(self.cpu_frame, 0, 0, 1, 1)
        



        self.cpu_percentage = roundProgressBar(self.cpu_page)
        self.cpu_percentage.setObjectName(u"cpu_percentage")
        self.cpu_percentage.setMinimumSize(QSize(100, 100))
        self.cpu_percentage.setMaximumSize(QSize(100, 100))

        self.gridLayout_2.addWidget(self.cpu_percentage, 0, 1, 1, 1)










        self.cpu_count.setMargin(10)
        self.cpu_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_count.setFont(font4)
        self.cpu_per.setMargin(10)
        self.cpu_per.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_per.setFont(font4)
        self.cpu_main_core.setMargin(10)
        self.cpu_main_core.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cpu_main_core.setFont(font4)
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_18.setMargin(10)
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"CPU Per", None))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_4.setMargin(10)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CPU Count", None))
        self.label_22.setFont(font3)
        self.label_22.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_22.setMargin(10)
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"CPU Main Core", None))

        self.label_222.setFont(font3)
        self.label_222.setStyleSheet(u"color: rgb(230,5,64);")
        self.label_222.setMargin(10)
        self.label_222.setText(QCoreApplication.translate("MainWindow", u"CPU", None))

        self.cpun.setMargin(10)
        self.cpun.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.cpun.setFont(font4)










#RAM




#=========================================================================================
        self.ram_page = QWidget()
        self.ram_page.setObjectName(u"ram_page")
        self.gridLayout_2_ram = QVBoxLayout(self.ram_page)
        self.gridLayout_2_ram.setObjectName(u"gridLayout_2")

#=========================================================================================


        self.gr = QFrame(self.ram_page)
        self.gauche_ram = QHBoxLayout(self.gr)
        self.gauche_ram.setSpacing(0)
        self.gauche_ram.setObjectName(u"gauche")
        self.gauche_ram.setContentsMargins(10, 10, 10, 10)

#================================nram=========================================================
        self.nram = QLabel(self.gr)
        font2 = QFont()
        font2.setPointSize(30)
        font2.setBold(True)
        font2.setWeight(120)
        self.nram.setFont(font2)
        self.nram.setWordWrap(True)
        self.nram.setObjectName('llr')
        self.nram.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:rgb(230, 5, 64);\">RAM DATA</span></p></body></html>", None))
        self.gauche_ram.addWidget(self.nram)
        

        self.gridLayout_2_ram.addWidget(self.gr,0,Qt.AlignVCenter)
        


        self.ram_frame = QFrame(self.ram_page)
        self.ram_frame.setObjectName(u"ram_frame")
        self.ram_frame.setFrameShape(QFrame.StyledPanel)
        self.ram_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.ram_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_11 = QLabel(self.ram_frame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_6.addWidget(self.label_11, 0, 0, 1, 1)

        self.total_ram = QLabel(self.ram_frame)
        self.total_ram.setObjectName(u"total_ram")

        self.gridLayout_6.addWidget(self.total_ram, 0, 1, 1, 1)

        self.label_12 = QLabel(self.ram_frame)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 1, 0, 1, 1)

        self.available_ram = QLabel(self.ram_frame)
        self.available_ram.setObjectName(u"available_ram")
        self.available_ram.setStyleSheet(u"border: 1px solid rgb(6,233,38);\n"
"border-radius: 10px;")

        self.gridLayout_6.addWidget(self.available_ram, 1, 1, 1, 1)

        self.label_14 = QLabel(self.ram_frame)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 2, 0, 1, 1)

        self.used_ram = QLabel(self.ram_frame)
        self.used_ram.setObjectName(u"used_ram")
        self.used_ram.setStyleSheet(u"border: 1px solid rgb(6,201,233);\n"
"border-radius: 10px;")

        self.gridLayout_6.addWidget(self.used_ram, 2, 1, 1, 1)

        self.label_16 = QLabel(self.ram_frame)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_6.addWidget(self.label_16, 3, 0, 1, 1)

        self.free_ram = QLabel(self.ram_frame)
        self.free_ram.setObjectName(u"free_ram")
        self.free_ram.setStyleSheet(u"border: 1px solid rgb(233,6,201);\n"
"border-radius: 10px;")

        self.gridLayout_6.addWidget(self.free_ram, 3, 1, 1, 1)

        self.label_24 = QLabel(self.ram_frame)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_6.addWidget(self.label_24, 4, 0, 1, 1)

        self.ram_usage = QLabel(self.ram_frame)
        self.ram_usage.setObjectName(u"ram_usage")

        self.gridLayout_6.addWidget(self.ram_usage, 4, 1, 1, 1)


        self.gridLayout_2_ram.addWidget(self.ram_frame,0,Qt.AlignVCenter)

        self.fg = QFrame(self.ram_frame)

        self.hfg = QHBoxLayout(self.fg)
        self.ram_percantage = spiralProgressBar(self.fg)
        self.ram_percantage.setObjectName(u"ram_percantage")
        self.ram_percantage.setMinimumSize(QSize(300, 300))
        self.ram_percantage.setMaximumSize(QSize(300, 300))
        self.hfg.addWidget(self.ram_percantage,0,Qt.AlignHCenter)
        self.gridLayout_2_ram.addWidget(self.fg,0,Qt.AlignVCenter)



#============================================================================
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"color: rgb(230,5,64)")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Total Ram", None))
        self.total_ram.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"color: rgb(230,5,64)")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Available Ram", None))
        self.available_ram.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"color: rgb(230,5,64)")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Used RAM", None))
        self.used_ram.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_16.setFont(font3)
        self.label_16.setStyleSheet(u"color: rgb(230,5,64)")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Free RAM", None))
        self.free_ram.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_24.setFont(font3)
        self.label_24.setStyleSheet(u"color: rgb(230,5,64)")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"RAM Usage", None))
        self.ram_usage.setText(QCoreApplication.translate("MainWindow", u"0", None))


        





#iv==


#=========================================================================================
        self.iv_page = QWidget()
        self.iv_page.setObjectName(u"iv_page")
        self.p_hb_for_iv = QHBoxLayout(self.iv_page)
        self.p_hb_for_iv.setObjectName(u"gridLayout_2")


        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

#=========================================================================================


        self.p_left_frame_for_iv = QFrame(self.iv_page)
        self.f_hb_for_p_left_frame = QHBoxLayout(self.p_left_frame_for_iv)
        self.f_hb_for_p_left_frame.setSpacing(0)
        self.f_hb_for_p_left_frame.setObjectName(u"gauche")

        sizePolicy.setHeightForWidth(self.p_left_frame_for_iv.sizePolicy().hasHeightForWidth())

#================================nram=========================================================
        self.treemodel_iv = QFileSystemModel()
        self.treemodel_iv.setObjectName('treeview')
        self.treemodel_iv.setRootPath(QDir.currentPath())
        self.treeview_iv = QTreeView()
        self.treeview_iv.setModel(self.treemodel_iv)
        self.treeview_iv.setSizePolicy(sizePolicy)
        self.treeview_iv.setStyleSheet("color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));")
        self.treeview_iv.setMinimumWidth(200)




        self.iframe_load = QFrame()
        self.lld = QVBoxLayout(self.iframe_load)

        self.lp = QLabel()
        self.lp.setMaximumSize(QSize(255,50))
        self.lp.setBackgroundRole(QPalette.Base)
        self.lp.setScaledContents(True)
        self.lp.hide()

        self.mv = QMovie(".\\images\\gif\\ld.gif")
        self.lp.setMovie(self.mv)
        self.mv.start()
        self.lld.addWidget(self.lp,0,Qt.AlignTop)

        self.img_list = QListWidget()
        self.img_list.setObjectName('listOutput')
        self.img_list.dragDropOverwriteMode()
        self.img_list.setSizePolicy(sizePolicy)
        self.img_list.setContentsMargins(10, 10, 10, 10)
        self.img_list.setStyleSheet("color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));border: 1px double cyan;")
        
        self.lld.addWidget(self.img_list)


        self.f_hb_for_p_left_frame.addWidget(self.treeview_iv,0,Qt.AlignLeft)
        self.f_hb_for_p_left_frame.addWidget(self.iframe_load,0,Qt.AlignRight)
        

        self.p_hb_for_iv.addWidget(self.p_left_frame_for_iv,0,Qt.AlignLeft)
        



        self.current_view = QLabel()
        self.current_view.setBackgroundRole(QPalette.Base)
        self.current_view.setSizePolicy(QSizePolicy.Ignored,
                                       QSizePolicy.Ignored)
        self.current_view.setScaledContents(True)

        self._scroll_area = QScrollArea(self.iv_page)
        self._scroll_area.setWidget(self.current_view)
        self._scroll_area.setMinimumSize(QSize(self._scroll_area.sizeHint()))
        self._scroll_area.setMinimumWidth(700)
        self.p_hb_for_iv.addWidget(self._scroll_area)
        #self._scroll_area.setVisFalse)









#vd==


#=========================================================================================
        self.vd_page = QWidget()
        self.vd_page.setObjectName(u"vd_page")
        self.p_hb_for_vd = QHBoxLayout(self.vd_page)
        self.p_hb_for_vd.setObjectName(u"gridLayout_2")


        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.vd_page.sizePolicy().hasHeightForWidth())

#=========================================================================================


        self.p_left_frame_for_vd = QFrame(self.vd_page)
        self.f_hb_for_p_left_frame_vd = QHBoxLayout(self.p_left_frame_for_vd)
        self.f_hb_for_p_left_frame_vd.setSpacing(0)
        self.f_hb_for_p_left_frame_vd.setObjectName(u"gauche")

#================================nram=========================================================
        self.treemodel_vd = QFileSystemModel()
        self.treemodel_vd.setObjectName('treeview')
        self.treemodel_vd.setRootPath(QDir.currentPath())
        self.treeview_vd = QTreeView()
        self.treeview_vd.setModel(self.treemodel_vd)
        self.treeview_vd.setSizePolicy(sizePolicy)
        self.treeview_vd.setStyleSheet("color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));")
        self.treeview_vd.setMinimumWidth(200)




        self.vd_list = QListWidget()
        self.vd_list.setObjectName('listOutput')
        self.vd_list.dragDropOverwriteMode()
        self.vd_list.setSizePolicy(sizePolicy)
        self.vd_list.setContentsMargins(10, 10, 10, 10)
        self.vd_list.setStyleSheet("color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));border: 1px double cyan;")






        self.f_hb_for_p_left_frame_vd.addWidget(self.treeview_vd,0,Qt.AlignLeft)
        self.f_hb_for_p_left_frame_vd.addWidget(self.vd_list,1,Qt.AlignRight)
        

        self.p_hb_for_vd.addWidget(self.p_left_frame_for_vd,0,Qt.AlignLeft)
        




        self._vid = QWidget(self.vd_page)
        self.p_hb_for_vd.addWidget(self._vid)









#==========================================process==========================================
        self.process_page = QWidget()
        self.process_page.setObjectName(u"process_page")

        self.verticalLayout_4_ = QVBoxLayout(self.process_page)
        self.verticalLayout_4_.setObjectName(u"verticalLayout_4_")
        self.verticalLayout_4_.setAlignment(Qt.AlignBottom)

        self.frame_3_ = QFrame(self.process_page)
        self.frame_3_.setObjectName(u"frame_3_")
        self.frame_3_.setMinimumSize(QSize(0, 40))
        self.frame_3_.setFrameShape(QFrame.StyledPanel)
        self.frame_3_.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7_ = QHBoxLayout(self.frame_3_)
        self.horizontalLayout_7_.setObjectName(u"horizontalLayout_7_")


        self.label_36_ = QLabel(self.frame_3_)
        self.label_36_.setObjectName(u"label_36_")
        self.label_36_.setFont(font2)
        self.label_36_.setStyleSheet(u"color: rgb(230, 5, 64);")
        self.label_36_.setText('PROCESS DATA')

        self.horizontalLayout_7_.addWidget(self.label_36_)

        self.frame_4_ = QFrame(self.frame_3_)
        self.frame_4_.setObjectName(u"frame_4_")
        self.frame_4_.setFrameShape(QFrame.StyledPanel)
        self.frame_4_.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8_ = QHBoxLayout(self.frame_4_)
        self.horizontalLayout_8_.setSpacing(0)
        self.horizontalLayout_8_.setObjectName(u"horizontalLayout_8_")
        self.horizontalLayout_8_.setContentsMargins(0, 0, 0, 0)
        self.activity_search = QLineEdit(self.frame_4_)
        self.activity_search.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_8_.addWidget(self.activity_search, 0, Qt.AlignCenter)



        self.horizontalLayout_7_.addWidget(self.frame_4_, 0, Qt.AlignRight)


        self.verticalLayout_4_.addWidget(self.frame_3_)
        

        self.tableWidget = QTableWidget()
        self.tableWidget.horizontalHeader().setStyleSheet(u"color: red;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
)
        self.tableWidget.verticalHeader().setStyleSheet(u"color: red;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)

        hd = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, hd)
        hd1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, hd1)
        hd2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, hd2)
        hd3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, hd3)
        hd4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, hd4)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setSizeIncrement(QSize(1, 1))
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(147)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_4_.addWidget(self.tableWidget,Qt.AlignCenter)

        self.activity_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search process name", None))

        fonthd = QFont()
        fonthd.setWeight(20)


        hd = self.tableWidget.horizontalHeaderItem(0)
        hd.setFont(fonthd)
        hd.setText(QCoreApplication.translate("MainWindow", u"Process ID", None));
        hd1 = self.tableWidget.horizontalHeaderItem(1)
        hd1.setFont(fonthd)
        hd1.setText(QCoreApplication.translate("MainWindow", u"Process Name", None));
        hd2 = self.tableWidget.horizontalHeaderItem(2)
        hd2.setFont(fonthd)
        hd2.setText(QCoreApplication.translate("MainWindow", u"Process Status", None));
        hd3 = self.tableWidget.horizontalHeaderItem(3)
        hd3.setFont(fonthd)
        hd3.setText(QCoreApplication.translate("MainWindow", u"Started", None));
        hd4 = self.tableWidget.horizontalHeaderItem(4)
        hd4.setFont(fonthd)
        hd4.setText(QCoreApplication.translate("MainWindow", u"Action", None));




        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_8 = QVBoxLayout(self.page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.page.setStyleSheet(
u"*{\n"
"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"border: 1px double cyan;border-radius: 5px;\n"
"}\n"
"#icon2{\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(238,174,202,1), stop:1 rgba(148,187,233,1));\n"
"   border: 1px solid rgb(9, 5, 13);\n"
"   padding: 5px 5px 5px 5px;\n"
"   border-radius: 5px;\n"
"   text-align: center;\n"
"   font-size: 30px;\n"
"}\n"
"#icon2:hover{\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(238,174,202,1), stop:1 rgba(148,187,233,1));\n"
"   border: 2px solid cyan;\n"
"   text-align: center;\n"
"   font-size: 50px;\n"
"}\n"
            )






        self.osm_page = QWidget()
        self.osm_page.setStyleSheet(
u"*{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"}\n"
"QLabel,QFrame{\n"
"background-color: transparent;"
"border: None;"
"}\n"
)
        self.osm_page.setObjectName(u"page")
        self.verticalLayout_8_osm = QVBoxLayout(self.osm_page)
        self.verticalLayout_8_osm.setObjectName(u"verticalLayout_8")

        self.scrollArea_osm_ = QScrollArea(self.osm_page)
        self.scrollArea_osm_.setObjectName(u"scrollArea")
        self.scrollArea_osm_.setWidgetResizable(True)
        self.scrollArea_osm_WidgetContents = QWidget()
        self.scrollArea_osm_WidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.verticalLayout_14_osm = QVBoxLayout(self.scrollArea_osm_WidgetContents)
        self.verticalLayout_14_osm.setObjectName(u"verticalLayout_14")
        self.webEngineView_osm = QWebEngineView(self.scrollArea_osm_WidgetContents)
        self.webEngineView_osm.setObjectName(u"webEngineView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.webEngineView_osm.sizePolicy().hasHeightForWidth())
        self.webEngineView_osm.setSizePolicy(sizePolicy2)
        self.webEngineView_osm.setMinimumSize(QSize(0, 0))
        self.webEngineView_osm.setUrl(QUrl(u"https://www.openstreetmap.org/"))

        self.verticalLayout_14_osm.addWidget(self.webEngineView_osm)

        self.scrollArea_osm_.setWidget(self.scrollArea_osm_WidgetContents)

        self.verticalLayout_8_osm.addWidget(self.scrollArea_osm_)



        self.y_page = QWidget()
        self.y_page.setStyleSheet(
u"*{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"}\n"
"QLabel,QFrame{\n"
"background-color: transparent;"
"border: None;"
"}\n"
)
        self.y_page.setObjectName(u"page")
        self.verticalLayout_8_y = QVBoxLayout(self.y_page)
        self.verticalLayout_8_y.setObjectName(u"verticalLayout_8")

        self.dtf_frame = QFrame(self.y_page)
        self.dtf_frame.setObjectName(u"dtf_frame")
        self.dtf_frame.setFrameShape(QFrame.StyledPanel)
        self.dtf_frame.setFrameShadow(QFrame.Raised)

        self.hlayout_5 = QHBoxLayout(self.dtf_frame)
        self.hlayout_5.setObjectName(u"hlayout_5")

        self.lineEdit2 = QLineEdit(self.frame)
        self.lineEdit2.setObjectName(u"lineEdit")
        self.hlayout_5.addWidget(self.lineEdit2,0,Qt.AlignLeft)
        self.lineEdit2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Set url and Download..", None))
        self.lineEdit2.setStyleSheet("border: 1px solid rgb(7 ,98 ,160);width: 160%;padding: 10px;border-radius:15px;")
        
        self.pushButton_down = QPushButton(self.dtf_frame)
        self.pushButton_down.setObjectName(u"pushButton_12")
        self.pushButton_down.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.pushButton_down.setStyleSheet("background-color: white;color: rgb(7 ,98 ,160);border: 1px solid rgb(7 ,98 ,160);width: 20%;padding: 10px;border-radius:15px;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_down.setIcon(icon2)
        self.pushButton_down.setIconSize(QSize(30, 30))
        self.hlayout_5.addWidget(self.pushButton_down)

        self.verticalLayout_8_y.addWidget(self.dtf_frame)

        self.scrollArea_y_ = QScrollArea(self.y_page)
        self.scrollArea_y_.setObjectName(u"scrollArea")
        self.scrollArea_y_.setWidgetResizable(True)
        self.scrollArea_y_WidgetContents = QWidget()
        self.scrollArea_y_WidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.verticalLayout_14_y = QVBoxLayout(self.scrollArea_y_WidgetContents)
        self.verticalLayout_14_y.setObjectName(u"verticalLayout_14")
        self.webEngineView_y = QWebEngineView(self.scrollArea_y_WidgetContents)
        self.webEngineView_y.setObjectName(u"webEngineView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.webEngineView_y.sizePolicy().hasHeightForWidth())
        self.webEngineView_y.setSizePolicy(sizePolicy2)
        self.webEngineView_y.setMinimumSize(QSize(0, 0))
        self.webEngineView_y.setUrl(QUrl(u"https://youtube.com"))

        self.verticalLayout_14_y.addWidget(self.webEngineView_y)

        self.scrollArea_y_.setWidget(self.scrollArea_y_WidgetContents)

        self.verticalLayout_8_y.addWidget(self.scrollArea_y_)





        self.i_page = QWidget()
        self.i_page.setStyleSheet(
u"*{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"}\n"
"QLabel,QFrame{\n"
"background-color: transparent;"
"border: None;"
"}\n"
)
        self.i_page.setObjectName(u"page")
        self.verticalLayout_8_i = QVBoxLayout(self.i_page)
        self.verticalLayout_8_i.setObjectName(u"verticalLayout_8")

        self.scrollArea_i_ = QScrollArea(self.i_page)
        self.scrollArea_i_.setObjectName(u"scrollArea")
        self.scrollArea_i_.setWidgetResizable(True)
        self.scrollArea_i_WidgetContents = QWidget()
        self.scrollArea_i_WidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.verticalLayout_14_i = QVBoxLayout(self.scrollArea_i_WidgetContents)
        self.verticalLayout_14_i.setObjectName(u"verticalLayout_14")
        self.webEngineView_i = QWebEngineView(self.scrollArea_i_WidgetContents)
        self.webEngineView_i.setObjectName(u"webEngineView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.webEngineView_i.sizePolicy().hasHeightForWidth())
        self.webEngineView_i.setSizePolicy(sizePolicy2)
        self.webEngineView_i.setMinimumSize(QSize(0, 0))
        self.webEngineView_i.setUrl(QUrl(u"https://instagram.com"))

        self.verticalLayout_14_i.addWidget(self.webEngineView_i)

        self.scrollArea_i_.setWidget(self.scrollArea_i_WidgetContents)

        self.verticalLayout_8_i.addWidget(self.scrollArea_i_)



        self.d_page = QWidget()
        self.d_page.setStyleSheet(
u"*{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"}\n"
"QLabel,QFrame{\n"
"background-color: transparent;"
"border: None;"
"}\n"
)
        self.d_page.setObjectName(u"page")
        self.verticalLayout_8_d = QVBoxLayout(self.d_page)
        self.verticalLayout_8_d.setObjectName(u"verticalLayout_8")

        self.scrollArea_d_ = QScrollArea(self.d_page)
        self.scrollArea_d_.setObjectName(u"scrollArea")
        self.scrollArea_d_.setWidgetResizable(True)
        self.scrollArea_d_didgetContents = QWidget()
        self.scrollArea_d_didgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.verticalLayout_14_d = QVBoxLayout(self.scrollArea_d_didgetContents)
        self.verticalLayout_14_d.setObjectName(u"verticalLayout_14")
        self.webEngineVied_d = QWebEngineView(self.scrollArea_d_didgetContents)
        self.webEngineVied_d.setObjectName(u"webEngineView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.webEngineVied_d.sizePolicy().hasHeightForWidth())
        self.webEngineVied_d.setSizePolicy(sizePolicy2)
        self.webEngineVied_d.setMinimumSize(QSize(0, 0))
        self.webEngineVied_d.setUrl(QUrl(u"https://dribbble.com"))

        self.verticalLayout_14_d.addWidget(self.webEngineVied_d)

        self.scrollArea_d_.setWidget(self.scrollArea_d_didgetContents)

        self.verticalLayout_8_d.addWidget(self.scrollArea_d_)



        self.f_page = QWidget()
        self.f_page.setStyleSheet(
u"*{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"}\n"
"QLabel,QFrame{\n"
"background-color: transparent;"
"border: None;"
"}\n"
)
        self.f_page.setObjectName(u"page")
        self.verticalLayout_8_f = QVBoxLayout(self.f_page)
        self.verticalLayout_8_f.setObjectName(u"verticalLayout_8")

        self.scrollArea_f_ = QScrollArea(self.f_page)
        self.scrollArea_f_.setObjectName(u"scrollArea")
        self.scrollArea_f_.setWidgetResizable(True)
        self.scrollArea_f_WidgetContents = QWidget()
        self.scrollArea_f_WidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.verticalLayout_14_f = QVBoxLayout(self.scrollArea_f_WidgetContents)
        self.verticalLayout_14_f.setObjectName(u"verticalLayout_14")
        self.webEngineView_f = QWebEngineView(self.scrollArea_f_WidgetContents)
        self.webEngineView_f.setObjectName(u"webEngineView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.webEngineView_f.sizePolicy().hasHeightForWidth())
        self.webEngineView_f.setSizePolicy(sizePolicy2)
        self.webEngineView_f.setMinimumSize(QSize(0, 0))
        self.webEngineView_f.setUrl(QUrl(u"https://facebook.com"))

        self.verticalLayout_14_f.addWidget(self.webEngineView_f)

        self.scrollArea_f_.setWidget(self.scrollArea_f_WidgetContents)

        self.verticalLayout_8_f.addWidget(self.scrollArea_f_)




        self.movie_page = QWidget()
        self.movie_page.setStyleSheet(
u"*{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));\n"
"}\n"
"QLabel,QFrame{\n"
"background-color: transparent;"
"border: None;"
"}\n"
)
        self.movie_page.setObjectName(u"page")
        self.verticalLayout_8_d = QVBoxLayout(self.movie_page)
        self.verticalLayout_8_d.setObjectName(u"verticalLayout_8")

        self.scrollArea_movie_ = QScrollArea(self.movie_page)
        self.scrollArea_movie_.setObjectName(u"scrollArea")
        self.scrollArea_movie_.setWidgetResizable(True)
        self.scrollArea_movie_didgetContents = QWidget()
        self.scrollArea_movie_didgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.verticalLayout_14_d = QVBoxLayout(self.scrollArea_movie_didgetContents)
        self.verticalLayout_14_d.setObjectName(u"verticalLayout_14")
        self.webEngineViemovie_d = QWebEngineView(self.scrollArea_movie_didgetContents)
        self.webEngineViemovie_d.setObjectName(u"webEngineView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.webEngineViemovie_d.sizePolicy().hasHeightForWidth())
        self.webEngineViemovie_d.setSizePolicy(sizePolicy2)
        self.webEngineViemovie_d.setMinimumSize(QSize(0, 0))
        self.webEngineViemovie_d.setUrl(QUrl(u"http://localhost/athena/video.html"))

        self.verticalLayout_14_d.addWidget(self.webEngineViemovie_d)

        self.scrollArea_movie_.setWidget(self.scrollArea_movie_didgetContents)

        self.verticalLayout_8_d.addWidget(self.scrollArea_movie_)


















        self.right_menu = QCustomSlideMenu()
        self.right_menu.setObjectName(u"right_menu")

        self.verticalLayout_21r = QVBoxLayout(self.right_menu)
        self.verticalLayout_21r.setSpacing(0)
        self.verticalLayout_21r.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21r.setContentsMargins(0, 0, 0, 0)



        self.frame_12r = QFrame(self.right_menu)
        self.frame_12r.setObjectName(u"notifications_widget")
        sizePolicy.setHeightForWidth(self.frame_12r.sizePolicy().hasHeightForWidth())
        self.frame_12r.setSizePolicy(sizePolicy)
        self.frame_12r.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));color: white;")
        self.frame_12r.setFrameShape(QFrame.StyledPanel)
        self.frame_12r.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16r = QVBoxLayout(self.frame_12r)
        self.verticalLayout_16r.setSpacing(10)
        self.verticalLayout_16r.setObjectName(u"verticalLayout_16")


        self.frame_audio = QFrame(self.frame_12r)
        self.frame_audio.setObjectName(u"frame_15")
        self.frame_audio.setFrameShape(QFrame.StyledPanel)
        self.frame_audio.setFrameShadow(QFrame.Raised)
        self.frame_audio.setStyleSheet(
u"*{background: transparent;}"
"#icon3{\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(238,174,202,1), stop:1 rgba(148,187,233,1));\n"
"   border: 1px solid rgb(9, 5, 13);\n"
"   padding: 5px 5px 5px 5px;\n"
"   border-radius: 5px;\n"
"   text-align: center;\n"
"}\n"
"#icon3:hover{\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(238,174,202,1), stop:1 rgba(148,187,233,1));\n"
"   border: 2px solid cyan;\n"
"   text-align: center;\n"
"}\n"
                )



        self.layout = QVBoxLayout(self.frame_audio)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.vlc = QFrame(self.frame_audio)


        self.layout1 = QHBoxLayout(self.vlc)
        self.layout1.setObjectName(u"horizontalLayout_16")

        self.repeat_btn = QPushButton(self.vlc)
        self.play_btn = QPushButton(self.vlc)
        self.left_btn = QPushButton(self.vlc)
        self.right_btn = QPushButton(self.vlc)
        self.stop_btn = QPushButton(self.vlc)
        self.playlist_btn = QPushButton(self.vlc)

        self.play_btn.setObjectName('icon3')
        self.play_btn.setBaseSize(QSize(50,50))
        self.left_btn.setObjectName('icon3')
        self.left_btn.setBaseSize(QSize(50,50))
        self.right_btn.setObjectName('icon3')
        self.right_btn.setBaseSize(QSize(50,50))
        self.stop_btn.setObjectName('icon3')
        self.stop_btn.setBaseSize(QSize(50,50))
        self.repeat_btn.setObjectName('icon3')
        self.repeat_btn.setBaseSize(QSize(50,50))
        self.repeat_btn.setIcon(QIcon(QPixmap(u":/icons/icons/repeat.svg")))
        self.playlist_btn.setObjectName('icon3')
        self.playlist_btn.setBaseSize(QSize(50,50))
        self.playlist_btn.setToolTip(u"use right click for more options")
        self.playlist_btn.setIcon(QIcon(QPixmap(u":/icons/icons/list.svg")))

        self.layout1.addWidget(self.repeat_btn,0,Qt.AlignLeft)
        self.layout1.addWidget(self.left_btn,0,Qt.AlignLeft)
        self.layout1.addWidget(self.play_btn,0,Qt.AlignHCenter)
        self.layout1.addWidget(self.right_btn,0,Qt.AlignRight)
        self.layout1.addWidget(self.stop_btn,0,Qt.AlignRight)
        self.layout1.addWidget(self.playlist_btn,0,Qt.AlignRight)


        




        font_ = QFont()
        font_.setPointSize(10)
        font_.setBold(True)
        font_.setWeight(5)


        self.titre_playlist = QLabel(self.frame_audio)
        self.titre_playlist.setStyleSheet("color: white;background-color: transparent;")
        self.titre_playlist.setFont(font_)








        self.level_sld = QSlider(self.frame_audio)
        self.level_sld.setOrientation(Qt.Horizontal)
        self.level_sld.setValue(50)

        

        self.pgf = QFrame(self.frame_audio)
        self.pgf.setStyleSheet(
u"#icon{\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(238,174,202,1), stop:1 rgba(148,187,233,1));\n"
"   border: 1px solid rgb(9, 5, 13);\n"
"   padding: 5px 5px 5px 5px;\n"
"   border-radius: 5px;\n"
"   text-align: center;\n"
"}\n"
"#icon:hover{\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(238,174,202,1), stop:1 rgba(148,187,233,1));\n"
"   border: 2px solid cyan;\n"
"   text-align: center;\n"
"}\n"
                )

        self.hpgf = QHBoxLayout(self.pgf)


        self.jfb = QPushButton()
        self.jfb.setObjectName("icon")
        self.hpgf.addWidget(self.jfb,0,Qt.AlignLeft)


        self.sp = roundProgressBar(self.pgf)
        self.sp.setObjectName(u"cpu_percentage")
        self.sp.setMinimumSize(QSize(100, 100))
        self.sp.setMaximumSize(QSize(100, 100))
            # SET PROGRESS BAR VALUE
        self.sp.rpb_setMaximum(3600) 
            # SET PROGRESS BAR STYLE
        self.sp.rpb_setBarStyle('Hybrid2')
            # SET PROGRESS BAR LINE COLOR
        self.sp.rpb_setLineColor((255, 30, 99))
            # SET PROGRESS BAR LINE COLOR
            # self.cpu_percentage[i].rpb_setCircleColor((45, 74, 83))
            # SET PROGRESS BAR LINE COLOR
        self.sp.rpb_setPieColor((45, 74, 83))
            #CHANGING THE PATH COLOR
            # self.cpu_percentage[i].rpb_setPathColor((45, 74, 83))
            #SET PROGRESS BAR TEXT COLOR
        self.sp.rpb_setTextColor((255, 255, 255)) 
            # SET PROGRESS BAR STARTING POSITION
            # North, East, West, South
        self.sp.rpb_setInitialPos('West')
            #SET PROGRESS BAR TEXT TYPE : VALUE OR PERCENTAGE
            # Value, Percentage
        self.sp.rpb_setTextFormat('Percentage')

            #SET PROGRESS BAR FONT
        self.sp.rpb_setTextFont('Arial')        
            #TEXT HIDDEN
            # self.cpu_percentage[i].rpb_enableText(False) 
            #SET PROGRESS BAR LINE WIDTH 
        self.sp.rpb_setLineWidth(7)
            #PATH WIDTH
        self.sp.rpb_setPathWidth(7)
            #SET PROGRESS BAR LINE CAP
            # RoundCap, SquareCap
        self.sp.rpb_setLineCap('RoundCap')

        self.hpgf.addWidget(self.sp,0,Qt.AlignHCenter)




        self.jrb = QPushButton()
        self.jrb.setObjectName("icon")
        self.hpgf.addWidget(self.jrb,0,Qt.AlignRight)


        self.lp2 = QLabel()
        self.lp2.setMaximumSize(QSize(250,100))
        self.lp2.setBackgroundRole(QPalette.Base)
        self.lp2.setScaledContents(True)
        self.lp2.hide()

        #self.mv2 = QMovie(".\\images\\gif\\9LJ3.gif")
        self.mv2 = QMovie(".\\images\\gif\\XDZT.gif")
        self.lp2.setMovie(self.mv2)


        self.layout.addWidget(self.lp2,0,Qt.AlignVCenter|Qt.AlignTop)
        self.layout.addWidget(self.pgf,0,Qt.AlignVCenter|Qt.AlignTop)
        self.layout.addWidget(self.vlc,0,Qt.AlignVCenter|Qt.AlignTop)
        self.layout.addWidget(self.level_sld,0,Qt.AlignVCenter|Qt.AlignTop)
        self.layout.addWidget(self.titre_playlist,0,Qt.AlignVCenter|Qt.AlignTop)
        self.pgf.hide()

        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.right_menu.sizePolicy().hasHeightForWidth())


        


        self.list_music = QListWidget(self.frame_audio)
        self.list_music.setObjectName('list_music')
        self.list_music.setStyleSheet("color: white;background-color: transparent;height: auto;")
        self.list_music.setAutoScroll(True)
        self.list_music.setSizePolicy(sizePolicy2)
        self.list_music.setSelectionRectVisible(True)
        self.list_music.setUniformItemSizes(True)
        self.list_music.setMinimumHeight(250)
        self.list_music.setMaximumHeight(10000)
        
        self.layout.addWidget(self.list_music,1,Qt.AlignVCenter|Qt.AlignTop)



        self.verticalLayout_16r.addWidget(self.frame_audio)






































        self.verticalLayout_21r.addWidget(self.frame_12r, 0, Qt.AlignTop)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.frame_26r = QFrame(self.right_menu)
        self.frame_26r.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));color: white;")
        self.frame_26r.setObjectName(u"frame_26")
        self.frame_26r.setFrameShape(QFrame.StyledPanel)
        self.frame_26r.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_26r)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.music_search = QLineEdit()
        self.music_search.setObjectName("music_search")
        self.search_menu_btn = QPushButton(self.frame_26r)
        self.search_menu_btn.setObjectName(u"search_menu_btn")
        self.search_menu_btn.setIcon(icon8)
        self.horizontalLayout_11.addWidget(self.music_search)
        self.horizontalLayout_11.addWidget(self.search_menu_btn)


        self.verticalLayout_21r.addWidget(self.frame_26r, 0, Qt.AlignBottom)














#=========main body======================
        self.m_m = QWidget(self.centralwidget)
        self.h_m = QHBoxLayout(self.m_m)
        self.m_m.setObjectName(u"home")

        self.tabWidget = QTabWidget(self.m_m)
        self.tabWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setStyleSheet(u"background: transparent;")
        self.tabWidget.addTab(self.frame_16,QIcon(QPixmap(u":/icons/icons/lock.svg")),"Login")
        self.tabWidget.tabBarAutoHide()
        self.tabWidget.setMovable(True)
        self.tabWidget.tabsClosable()
        
        







        self.left_menu_toggle = QCustomSlideMenu(self.m_m)
        self.left_menu_toggle.setObjectName("left_menu_toggle")
        self.left_menu_toggle.setMinimumWidth(150)
        self.left_menu_toggle.setSizePolicy(sizePolicy)
        #self.left_menu_toggle.setContentsMargins(-1,10,10,10)

        self.bl = QHBoxLayout(self.left_menu_toggle)
        self.list_model = QStandardItemModel(0, 0, self.left_menu_toggle)


        self.list_model.appendRow(QStandardItem(QIcon(QPixmap("./images/icons8-personne-homme-94.png")), "Directory"))
        self.list_model.appendRow(QStandardItem(QIcon(QPixmap("./images/icons8-personne-homme-94.png")), "Computer"))

        self.icon_mode_listview = QListView(self.left_menu_toggle)

        self.icon_mode_listview.setViewMode(QListView.IconMode)
        self.icon_mode_listview.setModel(self.list_model)








        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.left_menu_toggle.sizePolicy().hasHeightForWidth())

        self.star_menu = QFrame()
        self.star_menu.setSizePolicy(sizePolicy)
        self.bl.addWidget(self.star_menu,0,Qt.AlignLeft)
        self.bl.addWidget( self.icon_mode_listview,0,Qt.AlignRight)

        self.lmb_hl = QVBoxLayout(self.star_menu)

        #=====================================================================
        self.bg_ = QPushButton()
        self.lmb_hl.addWidget(self.bg_,0,Qt.AlignCenter)

        self.bg_2 = QPushButton()
        self.lmb_hl.addWidget(self.bg_2,0,Qt.AlignCenter)

        self.bg_3 = QPushButton()
        self.lmb_hl.addWidget(self.bg_3,0,Qt.AlignCenter)


        self.bg_4 = QPushButton()
        self.lmb_hl.addWidget(self.bg_4,0,Qt.AlignCenter)


        self.bg_5 = QPushButton()
        self.lmb_hl.addWidget(self.bg_5,0,Qt.AlignCenter)

        self.bg_6 = QPushButton()
        self.lmb_hl.addWidget(self.bg_6,0,Qt.AlignCenter)

        self.bg_7 = QPushButton()
        self.lmb_hl.addWidget(self.bg_7,0,Qt.AlignCenter)

        self.r_frame = QFrame()
        self.r_frame.setStyleSheet(u"background-color: transparent;margin-right: 1px;")
        self.r_frame.setContentsMargins(0,0,0,0)
        self.r_hb = QHBoxLayout(self.r_frame)









        self.hb = QHBoxLayout(self.home)

        self.frame_app = QCustomSlideMenu()
        self.frame_app.setObjectName(u"frame_app")
        self.frame_app.setContentsMargins(0,0,0,0)
        self.icon_list = QGridLayout(self.frame_app)
        self.icon_list.setObjectName(u"icon")
        
        self.hb.addWidget(self.frame_app,0,Qt.AlignLeft)
        self.hb.addWidget(self.bottom_menu,0,Qt.AlignBottom|Qt.AlignCenter)
        
        self.r_hb.addWidget(self.notifications_widget,0,Qt.AlignRight)
        self.r_hb.addWidget(self.right_menu,0,Qt.AlignRight)

        self.hb.addWidget(self.r_frame,0,Qt.AlignRight)
        
        #=====================================================================
        self.search_icon = DragButton(self.frame_app)
        search_icon = QIcon()
        search_icon.addFile(u"./images/icons8-logo-google-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_icon.setIcon(search_icon)
        self.search_icon.setIconSize(QSize(30,30))
        self.search_icon.setToolTip("Min Browser")
        self.icon_list.addWidget(self.search_icon,0,1,Qt.AlignLeft)
        #=====================================================================
        self.map_icon = DragButton(self.home)
        self.map_icon.setObjectName(u"icon")
        map_icon = QIcon()
        map_icon.addFile(u"./images/icons8-marqueur-de-plan-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.map_icon.setIcon(map_icon)
        self.map_icon.setIconSize(QSize(30,30))
        self.map_icon.setToolTip("OSM")
        self.icon_list.addWidget(self.map_icon,1,1,Qt.AlignLeft)
        #=====================================================================
        self.dribbble_icon = DragButton()
        self.dribbble_icon.setObjectName(u"icon")
        dribbble_icon = QIcon()
        dribbble_icon.addFile(u":/icons/icons/dribbble.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dribbble_icon.setIcon(dribbble_icon)
        self.dribbble_icon.setIconSize(QSize(30,30))
        self.dribbble_icon.setToolTip("Dribbble")
        self.icon_list.addWidget(self.dribbble_icon,2,1,Qt.AlignLeft)
        #=====================================================================
        self.facebook_icon = DragButton(self.frame_app)
        self.facebook_icon.setObjectName(u"icon")
        facebook_icon = QIcon()
        facebook_icon.addFile(u"./images/icons8-facebook-entouré-188.png", QSize(), QIcon.Normal, QIcon.Off)
        self.facebook_icon.setIcon(facebook_icon)
        self.facebook_icon.setIconSize(QSize(30,30))
        self.facebook_icon.setToolTip("Facebook")
        self.icon_list.addWidget(self.facebook_icon,3,1,Qt.AlignLeft)
        #=====================================================================
        self.youtube_icon = DragButton(self.frame_app)
        self.youtube_icon.setObjectName(u"icon")
        youtube_icon = QIcon()
        youtube_icon.addFile(u"./images/icons8-lecture-de-youtube-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.youtube_icon.setIcon(youtube_icon)
        self.youtube_icon.setIconSize(QSize(30,30))
        self.youtube_icon.setToolTip("YouTube")
        self.icon_list.addWidget(self.youtube_icon,4,1,Qt.AlignLeft)
        #=====================================================================
        self.user_icon = DragButton(self.frame_app)
        self.user_icon.setObjectName(u"icon")
        user_icon = QIcon()
        user_icon.addFile(u"./images/icons8-facebook-messenger-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.user_icon.setIcon(user_icon)
        self.user_icon.setIconSize(QSize(30,30))
        self.user_icon.setToolTip("Facebook messenger")
        self.icon_list.addWidget(self.user_icon,5,1,Qt.AlignLeft)
        #=====================================================================
        self.instagram_icon = DragButton(self.frame_app)
        self.instagram_icon.setObjectName(u"icon")
        instagram_icon = QIcon()
        instagram_icon.addFile(u"./images/icons8-instagram-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.instagram_icon.setIcon(instagram_icon)
        self.instagram_icon.setIconSize(QSize(30,30))
        self.instagram_icon.setToolTip("Instagram")
        self.icon_list.addWidget(self.instagram_icon,6,1,Qt.AlignLeft)
        #=====================================================================
        self.cpu_icon = DragButton(self.frame_app)
        self.cpu_icon.setObjectName(u"icon")
        cpu_icon = QIcon()
        cpu_icon.addFile(u":/icons/icons/cpu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cpu_icon.setIcon(cpu_icon)
        self.cpu_icon.setIconSize(QSize(30,30))
        self.cpu_icon.setToolTip("Central process unit")
        self.icon_list.addWidget(self.cpu_icon,7,1,Qt.AlignLeft)
        #=====================================================================
        self.battery_icon = DragButton(self.frame_app)
        self.battery_icon.setObjectName(u"icon")
        battery_icon = QIcon()
        battery_icon.addFile(u"./images/icons8-batterie-pleine-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.battery_icon.setIcon(battery_icon)
        self.battery_icon.setIconSize(QSize(30,30))
        self.battery_icon.setToolTip("Battery setting")
        self.icon_list.addWidget(self.battery_icon,8,1,Qt.AlignLeft)
        #=====================================================================
        self.archive_icon = DragButton(self.frame_app)
        self.archive_icon.setObjectName(u"icon")
        archive_icon = QIcon()
        archive_icon.addFile(u"./images/icons8-dossier-de-films-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.archive_icon.setIcon(archive_icon)
        self.archive_icon.setIconSize(QSize(30,30))
        self.archive_icon.setToolTip("Movies Folder")
        self.icon_list.addWidget(self.archive_icon,9,1,Qt.AlignLeft)
        #=====================================================================
        self.download_icon = DragButton(self.frame_app)
        self.download_icon.setObjectName(u"icon")
        download_icon = QIcon()
        download_icon.addFile(u"./images/icons8-nuage-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.download_icon.setIcon(download_icon)
        self.download_icon.setIconSize(QSize(30,30))
        self.icon_list.addWidget(self.download_icon,4,0,Qt.AlignLeft)
        self.download_icon.setAcceptDrops(True)
        self.download_icon.setCheckable(True)
        self.download_icon.setToolTip("Mino Cloud")
        #=====================================================================
        self.home_icon = DragButton(self.frame_app)
        self.home_icon.setObjectName(u"icon")
        home_icon = QIcon()
        home_icon.addFile(u"./images/icons8-ssd-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_icon.setIcon(home_icon)
        self.home_icon.setIconSize(QSize(30,30))
        self.icon_list.addWidget(self.home_icon,5,0,Qt.AlignLeft)
        self.home_icon.setAcceptDrops(True)
        self.home_icon.setCheckable(True)
        self.home_icon.setToolTip("Driver")
        #=====================================================================
        self.ram_icon = DragButton(self.frame_app)
        self.ram_icon.setObjectName(u"icon")
        ram_icon = QIcon()
        ram_icon.addFile(u"./images/icons8-emplacement-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ram_icon.setIcon(ram_icon)
        self.ram_icon.setIconSize(QSize(30,30))
        self.icon_list.addWidget(self.ram_icon,6,0,Qt.AlignLeft)
        self.ram_icon.setAcceptDrops(True)
        self.ram_icon.setCheckable(True)
        self.ram_icon.setToolTip("Read only memory")
        #=====================================================================
        self.thrending_icon = DragButton(self.frame_app)
        self.thrending_icon.setObjectName(u"icon")
        thrending_icon = QIcon()
        thrending_icon.addFile(u":/icons/icons/trending-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.thrending_icon.setIcon(thrending_icon)
        self.thrending_icon.setIconSize(QSize(30,30))
        self.icon_list.addWidget(self.thrending_icon,7,0,Qt.AlignLeft)
        self.thrending_icon.setAcceptDrops(True)
        self.thrending_icon.setCheckable(True)
        self.thrending_icon.setToolTip("Process")
        #=====================================================================
        self.movie_icon = DragButton(self.frame_app)
        self.movie_icon.setObjectName(u"icon")
        movie_icon = QIcon()
        movie_icon.addFile(u"./images/icons8-ios-photos-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.movie_icon.setIcon(movie_icon)
        self.movie_icon.setIconSize(QSize(30,30))
        self.icon_list.addWidget(self.movie_icon,8,0,Qt.AlignLeft)
        self.movie_icon.setAcceptDrops(True)
        self.movie_icon.setCheckable(True)
        self.movie_icon.setToolTip("Photos")
        #=====================================================================
        self.songs_icon = DragButton(self.frame_app)
        self.songs_icon.setObjectName(u"songs_icon")
        songs_icon = QIcon()
        songs_icon.addFile(u"./images/icons8-notes-de-musique-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.songs_icon.setIcon(songs_icon)
        self.songs_icon.setIconSize(QSize(30,30))
        self.icon_list.addWidget(self.songs_icon,9,0,Qt.AlignLeft)
        self.songs_icon.setAcceptDrops(True)
        self.songs_icon.setCheckable(True)
        self.songs_icon.setToolTip("Musique")
        #=====================================================================
        self.git_icon = DragButton(self.frame_app)
        self.git_icon.setObjectName(u"icon")
        git_icon = QIcon()
        git_icon.addFile(u"./images/icons8-github-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.git_icon.setIcon(git_icon)
        self.git_icon.setIconSize(QSize(30,30))
        self.icon_list.addWidget(self.git_icon,0,2,Qt.AlignLeft)
        self.git_icon.setAcceptDrops(True)
        self.git_icon.setCheckable(True)
        self.git_icon.setToolTip("Github")
        #=====================================================================
        self.red_icon = DragButton(self.frame_app)
        self.red_icon.setObjectName(u"icon")
        red_icon = QIcon()
        red_icon.addFile(u"./images/icons8-reddit-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.red_icon.setIcon(red_icon)
        self.red_icon.setIconSize(QSize(30,30))
        self.icon_list.addWidget(self.red_icon,1,2,Qt.AlignLeft)
        self.red_icon.setAcceptDrops(True)
        self.red_icon.setCheckable(True)
        self.red_icon.setToolTip("Reddit")
        #=====================================================================
        self.pint_icon = DragButton(self.frame_app)
        self.pint_icon.setObjectName(u"icon")
        pint_icon = QIcon()
        pint_icon.addFile(u"./images/icons8-pinterest-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pint_icon.setIcon(pint_icon)
        self.pint_icon.setIconSize(QSize(30,30))
        self.icon_list.addWidget(self.pint_icon,3,2,Qt.AlignLeft)
        self.pint_icon.setAcceptDrops(True)
        self.pint_icon.setCheckable(True)
        self.pint_icon.setToolTip("Pinterest")
        #=====================================================================
        self.zap_icon = DragButton(self.frame_app)
        self.zap_icon.setObjectName(u"icon")
        zap_icon = QIcon()
        zap_icon.addFile(u"./images/icons8-whatsapp-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.zap_icon.setIcon(zap_icon)
        self.zap_icon.setIconSize(QSize(30,30))
        self.icon_list.addWidget(self.zap_icon,4,2,Qt.AlignLeft)
        self.zap_icon.setAcceptDrops(True)
        self.zap_icon.setCheckable(True)
        self.zap_icon.setToolTip("Whatsapp")
        #=====================================================================
        self.nflix_icon = DragButton(self.frame_app)
        self.nflix_icon.setObjectName(u"icon")
        nflix_icon = QIcon()
        nflix_icon.addFile(u"./images/icons8-application-de-bureau-netflix-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nflix_icon.setIcon(nflix_icon)
        self.nflix_icon.setIconSize(QSize(30,30))
        self.icon_list.addWidget(self.nflix_icon,2,2,Qt.AlignLeft)
        self.nflix_icon.setAcceptDrops(True)
        self.nflix_icon.setCheckable(True)
        self.nflix_icon.setToolTip("NetFlix")
        #=====================================================================
        self.vlc_icon = DragButton(self.frame_app)
        self.vlc_icon.setObjectName(u"icon")
        vlc_icon = QIcon()
        vlc_icon.addFile(u"./images/icons8-vlc-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.vlc_icon.setIcon(vlc_icon)
        self.vlc_icon.setIconSize(QSize(30,30))
        self.icon_list.addWidget(self.vlc_icon,5,2,Qt.AlignLeft)
        self.vlc_icon.setAcceptDrops(True)
        self.vlc_icon.setCheckable(True)
        self.vlc_icon.setToolTip("Vlc")
        #=====================================================================
        self.telegram_icon = DragButton(self.frame_app)
        self.telegram_icon.setObjectName(u"icon")
        telegram_icon = QIcon()
        telegram_icon.addFile(u"./images/icons8-telegram-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.telegram_icon.setIcon(telegram_icon)
        self.telegram_icon.setIconSize(QSize(30,30))
        self.icon_list.addWidget(self.telegram_icon,6,2,Qt.AlignLeft)
        self.telegram_icon.setAcceptDrops(True)
        self.telegram_icon.setCheckable(True)
        self.telegram_icon.setToolTip("Telegram")
        #=====================================================================
        self.vk_icon = DragButton(self.frame_app)
        self.vk_icon.setObjectName(u"icon")
        vk_icon = QIcon()
        vk_icon.addFile(u"./images/icons8-vk.com-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.vk_icon.setIcon(vk_icon)
        self.vk_icon.setIconSize(QSize(30,30))
        self.icon_list.addWidget(self.vk_icon,7,2,Qt.AlignLeft)
        self.vk_icon.setAcceptDrops(True)
        self.vk_icon.setCheckable(True)
        self.vk_icon.setToolTip("Vk")
        #=====================================================================
        self.bc_icon = DragButton(self.frame_app)
        self.bc_icon.setObjectName(u"icon")
        bc_icon = QIcon()
        bc_icon.addFile(u"./images/icons8-bulle-de-conversation-avec-points-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bc_icon.setIcon(bc_icon)
        self.bc_icon.setIconSize(QSize(30,30))
        self.icon_list.addWidget(self.bc_icon,8,2,Qt.AlignLeft)
        self.bc_icon.setAcceptDrops(True)
        self.bc_icon.setCheckable(True)
        self.bc_icon.setToolTip("Mino messenger")
        #=====================================================================
        self.cl_icon = DragButton(self.frame_app)
        self.cl_icon.setObjectName(u"icon")
        cl_icon = QIcon()
        cl_icon.addFile(u"./images/icons8-calendrier-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cl_icon.setIcon(cl_icon)
        self.cl_icon.setIconSize(QSize(30,30))
        self.icon_list.addWidget(self.cl_icon,9,2,Qt.AlignLeft)
        self.cl_icon.setAcceptDrops(True)
        self.cl_icon.setCheckable(True)
        self.cl_icon.setToolTip("Calendar")


















        self.h_m.setContentsMargins(0,0,0,0)
        self.h_m.addWidget(self.left_menu_toggle)
        self.h_m.addWidget(self.tabWidget)
       

        self.verticalLayout.addWidget(self.m_m)



































        self.widget_7 = QWidget(self.centralwidget)
        self.widget_7.setMaximumHeight(40)
        self.widget_7.setStyleSheet(u"color: white;background-color: qlineargradient(spread:pad, x1:0, y1:0.989, x2:0.977273, y2:0.051, stop:0 rgba(35, 25, 73, 255), stop:1 rgba(0, 91, 156, 81));")

        self.horizontalLayout_4 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)


        self.left_menu_btn = QPushButton(self.widget_7)
        self.left_menu_btn.setObjectName(u"left_menu_btn")
        self.left_menu_btn.setStyleSheet(u"margin-left: 5px;")
        icon1 = QIcon()
        icon1.addFile(u"./images/toastlogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.left_menu_btn.setIcon(icon1)
        self.left_menu_btn.setIconSize(QSize(18, 18))
        self.horizontalLayout_4.addWidget(self.left_menu_btn , 0,Qt.AlignLeft)
        #===================================================================================

        self.footer = QFrame(self.widget_7)
        self.footer.setStyleSheet(
                u"*{\n"
                "color: white;\n"
                "background-color: transparent;\n"
                "}\n"
                )
        sizePolicy.setHeightForWidth(self.footer.sizePolicy().hasHeightForWidth())
        self.footer.setSizePolicy(sizePolicy)
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)

        self.toast_bar = QHBoxLayout(self.footer)
        self.toast_bar.setObjectName(u"toast_bar")

        #===================================================================================

        self.left_lineEdit = QLineEdit(self.footer)
        self.left_lineEdit.setObjectName(u"left_lineEdit")
        self.left_lineEdit.setStyleSheet(u"background-color: transparent;color: white;border-bottom: none")
        self.left_lineEdit.setMinimumSize(QSize(250, 3))
        self.left_lineEdit.setPlaceholderText(u"Taper ici pour rechercher")
        self.toast_bar.addWidget(self.left_lineEdit , 0, Qt.AlignLeft)
        #===================================================================================

        self.Btn_messages = QPushButton(self.footer)
        self.Btn_messages.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/icons8-bulle-de-conversation-avec-points-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_messages.setIcon(icon22)

        self.toast_bar.addWidget(self.Btn_messages,0,Qt.AlignLeft)

        #===================================================================================

        self.BackgroundAccess_btn = QPushButton(self.footer)
        self.BackgroundAccess_btn.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/icons8-logo-google-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BackgroundAccess_btn.setIcon(icon22)

        self.toast_bar.addWidget(self.BackgroundAccess_btn,0,Qt.AlignLeft)
        #===================================================================================

        self.BackgroundAccess_btn2 = QPushButton(self.footer)
        self.BackgroundAccess_btn2.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/icons8-appareil-photo-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BackgroundAccess_btn2.setIcon(icon22)

        self.toast_bar.addWidget(self.BackgroundAccess_btn2,0,Qt.AlignLeft)
        #===================================================================================

        self.Ba = QPushButton(self.footer)
        self.Ba.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/icons8-vlc-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Ba.setIcon(icon22)

        self.toast_bar.addWidget(self.Ba,0,Qt.AlignLeft)
        #===================================================================================

        self.Ba = QPushButton(self.footer)
        self.Ba.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/icons8-whatsapp-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Ba.setIcon(icon22)

        self.toast_bar.addWidget(self.Ba,0,Qt.AlignLeft)
        #===================================================================================
           

        self.Ba = QPushButton(self.footer)
        self.Ba.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/icons8-reddit-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Ba.setIcon(icon22)

        self.toast_bar.addWidget(self.Ba,0,Qt.AlignLeft)
        #===================================================================================
           

        self.Ba = QPushButton(self.footer)
        self.Ba.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/icons8-facebook-entouré-188.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Ba.setIcon(icon22)

        self.toast_bar.addWidget(self.Ba,0,Qt.AlignLeft)
        #===================================================================================      
           

        self.Ba = QPushButton(self.footer)
        self.Ba.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/icons8-facebook-messenger-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Ba.setIcon(icon22)

        self.toast_bar.addWidget(self.Ba,0,Qt.AlignLeft)
        #===================================================================================      

           

        self.Ba = QPushButton(self.footer)
        self.Ba.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/icons8-ios-photos-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Ba.setIcon(icon22)

        self.toast_bar.addWidget(self.Ba,0,Qt.AlignLeft)
        #===================================================================================      

           

        self.Ba = QPushButton(self.footer)
        self.Ba.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/icons8-map-as-drive-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Ba.setIcon(icon22)

        self.toast_bar.addWidget(self.Ba,0,Qt.AlignLeft)
        #===================================================================================      
           

        self.Ba = QPushButton(self.footer)
        self.Ba.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/icons8-calendrier-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Ba.setIcon(icon22)

        self.toast_bar.addWidget(self.Ba,0,Qt.AlignLeft)
        #===================================================================================      
           

        self.Bax = QPushButton(self.footer)
        self.Bax.setObjectName(u"Bax")
        icon22 = QIcon()
        icon22.addFile(u"./images/icons8-notes-de-musique-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Bax.setIcon(icon22)

        self.toast_bar.addWidget(self.Bax,0,Qt.AlignLeft)
        #===================================================================================      
           

        self.Ba = QPushButton(self.footer)
        self.Ba.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/icons8-bouclier-de-l'utilisateur-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Ba.setIcon(icon22)

        self.toast_bar.addWidget(self.Ba,0,Qt.AlignLeft)
        #===================================================================================      
           

        self.Ba = QPushButton(self.footer)
        self.Ba.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/icons8-vk.com-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Ba.setIcon(icon22)

        self.toast_bar.addWidget(self.Ba,0,Qt.AlignLeft)
        #===================================================================================      



        self.DMR_48_btn = QPushButton(self.footer)
        self.DMR_48_btn.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/DMR_48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.DMR_48_btn.setIcon(icon22)


        self.toast_bar.addWidget(self.DMR_48_btn,0,Qt.AlignRight)








        self.Vpn_btn = QPushButton(self.footer)
        self.Vpn_btn.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/@VpnToastIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Vpn_btn.setIcon(icon22)


        self.toast_bar.addWidget(self.Vpn_btn,0,Qt.AlignRight)






        self.optionalfeatures_btn = QPushButton(self.footer)
        self.optionalfeatures_btn.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/@optionalfeatures.png", QSize(), QIcon.Normal, QIcon.Off)
        self.optionalfeatures_btn.setIcon(icon22)


        self.toast_bar.addWidget(self.optionalfeatures_btn,0,Qt.AlignRight)







        self.bottom_menu_button = QPushButton(self.footer)
        self.bottom_menu_button.setObjectName(u"icon")

        self.toast_bar.addWidget(self.bottom_menu_button, 0, Qt.AlignHCenter)



        self.Defendericon_btn = QPushButton(self.footer)
        self.Defendericon_btn.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/Defendericon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Defendericon_btn.setIcon(icon22)


        self.toast_bar.addWidget(self.Defendericon_btn,0,Qt.AlignRight)





        self.audio_btn = QPushButton(self.footer)
        self.audio_btn.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/@AudioToastIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.audio_btn.setIcon(icon22)


        self.toast_bar.addWidget(self.audio_btn,0,Qt.AlignRight)




        self.WiFiNotificationIcon_btn = QPushButton(self.footer)
        self.WiFiNotificationIcon_btn.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/@WiFiNotificationIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.WiFiNotificationIcon_btn.setIcon(icon22)


        self.toast_bar.addWidget(self.WiFiNotificationIcon_btn,0,Qt.AlignRight)



        self.Notifier_btn = QPushButton(self.footer)
        self.Notifier_btn.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/@NotifierToastIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Notifier_btn.setIcon(icon22)


        self.toast_bar.addWidget(self.Notifier_btn,0,Qt.AlignRight)







        self.Enrollement_btn = QPushButton(self.footer)
        self.Enrollement_btn.setObjectName(u"icon")
        icon22 = QIcon()
        icon22.addFile(u"./images/@EnrollementToastIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Enrollement_btn.setIcon(icon22)


        self.toast_bar.addWidget(self.Enrollement_btn,0,Qt.AlignRight)








 










        self.right_menu_toggle_btn = QPushButton(self.footer)
        self.right_menu_toggle_btn.setObjectName(u"right_menu_toggle_btn")
        icon22 = QIcon()
        icon22.addFile(u"./images/icons8-cloche-94.png", QSize(), QIcon.Normal, QIcon.Off)
        self.right_menu_toggle_btn.setIcon(icon22)


        self.toast_bar.addWidget(self.right_menu_toggle_btn,0,Qt.AlignRight)



        self.horizontalLayout_4.addWidget(self.footer)






        self.size_grip = QFrame(self.widget_7)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(20, 40))
        self.size_grip.setMaximumSize(QSize(20, 40))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.size_grip)


        self.verticalLayout.addWidget(self.widget_7)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u" M I n o ", None))
        self.restoreWindow.setText("")
        self.minimizeWindow.setText("")
        self.closeWindow.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<big><b><h1> M I n o </h1></b></big>", None))





"""
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

        if len(self.image_file_list)>0:
            self.load_ivfile(self.image_file_list[0])

        if  self.first_loard:
            self.ui._scroll_area.setVisible(True)
            self.first_loard = False


    def load_ivfile(self,filename=None):

        if filename != None:
            try:
                if filename.endswith('.gif'):
                    self.gif_content = QMovie(filename)
                    self.ui.current_view.setMovie(self.gif_content)
                    self.gif_content.start()
                    self.gif_l = True
                else:
                    self.ui.current_view.setPixmap(QPixmap(filename))
                    if self.gif_l:
                        self.gif_content.stop()
                        self.gif_l = False
                self._fit_to_window()
            except:
                self.image_file_list.remove(filename)

            if filename.rpartition(".")[2].lower() in self.image_can_seek:
                self.ui.img_list.setFocus()
            else:
                speak("file does not support seeking")




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
        self.cls_f()
        if True:
            self.last_ivlen = len(self.image_file_list)
            if _path is None:
                pass
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
                pass
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




    def load_iv(self,_path=None):
        self.cls_f()
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

            if len(self.image_file_list) != self.last_ivlen:
                playsound("./Themes/Halo 4 He/windows ding.wav",block=False)
"""
    