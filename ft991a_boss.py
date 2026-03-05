#!/usr/bin/env python3
#
# This file is part of ft991a-boss.
#
# ft991a-boss is free software: you can redistribute it and/or modify it under the terms 
# of the GNU General Public License as published by the Free Software Foundation, version 3.
#
# ft991a-boss is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with ft991a-boss. 
# If not, see <https://www.gnu.org/licenses/>.
#
# Copyright (c) 2026 Noyan Kinayman, KC1VCN
#
# spr, spw pseudocode: Copyright (c) 2025 Gil Kloepfer, KI5BPK
# ft991a memory map: Copyright (c) 2023 Gil Kloepfer, KI5BPK
#

import os
import sys
import math
import re
import xlrd
import serial
import time
import ast
import random
import argparse
import json
import numpy
import zlib
import functools

import matplotlib
import matplotlib.pyplot as pyplot
import matplotlib.animation as animation
import serial.tools.list_ports
import xml.etree.ElementTree as ET

import soundcard

from datetime import datetime
from datetime import timezone
from functools import partial
from collections import deque

from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6 import QtGui

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QTextEdit
from PySide6.QtWidgets import QTableWidget
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QPlainTextEdit
from PySide6.QtWidgets import QAbstractButton
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QDialogButtonBox


from PySide6.QtCore import QLocale
from PySide6.QtCore import QFile
from PySide6.QtCore import QTimer
from PySide6.QtCore import QTime
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt
from PySide6.QtCore import QIODevice
from PySide6.QtCore import QTextStream
from PySide6.QtCore import QPoint
from PySide6.QtCore import QRect
from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QMetaObject

from PySide6.QtGui import QDoubleValidator
from PySide6.QtGui import QPainter
from PySide6.QtGui import QColor
from PySide6.QtGui import QPen

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import StrMethodFormatter
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import FormatStrFormatter
from matplotlib.patches import Rectangle, Polygon

matplotlib.use('QtAgg')

from ft991a_ui import Ui_MainWindow

import ft991a

import resources_rc

#
def pause_GUI_update(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        window.timer_1.stop()
        window.timer_2.stop()
        window.ani_IF.pause()
        ft991a.MESSAGE_FLAG = False

        result = func(self, *args, **kwargs)

        ft991a.MESSAGE_FLAG = True
        window.ani_IF.resume()
        window.timer_2.start()
        window.timer_1.start()

        return result

    return wrapper

#
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

        self.setWindowTitle('FT991A-boss')

# Widget tooltips
        tooltips_file = QFile(':/data/resources/help.json')

        if tooltips_file.open(QIODevice.ReadOnly | QIODevice.Text):
            stream = QTextStream(tooltips_file)
            tooltips = json.loads(stream.readAll())
            tooltips_file.close()

            for tips in tooltips:
                object_name = u'%s' % (tips)
                _object = getattr(self, object_name)

                _object.setToolTip(tooltips[tips]) 
                _object.setToolTipDuration(-1)

        else:
            print('\nError: can\'t load resource help file.')

# Radio menu table
        for m in ft991a.menu.keys():
            menu_index = int(m)-1

#
            menu_name = ft991a.menu[m][0]
            menu_function = ft991a.menu[m][1]
            menu_default = ft991a.menu[m][2]
            menu_range = ft991a.menu[m][3]
            menu_digits = ft991a.menu[m][4]
            menu_notes = ft991a.menu[m][5]

# Radio menu controls
            object_name = u'menu_label_%d' % (2*menu_index+1)
            menu_label = getattr(self, object_name)
            menu_label.setText('%s' % (m))
#            menu_label.setFixedHeight(30)
            menu_label.setFixedWidth(50)
            menu_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

#
            object_name = u'menu_label_%d' % (2*menu_index+2)
            menu_label = getattr(self, object_name)
            menu_label.setText('%s' % (menu_name.replace('_', ' ')))
#            menu_label.setFixedHeight(30)
            menu_label.setFixedWidth(200)
            menu_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

#
            object_name = u'menu_pushButton_%d' % (menu_index+1)
            menu_button = getattr(self, object_name)
            menu_button.setFixedWidth(100)
#            menu_button.setFixedHeight(30)
            menu_button.setText('Default')
            menu_button.clicked.connect(self.on_default_button_clicked)

#
            object_name = u'menu_comboBox_%d' % (menu_index+1)
            menu_combo_box = getattr(self, object_name)
            menu_combo_box.setMaxVisibleItems(10)
            menu_combo_box.setFixedWidth(250)
#            menu_combo_box.setFixedHeight(30)
            menu_combo_box.currentIndexChanged.connect(self.on_menu_parameter_changed)

# Radio menu selections
            was_blocked = menu_combo_box.blockSignals(True) 

            for i in range(len(menu_range)):
                value = '%s' % menu_function('%s' % (menu_range[i]))

                if (value) == '':
                    continue

                menu_combo_box.addItem(value)

                if (menu_default == value):
                    menu_combo_box.setItemData(i, QtGui.QColor('green'), QtCore.Qt.BackgroundRole)

            menu_combo_box.blockSignals(was_blocked)

# Memory channel table
#        self.Memory_tableWidget.itemChanged.connect(self.on_Memory_item_changed)
#        self.Memory_tableWidget.itemClicked.connect(self.on_Memory_cell_changed)
#        self.Memory_tableWidget.cellClicked.connect(self.on_Memory_cell_changed)
        self.Memory_tableWidget.currentCellChanged.connect(self.on_Memory_cell_changed)

        self.Memory_AM_pushButton.clicked.connect(self.on_Memory_AM_button_clicked)
        self.Memory_VM_pushButton.clicked.connect(self.on_Memory_VM_button_clicked)
        self.Memory_scan_up_pushButton.clicked.connect(self.on_Memory_scan_button_clicked)
        self.Memory_scan_down_pushButton.clicked.connect(self.on_Memory_scan_button_clicked)
        self.Memory_scan_stop_pushButton.clicked.connect(self.on_Memory_scan_button_clicked)

#
        self.Memory_tableWidget.setColumnWidth(0, 125)
        self.Memory_tableWidget.setColumnWidth(1, 50)
        self.Memory_tableWidget.setColumnWidth(2, 130)
        self.Memory_tableWidget.setColumnWidth(3, 50)
        self.Memory_tableWidget.setColumnWidth(4, 75)
        self.Memory_tableWidget.setColumnWidth(5, 75)
        self.Memory_tableWidget.setColumnWidth(6, 50)
        self.Memory_tableWidget.setColumnWidth(7, 125)

# Radio operating mode
        self.mode = ''
        self.mode_button = {'LSB':      '1',    'USB':      '2',    'CW-LSB':   '3',    'CW-USB':   '4',
                            'RTTY-LSB': '5',    'RTTY-USB': '6',    'DATA-LSB': '7',    'DATA-USB': '8',
                            'AM':       '9',    'FM':       '10',   'AM-N':     '9',    'FM-N':     '10',
                            'C4FM':     '11',   'DATA-FM':  '12'}

# Radio buttons and sliders
        for k in ft991a.CTCSS_tone.keys():
            self.Squelch_CTCSS_comboBox.addItem('%s' % (ft991a.CTCSS_tone[k]))

        self.Squelch_CTCSS_comboBox.setMaxVisibleItems(10)
        self.Squelch_CTCSS_comboBox.setStyleSheet('QComboBox { combobox-popup: 0; }')

#
        for k in ft991a.DCS_code.keys():
            self.Squelch_DCS_comboBox.addItem('%s' % (ft991a.DCS_code[k]))

        self.Squelch_DCS_comboBox.setMaxVisibleItems(10)
        self.Squelch_DCS_comboBox.setStyleSheet('QComboBox { combobox-popup: 0; }')

#
        self.VFO_A_dial.valueChanged.connect(self.VFO_A_dial_frequency)
        self.VFO_A_lineEdit.editingFinished.connect(self.VFO_A_set_frequency)
        self.VFO_A_Tx_radioButton.toggled.connect(self.VFO_A_set_Tx)
        self.VFO_A_fast_radioButton.toggled.connect(self.VFO_A_set_fast)
        self.VFO_A_fast = 1

        self.VFO_B_dial.valueChanged.connect(self.VFO_B_dial_frequency)
        self.VFO_B_lineEdit.editingFinished.connect(self.VFO_B_set_frequency)
        self.VFO_B_Tx_radioButton.toggled.connect(self.VFO_B_set_Tx)
        self.VFO_B_fast_radioButton.toggled.connect(self.VFO_B_set_fast)
        self.VFO_B_fast = 1

        self.RF_power_verticalSlider.valueChanged.connect(self.set_RF_power)
        self.AF_gain_verticalSlider.valueChanged.connect(self.set_AF_gain)
        self.RF_gain_verticalSlider.valueChanged.connect(self.set_RF_gain)
        self.RF_squelch_verticalSlider.valueChanged.connect(self.set_RF_squelch)

        self.Clar_dial.valueChanged.connect(self.set_RF_clar)
        self.Clar_clear_pushButton.clicked.connect(self.clear_RF_clar)
        self.Clar_comboBox.currentIndexChanged.connect(self.on_clar_mode_changed)

        self.S_meter_progressBar.setRange(0, 255)
        self.PO_meter_progressBar.setRange(0, 255)

        self.Squelch_CTCSS_comboBox.currentIndexChanged.connect(self.on_Squelch_CTCSS_changed)
        self.Squelch_DCS_comboBox.currentIndexChanged.connect(self.on_Squelch_DCS_changed)
        self.Squelch_offset_comboBox.currentIndexChanged.connect(self.on_Squelch_offset_changed)
        self.Squelch_mode_comboBox.currentIndexChanged.connect(self.on_Squelch_mode_changed)

#
        self.A_B_pushButton_1.clicked.connect(self.on_swap_VFO_button_clicked)
        self.A_B_pushButton_2.clicked.connect(self.on_copy_VFO_button_clicked)
        self.A_B_pushButton_3.clicked.connect(self.on_split_button_clicked)

#
        self.band_pushButton_1.clicked.connect(self.on_band_button_clicked)
        self.band_pushButton_2.clicked.connect(self.on_band_button_clicked)
        self.band_pushButton_3.clicked.connect(self.on_band_button_clicked)
        self.band_pushButton_4.clicked.connect(self.on_band_button_clicked)
        self.band_pushButton_5.clicked.connect(self.on_band_button_clicked)
        self.band_pushButton_6.clicked.connect(self.on_band_button_clicked)
        self.band_pushButton_7.clicked.connect(self.on_band_button_clicked)
        self.band_pushButton_8.clicked.connect(self.on_band_button_clicked)
        self.band_pushButton_9.clicked.connect(self.on_band_button_clicked)
        self.band_pushButton_10.clicked.connect(self.on_band_button_clicked)
        self.band_pushButton_11.clicked.connect(self.on_band_button_clicked)
        self.band_pushButton_12.clicked.connect(self.on_band_button_clicked)
        self.band_pushButton_13.clicked.connect(self.on_band_button_clicked)
        self.band_pushButton_14.clicked.connect(self.on_band_button_clicked)
        self.band_pushButton_15.clicked.connect(self.on_band_button_clicked)

#
        self.mode_pushButton_1.clicked.connect(self.on_mode_button_clicked)
        self.mode_pushButton_2.clicked.connect(self.on_mode_button_clicked)
        self.mode_pushButton_3.clicked.connect(self.on_mode_button_clicked)
        self.mode_pushButton_4.clicked.connect(self.on_mode_button_clicked)
        self.mode_pushButton_5.clicked.connect(self.on_mode_button_clicked)
        self.mode_pushButton_6.clicked.connect(self.on_mode_button_clicked)
        self.mode_pushButton_7.clicked.connect(self.on_mode_button_clicked)
        self.mode_pushButton_8.clicked.connect(self.on_mode_button_clicked)
        self.mode_pushButton_9.clicked.connect(self.on_mode_button_clicked)
        self.mode_pushButton_10.clicked.connect(self.on_mode_button_clicked)
        self.mode_pushButton_11.clicked.connect(self.on_mode_button_clicked)
        self.mode_pushButton_12.clicked.connect(self.on_mode_button_clicked)

#
        self.Notch_freq_horizontalSlider.valueChanged.connect(self.set_Notch_filter)
        self.Notch_pushButton.clicked.connect(self.Notch_filter_state)
        self.Notch_freq = 0

        self.Contour_freq_horizontalSlider.valueChanged.connect(self.set_Contour_filter)
        self.Contour_pushButton.clicked.connect(self.Contour_filter_state)
        self.Contour_BW_spinBox.valueChanged.connect(self.on_Contour_BW_changed)
        self.Contour_level_spinBox.valueChanged.connect(self.on_Contour_level_changed)
        self.Contour_freq = 0

        self.IF_filter_shift_horizontalSlider.valueChanged.connect(self.set_IF_filter_shift)
        self.IF_filter_BW_horizontalSlider.valueChanged.connect(self.set_IF_filter_bandwidth)
        self.IF_filter_BW_wide_pushButton.clicked.connect(self.set_IF_filter_type)
        self.IF_filter_BW_narrow_pushButton.clicked.connect(self.set_IF_filter_type)

        self.IF_filter_shift = 0
        self.IF_filter_bandwidth = 0
        self.IF_filter_type = 'wide'

        self.FFT_pushButton_1.clicked.connect(self.set_FFT_sampling)
        self.FFT_pushButton_2.clicked.connect(self.set_FFT_sampling)
        self.FFT_pushButton_3.clicked.connect(self.set_FFT_sampling)
        self.FFT_window_comboBox.currentIndexChanged.connect(self.on_FFT_window_changed)
        self.FFT_gain_comboBox.currentIndexChanged.connect(self.on_FFT_gain_changed)
        self.FFT_block_comboBox.currentIndexChanged.connect(self.on_FFT_block_changed)

#
        self.FrontEnd_ATT_pushButton.clicked.connect(self.set_FrontEnd_ATT)
        self.FrontEnd_IPO_comboBox.currentIndexChanged.connect(self.set_FrontEnd_IPO)

#
        self.Noise_DNF_pushButton.clicked.connect(self.set_Noise_DNF)
        self.Noise_DNR_comboBox.currentIndexChanged.connect(self.set_Noise_DNR_level)
        self.Noise_DNR_pushButton.clicked.connect(self.set_Noise_DNR)
        self.Noise_NB_comboBox.currentIndexChanged.connect(self.set_Noise_NB_level)
        self.Noise_NB_pushButton.clicked.connect(self.set_Noise_NB)

#
        self.Speech_Proc_pushButton.clicked.connect(self.set_Speech_Proc)
        self.Speech_Proc_horizontalSlider.valueChanged.connect(self.set_Speech_Proc_level)
        self.Speech_Proc_EQ_pushButton.clicked.connect(self.set_Speech_Proc_EQ)

#
        self.Microphone_Gain_horizontalSlider.valueChanged.connect(self.set_Microphone_Gain)
        self.Tx_Audio_BW_comboBox.currentIndexChanged.connect(self.set_Tx_Audio_BW)
        self.Monitor_level_horizontalSlider.valueChanged.connect(self.set_monitor_level)
        self.Monitor_state_pushButton.clicked.connect(self.set_monitor_state)

#
        self.EQ_1_center_verticalSlider.valueChanged.connect(self.set_EQ_center)
        self.EQ_1_gain_verticalSlider.valueChanged.connect(self.set_EQ_gain)
        self.EQ_1_BW_verticalSlider.valueChanged.connect(self.set_EQ_BW)
        self.EQ_2_center_verticalSlider.valueChanged.connect(self.set_EQ_center)
        self.EQ_2_gain_verticalSlider.valueChanged.connect(self.set_EQ_gain)
        self.EQ_2_BW_verticalSlider.valueChanged.connect(self.set_EQ_BW)
        self.EQ_3_center_verticalSlider.valueChanged.connect(self.set_EQ_center)
        self.EQ_3_gain_verticalSlider.valueChanged.connect(self.set_EQ_gain)
        self.EQ_3_BW_verticalSlider.valueChanged.connect(self.set_EQ_BW)
        self.EQ_comboBox.currentIndexChanged.connect(self.on_EQ_preset_selected)
        self.EQ_pushButton_1.clicked.connect(self.on_EQ_reset)
        self.EQ_pushButton_2.clicked.connect(self.on_EQ_bank)
        self.EQ_pushButton_3.clicked.connect(self.on_EQ_bank)

        self.EQ_param = {1: {1: {'center':    0.0, 'gain': 5.0, 'Q': 10.0},
                             2: {'center':    0.0, 'gain': 5.0, 'Q': 10.0},
                             3: {'center':    0.0, 'gain': 5.0, 'Q': 10.0}},
                         2: {1: {'center':  200.0, 'gain': 0.0, 'Q':  2.0},
                             2: {'center':  800.0, 'gain': 0.0, 'Q':  1.0},
                             3: {'center': 2100.0, 'gain': 0.0, 'Q':  1.0}}}

        self.EQ_bank = 1

#
        self.Audio_filter_horizontalSlider_1.valueChanged.connect(self.set_Audio_filter_cutoff)
        self.Audio_filter_horizontalSlider_2.valueChanged.connect(self.set_Audio_filter_cutoff)
        self.Audio_filter_comboBox_1.currentIndexChanged.connect(self.set_Audio_filter_slope)
        self.Audio_filter_comboBox_2.currentIndexChanged.connect(self.set_Audio_filter_slope)
        self.Audio_filter_pushButton_1.clicked.connect(self.on_Audio_filter_bank)
        self.Audio_filter_pushButton_2.clicked.connect(self.on_Audio_filter_bank)
        self.Audio_filter_pushButton_3.clicked.connect(self.on_Audio_filter_bank)
        self.Audio_filter_pushButton_4.clicked.connect(self.on_Audio_filter_bank)
        self.Audio_filter_pushButton_5.clicked.connect(self.on_Audio_filter_bank)

        self.Audio_filter_param = {1: {'cutoff_1':   0.0, 'cutoff_2':    0.0, 'slope_1':  6.0, 'slope_2':  6.0},
                                   2: {'cutoff_1': 250.0, 'cutoff_2': 1200.0, 'slope_1': 18.0, 'slope_2': 18.0},
                                   3: {'cutoff_1': 300.0, 'cutoff_2': 3000.0, 'slope_1': 18.0, 'slope_2': 18.0},
                                   4: {'cutoff_1': 300.0, 'cutoff_2': 3000.0, 'slope_1': 18.0, 'slope_2': 18.0},
                                   5: {'cutoff_1': 100.0, 'cutoff_2': 3000.0, 'slope_1':  6.0, 'slope_2':  6.0}}

        self.Audio_filter_bank = 1

# FFT parameters
        self.sample_rate = 8000
        self.block_size = 1024
        self.fft_window = numpy.hamming(self.block_size)
        self.fft_gain = 1.0

        self.mic = None
        self.channels = 1

#
        self.figure_IF, self.ax_IF = pyplot.subplots(figsize=(5, 5), layout=None)
        self.figure_IF.patch.set_alpha(0.0)
        pyplot.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.15)

        self.canvas_IF = FigureCanvasQTAgg(self.figure_IF)
        self.canvas_IF.setGeometry(5, 5, 625, 415)
        self.canvas_IF.setParent(self.IF_spectrum_frame)
        self.ani_IF = None
        self.set_IF_spectrum_plot()

