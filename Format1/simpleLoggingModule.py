#simpleLoggingModule.py

import logging

#create logger
logger = logging.getLogger('simpleLoggingModule')
logger.setLevel(logging.INFO)


#create console handler and set level to debug

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

#create formatter

formatter = logging.Formatter('%(asctime)s- %(name)s - %(levelname)s -: %(message)s')

#add formatter to ch
ch.setFormatter(formatter)

#add ch to logger
logger.addHandler(ch)

#application code

logger.debug('Debug message')
logger.info('Info message')
logger.warn('warn message')
logger.error('error messages')
logger.critical('critical messages')

