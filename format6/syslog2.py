import logging
import syslog
import socket
from logging.handlers import SysLogHandler

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# sysl = SysLogHandler(address='/dev/log',facility=syslog.LOG_USER)
sysl = SysLogHandler(address=('127.0.0.1', 514), facility=syslog.LOG_USER, socktype=socket.SOCK_DGRAM)
formatter = logging.Formatter('%(name)s: %(levelname)s %(message)s')
sysl.setFormatter(formatter)
logger.addHandler(sysl)
logger.addHandler(logging.FileHandler("hits.log"))

logger.debug('this is test of syslog using debug')
logger.info('this is test of syslog using info')

