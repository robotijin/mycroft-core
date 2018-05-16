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
""" 
Format functions for castillian (es-es)

"""

from mycroft.util.lang.format_common import convert_to_mixed_fraction

NUM_STRING_ES = {
    0: 'cero',
    1: 'uno',
    2: 'dos',
    3: 'tres',
    4: 'cuatro',
    5: 'cinco',
    6: 'seis',
    7: 'siete',
    8: 'ocho',
    9: 'nueve',
    10: 'diez',
    11: 'once',
    12: 'doce',
    13: 'trece',
    14: 'catorce',
    15: 'quince',
    16: 'dieciseis',
    17: 'diecisete',
    18: 'dieciocho',
    19: 'diecinueve',
    20: 'veinte',
    30: 'treinta',
    40: 'cuarenta',
    50: 'cincuenta',
    60: 'sesenta',
    70: 'setenta',
    80: 'ochenta',
    90: 'noventa'
}

FRACTION_STRING_ES = {
    2: 'medio',
    3: 'tercio',
    4: 'cuarto',
    5: 'quinto',
    6: 'sexto',
    7: 'séptimo',
    8: 'octavo',
    9: 'noveno',
    10: 'décimo',
    11: 'onceavo',
    12: 'doceavo',
    13: 'treceavo',
    14: 'catorceavo',
    15: 'quinceavo',
    16: 'dieciseisavo',
    17: 'diecisieteavo',
    18: 'dieciochoavo',
    19: 'diecinueveavo',
    20: 'veinteavo'
}


def nice_number_es(number, speech, denominators):
    """ Spanish helper for nice_number

    This function formats a float to human understandable functions. Like
    4.5 becomes "4 y medio" for speech and "4 1/2" for text

    Args:
        number (int or float): the float to format
        speech (bool): format for speech (True) or display (False)
        denominators (iter of ints): denominators to use, default [1 .. 20]
    Returns:
        (str): The formatted string.
    """
    strNumber = ""
    whole = 0
    num = 0
    den = 0

    result = convert_to_mixed_fraction(number, denominators)

    if not result:
        # Give up, just represent as a 3 decimal number
        whole = round(number, 3)
    else:
        whole, num, den = result

    if not speech:
        if num == 0:
            strNumber = '{:,}'.format(whole)
            strNumber = strNumber.replace(",", " ")
            strNumber = strNumber.replace(".", ",")
            return strNumber
        else:
            return '{} {}/{}'.format(whole, num, den)
    else:
        if num == 0:
            # if the number is not a fraction, nothing to do
            strNumber = str(whole)
            strNumber = strNumber.replace(".", ",")
            return strNumber
        den_str = FRACTION_STRING_ES[den]
        # if it is not an integer
        if whole == 0:
            # if there is no whole number
            if num == 1:
                # if numerator is 1, return "un medio", for example
                strNumber = 'un {}'.format(den_str)
            else:
                # else return "cuatro tercios", for example
                strNumber = '{} {}'.format(num, den_str)
        elif num == 1:
            # if there is a whole number and numerator is 1
            if den == 2:
                # if denominator is 2, return "1 y medio", for example
                strNumber = '{} y {}'.format(whole, den_str)
            else:
                # else return "1 y 1 tercio", for example
                strNumber = '{} y 1 {}'.format(whole, den_str)
        else:
            # else return "2 y 3 cuarto", for example
            strNumber = '{} y {} {}'.format(whole, num, den_str)
        if num > 1 and den != 3:
            # if the numerator is greater than 1 and the denominator
            # is not 3 ("tercio"), add an s for plural
            strNumber += 's'

    return strNumber


