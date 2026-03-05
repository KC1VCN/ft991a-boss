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
import re
import time
import locale
import threading

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

import serial

from datetime import datetime, timezone

#
SERIAL_HANDLE = None
TEXT_BROWSER = None
MESSAGE_FLAG = False
PORT = '/dev/ttyUSB0'
BAUDRATE = 38400
FREQRANGE = 0

#
def serial_read_until(*args, **kwargs):
    global SERIAL_HANDLE, MESSAGE_FLAG, TEXT_BROWSER

#
    data = SERIAL_HANDLE.read_until(*args, **kwargs)

    while (SERIAL_HANDLE.in_waiting > 0):
        data = data+SERIAL_HANDLE.read_until(*args, **kwargs)

#
    if (MESSAGE_FLAG == True and TEXT_BROWSER != None):
        utc_time = datetime.now(timezone.utc).strftime('%H%M%S.%f')[:-3]
        message = '%s: RCVD: <font color="green">%s</font>' % (utc_time, data)
        message = message.encode('unicode-escape').decode('ascii')

        TEXT_BROWSER.append(message)

#
    return data

#
def serial_write(*args, **kwargs):
    global SERIAL_HANDLE, MESSAGE_FLAG, TEXT_BROWSER

#
    SERIAL_HANDLE.write(*args, **kwargs)

#
    if (MESSAGE_FLAG == True and TEXT_BROWSER != None):
        utc_time = datetime.now(timezone.utc).strftime('%H%M%S.%f')[:-3]
        message = '%s: SENT: <font color="yellow">%s</font>' % (utc_time, args[0])
        message = message.encode('unicode-escape').decode('ascii')

        TEXT_BROWSER.append(message)

#
def open_serial():
    global SERIAL_HANDLE, PORT, BAUDRATE

#
    try:
        SERIAL_HANDLE = serial.Serial(port=PORT,
                                      baudrate=BAUDRATE,
                                      parity=serial.PARITY_NONE,
                                      stopbits=serial.STOPBITS_ONE,
                                      bytesize=serial.EIGHTBITS,
                                      timeout=1)

    except serial.SerialException as e:
        return e

#
    return True

