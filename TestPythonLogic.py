from unittest import TestCase
from PythonLogic import round_sum
from PythonLogic import alarm_clock
from PythonLogic import love_six
from PythonLogic import round10

class TestPythonLogic(TestCase):
    ########## Round Sum Tests ################
    def test_round_up_sum(self):
        self.assertEqual(round_sum(16, 17, 18), 60)

    def test_round_down_sum(self):
        self.assertEqual(round_sum(12, 14, 13), 30)

    def test_round_up_downsum(self):
        self.assertEqual(round_sum(6, 4, 4), 10)


    ########## Round Sum Tests ################
    def test_round10_up(self):
        self.assertEqual(round10(5), 10)

    def test_round10_down(self):
        self.assertEqual(round10(13), 10)

    def test_round10_down0(self):
        self.assertEqual(round10(51), 50)



    ########## Alarm Clock Tests ################
    def test_alarm_clock_monday(self):
        self.assertEqual(alarm_clock(1, False), "7:00")

    def test_alarm_clock_friday(self):
        self.assertEqual(alarm_clock(5, False), "7:00")

    def test_alarm_clock_sunday(self):
        self.assertEqual(alarm_clock(0, False), "10:00")

    def test_alarm_clock_vacayend(self):
        self.assertEqual(alarm_clock(6, False), "off")

    def test_alarm_clock_vacayday(self):
        self.assertEqual(alarm_clock(3, False), "off")


    ########## Love Six Tests ################
    def test_love_six_input6(self):
        self.assertEqual(love_six(6, 4), True)

    def test_love_six_false(self):
        self.assertEqual(love_six(4, 5), False)

    def test_love_six_sum(self):
        self.assertEqual(love_six(1, 5), True)

    def test_love_six_dif6(self):
        self.assertEqual(love_six(13, 19), True)

    def test_love_six_negdif6(self):
        self.assertEqual(love_six(4, -2), True)



    ########## Lone Sum Tests ################
    def lone_sum_none(self):
        self.assertEqual(lone_sum(3, 3, 3), 0)

    def lone_sum_all(self):
        self.assertEqual(lone_sum(1, 2, 3), 6)

    def lon_sum_2nd(self):
        self.assertEqual(lone_sum(3, 2, 3), 2)

    def lon_sum_last(self):
        self.assertEqual(lone_sum(5, 5, 3), 3)

    def lon_sum_neg(self):
        self.assertEqual(lone_sum(-5, 12, 8), 15)