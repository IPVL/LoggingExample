import logging
logging.getLogger('loggerTest')
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.getLogger('loggerTest')
logging.debug('This message should go to the log file')
logging.warning('Watch out!ddd')
logging.info("I told you so...")


