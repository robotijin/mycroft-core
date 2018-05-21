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
from datetime import datetime

from mycroft.util.parse import get_gender
from mycroft.util.parse import extract_datetime
from mycroft.util.parse import extractnumber
from mycroft.util.parse import normalize


class TestNormalize(unittest.TestCase):
    """
        Test cases for Spanish parsing
    """
    def test_articles_es(self):
        self.assertEqual(normalize("esta es la prueba", lang="es",
                                   remove_articles=True),
                         "esta es prueba")
        self.assertEqual(normalize("y otra prueba", lang="es",
                                   remove_articles=True),
                         "y otra prueba")

    def test_numbers_es(self):
        self.assertEqual(normalize("esto es un uno una", lang="es"),
                         "esto es 1 1 1")
        self.assertEqual(normalize("esto es dos tres prueba", lang="es"),
                         "esto es 2 3 prueba")
        self.assertEqual(normalize("esto es cuatro cinco seis prueba",
                                   lang="es"),
                         "esto es 4 5 6 prueba")
        self.assertEqual(normalize(u"siete mil ocho mil nueve", lang="es"),
                         u"7008 mil 9")
        self.assertEqual(normalize("diez once doce trece catorce quince",
                                   lang="es"),
                         "10 11 12 13 14 15")
        self.assertEqual(normalize(u"dieciséis diecisiete", lang="es"),
                         "16 17")
        self.assertEqual(normalize(u"dieciocho diecinueve", lang="es"),
                         "18 19")
        self.assertEqual(normalize(u"veinte treinta cuarenta", lang="es"),
                         "20 30 40")
        self.assertEqual(normalize(u"treinta y dos caballos", lang="es"),
                         "32 caballos")
        self.assertEqual(normalize(u"cien caballos", lang="es"),
                         "100 caballos")
        self.assertEqual(normalize(u"ciento once caballos", lang="es"),
                         "111 caballos")
        self.assertEqual(normalize(u"habï¿½a cuatrocientas una vacas",
                                   lang="es"),
                         u"habï¿½a 401 vacas")
        self.assertEqual(normalize(u"dos mil", lang="es"),
                         "2000")
        self.assertEqual(normalize(u"dos mil trescientas cuarenta y cinco",
                                   lang="es"),
                         "2345")
        # self.assertEqual(normalize(
        #     u"ciento veintitrés mil cuatrocientas cincuenta y seis",
        #     lang="es"),
        #     "123456")
        self.assertEqual(normalize(
            u"quinientas veinticinco mil", lang="es"),
            "525000")
        self.assertEqual(normalize(
            u"novecientos noventa y nueve mil novecientos noventa y nueve",
            lang="es"),
            "999999")
        self.assertEqual(extractnumber("una copa y media", lang="es"), 1.5)
        self.assertEqual(extractnumber("dos cuartos", lang="es"), 0.5)
        self.assertEqual(extractnumber("un cuarto de copa", lang="es"), 0.25)
        self.assertEqual(extractnumber(u" una veinteava parte", lang="es"),
                         1.0 / 20)
        self.assertEqual(extractnumber("once copas", lang="es"), 11)
        self.assertEqual(extractnumber("quiero una copa", lang="es"), 1)
        self.assertEqual(extractnumber("hace dos horas", lang="es"), 2)
        self.assertEqual(extractnumber("en veintisiete minutos", lang="es"), 27)
        self.assertEqual(extractnumber("esta es la primera prueba", lang="es"),
                         1)
        self.assertEqual(extractnumber("este es el segundo test", lang="es"),
                         2)
        self.assertEqual(extractnumber("este es el tercer test", lang="es"),
                         3)
        self.assertEqual(extractnumber(u"este es el test número 4", lang="es"),
                         4)
        self.assertEqual(extractnumber("un tercio de copa", lang="es"), 1.0 / 3.0)
        self.assertEqual(extractnumber("1/3 copa", lang="es"), 1.0 / 3.0)
        self.assertEqual(extractnumber("1/4 de copa", lang="es"), 0.25)
        self.assertEqual(extractnumber("2/3 de copa", lang="es"), 2.0 / 3.0)
        self.assertEqual(extractnumber("3/4 de copa", lang="es"), 3.0 / 4.0)
        self.assertEqual(extractnumber("1 y 3/4 copas", lang="es"), 1.75)
        self.assertEqual(extractnumber(u"una vigésima parte", lang="es"), 0.05)
        # self.assertEqual(extractnumber(u"4 trigésima parte", lang="es"), 0.13)
        # self.assertEqual(extractnumber(u"4 trigésimas parte", lang="es"), 4.0 / 30.0)
        self.assertEqual(extractnumber(u"dos vigésimas partes", lang="es"), 0.10)
        self.assertEqual(extractnumber("1 y medio", lang="es"), 1.5)
        self.assertEqual(extractnumber("tres cuartos de copa", lang="es"), 3.0 / 4.0)

    def test_gender_es(self):
        self.assertEqual(get_gender("mula", lang="es"), "f")
        self.assertEqual(get_gender("caballo", lang="es"), "m")
        self.assertEqual(get_gender("vacas", "las vacas", lang="es"), "f")
        self.assertEqual(get_gender("perros", "los perros", lang="es"), "m")
        # TODO create exceptions like 'buey' or 'leyes'
        # self.assertEqual(get_gender("buey", "el buey come hierba",
        #                             lang="es"), "m")
        self.assertEqual(get_gender("pescado", "el pescado nada",
                                    lang="es"), "m")
        self.assertEqual(get_gender("tigre", lang="es"), "m")
        self.assertEqual(get_gender("hombres", "estos hombres comen pasta",
                                    lang="es"), "m")
        self.assertEqual(get_gender("puente", "el puente", lang="es"), "m")
        self.assertEqual(get_gender("puente", u"este puente ha caído",
                                    lang="es"), "m")
        self.assertEqual(get_gender("escultora", "esta famosa escultora",
                                    lang="es"), "f")
        self.assertEqual(get_gender("escultor", "este famoso escultor",
                                    lang="es"), "m")
        self.assertEqual(get_gender("escultores", "los escultores renacentistas",
                                    lang="es"), "m")
        self.assertEqual(get_gender("escultoras", "las escultoras modernas",
                                    lang="es"), "f")

    def test_extractdatetime_es(self):
        def extractWithFormat_es(text):
            date = datetime(2017, 6, 27, 0, 0)
            [extractedDate, leftover] = extract_datetime(text, date,
                                                         lang="es-es")
            extractedDate = extractedDate.strftime("%Y-%m-%d %H:%M:%S")
            return [extractedDate, leftover]

        def testExtract_es(text, expected_date, expected_leftover):
            res = extractWithFormat_es(text)
            self.assertEqual(res[0], expected_date)
            self.assertEqual(res[1], expected_leftover)

        def extractWithFormatDate2_es(text):
            date = datetime(2017, 6, 30, 17, 0)
            [extractedDate, leftover] = extract_datetime(text, date,
                                                         lang="es-es")
            extractedDate = extractedDate.strftime("%Y-%m-%d %H:%M:%S")
            return [extractedDate, leftover]

        def testExtractDate2_es(text, expected_date, expected_leftover):
            res = extractWithFormatDate2_es(text)
            self.assertEqual(res[0], expected_date)
            self.assertEqual(res[1], expected_leftover)

        def extractWithFormatNoDate_es(text):
            [extractedDate, leftover] = extract_datetime(text, lang="es-es")
            extractedDate = extractedDate.strftime("%Y-%m-%d %H:%M:%S")
            return [extractedDate, leftover]

        def testExtractNoDate_es(text, expected_date, expected_leftover):
            res = extractWithFormatNoDate_es(text)
            self.assertEqual(res[0], expected_date)
            self.assertEqual(res[1], expected_leftover)

        testExtract_es("Planificar la emboscada en 5 días",
                       "2017-07-02 00:00:00", "planificar emboscada")
        testExtract_es("Qué tiempo hará pasado mañana ?",
                       "2017-06-29 00:00:00", "qué tiempo hará")
        testExtract_es("Pon un recordatorio a las 10:45 de la tarde",
                       "2017-06-27 22:45:00", "pon un recordatorio")
        testExtract_es("Qué tiempo está previsto para el viernes por la mañana?",
                       "2017-06-30 08:00:00", "qué tiempo está previsto")
        # In spanish, "tomorrow" and "morning" shares the same word, so we need to
        # evaluate previous words to see if there are an article "morning" or not
        # which will mean "tomorrow"
        # testExtract_es("Qué tiempo hará mañana ?",
        #                "2017-06-28 00:00:00", "qué tiempo hará")
        testExtract_es("recuérdame llamar a mamá en 8 semanas y 2 días",
                       "2017-08-24 00:00:00", "recuérdame llamar mamá y")
        testExtract_es("Reproducir música Beyonce 2 días desde el viernes",
                       "2017-07-02 00:00:00", "reproducir música beyonce")
        # La siguiente frase, aunque signigique lo mismo, no la entiende
        # testExtract_es("Reproducir música Beyonce 2 días después de este viernes",
        #                "2017-07-02 00:00:00", "reproducir música beyonce")
        testExtract_es("Empezar la invasión a las 15:45 del jueves",
                       "2017-06-29 15:45:00", "empezar invasión")
        # testExtract_es("El lunes reserva un pastel en la panadería",
        #                "2017-07-03 00:00:00", "reserva pastel en panadería")
        testExtract_es("Reproduce el Cumpleaños Feliz en 5 años",
                       "2022-06-27 00:00:00", "reproduce cumpleaño feliz")
        # Esta otra frase, con el mismo significado que la anterior, no la 
        # reconoce. Además, a "cumpleaños" le quita la "s" del final
        # testExtract_es("Reproduce el Cumpleaños Feliz de aquí a 5 años",
        #                "2022-06-27 00:00:00", "reproduce cumpleaño feliz")
        # testExtract_es("Hacer un Skype a mamá el próximo jueves a las 12:45",
        #                "2017-07-06 12:45:00", "hacer un skype")
        # En la siguiente frase, no entiende "el próximo", si no "el siguiente"
        testExtract_es("Qué tiempo hará el siguiente jueves?",
                       "2017-07-06 00:00:00", "qué tiempo hará")
        testExtract_es("Qué tiempo hará el viernes por la mañana ?",
                       "2017-06-30 08:00:00", "qué tiempo hará")
        # En castellano no hay "evening", pero "tarde noche" debería entenderse
        # testExtract_es("Qué tiempo hará el viernes por la tarde noche",
        #                "2017-06-30 19:00:00", "qué tiempo hará")
        testExtract_es("Qué tiempo hará el viernes por la tarde",
                       "2017-06-30 15:00:00", "qué tiempo hará")
        testExtract_es("recuérdame llamar a mamá el 3 de agosto",
                       "2017-08-03 00:00:00", "recuérdame llamar mamá")
        # Por algún motivo, en la siguiente frase entiende "julyy 14"
        # testExtract_es("Compra fuegos artificiales el 14 de julio",
        #                "2017-07-14 00:00:00", "compra fuegos artificiales")
        # testExtract_es("Qué tiempo hará 2 semanas después del viernes?",
        #                "2017-07-14 00:00:00", "qué tiempo hará")
        testExtract_es("Qué tiempo hará el miércoles a las 7",
                       "2017-06-28 07:00:00", "qué tiempo hará")
        testExtract_es("Crea una cita a las 12:45 el siguiente jueves",
                       "2017-07-06 12:45:00", "crea cita")
        testExtract_es("Qué tiempo hará este jueves?",
                       "2017-06-29 00:00:00", "qué tiempo hará")
        # Hay que hacer algo con las "y"
        testExtract_es("Organiza una visita 2 semanas y 6 días desde el sábado",
                       "2017-07-21 00:00:00", "organiza visita y")
        # tenemos que interpretar formatos como "3h 45" o "3 horas 45"?
        testExtract_es("Inicia la invasión a las 3 45 del jueves",
                       "2017-06-29 03:45:00", "inicia invasión")
        testExtract_es("Inicia la invasión a las 20 horas del jueves",
                       "2017-06-29 20:00:00", "inicia invasión")
        testExtract_es("La fiesta empieza el jueves a las 8 de la tarde",
                       "2017-06-29 20:00:00", "la fiesta empieza")
        # esta frase que sigue, poniendo el día después de la hora, no la entiende
        # testExtract_es("Inicia la invasión a las 4 de la tarde del jueves",
        #                "2017-06-29 16:00:00", "inicia invasión")
        # testExtract_es("Inicia la invasión el jueves a mediodía",
        #                "2017-06-29 12:00:00", "inicia invasión")
        # testExtract_es("Inicia la invasión el jeudi à minuit",
        #                "2017-06-29 00:00:00", "inicia invasión")
        # testExtract_es("Inicia la invasión el jeudi à dix-sept heures",
        #                "2017-06-29 17:00:00", "inicia invasión")
        # testExtract_es("rappelle-moi de me réveiller dans 4 années",
        #                "2021-06-27 00:00:00", "rappelle-moi me réveiller")
        # testExtract_es("rappelle-moi de me réveiller dans 4 ans et 4 jours",
        #                "2021-07-01 00:00:00", "rappelle-moi me réveiller")
        # testExtract_es("Qué tiempo hará 3 jours après demain ?",
        #                "2017-07-01 00:00:00", "qué tiempo hará")
        # testExtract_es("3 décembre",
        #                "2017-12-03 00:00:00", "")
        # testExtract_es("retrouvons-nous à 8:00 ce soir",
        #                "2017-06-27 20:00:00", "retrouvons-nous")
        # testExtract_es("retrouvons-nous demain à minuit et demi",
        #                "2017-06-28 00:30:00", "retrouvons-nous")
        # testExtract_es("retrouvons-nous à midi et quart",
        #                "2017-06-27 12:15:00", "retrouvons-nous")
        # testExtract_es("retrouvons-nous à midi moins le quart",
        #                "2017-06-27 11:45:00", "retrouvons-nous")
        # testExtract_es("retrouvons-nous à midi moins dix",
        #                "2017-06-27 11:50:00", "retrouvons-nous")
        # testExtract_es("retrouvons-nous à midi dix",
        #                "2017-06-27 12:10:00", "retrouvons-nous")
        # testExtract_es("retrouvons-nous à minuit moins 23",
        #                "2017-06-27 23:37:00", "retrouvons-nous")
        # testExtract_es("mangeons à 3 heures moins 23 minutes",
        #                "2017-06-27 02:37:00", "mangeons")
        # testExtract_es("mangeons aussi à 4 heures moins le quart du matin",
        #                "2017-06-27 03:45:00", "mangeons aussi")
        # testExtract_es("mangeons encore à minuit moins le quart",
        #                "2017-06-27 23:45:00", "mangeons encore")
        # testExtract_es("buvons à 4 heures et quart",
        #                "2017-06-27 04:15:00", "buvons")
        # testExtract_es("buvons également à 18 heures et demi",
        #                "2017-06-27 18:30:00", "buvons également")
        # testExtract_es("dormons à 20 heures moins le quart",
        #                "2017-06-27 19:45:00", "dormons")
        # testExtract_es("buvons le dernier verre à 10 heures moins 12 du soir",
        #                "2017-06-27 21:48:00", "buvons dernier verre")
        # testExtract_es("s'échapper de l'île à 15h45",
        #                "2017-06-27 15:45:00", "s'échapper île")
        # testExtract_es("s'échapper de l'île à 3h45min de l'après-midi",
        #                "2017-06-27 15:45:00", "s'échapper île")
        # testExtract_es("décale donc ça à 3h48min cet après-midi",
        #                "2017-06-27 15:48:00", "décale donc ça")
        # testExtract_es("construire un bunker à 9h42min du matin",
        #                "2017-06-27 09:42:00", "construire 1 bunker")
        # testExtract_es("ou plutôt à 9h43 ce matin",
        #                "2017-06-27 09:43:00", "ou plutôt")
        # testExtract_es("faire un feu à 8h du soir",
        #                "2017-06-27 20:00:00", "faire 1 feu")
        # testExtract_es("faire la fête jusqu'à 18h cette nuit",
        #                "2017-06-27 18:00:00", "faire fête jusqu'à")
        # testExtract_es("cuver jusqu'à 4h cette nuit",
        #                "2017-06-27 04:00:00", "cuver jusqu'à")
        # testExtract_es("réveille-moi dans 20 secondes aujourd'hui",
        #                "2017-06-27 00:00:20", "réveille-moi")
        # testExtract_es("réveille-moi dans 33 minutes",
        #                "2017-06-27 00:33:00", "réveille-moi")
        # testExtract_es("tais-toi dans 12 heures et 3 minutes",
        #                "2017-06-27 12:03:00", "tais-toi")
        # testExtract_es("ouvre-la dans 1 heure 3",
        #                "2017-06-27 01:03:00", "ouvre-la")
        # testExtract_es("ferme-la dans 1 heure et quart",
        #                "2017-06-27 01:15:00", "ferme-la")
        # testExtract_es("scelle-la dans 1 heure et demi",
        #                "2017-06-27 01:30:00", "scelle-la")
        # testExtract_es("zippe-la dans 2 heures moins 12",
        #                "2017-06-27 01:48:00", "zippe-la")
        # testExtract_es("soude-la dans 3 heures moins le quart",
        #                "2017-06-27 02:45:00", "soude-la")
        # testExtract_es("mange la semaine prochaine",
        #                "2017-07-04 00:00:00", "mange")
        # testExtract_es("bois la semaine dernière",
        #                "2017-06-20 00:00:00", "bois")
        # testExtract_es("mange le mois prochain",
        #                "2017-07-27 00:00:00", "mange")
        # testExtract_es("bois le mois dernier",
        #                "2017-05-27 00:00:00", "bois")
        # testExtract_es("mange l'an prochain",
        #                "2018-06-27 00:00:00", "mange")
        # testExtract_es("bois l'année dernière",
        #                "2016-06-27 00:00:00", "bois")
        # testExtract_es("reviens à lundi dernier",
        #                "2017-06-26 00:00:00", "reviens")
        # testExtract_es("capitule le 8 mai 1945",
        #                "1945-05-08 00:00:00", "capitule")
        # testExtract_es("rédige le contrat 3 jours après jeudi prochain",
        #                "2017-07-09 00:00:00", "rédige contrat")
        # testExtract_es("signe le contrat 2 semaines après jeudi dernier",
        #                "2017-07-06 00:00:00", "signe contrat")
        # testExtract_es("lance le four dans un quart d'heure",
        #                "2017-06-27 00:15:00", "lance four")
        # testExtract_es("enfourne la pizza dans une demi-heure",
        #                "2017-06-27 00:30:00", "enfourne pizza")
        # testExtract_es("arrête le four dans trois quarts d'heure",
        #                "2017-06-27 00:45:00", "arrête four")
        # testExtract_es("mange la pizza dans une heure",
        #                "2017-06-27 01:00:00", "mange pizza")
        # testExtract_es("bois la bière dans 2h23",
        #                "2017-06-27 02:23:00", "bois bière")
        # testExtract_es("faire les plantations le 3ème jour de mars",
        #                "2018-03-03 00:00:00", "faire plantations")
        # testExtract_es("récolter dans 10 mois",
        #                "2018-04-27 00:00:00", "récolter")
        # testExtract_es("point 6a: dans 10 mois",
        #                "2018-04-27 06:00:00", "point")
        # testExtract_es("l'après-midi démissionner à 4:59",
        #                "2017-06-27 16:59:00", "démissionner")
        # testExtract_es("cette nuit dormir",
        #                "2017-06-27 02:00:00", "dormir")
        # testExtract_es("ranger son bureau à 1700 heures",
        #                "2017-06-27 17:00:00", "ranger son bureau")

        # testExtractDate2_es("range le contrat 2 semaines après lundi",
        #                     "2017-07-17 00:00:00", "range contrat")
        # testExtractDate2_es("achète-toi de l'humour à 15h",
        #                     "2017-07-01 15:00:00", "achète-toi humour")
        # testExtractNoDate_es("tais-toi aujourd'hui",
        #                      datetime.now().strftime("%Y-%m-%d") + " 00:00:00",
        #                      "tais-toi")
        # self.assertEqual(extract_datetime("", lang="es-es"), None)
        # self.assertEqual(extract_datetime("phrase inutile", lang="es-es"),
        #                  None)
        # self.assertEqual(extract_datetime(
        #     "apprendre à compter à 37 heures", lang="es-es"), None)


if __name__ == "__main__":
    unittest.main()