#
menu = {

'001': ['AGC_FAST_DELAY',
lambda x: '%dmsec' % (int(x)),
'300msec',
range(20, 4020, 20),
4,
'20 ~ 4000 msec (P2= 0020 ~ 4000, 20 msec/step)'],

'002': ['AGC_MID_DELAY',
lambda x: '%dmsec' % (int(x)),
'700msec',
range(20, 4020, 20),
4,
'20 ~ 4000 msec (P2= 0020 ~ 4000, 20 msec/step)'],

'003': ['AGC_SLOW_DELAY',
lambda x: '%dmsec' % (int(x)),
'3000msec',
range(20, 4020, 20),
4,
'20 ~ 4000 msec (P2= 0020 ~ 4000, 20 msec/step)'],

'004': ['HOME_FUNCTION',
lambda x: {'0': 'SCOPE', '1': 'FUNCTION'}[x],
'SCOPE',
range(0, 2, 1),
1,
'0: SCOPE, 1: FUNCTION'],

'005': ['MY_CALL_INDICATION',
lambda x: '%dsec' % (int(x)),
'1sec',
range(0, 6, 1),
1,
'0 ~ 5 sec'],

'006': ['DISPLAY_COLOR',
lambda x: {'0': 'BLUE', '1': 'GRAY', '2': 'GREEN', '3': 'ORANGE', '4': 'PURPLE', '5': 'RED', '6': 'SKY BLUE'}[x],
'BLUE',
range(0, 7, 1),
1,
'0: BLUE, 1: GRAY, 2: GREEN, 3: ORANGE, 4: PURPLE, 5: RED, 6: SKY BLUE'],

'007': ['DIMMER_LED',
lambda x: {'0': '1', '1': '2'}[x],
'2',
range(0, 2, 1),
1,
'0: 1, 1: 2'],

'008': ['DIMMER_TFT',
lambda x: '%d' % (int(x)),
'8',
range(0, 16, 1),
2,
'00 ~ 15'],

'009': ['BAR_MTR_PEAK_HOLD',
lambda x: {'0': 'OFF', '1': '0.5 sec', '2': '1.0 sec', '3': '2.0 sec'}[x],
'OFF',
range(0, 4, 1),
1,
'0: OFF, 1: 0.5 sec, 2: 1.0 sec, 3: 2.0 sec'],

'010': ['DVS_RX_OUT_LEVEL',
lambda x: '%d' % (int(x)),
'50',
range(0, 101, 1),
3,
'0 ~ 100 (P2 = 000 ~ 100)'],

'011': ['DVS_TX_OUT_LEVEL',
lambda x: '%d' % (int(x)),
'50',
range(0, 101, 1),
3,
'0 ~ 100 (P2 = 000 ~ 100)'],

'012': ['KEYER_TYPE',
lambda x: {'0': 'OFF', '1': 'BUG', '2': 'ELEKEY-A', '3': 'ELEKEY-B', '4': 'ELEKEY-Y', '5': 'ACS'}[x],
'ELEKEY-B',
range(0, 6, 1),
1,
'0: OFF, 1: BUG, 2: ELEKEY-A, 3: ELEKEY-B, 4: ELEKEY-Y, 5: ACS'],

'013': ['KEYER_DOT/DASH',
lambda x: {'0': 'NORMAL', '1': 'REVERSE'}[x],
'NORMAL',
range(0, 2, 1),
1,
'0: NORMAL, 1: REVERSE'],

'014': ['CW_WEIGHT',
lambda x: '%.1f' % (float(x)/10.0),
'3.0',
range(25, 46, 1),
2,
'2.5 ~ 4.5 (P2 = 25 ~ 45)'],

'015': ['BEACON_INTERVAL',
lambda x: 'OFF' if (x=='000' or x=='0') else ('%ssec' % (x)),
'OFF',
range(0, 691, 1),
3,
'OFF / 1 ~ 690 sec (P2 = 000 ~ 690, 000: OFF)'],

'016': ['NUMBER_STYLE',
lambda x: {'0': '1290', '1': 'AUNO', '2': 'AUNT', '3': 'A2NO', '4': 'A2NT', '5': '12NO', '6': '12NT'}[x],
'1290',
range(0, 7, 1),
1,
'0: 1290, 1: AUNO, 2: AUNT, 3: A2NO, 4: A2NT, 5: 12NO, 6: 12NT'],

'017': ['CONTEST_NUMBER',
lambda x: '%d' % (int(x)),
'1',
range(0, 10000, 1),
4,
'0000 ~ 9999'],

'018': ['CW_MEMORY_1',
lambda x: {'0': 'TEXT', '1': 'MESSAGE'}[x],
'TEXT',
range(0, 2, 1),
1,
'0: TEXT, 1: MESSAGE'],

'019': ['CW_MEMORY_2',
lambda x: {'0': 'TEXT', '1': 'MESSAGE'}[x],
'TEXT',
range(0, 2, 1),
1,
'0: TEXT, 1: MESSAGE'],

'020': ['CW_MEMORY_3',
lambda x: {'0': 'TEXT', '1': 'MESSAGE'}[x],
'TEXT',
range(0, 2, 1),
1,
'0: TEXT, 1: MESSAGE'],

'021': ['CW_MEMORY_4',
lambda x: {'0': 'TEXT', '1': 'MESSAGE'}[x],
'TEXT',
range(0, 2, 1),
1,
'0: TEXT, 1: MESSAGE'],

'022': ['CW_MEMORY_5',
lambda x: {'0': 'TEXT', '1': 'MESSAGE'}[x],
'TEXT',
range(0, 2, 1),
1,
'0: TEXT, 1: MESSAGE'],

'023': ['NB_WIDTH',
lambda x: {'0': '1msec', '1': '3msec', '2': '10msec'}[x],
'3msec',
range(0, 3, 1),
1,
'0: 1 ms, 1: 3 ms, 2: 10 ms'],

'024': ['NB_REJECTION',
lambda x: {'0': '10dB', '1': '30dB', '2': '50dB'}[x],
'30dB',
range(0, 3, 1),
1,
'0: 10 dB, 1: 30 dB, 2: 50 dB'],

'025': ['NB_LEVEL',
lambda x: '%d' % (int(x)),
'5',
range(0, 11, 1),
2,
'0 ~ 10 (P2 = 00 ~ 10)'],

'026': ['BEEP_LEVEL',
lambda x: '%d' % (int(x)),
'50',
range(0, 101, 1),
3,
'0 ~ 100 (P2 = 000 ~ 100)'],

'027': ['TIME_ZONE',
lambda x: '%+05d' % (int(x)),
'+0000',
[-1200, -1130, -1100, -1030, -1000, -930, -900, -830, -800, -730, -700, -630, -600, -530, -500, -430, 
-400, -330, -300, -230, -200, -130, -100, -30, 0, 30, 100, 130, 200, 230, 300, 330, 400, 430, 500, 
530, 600, 630, 700, 730, 800, 830, 900, 930, 1000, 1030, 1100, 1130, 1200, 1230, 1300, 1330, 1400],
5,
'UTC –12:00 ~ +14:00'],

'028': ['GPS/232C_SELECT',
lambda x: {'0': 'GPS1', '1': 'GPS2', '2':'', '3': 'RS232C'}[x],
'GPS1',
range(0, 4, 1),
1,
'0: GPS1, 1: GPS2, 3: RS232C'],

'029': ['232C_RATE',
lambda x: {'0': '4800bps', '1': '9600bps', '2': '19200bps', '3': '38400bps'}[x],
'4800bps',
range(0, 4, 1),
1,
'0: 4800 bps, 1: 9600 bps, 2: 19200 bps, 3: 38400 bps'],

'030': ['232C_TOT',
lambda x: {'0': '10msec', '1': '100msec', '2': '1000msec', '3': '3000msec'}[x],
'10msec',
range(0, 4, 1),
1,
'0: 10 msec, 1: 100 msec, 2: 1000 msec, 3: 3000 msec'],

'031': ['CAT_RATE',
lambda x: {'0': '4800bps', '1': '9600bps', '2': '19200bps', '3': '38400bps'}[x],
'4800bps',
range(0, 4, 1),
1,
'0: 4800 bps, 1: 9600 bps, 2: 19200 bps, 3: 38400 bps'],

'032': ['CAT_TOT',
lambda x: {'0': '10msec', '1': '100msec', '2': '1000msec', '3': '3000msec'}[x],
'10msec',
range(0, 4, 1),
1,
'0: 10 msec, 1: 100 msec, 2: 1000 msec, 3: 3000 msec'],

'033': ['CAT_RTS',
lambda x: {'0': 'DISABLE', '1': 'ENABLE'}[x],
'ENABLE',
range(0, 2, 1),
1,
'0: DISABLE, 1: ENABLE'],

'034': ['MEM_GROUP',
lambda x: {'0': 'DISABLE', '1': 'ENABLE'}[x],
'DISABLE',
range(0, 2, 1),
1,
'0: DISABLE, 1: ENABLE'],

'035': ['QUICK_SPLIT_FREQ',
lambda x: '%dkHz' % (int(x)),
'5kHz',
range(-20, 21, 1),
3,
'–20 kHz ~ +00 (or –00) ~ +20 kHz (P2= –20 ~ +00 or –00 ~ +20)'],

'036': ['TX_TOT',
lambda x: 'OFF' if ('%02d' % (int(x)))=='00' else ('%dmin' % (int(x))),
'OFF',
range(0, 31, 1),
2,
'0 (OFF) ~ 30 min (P2= 00 ~ 30)'],

'037': ['MIC_SCAN',
lambda x: {'0': 'DISABLE', '1': 'ENABLE'}[x],
'ENABLE',
range(0, 2, 1),
1,
'0: DISABLE, 1: ENABLE'],

'038': ['MIC_SCAN_RESUME',
lambda x: {'0': 'PAUSE', '1': 'TIME'}[x],
'TIME',
range(0, 2, 1),
1,
'0: PAUSE, 1: TIME'],

'039': ['REF_FREQ_ADJ',
lambda x: '0' if (x=='+00' or x =='0') else ('%s' % (x)),
'0',
range(-25, 26, 1),
3,
'–25 ~ +00 (or –00) ~ +25 (P2= –25 ~ +00 or –00 ~ +25)'],

'040': ['CLAR_MODE_SELECT',
lambda x: {'0': 'RX', '1': 'TX', '2': 'TRX'}[x],
'RX',
range(0, 3, 1),
1,
'0: RX, 1: TX, 2: TRX'],

'041': ['AM_LCUT_FREQ',
lambda x: 'OFF' if ('%02d' % (int(x)))=='00' else ('%dHz' % (int(x)*50+50)),
'OFF',
range(0, 20, 1),
2,
'00: OFF, 01: 100 Hz ~ 19: 1000 Hz (50 Hz steps)'],

'042': ['AM_LCUT_SLOPE',
lambda x: {'0': '6dB/oct', '1': '18dB/oct'}[x],
'6dB/oct',
range(0, 2, 1),
1,
'0: 6 dB/oct, 1: 18 dB/oct'],

'043': ['AM_HCUT_FREQ',
lambda x: 'OFF' if ('%02d' % (int(x)))=='00' else ('%dHz' % (int(x)*50+650)),
'OFF',
range(0, 20, 1),
2,
'00: OFF 01: 700 Hz ~ 67: 4000 Hz (50 Hz steps)'],

'044': ['AM_HCUT_SLOPE',
lambda x: {'0': '6dB/oct', '1': '18dB/oct'}[x],
'6dB/oct',
range(0, 2, 1),
1,
'0: 6 dB/oct, 1: 18 dB/oct'],

'045': ['AM_MIC_SELECT',
lambda x: {'0': 'MIC', '1': 'REAR'}[x],
'MIC',
range(0, 2, 1),
1,
'0: MIC, 1: REAR'],

'046': ['AM_OUT_LEVEL',
lambda x: '%d' % (int(x)),
'50',
range(0, 101, 1),
3,
'0 ~ 100 (P2 = 000 ~ 100)'],

'047': ['AM_PTT_SELECT',
lambda x: {'0': 'DAKY', '1': 'RTS', '2':'DTR'}[x],
'DAKY',
range(0, 3, 1),
1,
'0: DAKY 1: RTS 2: DTR'],

'048': ['AM_PORT_SELECT',
lambda x: {'0': 'DATA', '1': 'USB'}[x],
'DATA',
range(0, 2, 1),
1,
'0: DATA 1: USB'],

'049': ['AM_DATA_GAIN',
lambda x: '%d' % (int(x)),
'50',
range(0, 101, 1),
3,
'0 ~ 100 (P2 = 000 ~ 100)'],

'050': ['CW_LCUT_FREQ',
lambda x: 'OFF' if ('%02d' % (int(x)))=='00' else ('%dHz' % (int(x)*50+50)),
'250Hz',
range(0, 20, 1),
2,
'00: OFF 01: 100 Hz ~ 19: 1000 Hz (50 Hz steps)'],

'051': ['CW_LCUT_SLOPE',
lambda x: {'0': '6dB/oct', '1': '18dB/oct'}[x],
'18dB/oct',
range(0, 2, 1),
1,
'0: 6 dB/oct 1: 18 dB/oct'],

'052': ['CW_HCUT_FREQ',
lambda x: 'OFF' if ('%02d' % (int(x)))=='00' else ('%dHz' % (int(x)*50+650)),
'1200Hz',
range(0, 20, 1),
2,
'00: OFF 01: 700 Hz ~ 67: 4000 Hz (50 Hz steps)'],

'053': ['CW_HCUT_SLOPE',
lambda x: {'0': '6dB/oct', '1': '18dB/oct'}[x],
'18dB/oct',
range(0, 2, 1),
1,
'0: 6 dB/oct 1: 18 dB/oct'],

'054': ['CW_OUT_LEVEL',
lambda x: '%d' % (int(x)),
'50',
range(0, 101, 1),
3,
'0 ~ 100 (P2 = 000 ~ 100)'],

'055': ['CW_AUTO_MODE',
lambda x: {'0': 'OFF', '1': '50 MHz', '2':'ON'}[x],
'OFF',
range(0, 3, 1),
1,
'0: OFF 1: 50 MHz 2: ON'],

'056': ['CW_BK-IN_TYPE',
lambda x: {'0': 'SEMI', '1': 'FULL'}[x],
'SEMI',
range(0, 2, 1),
1,
'0: SEMI BREAK-IN 1: FULL BREAK-IN'],

'057': ['CW_BK-IN_DELAY',
lambda x: '%dmsec' % (int(x)),
'200msec',
range(30, 3010, 10),
4,
'30 ~ 3000 msec (P2 = 0030 ~ 3000, 10 msec/step)'],

'058': ['CW_WAVE_SHAPE',
lambda x: {'0': '1msec', '1': '2msec', '2': '4msec', '3': '6msec'}[x],
'4msec',
range(0, 4, 1),
1,
'0: 1 msec 1: 2 msec 2: 4 msec 3: 6 msec'],

'059': ['CW_FREQ_DISPLAY',
lambda x: {'0': 'DIRECT FREQ', '1': 'PITCH OFFSET'}[x],
'PITCH OFFSET',
range(0, 2, 1),
1,
'0: DIRECT FREQ 1: PITCH OFFSET'],

'060': ['PC_KEYING',
lambda x: {'0': 'OFF', '1': 'DAKY', '2':'RTS', '3':'DTR'}[x],
'OFF',
range(0, 4, 1),
1,
'0: OFF 1: DAKY 2: RTS 3: DTR'],

'061': ['QSK_DELAY_TIME',
lambda x: {'0': '15msec', '1': '20msec', '2': '25msec', '3': '30msec'}[x],
'15msec',
range(0, 4, 1),
1,
'0: 15 msec 1: 20 msec 2: 25 mesc 3: 30 msec'],

'062': ['DATA_MODE',
lambda x: {'0': 'PSK', '1': 'OTHER'}[x],
'PSK',
range(0, 2, 1),
1,
'0: PSK 1: OTHER'],

'063': ['PSK_TONE',
lambda x: {'0': '1000Hz', '1': '1500Hz', '2': '2000Hz'}[x],
'1000Hz',
range(0, 2, 1),
1,
'0: 1000 Hz 1: 1500 Hz 2: 2000 Hz'],

'064': ['OTHER_DISP_(SSB)',
lambda x: '%dHz' % (int(x)),
'0Hz',
range(-3000, 3010, 10),
5,
'–3000 Hz ~ 0 ~ +3000 Hz (P2 = –3000 ~ –0000 or +0000 ~ +3000, 10 Hz steps)'],

'065': ['OTHER_SHIFT_(SSB)',
lambda x: '%dHz' % (int(x)),
'0Hz',
range(-3000, 3010, 10),
5,
'–3000 Hz ~ 0 ~ +3000 Hz (P2 = –3000 ~ –0000 or +0000 ~ +3000, 10 Hz steps)'],

'066': ['DATA_LCUT_FREQ',
lambda x: 'OFF' if ('%02d' % (int(x)))=='00' else ('%dHz' % (int(x)*50+50)),
'300Hz',
range(0, 21, 1),
2,
'00: OFF 01: 100 Hz ~ 19: 1000 Hz (50 Hz steps)'],

'067': ['DATA_LCUT_SLOPE',
lambda x: {'0': '6dB/oct', '1': '18dB/oct'}[x],
'18dB/oct',
range(0, 2, 1),
1,
'0: 6 dB/oct 1: 18 dB/oct'],

'068': ['DATA_HCUT_FREQ',
lambda x: 'OFF' if ('%02d' % (int(x)))=='00' else ('%dHz' % (int(x)*50+650)),
'3000Hz',
range(0, 68, 1),
2,
'00: OFF 01: 700 Hz ~ 67: 4000 Hz (50 Hz steps)'],

'069': ['DATA_HCUT_SLOPE',
lambda x: {'0': '6dB/oct', '1': '18dB/oct'}[x],
'18dB/oct',
range(0, 2, 1),
1,
'0: 6 dB/oct 1: 18 dB/oct'],

'070': ['DATA_IN_SELECT',
lambda x: {'0': 'MIC', '1': 'REAR'}[x],
'REAR',
range(0, 2, 1),
1,
'0: MIC 1: REAR'],

'071': ['DATA_PTT_SELECT',
lambda x: {'0': 'DAKY', '1': 'RTS', '2':'DTR'}[x],
'DAKY',
range(0, 3, 1),
1,
'0: DAKY 1: RTS 2: DTR'],

'072': ['DATA_PORT_SELECT',
lambda x: {'0': 'DATA', '1': 'USB'}[x],
'DATA',
range(0, 2, 1),
1,
'1: DATA 2: USB'],

'073': ['DATA_OUT_LEVEL',
lambda x: '%d' % (int(x)),
'50',
range(0, 101, 1),
3,
'0 ~ 100 (P2 = 000 ~ 100)'],

'074': ['FM_MIC_SELECT',
lambda x: {'0': 'MIC', '1': 'REAR'}[x],
'MIC',
range(0, 2, 1),
1,
'0: MIC 1: REAR'],

'075': ['FM_OUT_LEVEL',
lambda x: '%d' % (int(x)),
'50',
range(0, 101, 1),
3,
'0 ~ 100 (P2 = 000 ~ 100)'],

'076': ['FM_PKT_PTT_SELECT',
lambda x: {'0': 'DAKY', '1': 'RTS', '2':'DTR'}[x],
'DAKY',
range(0, 3, 1),
1,
'0: DAKY 1: RTS 2: DTR'],

'077': ['FM_PKT_PORT_SELECT',
lambda x: {'0': 'DATA', '1': 'USB'}[x],
'DATA',
range(0, 2, 1),
1,
'1: DATA 2: USB'],

'078': ['FM_PKT_TX_GAIN',
lambda x: '%d' % (int(x)),
'50',
range(0, 101, 1),
3,
'0 ~ 100 (P2 = 000 ~ 100)'],

'079': ['FM_PKT_MODE',
lambda x: {'0': '1200', '1': '9600'}[x],
'1200',
range(0, 2, 1),
1,
'0: 1200 1: 9600'],

'080': ['RPT_SHIFT_28MHz',
lambda x: '%dkHz' % (int(x)),
'100kHz',
range(0, 1010, 10),
4,
'0 ~ 1000 kHz (P2 = 0000 ~ 1000, 10 kHz/step)'],

'081': ['RPT_SHIFT_50MHz',
lambda x: '%dkHz' % (int(x)),
'1000kHz',
range(0, 4010, 10),
4,
'0 ~ 4000 kHz (P2 = 0000 ~ 4000, 10 kHz/step)'],

'082': ['RPT_SHIFT_144MHz',
lambda x: '%dkHz' % (int(x)),
'600kHz',
range(0, 4010, 10),
4,
'0 ~ 4000 kHz (P2 = 0000 ~ 4000, 10 kHz/step)'],

'083': ['RPT_SHIFT_430MHz',
lambda x: '%dkHz' % (int(x)),
'5000kHz',
range(0, 10010, 10),
5,
'0 ~ 10000 kHz (P2 = 0000 ~ 10000, 10 kHz/step)'],

'084': ['ARS_144MHz',
lambda x: {'0': 'OFF', '1': 'ON'}[x],
'ON',
range(0, 2, 1),
1,
'0: OFF 1: ON'],

'085': ['ARS_430MHz',
lambda x: {'0': 'OFF', '1': 'ON'}[x],
'ON',
range(0, 2, 1),
1,
'0: OFF 1: ON'],

'086': ['DCS_POLARITY',
lambda x: {'0': 'Tn-Rn', '1': 'Tn-Riv', '2': 'Tiv-Rn', '3': 'Tiv-Riv'}[x],
'Tn-Rn',
range(0, 4, 1),
1,
'0: Tn-Rn 1: Tn-Riv 2: Tiv-Rn 3: Tiv-Riv'],

'087': ['RADIO_ID',
lambda x: '',
'',
range(0),
1,
''],

'088': ['GM_DISPLY',
lambda x: {'0': 'DISTANCE', '1': 'STRENGTH'}[x],
'DISTANCE',
range(0, 2, 1),
1,
'0: DISTANCE 1: STRENGTH'],

'089': ['DISTANCE',
lambda x: {'0': 'km', '1': 'mile'}[x],
'mile',
range(0, 2, 1),
1,
'0: km 1: mile'],

'090': ['AMS_TX_MODE',
lambda x: {'0': 'AUTO', '1': 'MANUAL', '2': 'DN', '3': 'VW', '4':'ANALOG'}[x],
'AUTO',
range(0, 5, 1),
1,
'0: AUTO 1: MANUAL 2: DN 3: VW 4: ANALOG'],

'091': ['STANDBY_BEEP',
lambda x: {'0': 'OFF', '1': 'ON'}[x],
'ON',
range(0, 2, 1),
1,
'0: OFF 1: ON'],

'092': ['RTTY_LCUT_FREQ',
lambda x: 'OFF' if ('%02d' % (int(x)))=='00' else ('%dHz' % (int(x)*50+50)),
'300Hz',
range(0, 20, 1),
2,
'00: OFF 01: 100 Hz ~ 19: 1000Hz (50 Hz steps)'],

'093': ['RTTY_LCUT_SLOPE',
lambda x: {'0': '6dB/oct', '1': '18dB/oct'}[x],
'18dB/oct',
range(0, 2, 1),
1,
'0: 6 dB/oct 1: 18 dB/oct'],

'094': ['RTTY_HCUT_FREQ',
lambda x: 'OFF' if ('%02d' % (int(x)))=='00' else ('%dHz' % (int(x)*50+650)),
'3000Hz',
range(0, 68, 1),
2,
'00: OFF 01: 700 Hz ~ 67: 4000Hz (50 Hz steps)'],

'095': ['RTTY_HCUT_SLOPE',
lambda x: {'0': '6dB/oct', '1': '18dB/oct'}[x],
'18dB/oct',
range(0, 2, 1),
1,
'0: 6 dB/oct 1: 18 dB/oct'],

'096': ['RTTY_SHIFT_PORT',
lambda x: {'0': 'SHIFT', '1': 'DTR', '2': 'RTS'}[x],
'SHIFT',
range(0, 2, 1),
1,
'0: SHIFT 1: DTR 2: RTS'],

'097': ['RTTY_POLARITY-RX',
lambda x: {'0': 'NORMAL', '1': 'REVERSE'}[x],
'NORMAL',
range(0, 2, 1),
1,
'0: NORMAL 1: REVERSE'],

'098': ['RTTY_POLARITY-TX',
lambda x: {'0': 'NORMAL', '1': 'REVERSE'}[x],
'NORMAL',
range(0, 2, 1),
1,
'0: NORMAL 1: REVERSE'],

'099': ['RTTY_OUT_LEVEL',
lambda x: '%d' % (int(x)),
'50',
range(0, 101, 1),
3,
'0 ~ 100 (P2 = 000 ~ 100)'],

'100': ['RTTY_SHIFT_FREQ',
lambda x: {'0': '170Hz', '1': '200Hz', '2': '425Hz', '3': '850Hz'}[x],
'170Hz',
range(0, 4, 1),
1,
'1: 170 Hz 1: 200 Hz 2: 425 Hz 3: 850 Hz'],

'101': ['RTTY_MARK_FREQ',
lambda x: {'0': '1275Hz', '1': '2125Hz'}[x],
'2125Hz',
range(0, 2, 1),
1,
'1: 1275 Hz 2: 2125 Hz'],

'102': ['SSB_LCUT_FREQ',
lambda x: 'OFF' if ('%02d' % (int(x)))=='00' else ('%dHz' % (int(x)*50+50)),
'100Hz',
range(0, 20, 1),
2,
'00: OFF 01: 100 Hz ~ 19: 1000 Hz (50 Hz steps)'],

'103': ['SSB_LCUT_SLOPE',
lambda x: {'0': '6dB/oct', '1': '18dB/oct'}[x],
'6dB/oct',
range(0, 2, 1),
1,
'0: 6 dB/oct 1: 18 dB/oct'],

'104': ['SSB_HCUT_FREQ',
lambda x: 'OFF' if ('%02d' % (int(x)))=='00' else ('%dHz' % (int(x)*50+650)),
'3000Hz',
range(0, 68, 1),
2,
'00: OFF 01: 700 Hz ~ 67: 4000 Hz (50 Hz steps)'],

'105': ['SSB_HCUT_SLOPE',
lambda x: {'0': '6dB/oct', '1': '18dB/oct'}[x],
'6dB/oct',
range(0, 2, 1),
1,
'0: 6 dB/oct 1: 18 dB/oct'],

'106': ['SSB_MIC_SELECT',
lambda x: {'0': 'MIC', '1': 'REAR'}[x],
'MIC',
range(0, 2, 1),
1,
'0: MIC 1: REAR'],

'107': ['SSB_OUT_LEVEL',
lambda x: '%d' % (int(x)),
'50',
range(0, 101, 1),
3,
'0 ~ 100 (P2 = 000 ~ 100)'],

'108': ['SSB_PTT_SELECT',
lambda x: {'0': 'DAKY', '1': 'RTS', '2': 'DTR'}[x],
'DAKY',
range(0, 3, 1),
1,
'0: DAKY 1: RTS 2: DTR'],

'109': ['SSB_PORT_SELECT',
lambda x: {'0': 'DATA', '1': 'USB'}[x],
'DATA',
range(0, 2, 1),
1,
'0: DATA 1: USB'],

'110': ['SSB_TX_BPF',
lambda x: {'0': '50~3000', '1': '100~2900', '2': '200~2800', '3': '300~2700', '4': '400~2600'}[x],
'300~2700',
range(0, 5, 1),
1,
'0: 50 ~ 3000 1: 100 ~ 2900 2: 200 ~ 2800 3: 300 ~ 2700 4: 400 ~ 2600'],

'111': ['APF_WIDTH',
lambda x: {'0': 'NARROW', '1': 'MEDIUM', '2': 'WIDE'}[x],
'MEDIUM',
range(0, 3, 1),
1,
'0: NARROW 1: MEDIUM 2: WIDE'],

'112': ['CONTOUR_LEVEL',
lambda x: '%d' % (int(x)),
'-15',
range(-40, 21, 1),
3,
'–40 ~ 0 ~ +20 (P2 = –40 ~ –00 or +00 ~ +20)'],

'113': ['CONTOUR_WIDTH',
lambda x: '%d' % (int(x)),
'10',
range(1, 12, 1),
2,
'01 ~ 11'],

'114': ['IF_NOTCH_WIDTH',
lambda x: {'0': 'NARROW', '1': 'WIDE'}[x],
'WIDE',
range(0, 2, 1),
1,
'0: NARROW 1: WIDE'],

'115': ['SCP_DISPLAY_MODE',
lambda x: {'0': 'SPECTRUM', '1': 'WATER FALL'}[x],
'SPECTRUM',
range(0, 2, 1),
1,
'0: SPECTRUM 1: WATER FALL'],

'116': ['SCP_SPAN_FREQ',
lambda x: {'03': '50kHz', '04': '100kHz', '05': '200kHz', '06': '500kHz', '07': '1000kHz'}['%02d' % (int(x))],
'100kHz',
range(3, 8, 1),
2,
'03: 50 kHz 04: 100 kHz 05: 200 kHz 06: 500 kHz 07: 1000 kHz'],

'117': ['SPECTRUM_COLOR',
lambda x: {'0': 'BLUE', '1': 'GRAY', '2': 'GREEN', '3': 'ORANGE', '4': 'PURPLE', '5': 'RED', '6': 'SKY BLUE'}[x],
'BLUE',
range(0, 7, 1),
1,
'0: BLUE 1: GRAY 2: GREEN 3: ORANGE 4: PURPLE 5: RED 6: SKY BLUE'],

'118': ['WATER_FALL_COLOR',
lambda x: {'0': 'BLUE', '1': 'GRAY', '2': 'GREEN', '3': 'ORANGE', '4': 'PURPLE', '5': 'RED', '6': 'SKY BLUE', '7': 'MULTI'}[x],
'MULTI',
range(0, 8, 1),
1,
'0: BLUE 1: GRAY 2: GREEN 3: ORANGE 4: PURPLE 5: RED 6: SKY BLUE 7: MULTI'],

'119': ['PRMTRC_EQ1_FREQ',
lambda x: 'OFF' if ('%02d' % (int(x)))=='00' else ('%d' % (int(x)*100)),
'OFF',
range(0, 8, 1),
2,
'00 : OFF 01: 100 02: 200 03: 300 04: 400 05: 500 06: 600 07: 700 Hz'],

'120': ['PRMTRC_EQ1_LEVEL',
lambda x: '%d' % (int(x)),
'5',
range(-20, 11, 1),
3,
'–20 ~ 0 ~ +10 (P2 = –20 ~ –00 or +00 ~ +10)'],

'121': ['PRMTRC_EQ1_BWTH',
lambda x: '%d' % (int(x)),
'10',
range(1, 11, 1),
2,
'01 ~ 10'],

'122': ['PRMTRC_EQ2_FREQ',
lambda x: 'OFF' if ('%02d' % (int(x)))=='00' else ('%d' % (int(x)*100+600)),
'OFF',
range(0, 10, 1),
2,
'00: OFF 01: 700 02: 800 03: 900 04: 1000 05: 1100 06: 1200 07: 1300 08: 1400 09: 1500 Hz'],

'123': ['PRMTRC_EQ2_LEVEL',
lambda x: '%d' % (int(x)),
'5',
range(-20, 11, 1),
3,
'–20 ~ 0 ~ +10 (P2 = –20 ~ –00 or +00 ~ +10)'],

'124': ['PRMTRC_EQ2_BWTH',
lambda x: '%d' % (int(x)),
'10',
range(1, 11, 1),
2,
'01 ~ 10'],

'125': ['PRMTRC_EQ3_FREQ',
lambda x: 'OFF' if ('%02d' % (int(x)))=='00' else ('%d' % (int(x)*100+1400)),
'OFF',
range(0, 19, 1),
2,
'00 : OFF 01: 1500 02: 1600 03: 1700 04: 1800 05: 1900 06: 2000 ~ 18: 3200 Hz'],

'126': ['PRMTRC_EQ3_LEVEL',
lambda x: '%d' % (int(x)),
'5',
range(-20, 11, 1),
3,
'–20 ~ 0 ~ +10 (P2 = –20 ~ –00 or +00 ~ +10)'],

'127': ['PRMTRC_EQ3_BWTH',
lambda x: '%d' % (int(x)),
'10',
range(1, 11, 1),
2,
'01 ~ 10'],

'128': ['P-PRMTRC_EQ1_FREQ',
lambda x: 'OFF' if ('%02d' % (int(x)))=='00' else ('%d' % (int(x)*100)),
'200',
range(0, 8, 1),
2,
'00 : OFF 01: 100 02: 200 03: 300 04: 400 05: 500 06: 600 07: 700 Hz'],

'129': ['P-PRMTRC_EQ1_LEVEL',
lambda x: '%d' % (int(x)),
'0',
range(-20, 11, 1),
3,
'–20 ~ 0 ~ +10 (P2 = –20 ~ –00 or +00 ~ +10)'],

'130': ['P-PRMTRC_EQ1_BWTH',
lambda x: '%d' % (int(x)),
'2',
range(1, 11, 1),
2,
'01 ~ 10'],

'131': ['P-PRMTRC_EQ2_FREQ',
lambda x: 'OFF' if ('%02d' % (int(x)))=='00' else ('%d' % (int(x)*100+600)),
'800',
range(0, 9, 1),
2,
'00: OFF 01: 700 02: 800 03: 900 04: 1000 05: 1100 06: 1200 07: 1300 08: 1400'],

'132': ['P-PRMTRC_EQ2_LEVEL',
lambda x: '%d' % (int(x)),
'0',
range(-20, 11, 1),
3,
'–20 ~ 0 ~ +10 (P2 = –20 ~ –00 or +00 ~ +10)'],

'133': ['P-PRMTRC_EQ2_BWTH',
lambda x: '%d' % (int(x)),
'1',
range(1, 11, 1),
2,
'01 ~ 10'],

'134': ['P-PRMTRC_EQ3_FREQ',
lambda x: 'OFF' if ('%02d' % (int(x)))=='00' else ('%d' % (int(x)*100+1400)),
'2100',
range(0, 19, 1),
2,
'00 : OFF 01: 1500 02: 1600 03: 1700 04: 1800 05: 1900 06: 2000 ~ 18: 3200 Hz'],

'135': ['P-PRMTRC_EQ3_LEVEL',
lambda x: '%d' % (int(x)),
'0',
range(-20, 11, 1),
3,
'–20 ~ 0 ~ +10 (P2 = –20 ~ –00 or +00 ~ +10)'],

'136': ['P-PRMTRC_EQ3_BWTH',
lambda x: '%d' % (int(x)),
'1',
range(1, 11, 1),
2,
'01 ~ 10'],

'137': ['HF_TX_MAX_POWER',
lambda x: '%d' % (int(x)),
'100',
range(5, 101, 1),
3,
'5 ~ 100 (P2 = 005 ~ 100)'],

'138': ['50M_TX_MAX_POWER',
lambda x: '%d' % (int(x)),
'100',
range(5, 101, 1),
3,
'5 ~ 100 (P2 = 005 ~ 100)'],

'139': ['144M_TX_MAX_POWER',
lambda x: '%d' % (int(x)),
'50',
range(5, 101, 1),
3,
'5 ~ 50 (P2 = 005 ~ 050)'],

'140': ['430M_TX_MAX_POWER',
lambda x: '%d' % (int(x)),
'50',
range(5, 101, 1),
3,
'5 ~ 50 (P2 = 005 ~ 050)'],

'141': ['TUNER_SELECT',
lambda x: {'0': 'OFF', '1': 'INTERNAL', '2': 'EXTERNAL', '3': 'ATAS', '4': 'LAMP'}[x],
'INTERNAL',
range(0, 5, 1),
1,
'0: OFF 1: INTERNAL 2: EXTERNAL 3: ATAS 4: LAMP'],

'142': ['VOX_SELECT',
lambda x: {'0': 'MIC', '1': 'DATA'}[x],
'MIC',
range(0, 2, 1),
1,
'0: MIC 1: DATA'],

'143': ['VOX_GAIN',
lambda x: '%d' % (int(x)),
'50',
range(0, 101, 1),
3,
'000 ~ 100'],

'144': ['VOX_DELAY',
lambda x: '%dmsec' % (int(x)),
'500msec',
range(30, 3010, 10),
4,
'30 ~ 3000 msec (P2 = 0030 ~ 3000, 10 msec/step)'],

'145': ['ANTI_VOX_GAIN',
lambda x: '%d' % (int(x)),
'50',
range(0, 101, 1),
3,
'000 ~ 100'],

'146': ['DATA_VOX_GAIN',
lambda x: '%d' % (int(x)),
'50',
range(0, 101, 1),
3,
'000 ~ 100'],

'147': ['DATA_VOX_DELAY',
lambda x: '%dmsec' % (int(x)),
'100msec',
range(30, 3010, 10),
4,
'30 ~ 3000 msec (P2 = 0030 ~ 3000)'],

'148': ['ANTI_DVOX_GAIN',
lambda x: '%d' % (int(x)),
'0',
range(0, 101, 1),
3,
'000 ~ 100'],

'149': ['EMERGENCY_FREQ_TX',
lambda x: {'0': 'DISABLE', '1': 'ENABLE'}[x],
'DISABLE',
range(0, 2, 1),
1,
'0: DISABLE 1: ENABLE'],

'150': ['PRT/WIRES_FREQ',
lambda x: {'0': 'MANUAL', '1': 'PRESET'}[x],
'MANUAL',
range(0, 2, 1),
1,
'0: MANUAL 1: PRESET'],

'151': ['PRESET_FREQUENCY',
lambda x: '',
'',
range(0),
1,
''],

'152': ['SEARCH_SETUP',
lambda x: {'0': 'HISTORY', '1': 'ACTIVITY'}[x],
'HISTORY',
range(0, 2, 1),
1,
'0: HISTORY 1: ACTIVITY'],

'153': ['WIRES_DG-ID',
lambda x: 'AUTO' if ('%03d' % int(x))=='000' else ('%03d' % int(x)),
'AUTO',
range(0, 100, 1),
3,
'00: AUTO 01: DG-ID 01 ~ 99: DG-ID 99'],

}

