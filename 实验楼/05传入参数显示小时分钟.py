import sys


def Hours(minutes):
    if minutes > 0:
        hour = minutes // 60
        minute = minutes % 60

        print('{0} H, {1} M'.format(hour, minute))

    else:
        raise ValueError


try:
    Hours(int(sys.argv[1]))
except:
    print('Parameter Error')





