#
        self.figure_EQ, self.ax_EQ = pyplot.subplots(figsize=(5, 5), layout=None)
        self.figure_EQ.patch.set_alpha(0.0)
        pyplot.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.35)

        self.canvas_EQ = FigureCanvasQTAgg(self.figure_EQ)
        self.canvas_EQ.setGeometry(5, 10, 525, 250)
        self.canvas_EQ.setParent(self.EQ_filter_frame)
        self.ani_EQ = None
        self.set_EQ_spectrum_plot()

#
        self.figure_audio_filter, self.ax_audio_filter = pyplot.subplots(figsize=(5, 5), layout=None)
        self.figure_audio_filter.patch.set_alpha(0.0)
        pyplot.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.35)

        self.canvas_audio_filter = FigureCanvasQTAgg(self.figure_audio_filter)
        self.canvas_audio_filter.setGeometry(5, 10, 525, 250)
        self.canvas_audio_filter.setParent(self.Audio_filter_frame)
        self.ani_audio_filter = None
        self.set_audio_filter_plot()

# Program menu actions
        self.actionSave_Radio_Menu.triggered.connect(self.save_Radio_menu)
        self.actionLoad_Radio_Menu.triggered.connect(self.load_Radio_menu)
        self.actionSave_Memory_Channel.triggered.connect(self.save_Memory_raw)
        self.actionLoad_Memory_Channel.triggered.connect(self.load_Memory_raw)

        self.actionRefresh_Radio_Menu.triggered.connect(self.update_Radio_menu)
        self.actionRefresh_Memory_Channel.triggered.connect(self.update_Memory)
        self.actionRefresh_Settings.triggered.connect(self.update_RF_settings)
        self.actionRefresh_Equalizer.triggered.connect(self.EQ_get_parameters)
        self.actionRefresh_Audio_Filter.triggered.connect(self.Audio_filter_get_cutoff)
        self.actionRefresh_Audio_Filter.triggered.connect(self.Audio_filter_get_slope)

        self.actionAbout.triggered.connect(self.about)

        self.actionExit.triggered.connect(self.exit)

# Radio meter events for custom painting
        self.PO_meter_progressBar.installEventFilter(self)
        self.S_meter_progressBar.installEventFilter(self)

# Timers to update GUI
        self.timer_1 = QTimer(self)
        self.timer_1.setInterval(100)
        self.timer_1.timeout.connect(self.update_VFO_registers)
        self.timer_1.start()

        self.timer_2 = QTimer(self)
        self.timer_2.setInterval(25)
        self.timer_2.timeout.connect(self.update_gui_meters)
        self.timer_2.start()

#
#        self.Radio_tabWidget.currentChanged.connect(self.on_tab_changed)

#
        ft991a.MESSAGE_FLAG = True

#
    @pause_GUI_update
    def exit(self):
        QApplication.instance().quit()

#
    @pause_GUI_update
    def about(self):
        about_window = QtWidgets.QDialog()
        about_window.resize(581, 390)
        about_window.setObjectName(u'About')
        about_window.setWindowTitle(u'About')

        buttonBox = QDialogButtonBox(about_window)
        buttonBox.setObjectName(u'buttonBox')
        buttonBox.setGeometry(QRect(250, 340, 81, 32))
        buttonBox.setOrientation(Qt.Orientation.Horizontal)
        buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
        buttonBox.accepted.connect(about_window.accept)

        plainTextEdit = QPlainTextEdit(about_window)
        plainTextEdit.setObjectName(u'plainTextEdit')
        plainTextEdit.setGeometry(QRect(15, 10, 551, 311))
        plainTextEdit.setPlainText(QCoreApplication.translate('', u'ft991a-boss is free software: you can redistribute it \
and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3.\n\n\
ft991a-boss is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty \
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.\n\nYou should have \
received a copy of the GNU General Public License along with ft991a-boss. If not, see https://www.gnu.org/licenses/\n\n\
Copyright (c) 2026 Noyan Kinayman, KC1VCN\n\n\
spr, spw pseudocode : Copyright (c) 2025 Gil Kloepfer, KI5BPK\n\
ft991a memory map: Copyright (c) 2023 Gil Kloepfer, KI5BPK\n', None))

        QMetaObject.connectSlotsByName(about_window)

        about_window.exec()

#
    def on_tab_changed(self):
        self.update_RF_settings()

#
    def eventFilter(self, obj, event):
        if (obj is self.S_meter_progressBar) and (event.type() == QtCore.QEvent.Paint):
            obj.paintEvent(event)

            painter = QPainter(obj)

#
            pen = QPen(QColor('red'), 3)
            painter.setPen(pen)

            peak = obj.property('peak')

            peak_ratio = (peak-obj.minimum())/float(obj.maximum()-obj.minimum())
            peak_x = int(peak_ratio*obj.width())

            painter.drawLine(peak_x, 0, peak_x, obj.height())

#
            pen = QPen(QColor('blue'), 3)
            painter.setPen(pen)

            average = obj.property('average')

            average_ratio = (average-obj.minimum())/float(obj.maximum()-obj.minimum())
            average_x = int(average_ratio*obj.width())

#            painter.drawLine(average_x, 0, average_x, obj.height())

            return True

#
        if (obj is self.PO_meter_progressBar) and (event.type() == QtCore.QEvent.Paint):
            obj.paintEvent(event)

            painter = QPainter(obj)

#
            pen = QPen(QColor('red'), 3)
            painter.setPen(pen)

            peak = obj.property('peak')

            peak_ratio = (peak-obj.minimum())/float(obj.maximum()-obj.minimum())
            peak_x = int(peak_ratio*obj.width())

            painter.drawLine(peak_x, 0, peak_x, obj.height())

            return True

        return super().eventFilter(obj, event)

##############################
# GUI Update - RF Settings
##############################
    @pause_GUI_update
    def update_RF_settings(self):
        operating_mode = ft991a.get_operating_mode()
        if (operating_mode != None):
            self.mode = operating_mode
            mode_button = self.mode_button[operating_mode]

            object_name = u'mode_pushButton_%s' % (mode_button)
            mode_button = getattr(self, object_name)
            was_blocked = mode_button.blockSignals(True) 
            mode_button.click()
            mode_button.blockSignals(was_blocked)

#
            state = {'LSB': [True,   True],      'USB': [True,   True],   
                  'CW-USB': [True,   True],       'FM': [False, False],
                      'AM': [True,  False], 'RTTY-LSB': [True,   True],   
                  'CW-LSB': [True,   True], 'DATA-LSB': [True,   True],
                'RTTY-USB': [True,   True],  'DATA-FM': [False, False],    
                    'FM-N': [False, False], 'DATA-USB': [True,   True],
                    'AM-N': [True,  False],     'C4FM': [False, False]}[operating_mode]

            self.Notch_freq_horizontalSlider.setEnabled(state[0])
            self.Notch_pushButton.setEnabled(state[0])
            self.Contour_freq_horizontalSlider.setEnabled(state[0])
            self.Contour_pushButton.setEnabled(state[0])
            self.Contour_level_spinBox.setEnabled(state[0])
            self.Contour_BW_spinBox.setEnabled(state[0])
            self.IF_filter_shift_horizontalSlider.setEnabled(state[1])
            self.IF_filter_BW_horizontalSlider.setEnabled(state[1])
            self.Noise_DNF_pushButton.setEnabled(state[0])
            self.Noise_DNR_pushButton.setEnabled(state[0])
            self.Noise_DNR_comboBox.setEnabled(state[0])
            self.Noise_NB_pushButton.setEnabled(state[0])
            self.Noise_NB_comboBox.setEnabled(state[0])

#
        RF_power = ft991a.get_RF_power()
        if (RF_power != None):
            self.RF_power_lcdNumber.display(RF_power)
            was_blocked = self.RF_power_verticalSlider.blockSignals(True) 
            self.RF_power_verticalSlider.setValue(int(RF_power))
            self.RF_power_verticalSlider.blockSignals(was_blocked)

#
        AF_gain = ft991a.get_AF_gain()
        if (AF_gain != None):
            self.AF_gain_lcdNumber.display(round(AF_gain/2.55))
            was_blocked = self.AF_gain_verticalSlider.blockSignals(True) 
            self.AF_gain_verticalSlider.setValue(int(AF_gain))
            self.AF_gain_verticalSlider.blockSignals(was_blocked)

#
        RF_gain = ft991a.get_RF_gain()
        if (RF_gain != None):
            self.RF_gain_lcdNumber.display(round(RF_gain/2.55))
            was_blocked = self.RF_gain_verticalSlider.blockSignals(True) 
            self.RF_gain_verticalSlider.setValue(int(RF_gain))
            self.RF_gain_verticalSlider.blockSignals(was_blocked)

#
        RF_squelch = ft991a.get_RF_squelch()
        if (RF_squelch != None):
            self.RF_squelch_lcdNumber.display(RF_squelch)
            was_blocked = self.RF_squelch_verticalSlider.blockSignals(True) 
            self.RF_squelch_verticalSlider.setValue(RF_squelch)
            self.RF_squelch_verticalSlider.blockSignals(was_blocked)

#
        ctcss_tone = ft991a.get_ctcss_tone_freq()
        if (ctcss_tone != None):
            was_blocked = self.Squelch_CTCSS_comboBox.blockSignals(True) 
            self.Squelch_CTCSS_comboBox.setCurrentText('%.1f' % (ctcss_tone))
            self.Squelch_CTCSS_comboBox.blockSignals(was_blocked)

#
        dcs_tone = ft991a.get_dcs_code()
        if (dcs_tone != None):
            was_blocked = self.Squelch_DCS_comboBox.blockSignals(True) 
            self.Squelch_DCS_comboBox.setCurrentText('%d' % (dcs_tone))
            self.Squelch_DCS_comboBox.blockSignals(was_blocked)

#
        offset = ft991a.get_repeater_shift()
        if (offset != None):
            was_blocked = self.Squelch_offset_comboBox.blockSignals(True) 
            self.Squelch_offset_comboBox.setCurrentText('%s' % (offset))
            self.Squelch_offset_comboBox.blockSignals(was_blocked)