#
CTCSS_tone = {

'000': 67.0,
'001': 69.3,
'002': 71.9,
'003': 74.4,
'004': 77.0,
'005': 79.7,
'006': 82.5,
'007': 85.4,
'008': 88.5,
'009': 91.5,
'010': 94.8,
'011': 97.4,
'012': 100.0,
'013': 103.5,
'014': 107.2,
'015': 110.9,
'016': 114.8,
'017': 118.8,
'018': 123.0,
'019': 127.3,
'020': 131.8,
'021': 136.5,
'022': 141.3,
'023': 146.2,
'024': 151.4,
'025': 156.7,
'026': 159.8,
'027': 162.2,
'028': 165.5,
'029': 167.9,
'030': 171.3,
'031': 173.8,
'032': 177.3,
'033': 179.9,
'034': 183.5,
'035': 186.2,
'036': 189.9,
'037': 192.8,
'038': 196.6,
'039': 199.5,
'040': 203.5,
'041': 206.5,
'042': 210.7,
'043': 218.1,
'044': 225.7,
'045': 229.1,
'046': 233.6,
'047': 241.8,
'048': 250.3,
'049': 254.1,

}

#
DCS_code = {

'000':	23,
'001':	25,
'002':	26,
'003':	31,
'004':	32,
'005':	36,
'006':	43,
'007':	47,
'008':	51,
'009':	53,
'010':	54,
'011':	65,
'012':	71,
'013':	72,
'014':	73,
'015':	74,
'016':	114,
'017':	115,
'018':	116,
'019':	122,
'020':	125,
'021':	131,
'022':	132,
'023':	134,
'024':	143,
'025':	145,
'026':	152,
'027':	155,
'028':	156,
'029':	162,
'030':	165,
'031':	172,
'032':	174,
'033':	205,
'034':	212,
'035':	223,
'036':	225,
'037':	226,
'038':	243,
'039':	244,
'040':	245,
'041':	246,
'042':	251,
'043':	252,
'044':	255,
'045':	261,
'046':	263,
'047':	265,
'048':	266,
'049':	271,
'050':	274,
'051':	306,
'052':	311,
'053':	315,
'054':	325,
'055':	331,
'056':	332,
'057':	343,
'058':	346,
'059':	351,
'060':	356,
'061':	364,
'062':	365,
'063':	371,
'064':	411,
'065':	412,
'066':	413,
'067':	423,
'068':	431,
'069':	432,
'070':	445,
'071':	446,
'072':	452,
'073':	454,
'074':	455,
'075':	462,
'076':	464,
'077':	465,
'078':	466,
'079':	503,
'080':	506,
'081':	516,
'082':	523,
'083':	526,
'084':	532,
'085':	546,
'086':	565,
'087':	606,
'088':	612,
'089':	624,
'090':	627,
'091':	631,
'092':	632,
'093':	654,
'094':	662,
'095':	664,
'096':	703,
'097':	712,
'098':	723,
'099':	731,
'100':	732,
'101':	734,
'102':	743,
'103':	754,

}

