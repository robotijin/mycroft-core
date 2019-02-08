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
        self.assertEqual(
            normalize("esta es la prueba", lang="es", remove_articles=True),
            "esta es prueba"
        )
        self.assertEqual(
            normalize("este es el exámen", lang="es", remove_articles=True),
            "este es exámen"
        )
        self.assertEqual(
            normalize("estos son los carácteres", lang="es", remove_articles=True),
            "estos son carácteres"
        )
        self.assertEqual(
            normalize("y otra prueba", lang="es", remove_articles=True),
            "y otra prueba"
        )

    def test_numbers_es(self):
        self.assertEqual(
            normalize("esto es un uno una", lang="es"),
            "esto es 1 1 1"
        )
        self.assertEqual(
            normalize("esto es dos tres prueba", lang="es"),
            "esto es 2 3 prueba"
        )
        self.assertEqual(
            normalize("esto es cuatro cinco seis prueba", lang="es"),
            "esto es 4 5 6 prueba"
        )
        self.assertEqual(
            normalize("siete mil ocho mil nueve", lang="es"),
            "7008 mil 9"
        )
        self.assertEqual(
            normalize("diez once doce trece catorce quince", lang="es"),
            "10 11 12 13 14 15"
        )
        self.assertEqual(normalize("dieciséis diecisiete", lang="es"), "16 17")
        self.assertEqual(normalize("dieciocho diecinueve", lang="es"), "18 19")
        self.assertEqual(normalize("veinte treinta cuarenta", lang="es"),
            "20 30 40"
        )
        self.assertEqual(normalize("treinta y dos caballos", lang="es"),
            "32 caballos"
        )
        self.assertEqual(normalize("cien caballos", lang="es"),
            "100 caballos"
        )
        self.assertEqual(normalize("ciento once caballos", lang="es"),
            "111 caballos"
        )
        self.assertEqual(normalize("había cuatrocientas una vacas", lang="es"),
            "había 401 vacas"
        )
        self.assertEqual(normalize("dos mil", lang="es"), "2000")
        self.assertEqual(
            normalize("dos mil trescientas cuarenta y cinco", lang="es"),
            "2345"
        )
        self.assertEqual(
            normalize(
                "ciento veintitrés mil cuatrocientas cincuenta y seis",
                lang="es"
            ),
            "123456"
        )
        self.assertEqual(
            normalize("quinientas veinticinco mil", lang="es"),
            "525000"
        )
        self.assertEqual(
            normalize(
                "novecientos noventa y nueve mil novecientos noventa y nueve",
                lang="es"
            ),
            "999999"
        )
        self.assertEqual(extractnumber("una copa y media", lang="es"), 1.5)
        self.assertEqual(extractnumber("dos cuartos", lang="es"), 0.5)
        self.assertEqual(extractnumber("un cuarto de copa", lang="es"), 0.25)
        self.assertEqual(
            extractnumber("una veinteava parte", lang="es"),
            1.0 / 20
        )
        self.assertEqual(extractnumber("once copas", lang="es"), 11)
        self.assertEqual(extractnumber("quiero una copa", lang="es"), 1)
        self.assertEqual(extractnumber("hace dos horas", lang="es"), 2)
        self.assertEqual(extractnumber("en veintisiete minutos", lang="es"), 27)
        self.assertEqual(
            extractnumber("esta es la primera prueba", lang="es"),
            1
        )
        self.assertEqual(extractnumber("este es el segundo test", lang="es"), 2)
        self.assertEqual(extractnumber("este es el tercer test", lang="es"), 3)
        self.assertEqual(
            extractnumber("este es el test número 4", lang="es"),
            4
        )
        self.assertEqual(
            extractnumber("un tercio de copa", lang="es"),
            1.0 / 3.0
        )
        self.assertEqual(extractnumber("1/3 copa", lang="es"), 1.0 / 3.0)
        self.assertEqual(extractnumber("1/4 de copa", lang="es"), 0.25)
        self.assertEqual(extractnumber("2/3 de copa", lang="es"), 2.0 / 3.0)
        self.assertEqual(extractnumber("3/4 de copa", lang="es"), 3.0 / 4.0)
        self.assertEqual(extractnumber("1 y 3/4 copas", lang="es"), 1.75)
        self.assertEqual(extractnumber("una vigésima parte", lang="es"), 0.05)
        self.assertEqual(
            extractnumber("1 trigésima parte", lang="es"),
            1.0 / 30.0
        )
        self.assertEqual(
            extractnumber("4 trigésimas partes", lang="es"),
            (1.0 / 30.0) * 4
        )
        self.assertEqual(extractnumber("dos vigésimas partes", lang="es"), 0.10)
        self.assertEqual(extractnumber("1 y medio", lang="es"), 1.5)
        self.assertEqual(
            extractnumber("tres cuartos de copa", lang="es"),
            3.0 / 4.0
        )

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
        self.assertEqual(get_gender("puente", "este puente ha caído",
                                    lang="es"), "m")
        self.assertEqual(get_gender("escultora", "esta famosa escultora",
                                    lang="es"), "f")
        self.assertEqual(get_gender("escultor", "este famoso escultor",
                                    lang="es"), "m")
        self.assertEqual(
            get_gender("escultores", "los escultores renacentistas", lang="es"),
            "m"
        )
        self.assertEqual(
            get_gender("escultoras", "las escultoras modernas", lang="es"),
            "f"
        )

    def test_extractdatetime_es(self):
        def extractWithFormat_es(text):
            date = datetime(2017, 6, 27, 0, 0)
            # if text == "Inicia la invasión a las 4 de la tarde del jueves":
            #    import pdb; pdb.set_trace()
            [extractedDate, leftover] = extract_datetime(
                text,
                date,
                lang="es-es"
            )
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

        testExtract_es(
            "Planificar la emboscada en 5 días",
            "2017-07-02 00:00:00",
            "planificar emboscada"
        )
        testExtract_es(
            "Qué tiempo hará pasado mañana ?",
            "2017-06-29 00:00:00",
            "qué tiempo hará"
        )
        testExtract_es(
            "Pon un recordatorio a las 10:45 de la tarde",
            "2017-06-27 22:45:00",
            "pon recordatorio"
        )
        #testExtract_es(
        #    "Qué tiempo está previsto para el viernes por la mañana?",
        #    "2017-06-30 08:00:00",
        #    "qué tiempo está previsto"
        #)
        # In spanish, "tomorrow" and "morning" shares the same word, so we need to
        # evaluate previous words to see if there are an article "morning" or not
        # which will mean "tomorrow"
        testExtract_es(
            "Qué tiempo hará mañana?",
            "2017-06-28 00:00:00",
            "qué tiempo hará"
        )
        testExtract_es("recuérdame llamar a mamá en 8 semanas y 2 días",
                       "2017-08-24 00:00:00", "recuérdame llamar mamá y")
        testExtract_es("Reproducir música Beyonce 2 días desde el viernes",
                       "2017-07-02 00:00:00", "reproducir música beyonce")
        # La siguiente frase, aunque signigique lo mismo, no la entiende
        testExtract_es(
           "Reproducir música Beyonce este domingo",
           "2017-07-02 00:00:00",
           "reproducir música beyonce"
        )
        testExtract_es("Empezar la invasión a las 15:45 del jueves",
                       "2017-06-29 15:45:00", "empezar invasión")
        testExtract_es("Qué día es mañana",
                       "2017-06-28 00:00:00", "qué día es")
        testExtract_es(
            "El lunes reserva un pastel en la panadería",
            "2017-07-03 00:00:00",
            "reserva pastel en panadería"
        )
        testExtract_es("Reproduce el Cumpleaños Feliz en 5 años",
                       "2022-06-27 00:00:00", "reproduce cumpleaño feliz")
        # Esta otra frase, con el mismo significado que la anterior, no la
        # reconoce. Además, a "cumpleaños" le quita la "s" del final
        # testExtract_es("Reproduce el Cumpleaños Feliz de aquí a 5 años",
        #                "2022-06-27 00:00:00", "reproduce cumpleaño feliz")
        testExtract_es("Skype con mamá el siguiente jueves a las 12:45",
                       "2017-07-06 12:45:00", "skype con mamá")
        # En la siguiente frase, no entiende "el próximo", si no "el siguiente"
        testExtract_es("Qué tiempo hará el siguiente jueves?",
                       "2017-07-06 00:00:00", "qué tiempo hará")
        testExtract_es("Qué tiempo hará este viernes a las 8 ?",
                      "2017-06-30 08:00:00", "qué tiempo hará")
        # En castellano no hay "evening", pero "tarde noche" debería entenderse
        # testExtract_es("Qué tiempo hará el viernes por la tarde noche",
        #                "2017-06-30 19:00:00", "qué tiempo hará")
        testExtract_es(
            "Qué tiempo hará el viernes por la tarde",
            "2017-06-30 15:00:00",
            "qué tiempo hará"
        )
        testExtract_es("recuérdame llamar a mamá el 3 de agosto",
                       "2017-08-03 00:00:00", "recuérdame llamar mamá")

        testExtract_es("Compra fuegos artificiales el 15 de julio",
                       "2017-07-15 00:00:00", "compra fuegos artificiales")
        # testExtract_es("Qué tiempo hará 2 semanas después del viernes?",
        #                "2017-07-14 00:00:00", "qué tiempo hará")
        testExtract_es(
            "Qué tiempo hará el miércoles a las 7",
            "2017-06-28 07:00:00",
            "qué tiempo hará"
        )
        testExtract_es(
            "Crea una cita a las 12:45 el siguiente jueves",
            "2017-07-06 12:45:00",
            "crea cita"
        )
        testExtract_es(
            "Qué tiempo hará este jueves?",
            "2017-06-29 00:00:00",
            "qué tiempo hará"
        )
        # Hay que hacer algo con las "y"
        testExtract_es(
            "Organiza una visita 2 semanas y 6 días desde el sábado",
            "2017-07-21 00:00:00",
            "organiza visita y"
        )
        # tenemos que interpretar formatos como "3h 45" o "3 horas 45"?
        testExtract_es(
            "Inicia la invasión a las 3 45 del jueves",
            "2017-06-29 03:45:00",
            "inicia invasión"
        )
        testExtract_es(
            "Inicia la invasión a las 20 horas del jueves",
            "2017-06-29 20:00:00",
            "inicia invasión"
        )
        testExtract_es(
            "La fiesta empieza el jueves a las 8 de la tarde",
            "2017-06-29 20:00:00",
            "fiesta empieza"
        )
        testExtract_es(
            "Inicia la invasión a las 4 de la tarde del jueves",
            "2017-06-29 16:00:00",
            "inicia invasión"
        )
        # En el siguiente caso, entiende medio día (half day), no mediodía (noon)
        testExtract_es(
           "Inicia la invasión el jueves a medio día",
           "2017-06-29 12:00:00",
           "inicia invasión"
        )
        testExtract_es("Inicia la invasión el jueves a media noche",
                       "2017-06-29 00:00:00", "inicia invasión")
        testExtract_es("Inicia la invasión el jueves a media tarde",
                       "2017-06-29 17:00:00", "inicia invasión")
        testExtract_es("despiértame en 4 años",
                       "2021-06-27 00:00:00", "despiértame")
        testExtract_es("despiértame en 4 años y 4 días",
                       "2021-07-01 00:00:00", "despiértame y")
        # testExtract_es("Qué tiempo hará 3 días después de mañana ?",
        #                "2017-07-01 00:00:00", "qué tiempo hará")
        testExtract_es("3 diciembre",
                       "2017-12-03 00:00:00", "")
        testExtract_es("nos vemos a las 8:00 de esta noche.",
                       "2017-06-27 20:00:00", "nos vemos")
        # en castellano se dice las doce y media, no cero y media                       
        # testExtract_es("nos vemos mañana a las doce y media de la noche",
        #                "2017-06-28 00:30:00", "nos vemos")
        # testExtract_es("nos vemos a las doce y media",
        #                "2017-06-27 12:30:00", "nos vemos")
        # testExtract_es("nos vemos a las doce menos cuarto",
        #                "2017-06-27 11:45:00", "nos vemos")
        # testExtract_es("nos vemos a las doce menos diez",
        #                "2017-06-27 11:50:00", "nos vemos")
        # testExtract_es("nos vemos a las doce y diez",
        #                "2017-06-27 12:10:00", "nos vemos")
        # testExtract_es("nos vemos a las once y treinta y siete de la noche",
        #                "2017-06-27 23:37:00", "nos vemos")
        # testExtract_es("comemos a las 3 horas menos 23 minutoss",
        #                "2017-06-27 02:37:00", "comemos")
        # testExtract_es("comemos a las cuatro menos cuarto de la madrugada",
        #                "2017-06-27 03:45:00", "comemos")
        # testExtract_es("beberé a las cuatro y cuarto de la madrugada",
        #                "2017-06-27 04:15:00", "beberé")
        # testExtract_es("beberé a las seis y media de la tarde",
        #                "2017-06-27 18:30:00", "beberé")
        # testExtract_es("dormiré a las ocho menos cuarto de la tarde noche",
        #                "2017-06-27 19:45:00", "dormiré")
        # testExtract_es("beberé el último trago a las 10 de la noche.",
        #                "2017-06-27 22.00:00", "beberé último trago")
        testExtract_es("escapada de la isla a las 15 45",
                       "2017-06-27 15:45:00", "escapada isla")
        testExtract_es("escapada de la isla a las 3:45 de la tarde",
                       "2017-06-27 15:45:00", "escapada isla")
        testExtract_es("así que muévelo a las 3:48 de la tarde.",
                       "2017-06-27 15:48:00", "así que muévelo")
        testExtract_es("construir un búnker a las 9:42 am",
                       "2017-06-27 09:42:00", "construir búnker")
        # testExtract_es("o más bien a las 9:43 de la mañana",
        #                "2017-06-27 09:43:00", "o más bien")
        testExtract_es("hacer una hoguera a las 8:00 de la noche",
                       "2017-06-27 20:00:00", "hacer hoguera")
        # testExtract_es("fiesta hasta las 18h de esta tarde",
        #                "2017-06-27 18:00:00", "fiesta hasta")
        testExtract_es("dormir hasta las 4 de la madrugada",
                       "2017-06-27 04:00:00", "dormir hasta")
        # testExtract_es("Despiértame dentro de 20 segundos",
        #                "2017-06-27 00:00:20", "Despiértame")
        # testExtract_es("Despiértame en 33 minutos.",
        #                "2017-06-27 00:33:00", "Despiértame")
        # testExtract_es("Cállate de aquí as 12 horas y 3 minutos",
        #                "2017-06-27 12:03:00", "Cállate")
        # testExtract_es("ábrelo a la una y tres",
        #                "2017-06-27 01:03:00", "ábrelo")
        # testExtract_es("Cállate en una hora y cuarto.",
        #                "2017-06-27 01:15:00", "Cállate")
        # testExtract_es("sellarlo dentro de una hora y media",
        #                "2017-06-27 01:30:00", "sellarlo")
        # testExtract_es("apaga en dos horas menos 12.",
        #                "2017-06-27 01:48:00", "apaga")
        # testExtract_es("Soldarlo en 2 horas y 45",
        #                "2017-06-27 02:45:00", "Soldarlo")
        # testExtract_es("come la semana que viene",
        #                "2017-07-04 00:00:00", "come")
        # testExtract_es("madera la semana pasada",
        #                "2017-06-20 00:00:00", "madera")
        # testExtract_es("comer el mes que viene",
        #                "2017-07-27 00:00:00", "comer")
        # testExtract_es("madera el mes pasado",
        #                "2017-05-27 00:00:00", "madera")
        # testExtract_es("come el año que viene",
        #                "2018-06-27 00:00:00", "come")
        # testExtract_es("madera el pasado año",
        #                "2016-06-27 00:00:00", "madera")
        testExtract_es("volver al pasado lunes",
                       "2017-06-26 00:00:00", "volver")
        # testExtract_es("volver al lunes pasado",
        #                "2017-06-26 00:00:00", "volver")                       
        # testExtract_es("entregado el 8 de mayo de 1945",
        #                "1945-05-08 00:00:00", "entregado")
        # testExtract_es("redacta el contrato 3 días después del próximo jueves",
        #                "2017-07-09 00:00:00", "redacta contrato")
        # testExtract_es("firma el contrato 2 semanas después del jueves pasado",
        #                "2017-07-06 00:00:00", "firma contrato")
        testExtract_es("enciende el horno en un cuarto de hora",
                       "2017-06-27 00:15:00", "enciende horno")
        testExtract_es("poner la pizza en el horno en media hora",
                       "2017-06-27 00:30:00", "poner pizza en horno")
        # testExtract_es("apaga el horno en tres cuartos de hora",
        #                "2017-06-27 00:45:00", "apaga horno")
        # testExtract_es("comer la pizza dentro de una hora",
        #                "2017-06-27 01:00:00", "comer pizza")
        # testExtract_es("beber la cerveza en 2 horas y 23 minutos",
        #                "2017-06-27 02:23:00", "beber cerveza")
        testExtract_es("planta el 3 de marzo",
                       "2018-03-03 00:00:00", "planta")
        testExtract_es("cosecha en 10 meses",
                       "2018-04-27 00:00:00", "cosecha")
        # testExtract_es("point 6a: dans 10 mois",
        #                "2018-04-27 06:00:00", "point")
        testExtract_es("después del mediodía dimitir a las 4:59 pm",
                       "2017-06-27 16:59:00", "después mediodía dimitir")
        # testExtract_es("dormir a las dos de la madrugada",
        #                "2017-06-27 02:00:00", "dormir")
        testExtract_es("ordenar su escritorio a las 1700 horas",
                       "2017-06-27 17:00:00", "ordenar su escritorio")

        # testExtractDate2_es("guardar el contrato 2 semanas después del lunes",
        #                     "2017-07-17 00:00:00", "guardar contrato")
        testExtractDate2_es("cómprate un poco de humor a las 3:00 p.m.",
                            "2017-07-01 15:00:00", "cómprate poco humor")
        testExtractNoDate_es("cállate hoy",
                             datetime.now().strftime("%Y-%m-%d") + " 00:00:00",
                             "cállate")
        # self.assertEqual(extract_datetime("", lang="es-es"), None)
        # self.assertEqual(extract_datetime("frase inútil", lang="es-es"),
        #                  None)
        # self.assertEqual(extract_datetime(
        #     "aprender a contar a las 37 horas", lang="es-es"), None)


if __name__ == "__main__":
    unittest.main()
