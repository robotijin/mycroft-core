# -*- coding: utf-8 -*-
#
# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import unittest
import datetime

from mycroft.util.format import nice_number
from mycroft.util.format import nice_time
from mycroft.util.format import pronounce_number

NUMBERS_FIXTURE_ES = {
    1.435634: '1,436',
    2: '2',
    5.0: '5',
    0.027: '0,027',
    0.5: 'un medio',
    1.333: '1 y 1 tercio',
    2.666: '2 y 2 tercio',
    0.25: 'un cuarto',
    1.25: '1 y 1 cuarto',
    0.75: '3 cuartos',
    1.75: '1 y 3 cuartos',
    3.4: '3 y 2 quintos',
    16.8333: '16 y 5 sextos',
    12.5714: u'12 y 4 séptimos',
    9.625: '9 y 5 octavos',
    6.777: '6 y 7 novenos',
    3.1: u'3 y 1 décimo',
    2.272: '2 y 3 onceavos',
    5.583: '5 y 7 doceavos',
    8.384: '8 y 5 treceavos',
    0.071: 'un catorceavo',
    6.466: '6 y 7 quinceavos',
    8.312: '8 y 5 dieciseisavos',
    2.176: '2 y 3 diecisieteavos',
    200.722: '200 y 13 dieciochoavos',
    7.421: '7 y 8 diecinueveavos',
    0.05: 'un veinteavo'

}


class TestNiceNumberFormat_es(unittest.TestCase):
    def test_convert_float_to_nice_number_es(self):
        for number, number_str in NUMBERS_FIXTURE_ES.items():
            self.assertEqual(nice_number(number, lang="es-es"), number_str,
                             'should format {} as {} and not {}'.format(
                                 number, number_str, nice_number(
                                     number, lang="es-es")))

    def test_specify_denominator_es(self):
        self.assertEqual(nice_number(5.5, lang="es-es",
                                     denominators=[1, 2, 3]),
                         '5 y medio',
                         'should format 5.5 as 5 y medio not {}'.format(
                             nice_number(5.5, lang="es-es",
                                         denominators=[1, 2, 3])))
        self.assertEqual(nice_number(2.333, lang="es-es",
                                     denominators=[1, 2]),
                         '2,333',
                         'should format 2.333 as 2,333 not {}'.format(
                             nice_number(2.333, lang="es-es",
                                         denominators=[1, 2])))

    def test_no_speech_es(self):
        self.assertEqual(nice_number(6.777, lang="es-es", speech=False),
                         '6 7/9',
                         'should format 6.777 as 6 7/9 not {}'.format(
                             nice_number(6.777, lang="es-es", speech=False)))
        self.assertEqual(nice_number(6.0, lang="es-es", speech=False),
                         '6',
                         'should format 6.0 as 6 not {}'.format(
                             nice_number(6.0, lang="es-es", speech=False)))
        self.assertEqual(nice_number(1234567890, lang="es-es", speech=False),
                         '1 234 567 890',
                         'should format 1234567890 as'
                         '1 234 567 890 not {}'.format(
                             nice_number(1234567890, lang="es-es",
                                         speech=False)))
        self.assertEqual(nice_number(12345.6789, lang="es-es", speech=False),
                         '12 345,679',
                         'should format 12345.6789 as'
                         '12 345,679 not {}'.format(
                             nice_number(12345.6789, lang="es-es",
                                         speech=False)))




