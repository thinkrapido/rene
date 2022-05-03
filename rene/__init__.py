
import arrow
import numpy as np

to_date = lambda d : arrow.get(d)

def days_until(end_date):
    end_date = to_date(end_date)
    def fn(d):
        d = to_date(d)
        return (d - end_date).days
    return fn

def date_to_str(s):
    s = to_date(s)
    s = s.format('DDMMYYYY')
    return s
datum = lambda d : d.format('DD.MM.YYYY')

def date_parts(s): 
    s = date_to_str(s)
    s = [s[:2],s[2:4],s[4:6],s[6:]]
    s = np.array(s)
    return s

def quersumme(s):
    s = str(s)
    return sum(map(int, list(s)))

def lebenszahl(s):
    s = date_to_str(s)
    summe = quersumme(s)
    while summe >= 10:
        summe = quersumme(summe)
    return summe

def paarsumme(ich, anderer):
    split = lambda x : (x // 100, x % 100)
    parts = lambda s : np.vectorize(int)(np.split(np.array(list(s)), 4)).T
    multiply = lambda xi : xi[0] * 10 + xi[1]
    
    ich = multiply(parts(date_to_str(ich)))
    anderer = multiply(parts(date_to_str(anderer)))
    
    summe = ich + anderer
    summe = split(summe)
    summe = np.concatenate((summe[0], [0])), np.concatenate(([0], summe[1]))
    summe = summe[0] + summe[1]
    summe = np.sum(summe)
    
#    summe = map(split, get_nums(parts(date_to_str(ich))) + get_nums(parts(date_to_str(anderer))))
    return int(summe)

def line(d, ich=arrow.now()):
    return (d, days_until('00010101')(d), datum(d), lebenszahl(d), datum(ich), lebenszahl(ich), paarsumme(ich, d))

class DateIter:
    def __init__(self, end_date, start_date='0001-01-01'):
        self._end_date = arrow.get(end_date)
        self._current = arrow.get(start_date)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self._current > self._end_date:
            out = self._current
            self._current = self._current.shift(days=+1)
            return out
        else:
            raise StopIteration



def main(args):

    ich = args.date
    value = int(args.value)

    count = 1
    with open('data.txt', 'w') as fh:
        dates_iter = DateIter('2500-01-01')
        for date in dates_iter:
            summe = paarsumme(ich, date)
            if count % 100 == 0: print('.', end='', flush=True)
            if value == summe:
                fh.write(datum(date))
                fh.write(",")
                fh.write(str(value))
                fh.write("\n")
            count = count + 1

    print()
