# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '帮助文档界面.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\',\'宋体\'; font-size:36pt; font-weight:600; color:#000000;\">图像分割系统特点以及使用教程</span></h3>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:medium; font-weight:600; color:#333333;\">1.主要特点</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">该系统是基于python开发的,无需安装可直接使用。</span></li>\n"
"<li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">分割的效果可以直接显示在分割的界面。</span></li>\n"
"<li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">可以进行交互式分割。</span></li>\n"
"<li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">结和了滤波器，形态学，以及边缘检测。</span></li>\n"
"<li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">具有批量分割功能。</span></li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:medium; font-weight:600; color:#333333;\">2.基本操作</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:small; font-weight:600; color:#333333;\">一、自动分割</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">打开软件后进入主界面后点击 文件 -&gt; 打开 选择要分割图像</span></li>\n"
"<li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; background-color:#ffffff;\">进入文件选择界面后选择要分割的图像可以选择多张</span></li>\n"
"<li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">选择后进入分割界面，可以进行添加，删除等操作。</span></li>\n"
"<li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">单击要分割的图像，调整好需要的参数后点击开始分割，就能得到效果图像，如需保存直接点击保存即可。。</span></li>\n"
"<li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">若需要批量分割勾选相应的复选框，若没有选择保存路径，会提示选择保存路径，分割完成后会自动保存到指定目录。</span></li>\n"
"<li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333; background-color:#ffffff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">点击开始分割，会显示分割的进度。</span></li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:7pt; font-weight:600;\">二、交互分割说明：</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333; background-color:#ffffff;\">注：对于分割效果不是特别好的图像可以进行交互式分割。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333; background-color:#ffffff;\">1.选择交互式分割选项点击开始分割</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333; background-color:#ffffff;\">2.点击后会显示两个窗口，一个用于输入，一个用于输出。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333; background-color:#ffffff;\">3.首先，在输入窗口中，使用鼠标右键框选出前景区域。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333; background-color:#ffffff;\">4.然后按“ n”分割对象（一次或几次）要进行更精细的修饰，您可以按以下以下键并按下鼠标左键进行绘制。 然后再次按“ n”更新输出。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333; background-color:#ffffff;\">5.s-分割完成并退出（如果需要保存图片请点击保存图片即可）</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">交互分割快捷键：</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt; color:#0000ff;\">“ 0”-</span><span style=\" font-family:\'Calibri\',\'宋体\'; font-size:10.5pt; color:#0000ff;\">选择有背景的区域</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt; color:#0000ff;\">“ 1”-</span><span style=\" font-family:\'Calibri\',\'宋体\'; font-size:10.5pt; color:#0000ff;\">选择肯定前景的区域</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt; color:#0000ff;\">“ 2”-</span><span style=\" font-family:\'Calibri\',\'宋体\'; font-size:10.5pt; color:#0000ff;\">选择可能背景的区域</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt; color:#0000ff;\">“ 3”-</span><span style=\" font-family:\'Calibri\',\'宋体\'; font-size:10.5pt; color:#0000ff;\">选择可能的前景区域</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt; color:#0000ff;\">“ n”-</span><span style=\" font-family:\'Calibri\',\'宋体\'; font-size:10.5pt; color:#0000ff;\">更新细分</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt; color:#0000ff;\">“ r”-</span><span style=\" font-family:\'Calibri\',\'宋体\'; font-size:10.5pt; color:#0000ff;\">重置设置</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt; color:#0000ff;\">“ s”-</span><span style=\" font-family:\'宋体\'; font-size:10.5pt; color:#0000ff;\">分割完成并退出（如果需要保存图片请点击保存图片即可）</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:small; font-weight:600; color:#333333;\">三、参数的设置</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">大津阈值分割</span></li></ol>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">滤波器：提供中值滤波，双边滤波，高斯滤波用户可根据自己的需求进行组合使用，最多可选取两个。</span></li>\n"
"<li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">形态学：本系统提供腐蚀，膨胀，开操作，闭操作。当选取某种操作后会出现下拉列表供用户选择次数。</span></li>\n"
"<li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">边缘检测：本系统只提供了canny算子，用户可根据需求进行选择</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333;\">     2.简单全局阈值分割</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">默认阈值为127，用户可根据效果进行指定阈值，范围为0~255</span></li>\n"
"<li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">滤波器：提供中值滤波，双边滤波，高斯滤波用户可根据自己的需求进行组合使用，最多可选取两个。</span></li>\n"
"<li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">形态学：本系统提供腐蚀，膨胀，开操作，闭操作。当选取某种操作后会出现下拉列表供用户选择次数。</span></li>\n"
"<li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">边缘检测：本系统只提供了canny算子，用户可根据需求进行选择</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333;\">    3.Grabcut自动分割</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Open Sans\',\'Clear Sans\',\'Helvetica Neue\',\'Helvetica\',\'Arial\',\'sans-serif\'; font-size:16px; color:#333333;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">  滤波器：提供中值滤波，双边滤波，高斯滤波用户可根据自己的需求进行组合使用，最多可选取两个。</span></li></ul></body></html>"))