# def pronounce_number(number, lang="es-es", places=2):
class TestPronounceNumber(unittest.TestCase):
    def test_convert_int(self):
        self.assertEqual(pronounce_number(0, lang="es"), "cero")
        self.assertEqual(pronounce_number(1, lang="es"), "uno")
        self.assertEqual(pronounce_number(10, lang="es"), "diez")
        self.assertEqual(pronounce_number(15, lang="es"), "quince")
        self.assertEqual(pronounce_number(21, lang="es"), "veintiuno")
        self.assertEqual(pronounce_number(27, lang="es"), "veintisiete")
        self.assertEqual(pronounce_number(30, lang="es"), "treinta")
        self.assertEqual(pronounce_number(19, lang="es"), "diecinueve")
        self.assertEqual(pronounce_number(88, lang="es"), "ochenta y ocho")
        self.assertEqual(pronounce_number(46, lang="es"), "cuarenta y seis")
        self.assertEqual(pronounce_number(99, lang="es"), "noventa y nueve")

    def test_convert_negative_int(self):
        self.assertEqual(pronounce_number(-1, lang="es"), "menos uno")
        self.assertEqual(pronounce_number(-10, lang="es"), "menos diez")
        self.assertEqual(pronounce_number(-15, lang="es"), "menos quince")
        self.assertEqual(pronounce_number(-21, lang="es"), "menos veintiuno")
        self.assertEqual(pronounce_number(-27, lang="es"), "menos veintisiete")
        self.assertEqual(pronounce_number(-30, lang="es"), "menos treinta")
        self.assertEqual(pronounce_number(-35, lang="es"), "menos treinta y cinco")
        self.assertEqual(pronounce_number(-83, lang="es"), "menos ochenta y tres")
        self.assertEqual(pronounce_number(-19, lang="es"), "menos diecinueve")
        self.assertEqual(pronounce_number(-88, lang="es"), "menos ochenta y ocho")
        self.assertEqual(pronounce_number(-46, lang="es"), "menos cuarenta y seis")
        self.assertEqual(pronounce_number(-99, lang="es"), "menos noventa y nueve")        

    def test_convert_decimals(self):
        self.assertEqual(pronounce_number(1.234, lang="es"),
                         "uno punto dos tres")
        self.assertEqual(pronounce_number(21.234, lang="es"),
                         "veintiuno punto dos tres")
        self.assertEqual(pronounce_number(21.234, lang="es", places=1),
                         "veintiuno punto dos")
        self.assertEqual(pronounce_number(21.234, lang="es", places=0),
                         "veintiuno")
        self.assertEqual(pronounce_number(21.234, lang="es", places=3),
                         "veintiuno punto dos tres cuatro")
        self.assertEqual(pronounce_number(21.234, lang="es", places=4),
                         "veintiuno punto dos tres cuatro")
        self.assertEqual(pronounce_number(21.234, lang="es", places=5),
                         "veintiuno punto dos tres cuatro")
        self.assertEqual(pronounce_number(-21.234, lang="es"),
                         "menos veintiuno punto dos tres")
        self.assertEqual(pronounce_number(-21.234, lang="es", places=1),
                         "menos veintiuno punto dos")
        self.assertEqual(pronounce_number(-21.234, lang="es", places=0),
                         "menos veintiuno")
        self.assertEqual(pronounce_number(-21.234, lang="es", places=3),
                         "menos veintiuno punto dos tres cuatro")
        self.assertEqual(pronounce_number(-21.234, lang="es", places=4),
                         "menos veintiuno punto dos tres cuatro")
        self.assertEqual(pronounce_number(-21.234, lang="es", places=5),
                         "menos veintiuno punto dos tres cuatro")