##############################
# Radio Menus
##############################
def set_menu_value(index, value):
    command = 'EX%03d%s;' % (index, value)
    serial_write(command.encode('ASCII'))

#
    return get_menu_value(index)

#
def get_menu_value(index):
    command = 'EX%03d;' % (index)
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('EX(?:...)(.*?);', data)

    if (data != []):
        return data[-1]

    else:
        return None

##############################
# Check Frequency Range
##############################
def check_frequency_range(freq, mode):
    freq_range = {1: [(30.0E3, 56.0E6), (118.0E6, 164.0E6), (420.0E6, 470.0E6)],
                  0: [ (1.8E6, 54.0E6), (144.0E6, 148.0E6), (430.0E6, 450.0E6)]}[mode]

#
    error = 1

    if (freq < freq_range[0][0]):
        freq = freq_range[0][0]
        
    elif (freq > freq_range[0][1]) and (freq < freq_range[1][0]):
        d1 = abs(freq-freq_range[0][1])
        d2 = abs(freq-freq_range[1][0])

        freq = freq_range[0][1] if (d1 < d2) else freq_range[1][0]
    
    elif (freq > freq_range[1][1]) and (freq < freq_range[2][0]):
        d1 = abs(freq-freq_range[1][1])
        d2 = abs(freq-freq_range[2][0])

        freq = freq_range[1][1] if (d1 < d2) else freq_range[2][0]
        
    elif (freq > freq_range[2][1]):
        freq = freq_range[2][1]

    else:
        error = 0