#
        ctcss_mode = ft991a.get_ctcss_mode()
        if (ctcss_mode != None):
            was_blocked = self.Squelch_mode_comboBox.blockSignals(True) 
            self.Squelch_mode_comboBox.setCurrentText('%s' % (ctcss_mode))
            self.Squelch_mode_comboBox.blockSignals(was_blocked)

#
        Tx_mode = ft991a.get_function_Tx()
        if (Tx_mode != None):
            split = {'VFO_B': True, 'VFO_A': False}[Tx_mode]
            self.A_B_pushButton_3.setChecked(split)
            self.VFO_B_Tx_radioButton.setChecked(split)

#
        clar_Rx = ft991a.get_RF_clar_state()
        clar_Tx = ft991a.get_RF_clar_state_Tx()
        if (clar_Rx != None) and (clar_Tx != None):
            clar_mode = {(0,0): 'OFF', (1,0): 'Rx', (0,1): 'Tx', (1,1): 'Rx/Tx'}[(clar_Rx, clar_Tx)]
            was_blocked = self.Clar_comboBox.blockSignals(True) 
            self.Clar_comboBox.setCurrentText(clar_mode)
            self.Clar_comboBox.blockSignals(was_blocked)

#
        notch_freq = ft991a.get_manual_notch_level()
        if (notch_freq != None):
            self.Notch_freq = int(notch_freq)
            self.Notch_freq_lcdNumber.display(self.Notch_freq)
            was_blocked = self.Notch_freq_horizontalSlider.blockSignals(True)
            self.Notch_freq_horizontalSlider.setValue(self.Notch_freq/10)
            self.Notch_freq_horizontalSlider.blockSignals(was_blocked)

#
        notch_state = ft991a.get_manual_notch_state()
        if (notch_state != None):
            was_blocked = self.Notch_pushButton.blockSignals(True)
            self.Notch_pushButton.setChecked(notch_state)
            self.Notch_pushButton.blockSignals(was_blocked)

#
        contour_freq = int(ft991a.get_contour_level())
        if (contour_freq != None):
            self.Contour_freq = int(contour_freq)
            self.Contour_freq_lcdNumber.display(self.Contour_freq)
            was_blocked = self.Contour_freq_horizontalSlider.blockSignals(True)
            self.Contour_freq_horizontalSlider.setValue(self.Contour_freq/10)
            self.Contour_freq_horizontalSlider.blockSignals(was_blocked)

#
        contour_state = ft991a.get_contour_state()
        if (contour_state != None):
            was_blocked = self.Contour_pushButton.blockSignals(True)
            self.Contour_pushButton.setChecked(contour_state)
            self.Contour_pushButton.blockSignals(was_blocked)

#
        contour_level = ft991a.get_menu_value(112)
        if (contour_level != None):
            contour_level = int(contour_level)
            was_blocked = self.Contour_level_spinBox.blockSignals(True) 
            self.Contour_level_spinBox.setValue(contour_level)
            self.Contour_level_spinBox.blockSignals(was_blocked)

#
        contour_BW = ft991a.get_menu_value(113)
        if (contour_BW != None):
            contour_BW = int(contour_BW)
            was_blocked = self.Contour_BW_spinBox.blockSignals(True) 
            self.Contour_BW_spinBox.setValue(contour_BW)
            self.Contour_BW_spinBox.blockSignals(was_blocked)

#
        IF_filter_type = ft991a.get_IF_filter_type()
        if (IF_filter_type != None):
            self.IF_filter_type = IF_filter_type
            push_button = getattr(self, 'IF_filter_BW_%s_pushButton' % (self.IF_filter_type.lower()))
            was_blocked = push_button.blockSignals(True) 
            push_button.click()
            push_button.blockSignals(was_blocked)

#
        IF_bandwidth, index = ft991a.get_IF_bandwidth(self.mode, self.IF_filter_type)
        if (IF_bandwidth != None):
            self.IF_filter_bandwidth = int(IF_bandwidth)
            self.IF_filter_BW_lcdNumber.display(IF_bandwidth)
            was_blocked = self.IF_filter_BW_horizontalSlider.blockSignals(True)
            self.IF_filter_BW_horizontalSlider.setValue(index)
            self.IF_filter_BW_horizontalSlider.blockSignals(was_blocked)

#
        IF_shift = ft991a.get_IF_shift_level()
        if (IF_shift != None):
            self.IF_filter_shift = int(IF_shift)
            self.IF_filter_shift_lcdNumber.display(IF_shift)
            was_blocked = self.IF_filter_shift_horizontalSlider.blockSignals(True)
            self.IF_filter_shift_horizontalSlider.setValue(IF_shift/20)
            self.IF_filter_shift_horizontalSlider.blockSignals(was_blocked)

#
        attenuator_state = ft991a.get_RF_attenuator()
        if (attenuator_state != None):
            was_blocked = self.FrontEnd_ATT_pushButton.blockSignals(True) 
            self.FrontEnd_ATT_pushButton.setChecked(attenuator_state)
            self.FrontEnd_ATT_pushButton.blockSignals(was_blocked)

#
        IPO = ft991a.get_IPO()
        if (IPO != None):
            was_blocked = self.FrontEnd_IPO_comboBox.blockSignals(True) 
            self.FrontEnd_IPO_comboBox.setCurrentText(IPO)
            self.FrontEnd_IPO_comboBox.blockSignals(was_blocked)

#
        NB_state = ft991a.get_NB_state()
        if (NB_state != None):
            was_blocked = self.Noise_NB_pushButton.blockSignals(True) 
            self.Noise_NB_pushButton.setChecked(NB_state)
            self.Noise_NB_pushButton.blockSignals(was_blocked)

#
        NB_level = ft991a.get_NB_level()
        if (NB_level != None):
            was_blocked = self.Noise_NB_comboBox.blockSignals(True) 
            self.Noise_NB_comboBox.setCurrentIndex(int(NB_level))
            self.Noise_NB_comboBox.blockSignals(was_blocked)

#
        NR_state = ft991a.get_NR_state()
        if (NR_state != None):
            was_blocked = self.Noise_DNR_pushButton.blockSignals(True) 
            self.Noise_DNR_pushButton.setChecked(NR_state)
            self.Noise_DNR_pushButton.blockSignals(was_blocked)

#
        NR_level = ft991a.get_NR_level()
        if (NR_level != None):
            was_blocked = self.Noise_DNR_comboBox.blockSignals(True) 
            self.Noise_DNR_comboBox.setCurrentIndex(int(NR_level)-1)
            self.Noise_DNR_comboBox.blockSignals(was_blocked)

#
        DNF_state = ft991a.get_digital_notch_state()
        if (DNF_state != None):
            was_blocked = self.Noise_DNF_pushButton.blockSignals(True) 
            self.Noise_DNF_pushButton.setChecked(DNF_state)
            self.Noise_DNF_pushButton.blockSignals(was_blocked)

#
        SP_state = ft991a.get_SP_state()
        if (SP_state != None):
            was_blocked = self.Speech_Proc_pushButton.blockSignals(True) 
            self.Speech_Proc_pushButton.setChecked(SP_state)
            self.Speech_Proc_pushButton.blockSignals(was_blocked)

#
        EQ_state = ft991a.get_SP_EQ_state()
        if (EQ_state != None):
            was_blocked = self.Speech_Proc_EQ_pushButton.blockSignals(True) 
            self.Speech_Proc_EQ_pushButton.setChecked(EQ_state)
            self.Speech_Proc_EQ_pushButton.blockSignals(was_blocked)

#
        EQ_level = ft991a.get_SP_level()
        if (EQ_level != None):
            self.Speech_Proc_lcdNumber.display(EQ_level)
            was_blocked = self.Speech_Proc_horizontalSlider.blockSignals(True)
            self.Speech_Proc_horizontalSlider.setValue(EQ_level)
            self.Speech_Proc_horizontalSlider.blockSignals(was_blocked)

#
        monitor_state = ft991a.get_monitor_state()
        if (monitor_state != None):
            was_blocked = self.Monitor_state_pushButton.blockSignals(True) 
            self.Monitor_state_pushButton.setChecked(monitor_state)
            self.Monitor_state_pushButton.blockSignals(was_blocked)

#
        monitor_level = ft991a.get_monitor_level()
        if (monitor_level != None):
            self.Monitor_level_lcdNumber.display(monitor_level)
            was_blocked = self.Monitor_level_horizontalSlider.blockSignals(True)
            self.Monitor_level_horizontalSlider.setValue(monitor_level)
            self.Monitor_level_horizontalSlider.blockSignals(was_blocked)

#
        mic_gain = ft991a.get_microphone_gain()
        if (mic_gain != None):
            self.Microphone_Gain_lcdNumber.display(mic_gain)
            was_blocked = self.Microphone_Gain_horizontalSlider.blockSignals(True)
            self.Microphone_Gain_horizontalSlider.setValue(mic_gain)
            self.Microphone_Gain_horizontalSlider.blockSignals(was_blocked)

#
        Tx_audio_BW = ft991a.get_menu_value(110)
        if (Tx_audio_BW != None):
            value = ft991a.menu['110'][1](Tx_audio_BW)
            self.Tx_Audio_BW_comboBox.setCurrentText(value)

##############################
# GUI Update - VFO Registers
##############################
    def update_VFO_registers(self):
        ft991a.MESSAGE_FLAG = False

#
        operating_mode = self.mode

        PLL_state = ft991a.get_PLL_lock()

        if(PLL_state != None):
            PLL_state = True if (PLL_state == 'LOCK') else False
            self.PLL_lock_radioButton.setChecked(PLL_state)

#
        info_A, _ = ft991a.get_band_info()

        if (info_A != None):
            freq_A = '%d' % (int(info_A[1]))
            self.VFO_A_lcdNumber.display(freq_A)

            clar = '%d' % (int(info_A[2]))
            self.Clar_lcdNumber.display(clar)

            operating_mode = info_A[5]

            info = '%s %s %s\n%s %s %s %s' % (info_A[2].ljust(8, ' '), \
                                              info_A[3].ljust(13, ' '), \
                                              info_A[4].ljust(11, ' '), \
                                              info_A[5].ljust(8, ' '), \
                                              info_A[6].ljust(13, ' '), \
                                              info_A[7].ljust(13, ' '), \
                                              info_A[8].ljust(11, ' '))

            self.VFO_A_textBrowser.setPlainText(str(info).replace('_', ' '))

#
        info_B, _ = ft991a.get_opposite_band_info()

        if (info_B != None):
            freq_B = '%d' % (int(info_B[1]))
            self.VFO_B_lcdNumber.display(freq_B)

            info = '%s %s %s\n%s %s %s %s' % (info_B[2].ljust(8, ' '), \
                                              info_B[3].ljust(13, ' '), \
                                              info_B[4].ljust(11, ' '), \
                                              info_B[5].ljust(8, ' '), \
                                              info_B[6].ljust(13, ' '), \
                                              info_B[7].ljust(13, ' '), \
                                              info_B[8].ljust(11, ' '))

            self.VFO_B_textBrowser.setPlainText(str(info).replace('_', ' '))

#
        if (operating_mode != self.mode):
            self.update_RF_settings()

#
        ft991a.MESSAGE_FLAG = True

##############################
# GUI Update - Meters
##############################
    def update_gui_meters(self):
        active_widget = self.Radio_tabWidget.currentWidget()
        tab_name = active_widget.objectName()

        if (tab_name != 'tab_1'):
            return

#
        ft991a.MESSAGE_FLAG = False

#
        value = ft991a.get_meter('S')
        if (value != None):
            self.S_meter_progressBar.setValue(int(value))

            if (int(value) > self.S_meter_progressBar.property('peak')):
                self.S_meter_progressBar.setProperty('peak', int(value))

            if (self.S_meter_progressBar.property('hold') > 200):
                self.S_meter_progressBar.setProperty('peak', int(value))
                self.S_meter_progressBar.setProperty('hold', 0)

            else:
                hold = self.S_meter_progressBar.property('hold')+1
                self.S_meter_progressBar.setProperty('hold', hold)

#
            byte_data = self.S_meter_progressBar.property('samples')
            byte_data = byte_data+'%c' % (int(value))

            if len(byte_data) > 30:
                byte_data = byte_data[1:]

            self.S_meter_progressBar.setProperty('samples', byte_data)

            window_size = 30
            data = numpy.frombuffer(byte_data.encode('utf-8').replace(b'\xc2', b''), dtype=numpy.uint8)
            rolling_avg = numpy.convolve(data, numpy.ones(window_size), 'valid')/window_size

            self.S_meter_progressBar.setProperty('average', rolling_avg[-1])

#
        value = ft991a.get_meter('PO')
        if (value != None):
            self.PO_meter_progressBar.setValue(int(value))

            if (int(value) > self.PO_meter_progressBar.property('peak')):
                self.PO_meter_progressBar.setProperty('peak', int(value))

            if (self.PO_meter_progressBar.property('hold') > 200):
                self.PO_meter_progressBar.setProperty('peak', int(value))
                self.PO_meter_progressBar.setProperty('hold', 0)

            else:
                hold = self.PO_meter_progressBar.property('hold')+1
                self.PO_meter_progressBar.setProperty('hold', hold)

#
        ft991a.MESSAGE_FLAG = True

##############################
# Spectrum Plot - DSP IF
##############################
    def set_IF_spectrum_plot(self):
        f_step = float(self.sample_rate)/float(self.block_size)
        N = int(self.block_size/2)

#
        x = numpy.linspace(0, int(N*f_step/1000), num=N)
        y = numpy.zeros(N)

        self.IF_line = self.ax_IF.plot(x, y, label='', color='white', linewidth=1)[0]

#
        self.IF_notch_line = self.ax_IF.axvline(self.Notch_freq/1000, color='red', linestyle='--')
        self.IF_contour_line = self.ax_IF.axvline(self.Contour_freq/1000, color='blue', linestyle='--')

        width = self.IF_filter_bandwidth/1000
        center = 1.0
        shift = self.IF_filter_shift/1000

        x1 = center-width/2+shift
        x2 = center+width/2+shift

        vertices = [[x1, -30], [x1, 30], [x2, 30], [x2, -30], [x1, -30]]
        
        self.IF_filter_rect = Polygon(vertices, edgecolor='white', facecolor='powderblue', linestyle='--', alpha=0.9)
        self.ax_IF.add_patch(self.IF_filter_rect)

