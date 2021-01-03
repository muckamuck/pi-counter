'''
Turn on some LED lights for the main event
'''
import sys
import time
import logging
from RPi import GPIO

logger = logging.getLogger(__name__)
ON_TIME = 0.25
OFF_TIME = 0.25

BIT_1 = 11
BIT_2 = 13
BIT_4 = 15
BIT_8 = 12

BITS = [BIT_1, BIT_2, BIT_4, BIT_8]
BITS = [BIT_8, BIT_4, BIT_2, BIT_1]

logger.info('putting the Pi into BOARD mode')
GPIO.setmode(GPIO.BOARD)

logger.info('setting pins to do ouput')
for b in BITS:
    GPIO.setup(b, GPIO.OUT)


def reset_all():
    for b in BITS:
        GPIO.output(b, False)


def show_count(i, the_bits):
    logger.info('%s - %s', i, the_bits)
    for idx, status in enumerate(the_bits):
        logger.info('%s - %s', idx, status)
        GPIO.output(BITS[idx], status)
    print()
    time.sleep(1)


def blink():
    logger.info('blink() called')
    try:
        while True:
            logging.info('on')
            GPIO.output(BIT_8, True)
            time.sleep(ON_TIME)

            logging.info('off')
            GPIO.output(BIT_8, False)
            time.sleep(OFF_TIME)
    except KeyboardInterrupt as control_c:
        print(control_c)
        logger.info('stoppin\' the car boss')
    except Exception as wtf:
        logger.warning(wtf, exc_info=False)
    finally:
        logger.info('calling cleanup()')
        GPIO.cleanup()


def cleanup():
    try:
        GPIO.cleanup()
    except Exception:
        pass


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        format='[%(levelname)s] %(asctime)s (%(module)s) %(message)s',
        datefmt='%Y/%m/%d-%H:%M:%S'
    )

    reset_all()
    blink()
