# PythonLogic

## Love Six

The number 6 is a truly great number. Given two int values, `a` and `b`, `return True` if either one is 6. Or if their sum or difference is 6. Note: the function `abs(num)` computes the absolute value of a number.

|function call|return value|
|-----|-----|
|love_six(6, 4)|True|
|love_six(4, 5)|False|
|love_six(1, 5)|True|

## Lone Sum

Given 3 int values, `a b c`, `return` their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.

|function call|return value|
|-----|-----|
|lone_sum(1, 2, 3)|6|
|lone_sum(3, 2, 3)|2|
|lone_sum(3, 3, 3)|0|

## Round Sum

For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, `a b c`, `return` the sum of their rounded values. To avoid code repetition, write a separate helper `def round10(num):` and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().

|function call|return value|
|-----|-----|
|round_sum(16, 17, 18)|60|
|round_sum(12, 13, 14)|30|
|round_sum(6, 4, 4)|10|

## Alarm Clock

Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, `return` a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

|function call|return value|
|-----|-----|
|alarm_clock(1, False)|'7:00'|
|alarm_clock(5, False)|'7:00'|
|alarm_clock(0, False)|'10:00'|