#
        self.ax_IF.patch.set_alpha(0.0)
        self.ax_IF.spines['bottom'].set_color('white')
        self.ax_IF.spines['top'].set_color('white')
        self.ax_IF.spines['left'].set_color('white')
        self.ax_IF.spines['right'].set_color('white')
        self.ax_IF.tick_params(axis='y', colors='white')
        self.ax_IF.tick_params(axis='x', colors='white')

        self.ax_IF.set_xlabel('Frequency [kHz]', color='white')
        self.ax_IF.set_ylabel('Relative Magnitude [dB]', color='white')
        self.ax_IF.set_title('', color='white')

        x_min = 0.0
        x_max = int(f_step*N/1000)

        self.ax_IF.set_xlim(x_min, x_max)
        self.ax_IF.set_xticks(numpy.arange(0, x_max+1, 1))
        self.ax_IF.xaxis.set_minor_locator(MultipleLocator(0.1))
        self.ax_IF.tick_params(axis='x', which='minor', direction='out', length=2, width=1.0, color='white')
        self.ax_IF.tick_params(axis='x', which='major', direction='out', length=6, width=1.0, color='white')

        y_min = -30.0
        y_max = 30.0

        self.ax_IF.set_ylim(y_min, y_max)
        self.ax_IF.set_yticks(numpy.arange(y_min, y_max+5, 5))

#        for label in self.ax_IF.get_xticklabels():
#            label.set_horizontalalignment('center')
#            label.set_family('monospace')

#        for label in self.ax_IF.get_yticklabels():
#            label.set_verticalalignment('center')
#            label.set_family('monospace')

#
        self.IF_filter_mode = {     'LSB': 'SSB',       'USB': 'SSB',    'CW-LSB': 'CW',     'CW-USB': 'CW',  
                               'RTTY-LSB': 'RTTY', 'RTTY-USB': 'RTTY', 'DATA-LSB': 'DATA', 'DATA-USB': 'DATA',    
                                     'AM': 'AM',         'FM': 'FM',       'C4FM': 'FM',    'DATA-FM': 'FM',
                                   'AM-N': 'AM',       'FM-N': 'FM'}

        self.IF_filter_center = {'AM':   {'NARROW': [[6000, 6000],   [3000, 3000]],
                                            'WIDE': [[9000, 9000],   [4500, 4500]]},

                                 'FM':   {'NARROW': [[9000, 9000],   [4500, 4500]],
                                            'WIDE': [[16000, 16000], [8000, 8000]]},

                                 'SSB':  {'NARROW': [[ 200, 1800],   [1000, 1350]],
                                            'WIDE': [[1800, 3200],   [1400, 1750]]},

                                 'DATA': {'NARROW': [[ 50,   500],   [1000,  1000]],
                                            'WIDE': [[500,  3000],   [1000,  1250]]},

                                 'CW':   {'NARROW': [[ 50,   500],   [700,   700]],
                                            'WIDE': [[500,  3000],   [700,  1500]]},

                                 'RTTY': {'NARROW': [[ 50,   500],   [2200, 2220]],
                                            'WIDE': [[500,  3000],   [2200, 1750]]}}

#
        self.fft_window = numpy.hamming(self.block_size)

#
        if self.ani_IF:
            self.ani_IF.event_source.stop()
            del self.ani_IF

        self.ani_IF = animation.FuncAnimation(self.figure_IF, self.update_gui_IF_spectrum, \
                                              interval=10, blit=True, cache_frame_data=False)

#
    def update_gui_IF_spectrum(self, frame):
        active_widget = self.Radio_tabWidget.currentWidget()
        tab_name = active_widget.objectName()

        if (tab_name != 'tab_2'):
            return self.IF_line, self.IF_notch_line, self.IF_contour_line, self.IF_filter_rect

#
        if (self.mic == None):
            return self.IF_line, self.IF_notch_line, self.IF_contour_line, self.IF_filter_rect

#
        f_step = float(self.sample_rate)/float(self.block_size)
        N = int(self.block_size/2)

#
        try:
            IF_filter_mode = self.IF_filter_mode[self.mode]
            IF_filter_center = self.IF_filter_center[IF_filter_mode][self.IF_filter_type.upper()]

#
            with self.mic.recorder(samplerate=self.sample_rate, blocksize=self.block_size) as recorder:
                data = recorder.record(numframes=self.block_size)

            if data.shape[1] > 1:
                audio_data = data[:, 0]

            else:
                audio_data = data.flatten()

#
            x = numpy.linspace(0, int(N*f_step/1000), num=N)
            y = self.fft_gain*numpy.fft.rfft(audio_data*self.fft_window)[0:N]

            self.IF_line.set_xdata(x)
            self.IF_line.set_ydata(20*numpy.log10(numpy.abs(y)))

#
            self.IF_notch_line.set_xdata([self.Notch_freq/1000, self.Notch_freq/1000])
            self.IF_contour_line.set_xdata([self.Contour_freq/1000, self.Contour_freq/1000])

#
            width = self.IF_filter_bandwidth/1000
            center = numpy.interp(self.IF_filter_bandwidth, IF_filter_center[0], IF_filter_center[1])/1000
            shift = self.IF_filter_shift/1000

            x1 = center-width/2+shift
            x2 = center+width/2+shift

            vertices = [[x1-0.3, -30], [x1, 30], [x2, 30], [x2+0.3, -30], [x1, -30]]

            self.IF_filter_rect.set_xy(vertices)
       
        except Exception as e:
            print('\nError: can\'t read from microphone.')

#
        return self.IF_line, self.IF_notch_line, self.IF_contour_line, self.IF_filter_rect

##############################
# Spectrum Plot - EQ
##############################
    def peaking_filter(self, freq, param):
        j = complex(0.0, 1.0)

        f_center = param['center']
        gain = param['gain']
        Q = param['Q']

        if (f_center == 0):
            return numpy.ones(len(freq))

        w_0 = f_center*2*math.pi
        A = math.pow(10, gain/20.0)

        Q_p = Q if (A >= 1) else (A*Q)
        Q_z = Q/A if (A >= 1) else (Q)

        H = lambda s: (s*s+(w_0/Q_z)*s+w_0*w_0)/(s*s+(w_0/Q_p)*s+w_0*w_0)

#
        s = j*freq*2*math.pi*1000
        y = H(s)

        return y
    
#
    def set_EQ_spectrum_plot(self):
        N = 1000
        f_min = 1.0/16.0
        f_max = 4.0

#
        x = numpy.linspace(f_min, f_max, num=N)
        y = numpy.zeros(N)

        self.EQ_line = self.ax_EQ.semilogx(x, y, label='', color='white', linewidth=1, base=2)[0]

        vertices = [[0.1, -30], [0.1, 30], [3.2, 30], [3.2, -30], [0.1, -30]]

        self.EQ_rect = Polygon(vertices, edgecolor='white', facecolor='lightblue', linestyle='--', alpha=0.95)
        self.ax_EQ.add_patch(self.EQ_rect)

#
        self.ax_EQ.patch.set_alpha(0.0)
        self.ax_EQ.spines['bottom'].set_color('white')
        self.ax_EQ.spines['top'].set_color('white')
        self.ax_EQ.spines['left'].set_color('white')
        self.ax_EQ.spines['right'].set_color('white')
        self.ax_EQ.tick_params(axis='y', colors='white')
        self.ax_EQ.tick_params(axis='x', colors='white')

        self.ax_EQ.set_xlabel('Frequency [kHz]', color='white')
        self.ax_EQ.set_ylabel('Level [dB]', color='white')
        self.ax_EQ.set_title('', color='white')

        x_min = f_min
        x_max = f_max

#        self.ax_EQ.set_xlim(x_min, x_max)
#        self.ax_EQ.set_xticks(numpy.arange(0, x_max+0.5, 0.5))

#        formatter = ScalarFormatter(useMathText=True)
#        formatter.set_scientific(False)
        formatter = FormatStrFormatter('%.3g')
        self.ax_EQ.xaxis.set_major_formatter(formatter)

        y_min = -20.0
        y_max = 10.0

        self.ax_EQ.set_ylim(y_min, y_max)
        self.ax_EQ.set_yticks(numpy.arange(y_min, y_max+5, 5))

        for label in self.ax_EQ.get_xticklabels():
            label.set_horizontalalignment('center')
            label.set_family('monospace')

        for label in self.ax_EQ.get_yticklabels():
            label.set_verticalalignment('center')
            label.set_family('monospace')

        self.ax_EQ.text(0.15, 5, '100-3200 Hz')

#
        if self.ani_EQ:
            self.ani_EQ.event_source.stop()
            del self.ani_EQ

        self.ani_EQ = animation.FuncAnimation(self.figure_EQ, self.update_EQ_spectrum, \
                                              interval=100, blit=True, cache_frame_data=False)

#
    def update_EQ_spectrum(self, frame):
        active_widget = self.Radio_tabWidget.currentWidget()
        tab_name = active_widget.objectName()

        if (tab_name != 'tab_3'):
            return self.EQ_line,

#
        N = 1000
        f_min = 1.0/16.0
        f_max = 4.0

#
        x = numpy.linspace(f_min, f_max, num=N)

        y1 = self.peaking_filter(x, self.EQ_param[self.EQ_bank][1])
        y2 = self.peaking_filter(x, self.EQ_param[self.EQ_bank][2])
        y3 = self.peaking_filter(x, self.EQ_param[self.EQ_bank][3])

        y = 20*numpy.log10(abs(y1*y2*y3))

        self.EQ_line.set_xdata(x)
        self.EQ_line.set_ydata(y)

#
        return self.EQ_line,

##############################
# Spectrum Plot - Audio Filter
##############################
    def bandpass_filter(self, freq, param):
        j = complex(0.0, 1.0)

        w_cutoff_1 = param['cutoff_1']*2*math.pi
        slope_1 = param['slope_1']
        w_cutoff_2 = param['cutoff_2']*2*math.pi
        slope_2 = param['slope_2']

        if (w_cutoff_2 == 0.0):
            w_cutoff_2 = 1.0E6

        LP1 = lambda w: w_cutoff_2/(j*w+w_cutoff_2)
        LP2 = lambda w: (w_cutoff_2**3)/((j*w+w_cutoff_2)*((j*w)**2+j*w*w_cutoff_2+w_cutoff_2**2))

        HP1 = lambda w: (j*w)/(j*w+w_cutoff_1)
        HP2 = lambda w: ((j*w)**3)/((j*w+w_cutoff_1)*((j*w)**2+j*w*w_cutoff_1+w_cutoff_1**2))

        LP = {'6': LP1, '18': LP2}['%d' % (round(slope_2))]
        HP = {'6': HP1, '18': HP2}['%d' % (round(slope_1))]

#
        w = freq*2*math.pi*1000
        y = LP(w)*HP(w)

        return y

#
    def set_audio_filter_plot(self):
        N = 1000
        f_min = 1.0/16.0
        f_max = 4.0

#
        x = numpy.linspace(f_min, f_max, num=N)
        y = numpy.zeros(N)

        self.audio_filter_line = self.ax_audio_filter.semilogx(x, y, label='', color='white', linewidth=1, base=2)[0]

        vertices = [[0.1, -30], [0.1, 30], [3.2, 30], [3.2, -30], [0.1, -30]]

        self.audio_filter_rect = Polygon(vertices, edgecolor='white', facecolor='lightblue', linestyle='--', alpha=0.95)
        self.ax_audio_filter.add_patch(self.audio_filter_rect)

#
        self.ax_audio_filter.patch.set_alpha(0.0)
        self.ax_audio_filter.spines['bottom'].set_color('white')
        self.ax_audio_filter.spines['top'].set_color('white')
        self.ax_audio_filter.spines['left'].set_color('white')
        self.ax_audio_filter.spines['right'].set_color('white')
        self.ax_audio_filter.tick_params(axis='y', colors='white')
        self.ax_audio_filter.tick_params(axis='x', colors='white')

        self.ax_audio_filter.set_xlabel('Frequency [kHz]', color='white')
        self.ax_audio_filter.set_ylabel('Level [dB]', color='white')
        self.ax_audio_filter.set_title('', color='white')

        x_min = f_min
        x_max = f_max

        formatter = FormatStrFormatter('%.3g')
        self.ax_audio_filter.xaxis.set_major_formatter(formatter)

        y_min = -20.0
        y_max = 10.0

        self.ax_audio_filter.set_ylim(y_min, y_max)
        self.ax_audio_filter.set_yticks(numpy.arange(y_min, y_max+5, 5))

        for label in self.ax_audio_filter.get_xticklabels():
            label.set_horizontalalignment('center')
            label.set_family('monospace')

        for label in self.ax_audio_filter.get_yticklabels():
            label.set_verticalalignment('center')
            label.set_family('monospace')

        self.ax_audio_filter.text(0.15, 5, '100-3200 Hz')

#
        if self.ani_audio_filter:
            self.ani_audio_filter.event_source.stop()
            del self.ani_audio_filter

        self.ani_Audio_filter = animation.FuncAnimation(self.figure_audio_filter, self.update_audio_filter, \
                                                        interval=100, blit=True, cache_frame_data=False)

#
    def update_audio_filter(self, frame):
        active_widget = self.Radio_tabWidget.currentWidget()
        tab_name = active_widget.objectName()

        if (tab_name != 'tab_4'):
            return self.audio_filter_line,

#
        N = 1000
        f_min = 1.0/16.0
        f_max = 4.0

#
        x = numpy.linspace(f_min, f_max, num=N)

        y = self.bandpass_filter(x, self.Audio_filter_param[self.Audio_filter_bank])

        y = 20*numpy.log10(abs(y))

        self.audio_filter_line.set_xdata(x)
        self.audio_filter_line.set_ydata(y)

#
        return self.audio_filter_line,

##############################
# Audio Sampling
##############################
    def on_FFT_window_changed(self):
        combo_box = self.sender()
        fft_window_name = combo_box.currentText()

        fft_window_func = {'Hamming':  numpy.hamming, \
                           'Hanning':  numpy.hanning, \
                           'Bartlett': numpy.bartlett, \
                           'Blackman': numpy.blackman, \
                           'None':     numpy.ones}[fft_window_name]

        self.fft_window = fft_window_func(self.block_size)

#
    def on_FFT_gain_changed(self):
        combo_box = self.sender()
        fft_gain = combo_box.currentText()

        fft_gain = {'+20 dB':   math.pow(10, 20/20.0), \
                    '+10 dB':   math.pow(10, 10/20.0), \
                      '0 dB':   1.0, \
                    '-10 dB':   math.pow(10, -10/20.0), \
                    '-20 dB':   math.pow(10, -20/20.0)}[fft_gain]

        self.fft_gain = fft_gain

#
    def on_FFT_block_changed(self):
        combo_box = self.sender()
        fft_block = combo_box.currentText()

        self.block_size = int(fft_block)

        self.set_IF_spectrum_plot()

