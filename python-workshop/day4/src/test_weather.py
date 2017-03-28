import nose.tools as n
import weather as w


def get_message(name, expected, actual):
    message = '{0} was {2} instead of {1}'
    return message.format(name, expected, actual)


def test_monthdata():
    month = '01/14'
    max_temps = [10, 4, 6, 8]
    min_temps = [8, 2, 5, 3]
    avg_temps = [9, 3, 5, 6]
    precips = [1, 0, 2, 0]
    md = w.MonthData(month, max_temps, min_temps, avg_temps, precips)
    exp, act = md.max_temp, 10
    n.assert_equal(exp, act, get_message('max_temp', exp, act))
    exp, act = md.min_temp, 2
    n.assert_equal(exp, act, get_message('min_temp', exp, act))
    exp, act = md.avg_temp, 5.75
    n.assert_equal(exp, act, get_message('avg_temp', exp, act))
    exp, act = md.total_precip, 3
    n.assert_equal(exp, act, get_message('total_precip', exp, act))
    exp, act = md.days_precip, 2
    n.assert_equal(exp, act, get_message('days_precip', exp, act))
