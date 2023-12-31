""" ex_4_2.py """
from datetime import datetime


def logstamp_to_datetime(datestr):
    """
    Your docstring here.  Replace the pass keyword below with your implementation.
    """
    bad_guy = datestr
    good_guy = '%Y-%m-%dT%H:%M:%S'
    return datetime.strptime(bad_guy, good_guy)

# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    test_date = '2014-07-03T23:31:22'
    print(f'{logstamp_to_datetime(test_date)=}')
