#loggingModule2.py

import logging
import logging.config
import logTest
import time
import os


logging.config.fileConfig('logging.conf')
#create and start listener on port 9999

t = logging.config.listen(9999)
t.start()

#logger create
logger = logging.getLogger('simpleExample')


#application code
# def main():
#     logger.debug('Debug message')
#     logger.info('Info message')
#     logger.warn('warn message')
#     logTest.do_something()
#     logger.error('error messages')
#     logger.critical('critical messages')
#
#
# if __name__ == '__main__':
#     main()

try:
    while True:
        logger.debug('debug messages')
        logger.info('info message')
        logger.error('error message')
        logger.critical('critical messages')
        time.sleep(5)
except KeyboardInterrupt:
    logging.config.stopListening()
    t.join()