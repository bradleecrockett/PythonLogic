from unittest import TestCase

from python_logic import alarm_clock
from python_logic import lone_sum
from python_logic import love_six
from python_logic import round10
from python_logic import round_sum


class TestPythonLogic(TestCase):
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

    ########## Alarm Clock Tests ################
    def test_alarm_clock_monday(self):
        self.assertEqual(alarm_clock(1, False), "7:00")

    def test_alarm_clock_friday(self):
        self.assertEqual(alarm_clock(5, False), "7:00")

    def test_alarm_clock_sunday(self):
        self.assertEqual(alarm_clock(0, False), "10:00")

    def test_alarm_clock_vacayend(self):
        self.assertEqual(alarm_clock(6, True), "off")

    def test_alarm_clock_vacayday(self):
        self.assertEqual(alarm_clock(3, True), "10:00")

    ########## Round 10 Tests ################
    def test_round10_up(self):
        self.assertEqual(round10(5), 10)

    def test_round10_down(self):
        self.assertEqual(round10(13), 10)

    def test_round10_down0(self):
        self.assertEqual(round10(51), 50)



    ########## Round Sum Tests ################
    def test_round_up_sum(self):
        self.assertEqual(round_sum(16, 17, 18), 60)

    def test_round_down_sum(self):
        self.assertEqual(round_sum(12, 14, 13), 30)

    def test_round_up_downsum(self):
        self.assertEqual(round_sum(6, 4, 4), 10)



    ########## Lone Sum Tests ################
    def test_lone_sum_none(self):
        self.assertEqual(lone_sum(3, 3, 3), 0)

    def test_lone_sum_all(self):
        self.assertEqual(lone_sum(1, 2, 3), 6)

    def test_lone_sum_2nd(self):
        self.assertEqual(lone_sum(3, 2, 3), 2)

    def test_lone_sum_last(self):
        self.assertEqual(lone_sum(5, 5, 3), 3)

    def test_lone_sum_neg(self):
        self.assertEqual(lone_sum(-5, 12, 8), 15)