#
    return error, freq

##############################
# Identification
##############################
def get_id():
    command = 'ID;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('ID(.*?);', data)

    if (data != []):
        return data[-1]

    else:
        return None

##############################
# Date and Time
##############################
def set_date_time(value):
    utc_time = datetime.now(timezone.utc).strftime('%H%M%S')
    utc_date = datetime.now(timezone.utc).strftime('%Y%m%d')

    command = 'DT0%s;' % (utc_date)
    serial_write(command.encode('ASCII'))

    command = 'DT1%s;' % (utc_time)
    serial_write(command.encode('ASCII'))

##############################
# Frequency Band
##############################
def set_band(band):
    band = {'1.8': '00',
            '3.5': '01',
            '5':   '02',
            '7':   '03',
            '10':  '04',
            '14':  '05',
            '18':  '06',
            '21':  '07',
            '24':  '08',
            '28':  '09',
            '50':  '10',
            'GEN': '11',
            'MW':  '12',
            '-':   '13',
            'AIR': '14',
            '144': '15',
            '430': '16'}[band.upper()]

    command = 'BS%s;' % (band)
    serial_write(command.encode('ASCII'))

##############################
# Operating Mode
##############################
def set_operating_mode(mode):
    mode = {'LSB':      '1',
            'USB':      '2',
            'CW-USB':   '3',
            'FM':       '4',
            'AM':       '5',
            'RTTY-LSB': '6',
            'CW-LSB':   '7',
            'DATA-LSB': '8',
            'RTTY-USB': '9',
            'DATA-FM':  'A',
            'FM-N':     'B',
            'DATA-USB': 'C',
            'AM-N':     'D',
            'C4FM':     'E'}[mode.upper()]

    command = 'MD0%s;' % (mode)
    serial_write(command.encode('ASCII'))

#
    return get_operating_mode()

#
def get_operating_mode():
    mode = {'1': 'LSB',
            '2': 'USB',
            '3': 'CW-USB',
            '4': 'FM',
            '5': 'AM',
            '6': 'RTTY-LSB',
            '7': 'CW-LSB',
            '8': 'DATA-LSB',
            '9': 'RTTY-USB',
            'A': 'DATA-FM',
            'B': 'FM-N',
            'C': 'DATA-USB',
            'D': 'AM-N',
            'E': 'C4FM'}

    command = 'MD0;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

    data = re.findall('MD0(.*?);', data)

    if (data != []):
        return mode[data[-1]]

    else:
        return None

##############################
# Auto Information
##############################
def set_auto_info(value):
    if (value < 0):
        value = 0
        
    elif (value > 1):
        value = 1

#
    auto_info = '%d' % (value)
    command = 'AI%s;' % (auto_info)
    serial_write(command.encode('ASCII'))