#
    def set_FFT_sampling(self):
        sender_object = self.sender()
        sample_rate = sender_object.text()

        self.sample_rate = {'8 kHz':8000, '16 kHz':16000, '32 kHz':32000}[sample_rate]

        self.set_IF_spectrum_plot()

##############################
# Notch Filter
##############################
    def set_Notch_filter(self, value):
        notch_freq = ft991a.set_manual_notch_level(value*10)

        if (notch_freq != None):
            self.Notch_freq_lcdNumber.display(notch_freq)
            self.Notch_freq = int(notch_freq)

#   
    def Notch_filter_state(self):
        sender_object = self.sender()

        button_state = sender_object.isChecked()

        if (button_state) == True:
            ft991a.set_manual_notch_state(1)

        else:
            ft991a.set_manual_notch_state(0)

##############################
# RF Front End - IPO
##############################
    def set_FrontEnd_ATT(self):
        sender_object = self.sender()

        button_state = sender_object.isChecked()

        if (button_state) == True:
            ft991a.set_RF_attenuator(1)

        else:
            ft991a.set_RF_attenuator(0)

    def set_FrontEnd_IPO(self):
        combo_box = self.sender()
        IPO = combo_box.currentText()

        ft991a.set_IPO(IPO)

##############################
# RF Front End - Noise
##############################
    def set_Noise_DNF(self):
        sender_object = self.sender()

        button_state = sender_object.isChecked()

        if (button_state) == True:
            ft991a.set_digital_notch_state(1)

        else:
            ft991a.set_digital_notch_state(0)

#
    def set_Noise_DNR(self):
        sender_object = self.sender()

        button_state = sender_object.isChecked()

        if (button_state) == True:
            ft991a.set_NR_state(1)

        else:
            ft991a.set_NR_state(0)

#
    def set_Noise_DNR_level(self):
        combo_box = self.sender()
        DNR_level = combo_box.currentText()

# 
        ft991a.set_NR_level(int(DNR_level))

#
    def set_Noise_NB(self):
        sender_object = self.sender()

        button_state = sender_object.isChecked()

        if (button_state) == True:
            ft991a.set_NB_state(1)

        else:
            ft991a.set_NB_state(0)

#
    def set_Noise_NB_level(self):
        combo_box = self.sender()
        NB_level = combo_box.currentText()

#
        ft991a.set_NB_level(int(NB_level))

##############################
# Tx Audio
##############################
    def set_Microphone_Gain(self, value):
        Mic_gain = ft991a.set_microphone_gain(value)

        if (Mic_gain != None):
            self.Microphone_Gain_lcdNumber.display(Mic_gain)

#
    def set_Tx_Audio_BW(self):
        combo_box = self.sender()
        BW = combo_box.currentText()

        BW = {'50~3000': 0, '100~2900': 1, '200~2800':2, '300~2700':3, '400~2600':4}[BW]

        value = '%d' % (BW)

        value = ft991a.set_menu_value(110, value)

        value = ft991a.menu['110'][1](value)
        combo_box.setCurrentText(value)

#
    def set_monitor_level(self, value):
        monitor_level = ft991a.set_monitor_level(value)

        if (monitor_level != None):
            self.Monitor_level_lcdNumber.display(monitor_level)

#
    def set_monitor_state(self, value):
        sender_object = self.sender()

        button_state = sender_object.isChecked()

        if (button_state) == True:
            ft991a.set_monitor_state(1)

        else:
            ft991a.set_monitor_state(0)

##############################
# Speech Processor
##############################
    def set_Speech_Proc(self):
        sender_object = self.sender()

        button_state = sender_object.isChecked()

        if (button_state) == True:
            ft991a.set_SP_state(1)

        else:
            ft991a.set_SP_state(0)

#
    def set_Speech_Proc_EQ(self):
        sender_object = self.sender()

        button_state = sender_object.isChecked()

        if (button_state) == True:
            ft991a.set_SP_EQ_state(1)

        else:
            ft991a.set_SP_EQ_state(0)

#
    def set_Speech_Proc_level(self, value):
        PROC_level = ft991a.set_SP_level(value)

        if (PROC_level != None):
            self.Speech_Proc_lcdNumber.display(PROC_level)

##############################
# Contour Filter
##############################
    def set_Contour_filter(self, value):
        contour_freq = ft991a.set_contour_level(value*10)

        if (contour_freq != None):
            self.Contour_freq_lcdNumber.display(contour_freq)
            self.Contour_freq = int(contour_freq)

#   
    def Contour_filter_state(self):
        sender_object = self.sender()

        button_state = sender_object.isChecked()

        if (button_state) == True:
            ft991a.set_contour_state(1)

        else:
            ft991a.set_contour_state(0)

#   
    def on_Contour_BW_changed(self, value):
        sender_object = self.sender()

        value = '%02d' % (value)

        value = ft991a.set_menu_value(113, value)

        sender_object.setValue(int(value))

#
    def on_Contour_level_changed(self, value):
        sender_object = self.sender()

        value = '%+03d' % (value)

        value = ft991a.set_menu_value(112, value)

        sender_object.setValue(int(value))

##############################
# IF Shift
##############################
    def set_IF_filter_shift(self, value):
        IF_shift = ft991a.set_IF_shift_level(value*20)

        if (IF_shift != None):
            self.IF_filter_shift_lcdNumber.display(IF_shift)
            self.IF_filter_shift = int(IF_shift)

##############################
# IF Bandwidth
##############################
    def set_IF_filter_bandwidth(self, value):
        IF_bandwidth, _ = ft991a.set_IF_bandwidth(value, self.mode, self.IF_filter_type)

        if (IF_bandwidth != None):
            self.IF_filter_BW_lcdNumber.display(IF_bandwidth)
            self.IF_filter_bandwidth = int(IF_bandwidth)

##############################
# IF Filter Type
##############################
    def set_IF_filter_type(self):
        sender_object = self.sender()

        filter_type = sender_object.text()

        IF_filter_type = ft991a.set_IF_filter_type(filter_type)

        if (IF_filter_type != None):
            self.IF_filter_type = IF_filter_type

            IF_bandwidth, index = ft991a.get_IF_bandwidth(self.mode, self.IF_filter_type)

            if (IF_bandwidth != None):
                self.IF_filter_BW_lcdNumber.display(IF_bandwidth)
                self.IF_filter_bandwidth = int(IF_bandwidth)

                was_blocked = self.IF_filter_BW_horizontalSlider.blockSignals(True)
                self.IF_filter_BW_horizontalSlider.setValue(index)
                self.IF_filter_BW_horizontalSlider.blockSignals(was_blocked)

##############################
# Operating Band
##############################
    def on_band_button_clicked(self):
        sender_object = self.sender()

        band = sender_object.text()

        ft991a.set_band(band)

        self.update_RF_settings()

##############################
# Operating Mode
##############################
    def on_mode_button_clicked(self):
        sender_object = self.sender()

        operating_mode = sender_object.text()
        
        ft991a.set_operating_mode(operating_mode)

##############################
# Swap VFO
##############################
    def on_swap_VFO_button_clicked(self):
        ft991a.swap_VFO()

##############################
# Copy VFO
##############################
    def on_copy_VFO_button_clicked(self):
        ft991a.copy_VFO()

##############################
# Split Frequency
##############################
    def on_split_button_clicked(self):
        sender_object = self.sender()

        button_state = sender_object.isChecked()

        if (button_state) == True:
            self.VFO_B_Tx_radioButton.setChecked(True)

        else:
            self.VFO_A_Tx_radioButton.setChecked(True)

##############################
# Memory
##############################
    def on_Memory_scan_button_clicked(self):
        sender_object = self.sender()

        scan = sender_object.property('scan')

        ft991a.set_scan(scan)

#
    def on_Memory_AM_button_clicked(self):
        row = self.Memory_tableWidget.currentRow()

        if (row == -1):
            return

#
        _, info = ft991a.get_band_info()

        if (info != None):
            info = info[:20]+'0'+info[20+1:]

            ft991a.set_memory_data(row+1, info[3:])
            ft991a.memory_vm()
            ft991a.set_memory_vfo()

#
            was_blocked = self.Memory_tableWidget.blockSignals(True)

#
            ft991a.MESSAGE_FLAG = False
            memory, _ = ft991a.get_memory_direct(row)
            ft991a.MESSAGE_FLAG = True

            freq = '{:011,.0f}'.format(float(memory['freq']))
            mode = memory['mode']
            tag = memory['tag']
            skip = memory['skip']
            ctcss_tone = '%5.1f' % (memory['ctcss_tone'])
            dcs_code = '%03d' % (memory['dcs_code'])
            split = memory['split']
            freq_tx = '{:011,.0f}'.format(float(memory['freq_tx']))

#
            self.Memory_tableWidget.setItem(row, 0, QTableWidgetItem(freq))
            self.Memory_tableWidget.setItem(row, 1, QTableWidgetItem(mode))
            self.Memory_tableWidget.setItem(row, 2, QTableWidgetItem(tag))
            self.Memory_tableWidget.setItem(row, 3, QTableWidgetItem(skip))
            self.Memory_tableWidget.setItem(row, 4, QTableWidgetItem(ctcss_tone))
            self.Memory_tableWidget.setItem(row, 5, QTableWidgetItem(dcs_code))
            self.Memory_tableWidget.setItem(row, 6, QTableWidgetItem(split))
            self.Memory_tableWidget.setItem(row, 7, QTableWidgetItem(freq_tx))

#
            edit = []

            for l in range(8):
                if (freq == '-----------') or (l not in edit):
                    item = self.Memory_tableWidget.item(row, l)
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

#
            self.Memory_tableWidget.blockSignals(was_blocked)

#
    def on_Memory_VM_button_clicked(self):
        row = self.Memory_tableWidget.currentRow()

        if (row == -1):
            row = 0
            self.Memory_tableWidget.selectRow(row)

#
        button_state = self.Memory_VM_pushButton.isChecked()

        if (button_state) == True:
            item = self.Memory_tableWidget.item(row, 0)
            freq = item.text()

            if (freq[0] != '-'):
                ft991a.set_memory(row+1)

            else:
                self.Memory_VM_pushButton.setChecked(False)

        else:
            ft991a.memory_vm()

#
    def on_Memory_cell_changed(self):
        row = self.Memory_tableWidget.currentRow()

        item = self.Memory_tableWidget.item(row, 0)
        freq = item.text()

        self.Memory_tableWidget.scrollToItem(item)

        if (freq[0] != '-'):
            button_state = self.Memory_VM_pushButton.isChecked()

            if (button_state) == True:
                ft991a.set_memory(row+1)

#
    def on_Memory_item_changed(self):
        pass

#
    @pause_GUI_update
    def update_Memory(self):
        active_memory_channels = ft991a.get_active_memory()

#
        was_blocked = self.Memory_tableWidget.blockSignals(True)

        for i in range(99):
            if ((i+1) in active_memory_channels):
                memory, _ = ft991a.get_memory_direct(i)

                freq = '{:011,.0f}'.format(float(memory['freq']))
                mode = memory['mode']
                tag = memory['tag']
                skip = memory['skip']
                ctcss_tone = '%5.1f' % (memory['ctcss_tone'])
                dcs_code = '%03d' % (memory['dcs_code'])
                split = memory['split']
                freq_tx = '{:011,.0f}'.format(float(memory['freq_tx']))

            else:
                freq = '-----------'
                mode = '---'
                tag = '------------'
                skip = '-'
                ctcss_tone = '----'
                dcs_code = '----'
                split = '-'
                freq_tx = '-----------'

#
            self.Memory_tableWidget.setItem(i, 0, QTableWidgetItem(freq))
            self.Memory_tableWidget.setItem(i, 1, QTableWidgetItem(mode))
            self.Memory_tableWidget.setItem(i, 2, QTableWidgetItem(tag))
            self.Memory_tableWidget.setItem(i, 3, QTableWidgetItem(skip))
            self.Memory_tableWidget.setItem(i, 4, QTableWidgetItem(ctcss_tone))
            self.Memory_tableWidget.setItem(i, 5, QTableWidgetItem(dcs_code))
            self.Memory_tableWidget.setItem(i, 6, QTableWidgetItem(split))
            self.Memory_tableWidget.setItem(i, 7, QTableWidgetItem(freq_tx))

#
            edit = []

            for l in range(8):
                if (freq == '-----------') or (l not in edit):
                    item = self.Memory_tableWidget.item(i, l)
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

#
            self.statusbar.showMessage('Channel %d is updated...' % (i+1), 2000)
            QApplication.processEvents()

        self.Memory_tableWidget.blockSignals(was_blocked)

#
    @pause_GUI_update
    def save_Memory(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Memory Channel', dir=os.getcwd(), filter='XML Files (*.xml)')

        if (file_path == ''):
            return

        QApplication.processEvents()

#
        active_memory_channels = ft991a.get_active_memory()

#
        root = ET.Element('memory_channel')

        for i in range(99):
            if ((i+1) in active_memory_channels):
                memory, data = ft991a.get_memory_direct(i)

#
                memory_index = '%03d' % (i+1)
                child_memory = ET.SubElement(root, 'm%s' % (memory_index))

# Offset 0
                child = ET.SubElement(child_memory, 'MODE')
                child.text = memory['mode']

# Offset 1
                child = ET.SubElement(child_memory, 'SKIP')
                child.text = memory['skip']
                child = ET.SubElement(child_memory, 'CLAR')
                child.text = memory['clar']
                child = ET.SubElement(child_memory, 'CLAR_RX')
                child.text = memory['clar_rx']
                child = ET.SubElement(child_memory, 'CLAR_TX')
                child.text = memory['clar_tx']
                child = ET.SubElement(child_memory, 'TUNER')
                child.text = memory['tuner']

# Offset 2
                child = ET.SubElement(child_memory, 'REPEATER')
                child.text = memory['repeater']
                child = ET.SubElement(child_memory, 'SPLIT')
                child.text = memory['split']
                child = ET.SubElement(child_memory, 'SHIFT')
                child.text = memory['shift']

# Offset 3
                child = ET.SubElement(child_memory, 'STEP')
                child.text = memory['step']
                child = ET.SubElement(child_memory, 'CTCSS')
                child.text = memory['ctcss']
                child = ET.SubElement(child_memory, 'ATT')
                child.text = memory['att']

# Offset 4
                child = ET.SubElement(child_memory, 'BW_SSB')
                child.text = memory['bw_ssb']
                child = ET.SubElement(child_memory, 'BW_CW')
                child.text = memory['bw_cw']
                child = ET.SubElement(child_memory, 'BW_FM')
                child.text = memory['bw_fm']
                child = ET.SubElement(child_memory, 'BW_RTTY')
                child.text = memory['bw_rtty']
                child = ET.SubElement(child_memory, 'BW_DATA')
                child.text = memory['bw_data']
                child = ET.SubElement(child_memory, 'BW_AM')
                child.text = memory['bw_am']

# Offset 5
                child = ET.SubElement(child_memory, 'IPO')
                child.text = memory['ipo']

# Offset 70
                child = ET.SubElement(child_memory, 'CTCSS_TONE')
                child.text = '%.1f' % (memory['ctcss_tone'])

# Offset 71
                child = ET.SubElement(child_memory, 'DCS_CODE')
                child.text = '%d' % (memory['dcs_code'])

# Offset 74-76
                child = ET.SubElement(child_memory, 'CLAR_OFFSET')
                child.text = '%+d' % (memory['clar_offset'])

# Offset 76-80
                child = ET.SubElement(child_memory, 'FREQ')
                child.text = '%d' % (memory['freq'])
                
# Offset 80-84
                child = ET.SubElement(child_memory, 'FREQ_TX')
                child.text = '%d' % (memory['freq_tx'])

# Offset 84-96
                child = ET.SubElement(child_memory, 'TAG')
                child.text = memory['tag']

#
        ET.indent(root, space='  ')

        utc_time = datetime.now(timezone.utc).strftime('%H%M%S.%f')[:-3]
        file_name, extension = os.path.splitext(file_path)
        file_name = file_name+'.xml'
        base_name = os.path.basename(file_name)

#
        try:
            tree = ET.ElementTree(root)
            tree.write(file_name, encoding='utf-8', xml_declaration=True)

        except IOError as e:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='IO ERROR: %s' % (e), c='red')

        except ValueError as e:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='VALUE ERROR: %s' % (e), c='red')

        except Exception as e:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='EXCEPTION: %s' % (e), c='red')

        else:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='INFO: %s was saved successfully.' % (base_name), c='yellow')

        self.Message_textBrowser.append(message)

