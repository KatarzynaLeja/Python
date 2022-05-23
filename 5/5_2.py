from datetime import date, timedelta


def print_working_days(date1, date2):
    d1 = [int(i) for i in date1.split('-')]
    d2 = [int(i) for i in date2.split('-')]

    start = date(d1[0], d1[1], d1[2])
    end = date(d2[0], d2[1], d2[2])

    exclude = (6, 7)

    delta = end - start
    dates = []

    for i in range(delta.days):
        if start.isoweekday() not in exclude:
            dates.append(start)
        start = start + timedelta(days=1)

    return dates


print(print_working_days('2022-03-20', '2022-03-30'))