#
def get_auto_info():
    command = 'AI;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('AI(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

##############################
# Tx Oscillator
##############################
def set_function_Tx(VFO):
    VFO = {'VFO_A': 2, 'VFO_B': 3}[VFO.upper()]
    
    command = 'FT%d;' % (VFO)
    serial_write(command.encode('ASCII'))

#
def get_function_Tx():
    VFO = {'0': 'VFO_A', '1': 'VFO_B'}
    
    command = 'FT;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

    data = re.findall('FT(.*?);', data)

    if (data != []):
        return VFO[data[-1]]

    else:
        return None

##############################
# Squelch - Mode
##############################
def set_ctcss_mode(mode):
    mode = {'OFF': 0, 'CTCSS ENC/DEC': 1, 'CTCSS ENC': 2, 'DCS ENC/DEC': 3, 'DCS ENC': 4}[mode.upper()]

    command = 'CT0%d;' % (mode)
    serial_write(command.encode('ASCII'))

#
    return get_ctcss_mode()

#
def get_ctcss_mode():
    mode = {0: 'OFF', 1: 'CTCSS ENC/DEC', 2: 'CTCSS ENC', 3: 'DCS ENC/DEC', 4: 'DCS ENC'}

    command = 'CT0;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

    data = re.findall('CT0(.*?);', data)

    if (data != []):
        return mode[int(data[-1])]

    else:
        return None

##############################
# Repeater Shift
##############################
def set_repeater_shift(mode):
    mode = {'SIMPLEX': 0, 'PLUS SHIFT': 1, 'MINUS SHIFT': 2}[mode.upper()]

    command = 'OS0%d;' % (mode)
    serial_write(command.encode('ASCII'))

#
    return get_repeater_shift()

#
def get_repeater_shift():
    mode = {0: 'SIMPLEX', 1: 'PLUS SHIFT', 2: 'MINUS SHIFT'}

    command = 'OS0;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

    data = re.findall('OS0(.*?);', data)

    if (data != []):
        return mode[int(data[-1])]

    else:
        return None

##############################
# Squelch - CTCSS
##############################
def set_ctcss_tone_freq(index):
    command = 'CN00%03d;' % (index)
    serial_write(command.encode('ASCII'))

#
    return get_ctcss_tone_freq()

#
def get_ctcss_tone_freq():
    command = 'CN00;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('CN00(.*?);', data)

    if (data != []):
        return CTCSS_tone[data[-1]]

    else:
        return None

#
def get_dcs_code():
    command = 'CN01;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('CN01(.*?);', data)

    if (data != []):
        return DCS_code[data[-1]]

    else:
        return None

##############################
# Squelch - DCS
##############################
def set_dcs_code(index):
    command = 'CN01%03d;' % (index)
    serial_write(command.encode('ASCII'))

#
    return get_dcs_code()

#
def get_dcs_code():
    command = 'CN01;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('CN01(.*?);', data)

    if (data != []):
        return DCS_code[data[-1]]

    else:
        return None

##############################
# Digital Notch Filter (DNF)
##############################
def set_digital_notch_state(value):
    if (value  < 0):
        value = 0
        
    elif (value > 1):
        value = 1

#
    notch_state = '%d' % (value)
    command = 'BC0%s;' % (notch_state)
    serial_write(command.encode('ASCII'))

#
    return get_digital_notch_state()

#
def get_digital_notch_state():
    command = 'BC0;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('BC0(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

##############################
# Notch Filter
##############################
def set_manual_notch_state(value):
    notch_state = '%03d' % (value)
    command = 'BP00%s;' % (notch_state)
    serial_write(command.encode('ASCII'))

#
    return get_manual_notch_state()

#
def get_manual_notch_state():
    command = 'BP00;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('BP00(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

#
def set_manual_notch_level(value):
    if (value  < 10):
        value = 10
        
    elif (value > 3200):
        value = 3200

#
    notch_level = '%03d' % (value/10)
    command = 'BP01%s;' % (notch_level)
    serial_write(command.encode('ASCII'))

#
    return get_manual_notch_level()

#
def get_manual_notch_level():
    command = 'BP01;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('BP01(.*?);', data)

    if (data != []):
        return int(data[-1])*10

    else:
        return None

##############################
# Contour Filter
##############################
def set_contour_state(value):
    contour_state = '0%04d' % (value)
    command = 'CO0%s;' % (contour_state)
    serial_write(command.encode('ASCII'))

#
    return get_contour_state()

#
def get_contour_state():
    command = 'CO00;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('CO00(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

#
def set_contour_level(value):
    if (value < 10):
        value = 10
        
    elif (value > 3200):
        value = 3200

#
    contour_level = '1%04d' % (value)
    command = 'CO0%s;' % (contour_level)
    serial_write(command.encode('ASCII'))

#
    return get_contour_level()

#
def get_contour_level():
    command = 'CO01;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('CO01(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

##############################
# IF Shift
##############################
def set_IF_shift_level(value):
    if (value < -1200):
        value = -1200
        
    elif (value > 1200):
        value = 1200

#
    IF_shift = '%+05d' % (value)
    command = 'IS0%s;' % (IF_shift)
    serial_write(command.encode('ASCII'))

#
    return get_IF_shift_level()

#
def get_IF_shift_level():
    command = 'IS0;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('IS0(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

##############################
# IF Bandwidth
##############################
def set_IF_filter_type(value):
    value = {'WIDE': 0, 'NARROW': 1}[value.upper()]

#
    filter_type = '%d' % (value)
    command = 'NA0%s;' % (filter_type)
    serial_write(command.encode('ASCII'))

#
    return get_IF_filter_type()

#
def get_IF_filter_type():
    value = {0: 'WIDE', 1: 'NARROW'}

#
    command = 'NA0;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('NA0(.*?);', data)
    
    if (data != []):
        return value[int(data[-1])]

    else:
        return None

#
def set_IF_bandwidth(value, mode, filter_type):
    IF_filter_mode = {     'LSB': 'SSB',       'USB': 'SSB',    'CW-LSB': 'CW',     'CW-USB': 'CW',  
                      'RTTY-LSB': 'RTTY', 'RTTY-USB': 'RTTY', 'DATA-LSB': 'RTTY', 'DATA-USB': 'RTTY',    
                            'AM': 'AM',         'FM': 'FM',       'C4FM': 'FM',    'DATA-FM': 'FM',     
                          'AM-N': 'AM',       'FM-N': 'FM'}[mode.upper()]

    IF_filter_bw = {'AM': {'NARROW': [6000, 6000, 6000], 
                             'WIDE': [9000, 9000, 9000]},

                    'FM': {'NARROW': [9000, 9000, 9000], 
                             'WIDE': [16000, 16000, 16000]},

                   'SSB': {'NARROW': [1500, 200, 400, 600, 850, 1100, 1350, 1500, 1650, 1800], 
                             'WIDE': [2400, 1800, 1950, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3200]},

                    'CW': {'NARROW': [500, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500],
                             'WIDE': [2400, 500, 800, 1200, 1400, 1700, 2000, 2400, 3000]},

                  'RTTY': {'NARROW': [300, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500],
                             'WIDE': [500, 500, 800, 1200, 1400, 1700, 2000, 2400, 3000]}}

#
    if (IF_filter_mode in ['AM', 'FM']):
        return get_IF_bandwidth(mode, filter_type)

#
    if (value > len(IF_filter_bw[IF_filter_mode][filter_type.upper()])-1):
        value = len(IF_filter_bw[IF_filter_mode][filter_type.upper()])-1

#
    if (value > 0) and (filter_type.upper() == 'WIDE'):
        index = value+len(IF_filter_bw[IF_filter_mode]['NARROW'])-2

    else:
        index = value

#
    index = '%02d' % (index)
    command = 'SH0%s;' % (index)
    serial_write(command.encode('ASCII'))

#
    return get_IF_bandwidth(mode, filter_type)

#
def get_IF_bandwidth(mode, filter_type):
    IF_filter_mode = {     'LSB': 'SSB',       'USB': 'SSB',    'CW-LSB': 'CW',     'CW-USB': 'CW',  
                      'RTTY-LSB': 'RTTY', 'RTTY-USB': 'RTTY', 'DATA-LSB': 'RTTY', 'DATA-USB': 'RTTY',    
                            'AM': 'AM',         'FM': 'FM',       'C4FM': 'FM',    'DATA-FM': 'FM',
                          'AM-N': 'AM',       'FM-N': 'FM'}[mode.upper()]

    IF_filter_bw = {'AM': {'NARROW': [6000, 6000, 6000], 
                             'WIDE': [9000, 9000, 9000]},

                    'FM': {'NARROW': [9000, 9000, 9000], 
                             'WIDE': [16000, 16000, 16000]},

                   'SSB': {'NARROW': [1500, 200, 400, 600, 850, 1100, 1350, 1500, 1650, 1800], 
                             'WIDE': [2400, 1800, 1950, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3200]},

                    'CW': {'NARROW': [500, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500],
                             'WIDE': [2400, 500, 800, 1200, 1400, 1700, 2000, 2400, 3000]},

                  'RTTY': {'NARROW': [300, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500],
                             'WIDE': [500, 500, 800, 1200, 1400, 1700, 2000, 2400, 3000]}}

#
    if (IF_filter_mode in ['AM', 'FM']):
        return IF_filter_bw[IF_filter_mode][filter_type.upper()][0], 0

#
    command = 'SH0;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('SH0(.*?);', data)

    if (data != []):
        value = int(data[-1])

        if (value > 0) and (filter_type.upper() == 'WIDE'):
            index = value-len(IF_filter_bw[IF_filter_mode]['NARROW'])+2

        else:
            index = value

        IF_bandwidth = IF_filter_bw[IF_filter_mode][filter_type.upper()][index]

        return IF_bandwidth, index

    else:
        return None, None

##############################
# Audio Peak Filter (APF)
##############################
def set_APF_state(value):
    contour_state = '2%04d' % (value)
    command = 'CO0%s;' % (contour_state)
    serial_write(command.encode('ASCII'))

#
def get_APF_state():
    command = 'CO02;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('CO00(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

#
def set_APF_level(value):
    if (value < -250):
        value = -250
        
    elif (value > 250):
        value = 250

#
    value = int((value+250)/10)

#
    APF_value = '3%04d' % (value)
    command = 'CO0%s;' % (APF_value)
    serial_write(command.encode('ASCII'))

#
    return get_APF_level()

#
def get_APF_level():
    command = 'CO03;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('CO03(.*?);', data)

    if (data != []):
        return int(data[-1])*10-250

    else:
        return None

##############################
# Noise Blanker (NB)
##############################
def set_NB_state(value):
    if (value  < 0):
        value = 0
        
    elif (value > 1):
        value = 1

#
    NB_state = '%d' % (value)
    command = 'NB0%s;' % (NB_state)
    serial_write(command.encode('ASCII'))

#
    return get_NB_state()

#
def get_NB_state():
    command = 'NB0;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('NB0(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

#
def set_NB_level(value):
    if (value < 0):
        value = 0
        
    elif (value > 10):
        value = 10

#
    NB_level = '%03d' % (value)
    command = 'NL0%s;' % (NB_level)
    serial_write(command.encode('ASCII'))

#
    return get_NB_level()

#
def get_NB_level():
    command = 'NL0;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('NL0(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

##############################
# Noise Reduction (NR)
##############################
def set_NR_state(value):
    NR_state = '%d' % (value)
    command = 'NR0%s;' % (NR_state)
    serial_write(command.encode('ASCII'))

    return get_NR_state()

#
def get_NR_state():
    command = 'NR0;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('NR0(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

#
def set_NR_level(value):
    if (value < 1):
        value = 1
        
    elif (value > 15):
        value = 15

#
    NR_level = '%02d' % (value)
    command = 'RL0%s;' % (NR_level)
    serial_write(command.encode('ASCII'))

#
    return get_NR_level()

#
def get_NR_level():
    command = 'RL0;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('RL0(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

##############################
# Monitor Level
##############################
def set_monitor_state(state):
    if (state < 0):
        state = 0
        
    elif (state > 1):
        state = 1

#
    monitor_state = '%03d' % (state)
    command = 'ML0%s;' % (monitor_state)
    serial_write(command.encode('ASCII'))

    return get_monitor_state()

#
def get_monitor_state():
    command = 'ML0;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('ML0(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None
#
def set_monitor_level(value):
    if (value < 0):
        value = 0
        
    elif (value > 100):
        value = 100

#
    monitor_level = '%03d' % (value)
    command = 'ML1%s;' % (monitor_level)
    serial_write(command.encode('ASCII'))

    return get_monitor_level()

#
def get_monitor_level():
    command = 'ML1;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('ML1(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

##############################
# Speech Processor
##############################
def set_SP_state(value):
    if (value < 0):
        value = 0
        
    elif (value > 1):
        value = 1

#
    SP_state = '%d' % (value)
    command = 'PR0%s;' % (SP_state)
    serial_write(command.encode('ASCII'))

    return get_SP_state()

#
def get_SP_state():
    command = 'PR0;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('PR0(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

#
def set_SP_EQ_state(value):
    if (value < 0):
        value = 0
        
    elif (value > 1):
        value = 1

#
    SP_state = '%d' % (value)
    command = 'PR1%s;' % (SP_state)
    serial_write(command.encode('ASCII'))

    return get_SP_state()

#
def get_SP_EQ_state():
    command = 'PR1;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('PR1(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

##############################
# Speech Processor Level
##############################
def set_SP_level(value):
    if (value < 0):
        value = 0
        
    elif (value > 100):
        value = 100

#
    SP_level = '%03d' % (value)
    command = 'PL%s;' % (SP_level)
    serial_write(command.encode('ASCII'))

#
    return get_SP_level()

#
def get_SP_level():
    command = 'PL;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('PL(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

##############################
# Microphone Gain
##############################
def set_microphone_gain(value):
    if (value < 0):
        value = 0
        
    elif (value > 100):
        value = 100

#
    SP_level = '%03d' % (value)
    command = 'MG%s;' % (SP_level)
    serial_write(command.encode('ASCII'))

#
    return get_microphone_gain()

#
def get_microphone_gain():
    command = 'MG;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('MG(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

##############################
# VFO Copy/Swap
##############################
def copy_VFO():
    command = 'AB;'
    serial_write(command.encode('ASCII'))

#
def swap_VFO():
    command = 'SV;'
    serial_write(command.encode('ASCII'))

##############################
# CLAR Rx
##############################
def set_RF_clar_state(value):
    rf_clar_state = '%d' % (value)
    command = 'RT%s;' % (rf_clar_state)
    serial_write(command.encode('ASCII'))

#
def get_RF_clar_state():
    command = 'RT;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('RT(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

##############################
# CLAR Tx
##############################
def set_RF_clar_state_Tx(value):
    rf_clar_state_tx = '%d' % (value)
    command = 'XT%s;' % (rf_clar_state_tx)
    serial_write(command.encode('ASCII'))

#
def get_RF_clar_state_Tx():
    command = 'XT;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('XT(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

##############################
# CLAR Up/Down
##############################
def clear_RF_clar():
    command = 'RC;'
    serial_write(command.encode('ASCII'))

#
def RF_clar_up(value):
    if (value < 0):
        value = 0

#
    rf_clar = '%04d' % (value)
    command = 'RU%s;' % (rf_clar)
    serial_write(command.encode('ASCII'))

#
def RF_clar_down(value):
    if (value < 0):
        value = 0

#
    rf_clar = '%04d' % (value)
    command = 'RD%s;' % (rf_clar)
    serial_write(command.encode('ASCII'))

##############################
# RF Squelch
##############################
def set_RF_squelch(value):
    if (value  < 0):
        value = 0
        
    elif (value > 100):
        value = 100

#
    rf_squelch = '%03d' % (value)
    command = 'SQ0%s;' % (rf_squelch)
    serial_write(command.encode('ASCII'))

#
    return get_RF_squelch()

#
def get_RF_squelch():
    command = 'SQ0;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('SQ0(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

##############################
# RF Attenuator
##############################
def set_RF_attenuator(value):
    if (value  < 0):
        value = 0
        
    elif (value > 1):
        value = 1

#
    rf_att = '%d' % (value)
    command = 'RA0%s;' % (rf_att)
    serial_write(command.encode('ASCII'))

#
    return get_RF_attenuator()

#
def get_RF_attenuator():
    command = 'RA0;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('RA0(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

##############################
# RF Pre-Amp (IPO)
##############################
def set_IPO(value):
    value = {'IPO': 0, 'AMP 1': 1, 'AMP 2': 2}[value.upper()]

#
    IPO = '%d' % (value)
    command = 'PA0%s;' % (IPO)
    serial_write(command.encode('ASCII'))

#
    return get_IPO()

#
def get_IPO():
    value = {0: 'IPO', 1: 'AMP 1', 2: 'AMP 2'}

#
    command = 'PA0;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('PA0(.*?);', data)

    if (data != []):
        return value[int(data[-1])]

    else:
        return None

##############################
# RF Gain
##############################
def set_RF_gain(value):
    if (value  < 0):
        value = 0
        
    elif (value > 255):
        value = 255

#
    rf_gain = '%03d' % (value)
    command = 'RG0%s;' % (rf_gain)
    serial_write(command.encode('ASCII'))

#
    return get_RF_gain()

#
def get_RF_gain():
    command = 'RG0;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('RG0(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

##############################
# AF Gain
##############################
def set_AF_gain(value):
    if (value  < 0):
        value = 0
        
    elif (value > 255):
        value = 255

#
    af_gain = '%03d' % (value)
    command = 'AG0%s;' % (af_gain)
    serial_write(command.encode('ASCII'))

#
    return get_AF_gain()

#
def get_AF_gain():
    command = 'AG0;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('AG0(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

##############################
# RF Power
##############################
def set_RF_power(power):
    command = 'PC%03d;' % (power)
    serial_write(command.encode('ASCII'))

#
    return get_RF_power()

#
def get_RF_power():
    command = 'PC;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('PC(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

##############################
# VFO_A Frequency
##############################
def set_frequency_VFO_A(freq):
    error, freq = check_frequency_range(freq, FREQRANGE)

#
    freq = '%09d' % (freq)
    command = 'FA%s;' % (freq[:9])
    serial_write(command.encode('ASCII'))

#
    return get_frequency_VFO_A()

#
def get_frequency_VFO_A():
    command = 'FA;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('FA(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

##############################
# VFO_B Frequency
##############################
def set_frequency_VFO_B(freq):
    error, freq = check_frequency_range(freq, FREQRANGE)

#
    freq = '%09d' % (freq)
    command = 'FB%s;' % (freq[:9])
    serial_write(command.encode('ASCII'))

#
    return get_frequency_VFO_B()

#
def get_frequency_VFO_B():
    command = 'FB;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('FB(.*?);', data)

    if (data != []):
        return int(data[-1])

    else:
        return None

##############################
# Meters
##############################
def get_meter(meter):
    meter = {'PANEL1': '0',
             'S':      '1',
             'PANEL2': '2',
             'COMP':   '3',
             'ALC':    '4',
             'PO':     '5',
             'SWR':    '6',
             'ID':     '7',
             'VDD':    '8'}[meter]

    command = 'RM%s;' % (meter)
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('RM(?:.)(.*?);', data)

    if (data != []):
        return data[-1]

    else:
        return None

##############################
# PLL Lock
##############################
def get_PLL_lock():
    stat = {'0': 'LOCK', '1': 'UNLOCK'}

    command = 'UL;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('UL(.*?);', data)

    if (data != []):
        return stat[data[-1]]

    else:
        return None

##############################
# Band Info
##############################
def get_band_info():
    command = 'IF;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('IF(.*?);', data)

    if (data != []):
        memory = data[-1][0:3]

        freq = data[-1][3:12]

        clar_dir = data[-1][12:17]

        clar_Rx = {'0': 'Rx_CLAR_OFF', '1': 'Rx_CLAR_ON'}[data[-1][17]]

        clar_Tx = {'0': 'Tx_CLAR_OFF', '1': 'Tx_CLAR_ON'}[data[-1][18]]

        mode = {'1': 'LSB',      '2': 'USB',      '3': 'CW-USB',    '4': 'FM',       '5': 'AM', 
                '6': 'RTTY-LSB', '7': 'CW-LSB',   '8': 'DATA-LSB',  '9': 'RTTY-USB', 'A': 'DATA-FM', 
                'B': 'FM-N',     'C': 'DATA-USB', 'D': 'AM-N',      'E': 'C4FM'}[data[-1][19]]

        vfo  = {'0': 'VFO',     '1': 'MEMORY',  '2': 'MEMORY_TUNE', '3': 'QMB', 
                '4': 'QMB_MT',  '5': 'PMS',     '6': 'HOME'}[data[-1][20]]

        ctcss = {'0': 'CTCSS_OFF',   '1': 'CTCSS_ENC/DEC', '2': 'CTCSS_ENC', 
                 '3': 'DCS_ENC/DEC', '4': 'DCS_ENC'}[data[-1][21]]

        simplex = {'0': 'SIMPLEX', '1': 'PLUS_SHIFT', '2': 'MINUS_SHIFT'}[data[-1][24]]

        return [memory, freq, clar_dir, clar_Rx, clar_Tx, mode, vfo, ctcss, simplex], data[-1]

    else:
        return None, None

##############################
# Opposite Band Info
##############################
def get_opposite_band_info():
    command = 'OI;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('OI(.*?);', data)

    if (data != []):
        memory = data[-1][0:3]

        freq = data[-1][3:12]

        clar_dir = data[-1][12:17]

        clar_Rx = {'0': 'Rx_CLAR_OFF', '1': 'Rx_CLAR_ON'}[data[-1][17]]

        clar_Tx = {'0': 'Tx_CLAR_OFF', '1': 'Tx_CLAR_ON'}[data[-1][18]]

        mode = {'1': 'LSB',      '2': 'USB',      '3': 'CW-USB',   '4': 'FM',       '5': 'AM', 
                '6': 'RTTY-LSB', '7': 'CW-LSB',   '8': 'DATA-LSB', '9': 'RTTY-USB', 'A': 'DATA-FM', 
                'B': 'FM-N',     'C': 'DATA-USB', 'D': 'AM-N',     'E': 'C4FM'}[data[-1][19]]

        vfo  = {'0': 'VFO',     '1': 'MEMORY',  '2': 'MEMORY_TUNE', '3': 'QMB', 
                '4': 'QMB_MT',  '5': 'PMS',     '6': 'HOME'}[data[-1][20]]

        ctcss = {'0': 'CTCSS_OFF',   '1': 'CTCSS_ENC/DEC', '2': 'CTCSS_ENC', 
                 '3': 'DCS_ENC/DEC', '4': 'DCS_ENC'}[data[-1][21]]

        simplex = {'0': 'SIMPLEX', '1': 'PLUS_SHIFT', '2': 'MINUS_SHIFT'}[data[-1][24]]

        return [memory, freq, clar_dir, clar_Rx, clar_Tx, mode, vfo, ctcss, simplex], data[-1]

    else:
        return None, None

##############################
# Scan
##############################
def set_scan(mode):
    mode = {'UP': 1, 'DOWN': 2, 'OFF': 0}[mode]
    
    command = 'SC%d;' % (mode)
    serial_write(command.encode('ASCII'))

#
    return get_scan()

#
def get_scan():
    mode = {'1': 'UP', '2': 'DOWN', '0': 'OFF'}
    
    command = 'SC;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('SC(.*?);', data)

    if (data != []):
        return mode[data[-1]]

    else:
        return None

##############################
# Memory Channel
##############################
def memory_vm():
    command = 'VM;'
    serial_write(command.encode('ASCII'))

#
def set_memory_vfo():
    command = 'AM;'
    serial_write(command.encode('ASCII'))

#
def set_memory(channel):
    channel = '%03d' % (channel)
    command = 'MC%s;' % (channel)
    serial_write(command.encode('ASCII'))

#
    return get_memory()

#
def get_memory():
    command = 'MC;'
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('MC(.*?);', data)

    if (data != []):
        return data[-1]

    else:
        return None

#
def set_memory_data(channel, mem):
    data = '%03d%s' % (channel, mem)
    command = 'MW%s;' % (data)
    serial_write(command.encode('ASCII'))

#
def get_memory_data(channel):
    command = 'MR%03d;' % (channel)
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('MR(.*?);', data)

    if (data != []):
        return data[-1]

    else:
        return None

#
def set_memory_data_tag(channel, memory):
    data = []

#
    freq = memory['freq']
    data.append(freq)

    clar_offset = memory['clar_offset']
    data.append(clar_offset)

    clar_Rx = {'OFF': '0', 'ON': '1'}[memory['clar_rx']]
    data.append(clar_Rx)

    clar_Tx = {'OFF': '0', 'ON': '1'}[memory['clar_tx']]
    data.append(clar_Tx)

    mode = {'LSB':      '1',    'USB':      '2',    'CW-USB':   '3',    'FM':       '4',    'AM':       '5', 
            'RTTY-LSB': '6',    'CW-LSB':   '7',    'DATA-LSB': '8',    'RTTY-USB': '9',    'DATA-FM':  'A',
            'FM-N':     'B',    'DATA-USB': 'C',    'AM-N':     'D',    'C4FM':     'E'}[memory['mode']]
    data.append(mode)

    data.append('0')

    ctcss = {'OFF':         '0',    'CTCSS_ENC/DEC':    '1',    'CTCSS_ENC':    '2', 
             'DCS_ENC/DEC': '3',    'DCS_ENC':          '4'}[memory['ctcss']]
    data.append(ctcss)

    data.append('00')

    shift = {'SIMPLEX': '0', 'PLUS_SHIFT': '1', 'MINUS_SHIFT': '2'}[memory['shift']]
    data.append(shift)

    data.append('0')

    tag = memory['tag']
    data.append(tag)

#
    data = '%03d%s' % (channel, ''.join(data))
    command = 'MT%s;' % (data)
    serial_write(command.encode('ASCII'))

    return get_memory_data_tag(channel)

#
def get_memory_data_tag(channel):
    command = 'MT%03d;' % (channel)
    serial_write(command.encode('ASCII'))
    data = serial_read_until(expected=b';').decode('ASCII')

#
    data = re.findall('MT(?:...)(.*?);', data)

    if (data != []):
        memory = {}

        memory['freq'] = data[-1][0:9]

        memory['clar_offset'] = data[-1][9:14]

        memory['clar_rx'] = {'0': 'OFF', '1': 'ON'}[data[-1][14]]

        memory['clar_tx'] = {'0': 'OFF', '1': 'ON'}[data[-1][15]]

        memory['mode'] = {'1':    'LSB',      '2': 'USB',         '3': 'CW-USB',      '4': 'FM',          '5': 'AM',
                          '6':    'RTTY-LSB', '7': 'CW-LSB',      '8': 'DATA-LSB',    '9': 'RTTY-USB',    'A': 'DATA-FM',
                          'B':    'FM-N',     'C': 'DATA-USB',    'D': 'AM-N',        'E': 'C4FM'}[data[-1][16]]

        memory['ctcss'] = {'0':   'OFF',          '1': 'CTCSS_ENC/DEC',   '2':    'CTCSS_ENC', 
                           '3':   'DCS_ENC/DEC',  '4': 'DCS_ENC'}[data[-1][18]]

        memory['shift'] = {'0': 'SIMPLEX', '1': 'PLUS_SHIFT', '2': 'MINUS_SHIFT'}[data[-1][21]]

        memory['tag'] = data[-1][23:]

#
        return memory, data[-1]

    else:
        return None, None

##############################
# Memory Channel Direct
##############################
def get_active_memory():
    address = 0x3229

#
    data = [0]*16

#
    for offset in range(8):
        data[2*offset:2*offset+2] = spr(address+2*offset)

#
    active_channels = []

#
    for i in range(128):
        row = int(i/8)
        column = i-row*8

        state = (data[row] >> column) & 1

        if (state):
            active_channels.append(i+1)
    
#
    return active_channels

#
def set_active_memory(channels):
    address = 0x3229

#
    data = [0]*16

#
    for i in range(len(channels)):
        row = int((channels[i]-1)/8)
        column = (channels[i]-1)-row*8

        data[row] = data[row] | (1 << column)

#
    for offset in range(8):
        value = spw(address+2*offset, data[2*offset:2*offset+2])

        if (value == None):
            raise Exception('data transmit error')

#
    return data

#
def get_memory_direct(channel):
    address = 0x3249+96*channel

#
    data = [0]*96
    memory = {}

#
    data[0:2] =   spr(address)
    data[2:4] =   spr(address+2)
    data[4:6] =   spr(address+4)
    data[70:72] = spr(address+70)
    data[74:76] = spr(address+74)
    data[76:78] = spr(address+76)
    data[78:80] = spr(address+78)
    data[80:82] = spr(address+80)
    data[82:84] = spr(address+82)
    data[84:86] = spr(address+84)
    data[86:88] = spr(address+86)
    data[88:90] = spr(address+88)
    data[90:92] = spr(address+90)
    data[92:94] = spr(address+92)
    data[94:96] = spr(address+94)

#
    if (MESSAGE_FLAG == True and TEXT_BROWSER != None):
        utc_time = datetime.now(timezone.utc).strftime('%H%M%S.%f')[:-3]
        message = '<br>'.join(re.findall(f'.{{1,{32}}}', bytearray(data).hex()))
        message = 'address %X data: <br>%s' % (address, message)
        message = '%s: INFO: <font color="yellow">%s</font>' % (utc_time, message)

        TEXT_BROWSER.append(message)

# Offset 0
    memory['mode'] = {0:  'LSB',      1:  'USB',      2: 'CW-USB',    3:  'CW-LSB',   4: 'AM',
                      5:  'FM',       6:  'RTTY-LSB', 7: 'RTTY-USB',  8:  'DATA-LSB', 9: 'DATA-USB', 
                      10: 'DATA-FM',  11: 'C4FM'}[data[0]]

# Offset 1
    memory['skip']    = {1: 'YES', 0: 'NO'}[(data[1] >> 7) & 1]
    memory['clar']    = {0: 'OFF', 1: 'ON'}[(data[1] >> 5) & 1]
    memory['clar_rx'] = {0: 'OFF', 1: 'ON'}[(data[1] >> 4) & 1]
    memory['clar_tx'] = {0: 'OFF', 1: 'ON'}[(data[1] >> 3) & 1]
    memory['tuner']   = {0: 'OFF', 1: 'ON'}[(data[1] >> 2) & 1]

# Offset 2
    memory['repeater'] = {1: 'YES', 0: 'NO'}[(data[2] >> 7) & 1]
    memory['split']    = {1: 'YES', 0: 'NO'}[(data[2] >> 6) & 1]
    memory['shift']    = {1: 'SIMPLEX', 2: 'PLUS_SHIFT', 0: 'MINUS_SHIFT'}[(data[2] >> 2) & 3]

# Offset 3
    memory['step']  = {0: '5Hz', 1: '10Hz'}[(data[3] >> 7) & 1]
    memory['ctcss'] = {0: 'OFF',          2: 'CTCSS_ENC/DEC', 1:  'CTCSS_ENC', 
                       4: 'DCS_ENC/DEC',  3: 'DCS_ENC'}[(data[3] >> 3) & 7]
    memory['att' ]  = {0: 'OFF', 1: 'ON'}[(data[3]) & 1]

# Offset 4
    memory['bw_ssb']  = {1: 'NARROW', 0: 'WIDE'}[(data[4] >> 6) & 1]
    memory['bw_cw']   = {1: 'NARROW', 0: 'WIDE'}[(data[4] >> 5) & 1]
    memory['bw_fm']   = {1: 'NARROW', 0: 'WIDE'}[(data[4] >> 4) & 1]
    memory['bw_rtty'] = {1: 'NARROW', 0: 'WIDE'}[(data[4] >> 3) & 1]
    memory['bw_data'] = {1: 'NARROW', 0: 'WIDE'}[(data[4] >> 2) & 1]
    memory['bw_am']   = {1: 'NARROW', 0: 'WIDE'}[(data[4] >> 1) & 1]

# Offset 5
    memory['ipo'] = {3: 'AMP2', 2: 'AMP1', 0: 'IPO'}[(data[5]) & 3]

# Offset 70
    memory['ctcss_tone'] = CTCSS_tone['%03d' % data[70]]

# Offset 71
    memory['dcs_code'] = DCS_code['%03d' % data[71]]

# Offset 74-76
    memory['clar_offset'] = int.from_bytes(data[74:76], byteorder='big', signed=True)

# Offset 76-80
    memory['freq'] = int.from_bytes(data[76:80], byteorder='big')

# Offset 80-84
    memory['freq_tx'] = int.from_bytes(data[80:84], byteorder='big')

# Offset 84-96
    memory['tag'] = bytearray(data[84:96]).decode('ascii')

#
    return memory, data

#
def set_memory_direct(channel, memory):
    address = 0x3249+96*channel

#
    data = [0]*96

# Offset 0
    data[0] = {'LSB':       0,      'USB':      1,      'CW-USB':   2,  'CW-LSB':   3,  'AM':       4,
               'FM':        5,      'RTTY-LSB': 6,      'RTTY-USB': 7,  'DATA-LSB': 8,  'DATA-USB': 9, 
               'DATA-FM':   10,     'C4FM':     11}[memory['mode']]

# Offset 1
    skip    = {'YES': 1, 'NO': 0}[memory['skip']]
    clar    = {'OFF': 0, 'ON': 1}[memory['clar']]
    clar_rx = {'OFF': 0, 'ON': 1}[memory['clar_rx']]
    clar_tx = {'OFF': 0, 'ON': 1}[memory['clar_tx']]
    tuner   = {'OFF': 0, 'ON': 1}[memory['tuner']]
    data[1] = (skip << 7) | (clar << 5 ) | (clar_rx << 4) | (clar_tx << 3) | (tuner << 2)

# Offset 2
    repeater = {'YES': 1, 'NO': 0}[memory['repeater']]
    split    = {'YES': 1, 'NO': 0}[memory['split']]
    shift    = {'SIMPLEX': 1, 'PLUS_SHIFT': 2, 'MINUS_SHIFT': 0}[memory['shift']]
    data[2]  = (repeater << 7) | (split << 6) | (shift << 2)

# Offset 3
    step    = {'5Hz': 0, '10Hz': 1}[memory['step']]
    ctcss   = {'OFF':           0,  'CTCSS_ENC/DEC':    2, 'CTCSS_ENC': 1, 
               'DCS_ENC/DEC':   4,  'DCS_ENC':          3}[memory['ctcss']]
    att     = {'OFF': 0, 'ON': 1}[memory['att']]
    data[3] = (step << 7) | (ctcss << 3) | (att)

# Offset 4
    bw_ssb  = {1: 'NARROW', 0: 'WIDE'}[memory['bw_ssb']]
    bw_cw   = {1: 'NARROW', 0: 'WIDE'}[memory['bw_cw']]
    bw_fm   = {1: 'NARROW', 0: 'WIDE'}[memory['bw_fm']]
    bw_rtty = {1: 'NARROW', 0: 'WIDE'}[memory['bw_rtty']]
    bw_data = {1: 'NARROW', 0: 'WIDE'}[memory['bw_data']]
    bw_am   = {1: 'NARROW', 0: 'WIDE'}[memory['bw_am']]
    data[4] = (bw_ssb << 6) | (bw_cw << 5) | (bw_fm << 4) | (bw_rtty << 3) | (bw_data << 2) | (bw_am << 1)

# Offset 5
    ipo      = {'AMP2': 3, 'AMP1': 2, 'IPO': 0}[memory['ipo']]
    data[5]  = ipo

# Offset 70
    ctcss_tone = [k for k, v in CTCSS_tone.items() if ('%.1f' % (v)) == memory['ctcss_tone']]
    data[70]   = int(ctcss_tone[0])

# Offset 71
    dcs_code = [k for k, v in DCS_code.items() if ('%d' % (v)) == memory['dcs_code']]
    data[71] = int(dcs_code[0])

# Offset 74-76
    data[74:76] = int(memory['clar_offset']).to_bytes(2, byteorder='big', signed=True)

# Offset 76-80
    data[76:80] = int(memory['freq']).to_bytes(4, byteorder='big')

# Offset 80-84
    data[80:84] = int(memory['freq_tx']).to_bytes(4, byteorder='big')

# Offset 94-96
    data[84:96] = [ord(x) for x in memory['tag']]

#
    if (MESSAGE_FLAG == True and TEXT_BROWSER != None):
        utc_time = datetime.now(timezone.utc).strftime('%H%M%S.%f')[:-3]
        message = '<br>'.join(re.findall(f'.{{1,{32}}}', bytearray(data).hex()))
        message = 'address %X data: <br>%s' % (address, message)
        message = '%s: INFO: <font color="yellow">%s</font>' % (utc_time, message)

        TEXT_BROWSER.append(message)

#
    spw(address,    data[0:2])
    spw(address+2,  data[2:4])
    spw(address+4,  data[4:6])
    spw(address+70, data[70:72])
    spw(address+74, data[74:76])
    spw(address+76, data[76:78])
    spw(address+78, data[78:80])
    spw(address+80, data[80:82])
    spw(address+82, data[82:84])
    spw(address+84, data[84:86])
    spw(address+86, data[86:88])
    spw(address+88, data[88:90])
    spw(address+90, data[90:92])
    spw(address+92, data[92:94])
    spw(address+94, data[94:96])

#
def get_memory_direct_raw(channel):
    address = 0x3249+96*channel

#
    data = [0]*96

#
    for offset in range(48):
        data[2*offset:2*offset+2] = spr(address+2*offset)

#
    if (MESSAGE_FLAG == True and TEXT_BROWSER != None):
        utc_time = datetime.now(timezone.utc).strftime('%H%M%S.%f')[:-3]
        message = '<br>'.join(re.findall(f'.{{1,{32}}}', bytearray(data).hex()))
        message = 'address %X data: <br>%s' % (address, message)
        message = '%s: INFO: <font color="yellow">%s</font>' % (utc_time, message)

        TEXT_BROWSER.append(message)

#
    return data

#
def set_memory_direct_raw(channel, data):
    address = 0x3249+96*channel

#
    for offset in range(48):
        value = spw(address+2*offset, data[2*offset:2*offset+2])

        if (value == None):
            raise Exception('data transmit error')

#
    if (MESSAGE_FLAG == True and TEXT_BROWSER != None):
        utc_time = datetime.now(timezone.utc).strftime('%H%M%S.%f')[:-3]
        message = '<br>'.join(re.findall(f'.{{1,{32}}}', bytearray(data).hex()))
        message = 'address %X data: <br>%s' % (address, message)
        message = '%s: INFO: <font color="yellow">%s</font>' % (utc_time, message)

        TEXT_BROWSER.append(message)

#
def dump_memory():
    data = [0]*0x8000

#
    for address in range(0x000, 0x8000, 2):
        data[address:address+2] = spr(address)

#
    return data

#
def spr(address):
    if (address < 0) or (address > 32767):
        return None

    address_high = (address & 0xFF00) >> 8
    address_low = (address & 0x00FF)

    command = b'SPR%c%c' % (address_high, address_low)

    check_byte = sum(command) & 0x00FF

    command = b'%s%c;' % (command, check_byte)

    serial_write(command)
    data = serial_read_until(expected=b';')

#
    if (data[0:5] == command[0:5]):
        check_byte = (check_byte+data[5]+data[6]) & 0x00FF

        if (check_byte != data[7]):
            return None

        else:
            return data[5:7]

    else:
        return None

#
def spw(address, data):
    address_range = [(0x3229, 0x3238), (0x3249, 0x6368)]
    in_range = any(start <= address <= end for start, end in address_range)

    if (in_range == False):
        return None

#
    address_high = (address & 0xFF00) >> 8
    address_low = (address & 0x00FF)

    command = b'SPW%c%c%c%c' % (address_high, address_low, data[0], data[1])

    check_byte = sum(command) & 0x00FF

    command = b'%s%c;' % (command, check_byte)

    serial_write(command)
    data = serial_read_until(expected=b';')

#
    if (data == b'A;'):
        return data

    else:
        return None