#
    @pause_GUI_update
    def load_Memory(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Load Memory Channel', dir=os.getcwd(), filter='XML Files (*.xml)')

        if (file_path == ''):
            return

        QApplication.processEvents()

#
        utc_time = datetime.now(timezone.utc).strftime('%H%M%S.%f')[:-3]
        file_name, extension = os.path.splitext(file_path)
        file_name = file_name+'.xml'
        base_name = os.path.basename(file_name)

#
        try:
            tree = ET.parse(file_name)

            root = tree.getroot()

            if root.tag != 'memory_channel':
                raise Exception('incorrect xml root tag')


            memory = {}

            for child_memory in root:
                channel = int(child_memory.tag[1:])

# Offset 0
                child = child_memory.find('MODE')
                memory['mode'] = child.text

# Offset 1
                child = child_memory.find('SKIP')
                memory['skip'] = child.text
                child = child_memory.find('CLAR')
                memory['clar'] = child.text
                child = child_memory.find('CLAR_RX')
                memory['clar_rx'] = child.text
                child = child_memory.find('CLAR_TX')
                memory['clar_tx'] = child.text
                child = child_memory.find('TUNER')
                memory['tuner'] = child.text

# Offset 2
                child = child_memory.find('REPEATER')
                memory['repeater'] = child.text
                child = child_memory.find('SPLIT')
                memory['split'] = child.text
                child = child_memory.find('SHIFT')
                memory['shift'] = child.text

# Offset 3
                child = child_memory.find('STEP')
                memory['step'] = child.text
                child = child_memory.find('CTCSS')
                memory['ctcss'] = child.text
                child = child_memory.find('ATT')
                memory['att'] = child.text

# Offset 4
                child = child_memory.find('BW_SSB')
                memory['bw_ssb'] = child.text
                child = child_memory.find('BW_CW')
                memory['bw_cw'] = child.text
                child = child_memory.find('BW_FM')
                memory['bw_fm'] = child.text
                child = child_memory.find('BW_RTTY')
                memory['bw_rtty'] = child.text
                child = child_memory.find('BW_DATA')
                memory['bw_data'] = child.text
                child = child_memory.find('BW_AM')
                memory['bw_am'] = child.text

# Offset 5
                child = child_memory.find('IPO')
                memory['ipo'] = child.text

# Offset 70
                child = child_memory.find('CTCSS_TONE')
                memory['ctcss_tone'] = child.text

# Offset 71
                child = child_memory.find('DCS_CODE')
                memory['dcs_code'] = child.text

# Offset 74-76
                child = child_memory.find('CLAR_OFFSET')
                memory['clar_offset'] = child.text

# Offset 76-80
                child = child_memory.find('FREQ')
                memory['freq'] = child.text

# Offset 80-84
                child = child_memory.find('FREQ_TX')
                memory['freq_tx'] = child.text
               
# Offset 84-96
                child = child_memory.find('TAG')
                memory['tag'] = child.text

#
                data = ft991a.set_memory_direct(channel-1, memory)

#
                self.statusbar.showMessage('Channel %d is loaded...' % (channel), 10000)
                QApplication.processEvents()

        except IOError as e:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='IO ERROR: %s' % (e), c='red')

        except ValueError as e:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='VALUE ERROR: %s' % (e), c='red')

        except Exception as e:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='EXCEPTION: %s' % (e), c='red')

        else:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='INFO: %s was loaded successfully.' % (base_name), c='yellow')

        self.Message_textBrowser.append(message)

#
    @pause_GUI_update
    def save_Memory_raw(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Memory Channel', dir=os.getcwd(), filter='XML Files (*.xml)')

        if (file_path == ''):
            return

        QApplication.processEvents()

#
        root = ET.Element('memory_channel')

#
        active_memory_channels = ft991a.get_active_memory()

#
        for i in range(99):
            if ((i+1) in active_memory_channels):
                data = ft991a.get_memory_direct_raw(i)
                channel_tag = ''.join([chr(x) for x in data[84:96]])

#
                checksum = zlib.crc32(bytes(data))
                data = bytearray(data).hex()

#
                memory_index = '%03d' % (i+1)
                child_memory = ET.SubElement(root, 'm%s' % (memory_index))

                child_comment =  ET.Comment(channel_tag)
                child_memory.insert(0, child_comment)

                child_comment = ET.Comment('00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F')
                child_memory.insert(1, child_comment)

#
                for l in range(6):
                    child = ET.SubElement(child_memory, 'R%d' % (l))

                    child.text = ' '.join(re.findall(f'.{{1,{2}}}', data[l*32:l*32+32]))

                child = ET.SubElement(child_memory, 'checksum')
                child.text = '%d' % (checksum)

        ET.indent(root, space='  ')

        utc_time = datetime.now(timezone.utc).strftime('%H%M%S.%f')[:-3]
        file_name, extension = os.path.splitext(file_path)
        file_name = file_name+'.xml'
        base_name = os.path.basename(file_name)

#
        try:
            tree = ET.ElementTree(root)
            tree.write(file_name, encoding='utf-8', xml_declaration=True)

        except IOError as e:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='IO ERROR: %s' % (e), c='red')

        except ValueError as e:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='VALUE ERROR: %s' % (e), c='red')

        except Exception as e:
            _, _, tb = sys.exc_info()
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='EXCEPTION: line %d, %s' % (tb.tb_lineno, e), c='red')

        else:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='INFO: %s was saved successfully.' % (base_name), c='yellow')

        self.Message_textBrowser.append(message)

#
    @pause_GUI_update
    def load_Memory_raw(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Load Memory Channel', dir=os.getcwd(), filter='XML Files (*.xml)')

        if (file_path == ''):
            return

        QApplication.processEvents()

#
        utc_time = datetime.now(timezone.utc).strftime('%H%M%S.%f')[:-3]
        message = '%s: <font color="{c}">{m}</font>' % (utc_time)
        file_name, extension = os.path.splitext(file_path)
        file_name = file_name+'.xml'
        base_name = os.path.basename(file_name)

#
        active_memory_channels = []

#
        error_flag = 0

#
        try:
            tree = ET.parse(file_name)

            root = tree.getroot()

            if root.tag != 'memory_channel':
                raise Exception('incorrect xml root tag')

#
            for child_memory in root:
                channel = int(child_memory.tag[1:])

                if (channel < 1) or (channel > 99):
                    message = '%s: <font color="{c}">{m}</font>' % (utc_time)
                    message = message.format(m='ERROR: incorrect memory index: %d' % (channel), c='red')
                    self.Message_textBrowser.append(message)

                    error_flag = 1

                    continue

#
                memory = []

                for l in range(6):
                    child = child_memory.find('R%d' % (l))
                    data = child.text.replace(' ', '')

                    data = list(bytes.fromhex(data))
                    memory.extend(data)

                child = child_memory.find('checksum')
                checksum = int(child.text)

                if (checksum != zlib.crc32(bytes(memory))):
                    message = '%s: <font color="{c}">{m}</font>' % (utc_time)
                    message = message.format(m='ERROR: wrong checksum for memory %d' % (channel), c='red')
                    self.Message_textBrowser.append(message)

                    error_flag = 1

                    continue

#
                ft991a.set_memory_direct_raw(channel-1, bytes(memory))
                active_memory_channels.append(channel)

#
                self.statusbar.showMessage('Channel %d is loaded...' % (channel), 10000)
                QApplication.processEvents()

#
            ft991a.set_active_memory(active_memory_channels)
            self.update_Memory()

        except IOError as e:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='IO ERROR: %s' % (e), c='red')

        except ValueError as e:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='VALUE ERROR: %s' % (e), c='red')

        except Exception as e:
            _, _, tb = sys.exc_info()
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='EXCEPTION: line %d, %s' % (tb.tb_lineno, e), c='red')

        else:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)

            if (error_flag == 0):
                message = message.format(m='INFO: %s was loaded successfully.' % (base_name), c='yellow')

            else:
                message = message.format(m='INFO: %s was loaded with error(s).' % (base_name), c='yellow')

        self.Message_textBrowser.append(message)

##############################
# VFO_A Tx
##############################
    def VFO_A_set_Tx(self):
        button = self.sender()

        if button.isChecked():
            ft991a.set_function_Tx('VFO_A')

            self.A_B_pushButton_3.setChecked(False)

##############################
# VFO_B Tx
##############################
    def VFO_B_set_Tx(self):
        button = self.sender()

        if button.isChecked():
            ft991a.set_function_Tx('VFO_B')

            self.A_B_pushButton_3.setChecked(True)

##############################
# RF CLAR - Clear
##############################
    def clear_RF_clar(self):
        ft991a.clear_RF_clar()

        was_blocked = self.Clar_dial.blockSignals(True) 
        self.Clar_dial.setValue(0)
        self.Clar_dial.blockSignals(was_blocked)

        self.Clar_dial.setProperty('stored_value', 0)
        self.Clar_lcdNumber.display(0)

##############################
# RF CLAR - Set
##############################
    def set_RF_clar(self, value):
        dial_value = self.Clar_dial.value()

        stored_dial_value = self.Clar_dial.property('stored_value')

        step = dial_value-stored_dial_value

        if abs(step) > 50:
            step = (step+99) if step < 0 else (step-99)

        self.Clar_dial.setProperty('stored_value', dial_value)

#
        clar = int(self.Clar_lcdNumber.value())+step

#
        clar = '%d' % (clar)
        self.Clar_lcdNumber.display(clar)

#
        if (step > 0):
            ft991a.RF_clar_up(step)

        else:
            ft991a.RF_clar_down(abs(step))

##############################
# RF CLAR - Mode
##############################
    def on_clar_mode_changed(self):
        combo_box = self.sender()
        clar_mode = combo_box.currentText()

#
        if (clar_mode == 'Rx'):
            ft991a.set_RF_clar_state(1)
            ft991a.set_RF_clar_state_Tx(0)

        elif (clar_mode == 'Tx'):
            ft991a.set_RF_clar_state(0)
            ft991a.set_RF_clar_state_Tx(1)

        elif (clar_mode == 'Rx/Tx'):
            ft991a.set_RF_clar_state(1)
            ft991a.set_RF_clar_state_Tx(1)

        else:
            ft991a.set_RF_clar_state(0)
            ft991a.set_RF_clar_state_Tx(0)

##############################
# Set RF Squelch
##############################
    def set_RF_squelch(self, value):
        RF_squelch = ft991a.set_RF_squelch(value)

        if (RF_squelch != None):
            self.RF_squelch_lcdNumber.display(RF_squelch)

##############################
# Set RF Power
##############################
    def set_RF_power(self, value):
        RF_power = ft991a.set_RF_power(value)

        if (RF_power != None):
            self.RF_power_lcdNumber.display(RF_power)
            self.RF_power_verticalSlider.setValue(RF_power)

        else:
            RF_power = ft991a.get_RF_power()
            self.RF_power_verticalSlider.setValue(RF_power)

##############################
# Set AF Gain
##############################
    def set_AF_gain(self, value):
        AF_gain = ft991a.set_AF_gain(int(value))

        if (AF_gain != None):
            self.AF_gain_lcdNumber.display(round(AF_gain/2.55))

##############################
# Set RF Gain
##############################
    def set_RF_gain(self, value):
        RF_gain = ft991a.set_RF_gain(int(value))

        if (RF_gain != None):
            self.RF_gain_lcdNumber.display(round(RF_gain/2.55))

##############################
# Squelch - CTCSS Changed
##############################
    def on_Squelch_CTCSS_changed(self, index):
        ft991a.set_ctcss_tone_freq(index)

##############################
# Squelch - DCS Changed
##############################
    def on_Squelch_DCS_changed(self, index):
        ft991a.set_dcs_code(index)

##############################
# Squelch - Offset Changed
##############################
    def on_Squelch_offset_changed(self):
        combo_box = self.sender()
        offset = combo_box.currentText()

        ft991a.set_repeater_shift(offset)

##############################
# Squelch - Mode Changed
##############################
    def on_Squelch_mode_changed(self):
        combo_box = self.sender()
        Squelch_mode = combo_box.currentText()

        ft991a.set_ctcss_mode(Squelch_mode)

##############################
# EQ
##############################
    def on_EQ_bank(self):
        sender_object = self.sender()

        EQ_bank = sender_object.text()

        self.EQ_bank = {'Bank 1': 1, 'Bank 2': 2}[EQ_bank]

        self.EQ_get_parameters()

#
    @pause_GUI_update
    def EQ_get_parameters(self):
        menu_index = {'11': [119, 120, 121], 
                      '12': [122, 123, 124], 
                      '13': [125, 126, 127],
                      '21': [128, 129, 130], 
                      '22': [131, 132, 133], 
                      '23': [134, 135, 136]}