# def nice_time(dt, lang="it-it", speech=True, use_24hour=False,
#              use_ampm=False):
class TestNiceDateFormat(unittest.TestCase):
    def test_convert_times(self):
        dt = datetime.datetime(2017, 1, 31,
                               13, 22, 3)

        # Verify defaults haven't changed
        self.assertEqual(nice_time(dt, lang="es-es"),
                         nice_time(dt, "es-es", True, False, False))

        self.assertEqual(nice_time(dt, lang="es"),
                         "una veintidos")
        self.assertEqual(nice_time(dt, lang="es", use_ampm=True),
                         "una veintidos de la tarde")
        self.assertEqual(nice_time(dt, lang="es", speech=False), "1:22")
        self.assertEqual(nice_time(dt, lang="es", speech=False,
                                   use_ampm=True), "1:22 PM")
        self.assertEqual(nice_time(dt, lang="es", speech=False,
                                   use_24hour=True), "13:22")
        self.assertEqual(nice_time(dt, lang="es", speech=False,
                                   use_24hour=True, use_ampm=True), "13:22")
        self.assertEqual(nice_time(dt, lang="es", use_24hour=True,
                                   use_ampm=True), "una veintidos")
        self.assertEqual(nice_time(dt, lang="es", use_24hour=True,
                                   use_ampm=False), "una veintidos")

        dt = datetime.datetime(2017, 1, 31,
                               13, 0, 3)
        self.assertEqual(nice_time(dt, lang="es"),
                         "una")
        self.assertEqual(nice_time(dt, lang="es", use_ampm=True),
                         "una de la tarde")
        self.assertEqual(nice_time(dt, lang="es", speech=False),
                         "1:00")
        self.assertEqual(nice_time(dt, lang="es", speech=False,
                                   use_ampm=True), "1:00 PM")
        self.assertEqual(nice_time(dt, lang="es", speech=False,
                                   use_24hour=True), "13:00")
        self.assertEqual(nice_time(dt, lang="es", speech=False,
                                   use_24hour=True, use_ampm=True), "13:00")
        self.assertEqual(nice_time(dt, lang="es", use_24hour=True,
                                   use_ampm=True), "una")
        self.assertEqual(nice_time(dt, lang="es", use_24hour=True,
                                   use_ampm=False), "una")

        dt = datetime.datetime(2017, 1, 31,
                               13, 2, 3)
        self.assertEqual(nice_time(dt, lang="es", use_24hour=True),
                         "una dos")
        self.assertEqual(nice_time(dt, lang="es", use_ampm=True),
                         "una dos de la tarde")
        self.assertEqual(nice_time(dt, lang="es", speech=False),
                         "1:02")
        self.assertEqual(nice_time(dt, lang="es", speech=False,
                                   use_ampm=True), "1:02 PM")
        self.assertEqual(nice_time(dt, lang="es", speech=False,
                                   use_24hour=True), "13:02")
        self.assertEqual(nice_time(dt, lang="es", speech=False,
                                   use_24hour=True, use_ampm=True), "13:02")
        self.assertEqual(nice_time(dt, lang="es", use_24hour=True,
                                   use_ampm=True), "una dos")
        self.assertEqual(nice_time(dt, lang="es", use_24hour=True,
                                   use_ampm=False), "una dos")

        dt = datetime.datetime(2017, 1, 31,
                               0, 2, 3)
        self.assertEqual(nice_time(dt, lang="es"),
                         "medianoche dos")
        self.assertEqual(nice_time(dt, lang="es", use_ampm=True),
                         "medianoche dos")
        self.assertEqual(nice_time(dt, lang="es", speech=False),
                         "12:02")
        self.assertEqual(nice_time(dt, lang="es", speech=False,
                                   use_ampm=True), "12:02 AM")
        self.assertEqual(nice_time(dt, lang="es", speech=False,
                                   use_24hour=True), "00:02")
        self.assertEqual(nice_time(dt, lang="es", speech=False,
                                   use_24hour=True,
                                   use_ampm=True), "00:02")
        self.assertEqual(nice_time(dt, lang="es", use_24hour=True,
                                   use_ampm=True), "medianoche dos")
        self.assertEqual(nice_time(dt, lang="es", use_24hour=True,
                                   use_ampm=False), "medianoche dos")
        
        dt = datetime.datetime(2017, 1, 31,
                               12, 15, 9)
        self.assertEqual(nice_time(dt, lang="es-es"),
                         "mediodía y cuarto")
        self.assertEqual(nice_time(dt, lang="es-es", use_ampm=True),
                         "mediodía y cuarto")
        self.assertEqual(nice_time(dt, lang="es-es", speech=False),
                         "12:15")
        self.assertEqual(nice_time(dt, lang="es-es", speech=False,
                                   use_ampm=True),
                         "12:15 PM")
        self.assertEqual(nice_time(dt, lang="es-es", speech=False,
                                   use_24hour=True),
                         "12:15")
        self.assertEqual(nice_time(dt, lang="es-es", speech=False,
                                   use_24hour=True, use_ampm=True),
                         "12:15")
        self.assertEqual(nice_time(dt, lang="es-es", use_24hour=True,
                                   use_ampm=True),
                         "mediodía quince")
        self.assertEqual(nice_time(dt, lang="es-es", use_24hour=True,
                                   use_ampm=False),
                         "mediodía quince")
        
        dt = datetime.datetime(2017, 1, 31,
                               19, 40, 49)
        self.assertEqual(nice_time(dt, lang="es-es"),
                         "ocho horas menos veinte")
        self.assertEqual(nice_time(dt, lang="es-es", use_ampm=True),
                         "ocho horas menos veinte de la noche")
        self.assertEqual(nice_time(dt, lang="es-es", speech=False),
                         "7:40")
        self.assertEqual(nice_time(dt, lang="es-es", speech=False,
                                   use_ampm=True),
                         "7:40 PM")
        self.assertEqual(nice_time(dt, lang="es-es", speech=False,
                                   use_24hour=True),
                         "19:40")
        self.assertEqual(nice_time(dt, lang="es-es", speech=False,
                                   use_24hour=True, use_ampm=True),
                         "19:40")
        self.assertEqual(nice_time(dt, lang="es-es", use_24hour=True,
                                   use_ampm=True),
                         "diecinueve horas cuarenta")
        self.assertEqual(nice_time(dt, lang="es-es", use_24hour=True,
                                   use_ampm=False),
                         "diecinueve horas cuarenta")
        
        dt = datetime.datetime(2017, 1, 31,
                               1, 15, 00)
        self.assertEqual(nice_time(dt, lang="es-es", use_24hour=True),
                         "una quince")

        dt = datetime.datetime(2017, 1, 31,
                               1, 35, 00)
        self.assertEqual(nice_time(dt, lang="es-es"),
                         "dos horas menos veinticinco")

        dt = datetime.datetime(2017, 1, 31,
                               1, 45, 00)
        self.assertEqual(nice_time(dt, lang="es-es"),
                         "dos horas menos cuarto")

        dt = datetime.datetime(2017, 1, 31,
                               4, 50, 00)
        self.assertEqual(nice_time(dt, lang="es-es"),
                         "cinco horas menos diez")

        dt = datetime.datetime(2017, 1, 31,
                               5, 55, 00)
        self.assertEqual(nice_time(dt, lang="es-es"),
                         "seis horas menos cinco")

        dt = datetime.datetime(2017, 1, 31,
                               5, 30, 00)
        self.assertEqual(nice_time(dt, lang="es-es", use_ampm=True),
                         "cinco horas y media de la mañana")


if __name__ == "__main__":
    unittest.main()
