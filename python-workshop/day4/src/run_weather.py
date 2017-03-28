from weather import WeatherByCity
import sys
import os


def print_extreme_city_results(d, value):
    print "{:8s}{:8s}{:>6s}".format("month", "city", value)
    for month, (city, val) in d.iteritems():
        print "{:8s}{:8s}{:6.2f}".format(month, city, val)


def main(w):
    print "*HOTTEST CITY BY MONTH*"
    print_extreme_city_results(w.warmest_city_per_month(), 'temp')
    print
    print "*COLDEST CITY BY MONTH*"
    print_extreme_city_results(w.coldest_city_per_month(), 'temp')
    print
    print "*CITY WITH MOST RAIN BY MONTH*"
    print_extreme_city_results(w.rainiest_city_per_month(), 'rain')
    print
    print "*CITY WITH MOST RAINY DAYS BY MONTH*"
    print_extreme_city_results(w.days_rain_city_per_month(), 'days rain')


if __name__ == '__main__':
    error_message = "Usage: python weather.py directory\n"
    if len(sys.argv) != 2:
        print error_message
        exit()
    try:
        w = WeatherByCity(sys.argv[1])
    except IOError as e:
        print e.message
        print error_message
        exit()
    main(w)