#
        for i in range(3):
            index = '%d%d' % (self.EQ_bank, i+1)

            value = int(ft991a.get_menu_value(menu_index[index][0]))

            object_name = u'EQ_%d_center_verticalSlider' % (i+1)
            _object = getattr(self, object_name)
            _object.valueChanged.disconnect(self.set_EQ_center)
            _object.setValue(value)
            _object.valueChanged.connect(self.set_EQ_center)

            value = ft991a.menu['%03d' % (menu_index[index][0])][1](value)
            self.EQ_param[self.EQ_bank][i+1]['center'] = 0 if (value == 'OFF') else float(value)

#
            value = int(ft991a.get_menu_value(menu_index[index][1]))

            object_name = u'EQ_%d_gain_verticalSlider' % (i+1)
            _object = getattr(self, object_name)
            _object.valueChanged.disconnect(self.set_EQ_gain)
            _object.setValue(value)
            _object.valueChanged.connect(self.set_EQ_gain)

            value = ft991a.menu['%03d' % (menu_index[index][1])][1](value)
            self.EQ_param[self.EQ_bank][i+1]['gain'] = float(value)

#
            value = int(ft991a.get_menu_value(menu_index[index][2]))

            object_name = u'EQ_%d_BW_verticalSlider' % (i+1)
            _object = getattr(self, object_name)
            _object.valueChanged.disconnect(self.set_EQ_BW)
            _object.setValue(value)
            _object.valueChanged.connect(self.set_EQ_BW)

            value = ft991a.menu['%03d' % (menu_index[index][2])][1](value)
            self.EQ_param[self.EQ_bank][i+1]['Q'] = float(value)

#
    def EQ_set_parameters(self, param):
        menu_index = {'11': [119, 120, 121], 
                      '12': [122, 123, 124], 
                      '13': [125, 126, 127],
                      '21': [128, 129, 130], 
                      '22': [131, 132, 133], 
                      '23': [134, 135, 136]}

#
        for i in range(3):
            index = '%d%d' % (self.EQ_bank, i+1)

            value = '%02d' % (param[i+1]['center'])
            ft991a.set_menu_value(menu_index[index][0], value)

            object_name = u'EQ_%d_center_verticalSlider' % (i+1)
            _object = getattr(self, object_name)
            _object.valueChanged.disconnect(self.set_EQ_center)
            _object.setValue(param[i+1]['center'])
            _object.valueChanged.connect(self.set_EQ_center)

            value = ft991a.menu['%03d' % (menu_index[index][0])][1](param[i+1]['center'])
            self.EQ_param[self.EQ_bank][i+1]['center'] = 0 if (value == 'OFF') else float(value)

#
            value =  '%+03d' % (param[i+1]['gain'])
            ft991a.set_menu_value(menu_index[index][1], value)

            object_name = u'EQ_%d_gain_verticalSlider' % (i+1)
            _object = getattr(self, object_name)
            _object.valueChanged.disconnect(self.set_EQ_gain)
            _object.setValue(param[i+1]['gain'])
            _object.valueChanged.connect(self.set_EQ_gain)

            value = ft991a.menu['%03d' % (menu_index[index][1])][1](param[i+1]['gain'])
            self.EQ_param[self.EQ_bank][i+1]['gain'] = float(value)

#
            value =  '%02d' % (param[i+1]['Q'])
            ft991a.set_menu_value(menu_index[index][2], value)

            object_name = u'EQ_%d_BW_verticalSlider' % (i+1)
            _object = getattr(self, object_name)
            _object.valueChanged.disconnect(self.set_EQ_BW)
            _object.setValue(param[i+1]['Q'])
            _object.valueChanged.connect(self.set_EQ_BW)

            value = ft991a.menu['%03d' % (menu_index[index][2])][1](param[i+1]['Q'])
            self.EQ_param[self.EQ_bank][i+1]['Q'] = float(value)

#
    def on_EQ_reset(self):
        EQ_param = {1: {1: {'center':  0, 'gain': 5, 'Q': 10},
                        2: {'center':  0, 'gain': 5, 'Q': 10},
                        3: {'center':  0, 'gain': 5, 'Q': 10}},
                    2: {1: {'center':  2, 'gain': 0, 'Q':  2},
                        2: {'center':  2, 'gain': 0, 'Q':  1},
                        3: {'center':  7, 'gain': 0, 'Q':  1}}}

#
        self.EQ_set_parameters(EQ_param[self.EQ_bank])

#
    def on_EQ_preset_selected(self):
        combo_box = self.sender()
        preset = combo_box.currentText()

        if (preset == ''):
            return

#
        EQ_preset = {'High Boost 1': {1: {'center':  0, 'gain':  5,  'Q': 10},
                                      2: {'center':  8, 'gain':  3,  'Q':  1},
                                      3: {'center': 15, 'gain':  3,  'Q':  1}},

                     'High Boost 2': {1: {'center':  0, 'gain':  5,  'Q': 10},
                                      2: {'center':  8, 'gain':  3,  'Q':  2},
                                      3: {'center':  7, 'gain':  3,  'Q':  2}},

                     'Mid Boost 1':  {1: {'center': 7,  'gain':  3,  'Q':  1},
                                      2: {'center': 9,  'gain':  3,  'Q':  1},
                                      3: {'center': 0,  'gain':  5,  'Q': 10}},

                     'Mid Boost 2':  {1: {'center': 7,  'gain':  5,  'Q':  2},
                                      2: {'center': 5,  'gain':  5,  'Q':  2},
                                      3: {'center': 0,  'gain':  5,  'Q': 10}},

                    'Studio Mic 1':  {1: {'center': 1,  'gain': -10, 'Q':  2},
                                      2: {'center': 2,  'gain':  -3, 'Q':  3},
                                      3: {'center': 7,  'gain':   8, 'Q':  1}}}

#
        self.EQ_set_parameters(EQ_preset[preset])

#
    def set_EQ_center(self, value):
        slider = self.sender() 
        slider_name = slider.objectName()

        EQ_band = int(re.findall('EQ_(.*)_center_verticalSlider', slider_name)[0])

        menu_index = {1: {1: 119, 2: 122, 3: 125},
                      2: {1: 128, 2: 131, 3: 134}}[self.EQ_bank][EQ_band]

        value = '%02d' % (value)

        value = ft991a.set_menu_value(menu_index, value)

        value = ft991a.menu['%03d' % (menu_index)][1](value)
        value = 0.0 if (value == 'OFF') else float(value)
        self.EQ_param[self.EQ_bank][EQ_band]['center'] = value

#
    def set_EQ_gain(self, value):
        slider = self.sender() 
        slider_name = slider.objectName()

        EQ_band = int(re.findall('EQ_(.*)_gain_verticalSlider', slider_name)[0])

        menu_index = {1: {1: 120, 2: 123, 3: 126},
                      2: {1: 129, 2: 132, 3: 135}}[self.EQ_bank][EQ_band]

        value = '%+03d' % (value)

        value = ft991a.set_menu_value(menu_index, value)

        value = ft991a.menu['%03d' % (menu_index)][1](value)
        self.EQ_param[self.EQ_bank][EQ_band]['gain'] = float(value)

#
    def set_EQ_BW(self, value):
        slider = self.sender() 
        slider_name = slider.objectName()

        EQ_band = int(re.findall('EQ_(.*)_BW_verticalSlider', slider_name)[0])

        menu_index = {1: {1: 121, 2: 124, 3: 127},
                      2: {1: 130, 2: 133, 3: 136}}[self.EQ_bank][EQ_band]

        value = '%02d' % (value)

        value = ft991a.set_menu_value(menu_index, value)

        value = ft991a.menu['%03d' % (menu_index)][1](value)
        self.EQ_param[self.EQ_bank][EQ_band]['Q'] = float(value)

##############################
# Audio Filter
##############################
    def on_Audio_filter_bank(self):
        sender_object = self.sender()

        self.Audio_filter_bank = sender_object.property('bank')

        self.Audio_filter_get_cutoff()
        self.Audio_filter_get_slope()

#
    @pause_GUI_update
    def Audio_filter_get_cutoff(self):
        menu_index = {1: {1:  41, 2:  43},
                      2: {1:  50, 2:  52},
                      3: {1:  66, 2:  68},
                      4: {1:  92, 2:  94},
                      5: {1: 102, 2: 104}}[self.Audio_filter_bank]

#
        value = int(ft991a.get_menu_value(menu_index[1]))

        object_name = u'Audio_filter_horizontalSlider_1'
        _object = getattr(self, object_name)
        _object.valueChanged.disconnect(self.set_Audio_filter_cutoff)
        _object.setValue(value)
        _object.valueChanged.connect(self.set_Audio_filter_cutoff)

        value = ft991a.menu['%03d' % (menu_index[1])][1](value)
        value = 0.0 if (value == 'OFF') else float(re.findall('(.*)Hz', value)[0])
        self.Audio_filter_param[self.Audio_filter_bank]['cutoff_1'] = value

#
        value = int(ft991a.get_menu_value(menu_index[2]))

        object_name = u'Audio_filter_horizontalSlider_2'
        _object = getattr(self, object_name)
        _object.valueChanged.disconnect(self.set_Audio_filter_cutoff)
        _object.setValue(value)
        _object.valueChanged.connect(self.set_Audio_filter_cutoff)

        value = ft991a.menu['%03d' % (menu_index[2])][1](value)
        value = 0.0 if (value == 'OFF') else float(re.findall('(.*)Hz', value)[0])
        self.Audio_filter_param[self.Audio_filter_bank]['cutoff_2'] = value

#
    @pause_GUI_update
    def Audio_filter_get_slope(self):
        menu_index = {1: {1:  42, 2:  44},
                      2: {1:  51, 2:  53},
                      3: {1:  67, 2:  69},
                      4: {1:  93, 2:  95},
                      5: {1: 103, 2: 105}}[self.Audio_filter_bank]

#
        value = ft991a.get_menu_value(menu_index[1])

        object_name = u'Audio_filter_comboBox_1'
        _object = getattr(self, object_name)
        _object.currentIndexChanged.disconnect(self.set_Audio_filter_slope)
        _object.setCurrentIndex(int(value))
        _object.currentIndexChanged.connect(self.set_Audio_filter_slope)

        value = ft991a.menu['%03d' % (menu_index[1])][1](value)
        value = re.findall('(.*)dB/oct', value)
        self.Audio_filter_param[self.Audio_filter_bank]['slope_1'] = float(value[0])

#
        value = ft991a.get_menu_value(menu_index[2])

        object_name = u'Audio_filter_comboBox_2'
        _object = getattr(self, object_name)
        _object.currentIndexChanged.disconnect(self.set_Audio_filter_slope)
        _object.setCurrentIndex(int(value))
        _object.currentIndexChanged.connect(self.set_Audio_filter_slope)

        value = ft991a.menu['%03d' % (menu_index[2])][1](value)
        value = re.findall('(.*)dB/oct', value)
        self.Audio_filter_param[self.Audio_filter_bank]['slope_2'] = float(value[0])

#
    def set_Audio_filter_cutoff(self, value):
        slider = self.sender() 
        slider_name = slider.objectName()

        side = slider.property('side')

        menu_index = {1: {1:  41, 2:  43},
                      2: {1:  50, 2:  52},
                      3: {1:  66, 2:  68},
                      4: {1:  92, 2:  94},
                      5: {1: 102, 2: 104}}[self.Audio_filter_bank][side]

        value = '%02d' % (value)

        value = ft991a.set_menu_value(menu_index, value)

        value = ft991a.menu['%03d' % (menu_index)][1](value)
        value = 0.0 if (value == 'OFF') else float(re.findall('(.*)Hz', value)[0])
        self.Audio_filter_param[self.Audio_filter_bank]['cutoff_%d' % (side)] = value

#
    def set_Audio_filter_slope(self, value):
        combo_box = self.sender() 
        combo_box_name = combo_box.objectName()

        side = combo_box.property('side')

        menu_index = {1: {1:  42, 2:  44},
                      2: {1:  51, 2:  53},
                      3: {1:  67, 2:  69},
                      4: {1:  93, 2:  95},
                      5: {1: 103, 2: 105}}[self.Audio_filter_bank][side]

        value = '%d' % (value)

        value = ft991a.set_menu_value(menu_index, value)

        value = ft991a.menu['%03d' % (menu_index)][1](value)
        value = float(re.findall('(.*)dB/oct', value)[0])
        self.Audio_filter_param[self.Audio_filter_bank]['slope_%d' % (side)] = value

##############################
# VFO_A Frequency - Keyboard
##############################
    def VFO_A_set_frequency(self):
        entered_value = self.VFO_A_lineEdit.text()
        entered_value = entered_value.replace(',', '').replace(' ', '.')

#
        try:
            freq = float(entered_value)*1E6

            if (entered_value[0] == '+') or (entered_value[0] == '-'):
                curret_freq = ft991a.get_frequency_VFO_A()
                freq = ft991a.set_frequency_VFO_A(curret_freq+freq)

            else:
                freq = ft991a.set_frequency_VFO_A(freq)

        except:
            return

        if (freq != None):
            freq = '%d' % (freq)
            self.VFO_A_lcdNumber.display(freq)

##############################
# VFO_B Frequency - Keyboard
##############################
    def VFO_B_set_frequency(self):
        entered_value = self.VFO_B_lineEdit.text()
        entered_value = entered_value.replace(',', '').replace(' ', '.')

#
        try:
            freq = float(entered_value)*1E6

            if (entered_value[0] == '+') or (entered_value[0] == '-'):
                curret_freq = ft991a.get_frequency_VFO_B()
                freq = ft991a.set_frequency_VFO_B(curret_freq+freq)

            else:
                freq = ft991a.set_frequency_VFO_B(freq)

        except:
            return

#
        if (freq != None):
            freq = '%d' % (freq)
            self.VFO_B_lcdNumber.display(freq)

##############################
# VFO_A Frequency - Dial
##############################
    def VFO_A_set_fast(self):
        button = self.sender()

        if button.isChecked():
            self.VFO_A_fast = 100

        else:
            self.VFO_A_fast = 1

#
    def VFO_A_dial_frequency(self):
        dial_value = self.VFO_A_dial.value()

        stored_dial_value = self.VFO_A_dial.property('stored_value')

        step = dial_value-stored_dial_value

        if abs(step) > 50:
            step = (step+99) if step < 0 else (step-99)

        self.VFO_A_dial.setProperty('stored_value', dial_value)

#
        freq = int(self.VFO_A_lcdNumber.value())+step*10*self.VFO_A_fast
        freq = ft991a.set_frequency_VFO_A(freq)

        if (freq != None):
            freq = '%d' % (freq)
            self.VFO_A_lcdNumber.display(freq)

##############################
# VFO_B Frequency - Dial
##############################
    def VFO_B_set_fast(self):
        button = self.sender()

        if button.isChecked():
            self.VFO_B_fast = 100

        else:
            self.VFO_B_fast = 1