def pronounce_number_es(num, places=2):
    """
    Convert a number to it's spoken equivalent

    For example, '5.2' would return 'cinco punto dos'

    Args:
        num(float or int): the number to pronounce (under 100)
        places(int): maximum decimal places to speak
    Returns:
        (str): The pronounced number
    """
    if abs(num) >= 100:
        # TODO: Support for numbers over 100
        return str(num)

    result = ""
    if num < 0:
        result = "menos "
    num = abs(num)

    # if num > 16:
    #     tens = int(num-int(num) % 10)
    #     ones = int(num-tens)
    #     if ones != 0:
    #         if tens > 10 and tens <= 60 and int(num-tens) == 1:
    #             result += NUM_STRING_FR[tens] + "-et-" + NUM_STRING_FR[ones]
    #         elif num == 71:
    #             result += "soixante-et-onze"
    #         elif tens == 70:
    #             result += NUM_STRING_FR[60] + "-"
    #             if ones < 7:
    #                 result += NUM_STRING_FR[10 + ones]
    #             else:
    #                 result += NUM_STRING_FR[10] + "-" + NUM_STRING_FR[ones]
    #         elif tens == 90:
    #             result += NUM_STRING_FR[80] + "-"
    #             if ones < 7:
    #                 result += NUM_STRING_FR[10 + ones]
    #             else:
    #                 result += NUM_STRING_FR[10] + "-" + NUM_STRING_FR[ones]
    #         else:
    #             result += NUM_STRING_FR[tens] + "-" + NUM_STRING_FR[ones]
    #     else:
    #         if num == 80:
    #             result += "quatre-vingts"
    #         else:
    #             result += NUM_STRING_FR[tens]
    # else:
    #     result += NUM_STRING_FR[int(num)]
    if 20 <= num <= 29: # 21-29 has special pronunciation
        tens = int(num-int(num) % 10)
        ones = int(num - tens)
        result += NUM_STRING_ES[tens]
        if ones > 0:
            result = result[:-1]  
            result += "i" + NUM_STRING_ES[ones]
    elif num >= 30:  # from 30 onwards
        tens = int(num-int(num) % 10)
        ones = int(num - tens)
        result += NUM_STRING_ES[tens]
        if ones > 0:
            result += " y " + NUM_STRING_ES[ones]
    else:
        result += NUM_STRING_ES[int(num)]    

    # Deal with decimal part
    if not num == int(num) and places > 0:
        result += " punto"
        place = 10
        while int(num*place) % 10 > 0 and places > 0:
            result += " " + NUM_STRING_ES[int(num*place) % 10]
            place *= 10
            places -= 1
    return result


def nice_time_es(dt, speech=True, use_24hour=False, use_ampm=False):
    """
    Format a time to a comfortable human format

    For example, generate 'cinq heures trente' for speech or '5:30' for
    text display.

    Args:
        dt (datetime): date to format (assumes already in local timezone)
        speech (bool): format for speech (default/True) or display (False)=Fal
        use_24hour (bool): output in 24-hour/military or 12-hour format
        use_ampm (bool): include the am/pm for 12-hour format
    Returns:
        (str): The formatted time string
    """
    if use_24hour:
        # e.g. "03:01" or "14:22"
        string = dt.strftime("%H:%M")
    else:
        if use_ampm:
            # e.g. "3:01 AM" or "2:22 PM"
            string = dt.strftime("%I:%M %p")
        else:
            # e.g. "3:01" or "2:22"
            string = dt.strftime("%I:%M")
        if string[0] == '0':
            string = string[1:]  # strip leading zeros

    if not speech:
        return string

    # Generate a speakable version of the time
    speak = ""
    if use_24hour:

        # "13 heures trente"
        if dt.hour == 0:
            speak += "medianoche"
        elif dt.hour == 12:
            speak += "mediodía"
        elif dt.hour == 1 or dt.hour == 13:
            speak += "una"
        else:
            speak += pronounce_number_es(dt.hour) + " horas"

        if dt.minute != 0:
            speak += " " + pronounce_number_es(dt.minute)

    else:
        # Prepare for "tres horas menos cuarto" ??
        if dt.minute == 35:
            minute = -25
            hour = dt.hour + 1
        elif dt.minute == 40:
            minute = -20
            hour = dt.hour + 1
        elif dt.minute == 45:
            minute = -15
            hour = dt.hour + 1
        elif dt.minute == 50:
            minute = -10
            hour = dt.hour + 1
        elif dt.minute == 55:
            minute = -5
            hour = dt.hour + 1
        else:
            minute = dt.minute
            hour = dt.hour

        if hour == 0:
            speak += "medianoche"
        elif hour == 12:
            speak += "mediodía"
        elif hour == 1 or hour == 13:
            speak += "una"
        elif hour < 13:
            speak = pronounce_number_es(hour) + " horas"
        else:
            speak = pronounce_number_es(hour-12) + " horas"

        if minute != 0:
            if minute == 15:
                speak += " y cuarto"
            elif minute == 30:
                speak += " y media"
            elif minute == -15:
                speak += " menos cuarto"
            else:
                speak += " " + pronounce_number_es(minute)

        if use_ampm:
            if hour > 17:
                speak += " de la noche"
            elif hour > 12:
                speak += " de la tarde"
            elif hour > 0 and hour < 12:
                speak += " de la mañana"

    return speak
