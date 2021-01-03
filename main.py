'''
Count to some power of 2 - 1
'''
# pylint: disable=C0103
# pylint: disable=W0703

import sys
import logging

from utility import reset_all
from utility import show_count
from utility import cleanup


logger = logging.getLogger(__name__)


def count(light_count):
    '''
    Count in binary and ask a friend to turn on some lights
    '''
    for i in range(2 ** light_count):
        status = list()
        for j in range(light_count):
            tmp = (i >> j) & 1 == 1
            status.insert(0, tmp)
        show_count(i, status)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        format='[%(levelname)s] %(asctime)s (%(module)s) %(message)s',
        datefmt='%Y/%m/%d-%H:%M:%S'
    )

    reset_all()
    try:
        while True:
            count(4)
    except KeyboardInterrupt as control_c:
        print()
        logger.debug(control_c)
        logger.info('stoppin\' the car boss')
    except Exception as wtf:
        logger.warning(wtf, exc_info=False)
    finally:
        logger.info('calling cleanup()')
        cleanup()