#
    def VFO_B_dial_frequency(self):
        dial_value = self.VFO_B_dial.value()

        stored_dial_value = self.VFO_B_dial.property('stored_value')

        step = dial_value-stored_dial_value

        if abs(step) > 50:
            step = (step+99) if step < 0 else (step-99)

        self.VFO_B_dial.setProperty('stored_value', dial_value)

#
        freq = int(self.VFO_B_lcdNumber.value())+step*10*self.VFO_B_fast
        freq = ft991a.set_frequency_VFO_B(freq)

        if (freq != None):
            freq = '%d' % (freq)
            self.VFO_B_lcdNumber.display(freq)

##############################
# Radio Menu - Default
##############################
    def on_default_button_clicked(self):
        sender_object = self.sender()

        menu_index = int(sender_object.objectName().split('_')[2])

        object_name = u'menu_comboBox_%s' % (menu_index)
        combo_box = getattr(self, object_name)

        menu_name = ft991a.menu['%03d' % (menu_index)][0]
        menu_function = ft991a.menu['%03d' % (menu_index)][1]
        menu_default = ft991a.menu['%03d' % (menu_index)][2]
        menu_range = ft991a.menu['%03d' % (menu_index)][3]
        menu_digits = ft991a.menu['%03d' % (menu_index)][4]
        menu_notes = ft991a.menu['%03d' % (menu_index)][5]

        default_index = combo_box.findText(menu_default)

        was_blocked = combo_box.blockSignals(True)

        if (menu_range[0] < 0):
            value = '{value:+0{w}d}'.format(value=menu_range[default_index], w=menu_digits)

        else:
            value = '{value:0{w}d}'.format(value=menu_range[default_index], w=menu_digits)

        value = ft991a.set_menu_value(menu_index, value)

        combo_box.setCurrentText(menu_function(value))

        combo_style = 'QComboBox{combobox-popup: 0;}\n'
        combo_box.setStyleSheet(combo_style)

        combo_box.blockSignals(was_blocked)

##############################
# Radio Menu - Selection
##############################
    def on_menu_parameter_changed(self, index):
        sender_object = self.sender()

        menu_index = int(sender_object.objectName().split('_')[2])

        object_name = u'menu_comboBox_%s' % (menu_index)
        combo_box = getattr(self, object_name)

        menu_name = ft991a.menu['%03d' % (menu_index)][0]
        menu_function = ft991a.menu['%03d' % (menu_index)][1]
        menu_default = ft991a.menu['%03d' % (menu_index)][2]
        menu_range = ft991a.menu['%03d' % (menu_index)][3]
        menu_digits = ft991a.menu['%03d' % (menu_index)][4]
        menu_notes = ft991a.menu['%03d' % (menu_index)][5]

        default_index = combo_box.findText(menu_default)

#
        combo_style = 'QComboBox{combobox-popup: 0;}\n'

        if (default_index != index):
            combo_style = combo_style+'QComboBox{color: red;}'

        combo_box.setStyleSheet(combo_style)

#
        was_blocked = combo_box.blockSignals(True)

        if (menu_range[0] < 0):
            value = '{value:+0{w}d}'.format(value=menu_range[index], w=menu_digits)

        else:
            value = '{value:0{w}d}'.format(value=menu_range[index], w=menu_digits)

        value = ft991a.set_menu_value(menu_index, value)

        combo_box.setCurrentText(menu_function(value))

        combo_box.blockSignals(was_blocked)

##############################
# Radio Menu
##############################
    @pause_GUI_update
    def save_Radio_menu(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Radio Menu', dir=os.getcwd(), filter='XML Files (*.xml)')

        if (file_path == ''):
            return

        QApplication.processEvents()

#
        root = ET.Element('radio_menu')

        for m in ft991a.menu.keys():
            menu_index = int(m)

            object_name = u'menu_comboBox_%s' % (menu_index)
            combo_box = getattr(self, object_name)

            value = combo_box.currentText()

            child = ET.SubElement(root, 'm%s' % (m))
            child.text = str(value)

        ET.indent(root, space='  ')

        utc_time = datetime.now(timezone.utc).strftime('%H%M%S.%f')[:-3]
        file_name, extension = os.path.splitext(file_path)
        file_name = file_name+'.xml'
        base_name = os.path.basename(file_name)

#
        try:
            tree = ET.ElementTree(root)
            tree.write(file_name, encoding='utf-8', xml_declaration=True)

        except IOError as e:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='IO ERROR: %s' % (e), c='red')

        except ValueError as e:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='VALUE ERROR: %s' % (e), c='red')

        except Exception as e:
            _, _, tb = sys.exc_info()
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='EXCEPTION: line %d, %s' % (tb.tb_lineno, e), c='red')

        else:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='INFO: %s was saved successfully.' % (base_name), c='yellow')

        self.Message_textBrowser.append(message)

#
    @pause_GUI_update
    def load_Radio_menu(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Load Radio Menu', dir=os.getcwd(), filter='XML Files (*.xml)')

        if (file_path == ''):
            return

        QApplication.processEvents()

#
        utc_time = datetime.now(timezone.utc).strftime('%H%M%S.%f')[:-3]
        file_name, extension = os.path.splitext(file_path)
        file_name = file_name+'.xml'
        base_name = os.path.basename(file_name)

#
        error_flag = 0 

#
        try:
            tree = ET.parse(file_name)

            root = tree.getroot()

            if root.tag != 'radio_menu':
                raise Exception('incorrect xml root tag')

#
            for child in root:
                tag = child.tag
                value = child.text

                menu_index = int(tag[1:])

                if (menu_index < 1) or (menu_index > 153):
                    message = '%s: <font color="{c}">{m}</font>' % (utc_time)
                    message = message.format(m='ERROR: incorrect menu index: %d' % (menu_index), c='red')
                    self.Message_textBrowser.append(message)

                    error_flag = 1

                    continue

                object_name = u'menu_comboBox_%d' % (menu_index)
                menu_combo_box = getattr(self, object_name)

                value_index = menu_combo_box.findText(value)

                if (value_index == -1) and (value != None):
                    message = '%s: <font color="{c}">{m}</font>' % (utc_time)
                    message = message.format(m='ERROR: wrong value for menu %d: %s' % (menu_index, value), c='red')
                    self.Message_textBrowser.append(message)

                    error_flag = 1

                    continue

#
                menu_combo_box.setCurrentText(value)

#
                self.statusbar.showMessage('Menu %d of 153 was loaded...' % (menu_index), 10000)
                QApplication.processEvents()

        except IOError as e:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='IO ERROR: %s' % (e), c='red')

        except ValueError as e:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='VALUE ERROR: %s' % (e), c='red')

        except Exception as e:
            _, _, tb = sys.exc_info()
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)
            message = message.format(m='EXCEPTION: line %d, %s' % (tb.tb_lineno, e), c='red')

        else:
            message = '%s: <font color="{c}">{m}</font>' % (utc_time)

            if (error_flag == 0):
                message = message.format(m='INFO: %s was loaded successfully.' % (base_name), c='yellow')

            else:
                message = message.format(m='INFO: %s was loaded with error(s).' % (base_name), c='yellow')

        self.Message_textBrowser.append(message)

#
    @pause_GUI_update
    def update_Radio_menu(self):
        for m in ft991a.menu.keys():
            menu_index = int(m)-1

            menu_value = ft991a.get_menu_value(menu_index+1)

#
            menu_name = ft991a.menu[m][0]
            menu_function = ft991a.menu[m][1]
            menu_default = ft991a.menu[m][2]
            menu_range = ft991a.menu[m][3]
            menu_digits = ft991a.menu[m][4]
            menu_notes = ft991a.menu[m][5]

#
            object_name = u'menu_comboBox_%d' % (menu_index+1)
            menu_combo_box = getattr(self, object_name)

            object_name = u'menu_pushButton_%d' % (menu_index+1)
            menu_button = getattr(self, object_name)

#
            was_blocked = menu_combo_box.blockSignals(True) 

            if (menu_default == '') or (menu_value == None):
                menu_combo_box.setEnabled(False)
                menu_button.setEnabled(False)

            else:
                menu_combo_box.setEnabled(True)
                menu_button.setEnabled(True)

                menu_combo_box.setCurrentText(menu_function(menu_value))

                combo_style = 'QComboBox{ combobox-popup: 0;}\n'
                if (menu_function(menu_value) != menu_default):
                    combo_style = combo_style+'QComboBox{ color: red;}'

                menu_combo_box.setStyleSheet(combo_style)

            menu_combo_box.blockSignals(was_blocked)

#
            self.statusbar.showMessage('Menu %d of 153 was updated...' % (int(m)), 2000)
            QApplication.processEvents()

#
def get_serial_ports():
    ports = serial.tools.list_ports.comports()
    results = []

    for port in ports:
        permission = False

        try:
            test_ser = serial.Serial(port.device)
            test_ser.close()

            permission = True

        except (OSError, serial.SerialException) as e:
            permission = False

        results.append({'dev': port.device,
                        'desc': port.description,
                        'hwid': port.hwid,
                        'perm': permission})
    
    return results

#
def auto_detect_port(baudrate):
    ports = serial.tools.list_ports.comports()
    results = []

    for port in ports:
        radio_id = None

        try:
            ser = serial.Serial(port.device, 
                                baudrate=baudrate,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                bytesize=serial.EIGHTBITS,
                                timeout=0.5)

            ser.write('ID;'.encode('ASCII'))
            data = ser.read_until(expected=b';').decode('ASCII')

            radio_id = re.findall('ID(.*?);', data)[0]

        except:
            pass

        port = ser.port

        if (ser.is_open == True):
            ser.close()

        if (radio_id == '0670'):
            return radio_id, port

    return None

#
def dump_memory():
    data = ft991a.dump_memory()
    data_hex = bytearray(data).hex()

    data = []
        
    utc_time = datetime.now(timezone.utc).strftime('%H%M%S%f')[:-3]
    fp = open('radio_nvram_%s' % (utc_time), 'w')  

    for i in range(len(data_hex)//32):
        data.append(' '.join(re.findall(f'.{{1,{2}}}', data_hex[i*32:i*32+32])).upper())

        fp.write('%04X  %s\n' % (16*i, data[-1]))

    fp.close()

#
if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='ft991a_boss.py',
                    description='A Python based control software for the Yaesu FT991A transceiver.',
                    epilog='', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    required_named = parser.add_argument_group('required named arguments')

    parser.add_argument('-baud', metavar='<baudrate>', dest='baudrate', default='38400',
                        help='data rate of the radio serial port.')
    parser.add_argument('-cid', metavar='<com_id>', dest='com_id',  default='auto',
                        help='serial communication interface ID. Use --listcom to list the available interfaces.')
    parser.add_argument('-sid', metavar='<sound_id>', dest='sound_id',  default='auto',
                        help='sound interface ID. Use --listsound to list the available sound interfaces.')
    parser.add_argument('--listcom', action='store_true',  
                        help='list available serial ports.')
    parser.add_argument('--listsound', action='store_true', 
                        help='list available sound interfaces.')
    parser.add_argument('--exop', action='store_true', 
                        help='extended operating Rx frequency range.')
    parser.add_argument('--dumpram', action='store_true', 
                        help='dump radio\'s NVRAM to a file.')
    
    args, unknown = parser.parse_known_args()

    list_com = args.listcom
    list_sound = args.listsound
    dump_ram = args.dumpram
    freq_range = args.exop
    baudrate = int(args.baudrate)
    com_id = 'auto' if (args.com_id == 'auto') else int(args.com_id)
    sound_id = 'auto' if (args.sound_id == 'auto') else int(args.sound_id)

#
    mics = soundcard.all_microphones()

#
    if (list_com):
        comports = get_serial_ports()

        print('\nAvailable serial ports:\n')

        print('%s  %-14s  %-64s  %-54s  %s' % ('No', 'Port', 'Description', 'HWID', 'Permission'))
        print('%s  %-14s  %-64s  %-54s  %s' % ('--', '-'*14, '-'*64,        '-'*54, '-'*10))

        for i in range(len(comports)):
            port = comports[i]

            print('%2d  %-14s  %-64s  %-54s  %s' % (i+1, port['dev'][:14], port['desc'][:64], port['hwid'][:54], port['perm']))
        print('\n')

#
    if (list_sound):
        print('\nAvailable sound interfaces:\n')

        print('%s  %-50s  %-64s' % ('No', 'Name', 'ID'))
        print('%s  %-50s  %-64s' % ('--', '-'*50, '-'*70))

        for i in range(len(mics)):
            mic = mics[i]

            print('%2d  %-50s  %-70s' % (i+1, mic.name[:50], mic.id[:70]))
        print('\n')

#
    if (list_sound or list_com):
        sys.exit(0)

#
    if (com_id == 'auto'):
        try:
            radio_id, port = auto_detect_port(baudrate)

            if (radio_id == '0670'):
                print('\nInfo: using com port %s' % (port))

            else:
                print('\nError: radio model mismatch. Exiting...')
                sys.exit(1)

        except:
            print('\nError: can\'t detect radio. Exiting...')
            sys.exit(1)

    else:
        port = get_serial_ports()[com_id-1]['dev']
        hwid = get_serial_ports()[com_id-1]['hwid']

#
    if (sound_id == 'auto'):
        for i in range(len(mics)):
            mic = mics[i]

            if (mic.name == 'PCM2903B Audio CODEC Digital Stereo (IEC958)'):
                print('\nInfo: using microphone %s' % (mic.name))

                break

    else:
        mic = mics[sound_id-1]

#
    ft991a.FREQRANGE = 1 if (freq_range) else 0

#
    ft991a.PORT = port
    ft991a.BAUDRATE = baudrate

    status = ft991a.open_serial()

    if (status != True):
        print('\nError: can\'t open serial port. Exiting...')
        sys.exit(1)

    ft991a.set_auto_info(0)
    ft991a.SERIAL_HANDLE.reset_input_buffer()
    ft991a.SERIAL_HANDLE.reset_output_buffer()

#
    if (dump_ram):
        print('\nDumping radio\'s NVRAM... This may take a while.')

        dump_memory()

        sys.exit(0)

#
    app = QtWidgets.QApplication(sys.argv)

#
    window = MainWindow()
    window.statusBar().setFixedHeight(31)

#
    window.mic = mic
    window.update_RF_settings()
    window.update_Memory()
    window.update_Radio_menu()
    window.EQ_get_parameters()
    window.Audio_filter_get_cutoff()
    window.Audio_filter_get_slope()

    ft991a.TEXT_BROWSER = window.Message_textBrowser

    window.show()

    sys.exit(app.exec())

