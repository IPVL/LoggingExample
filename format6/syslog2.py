import logging
import syslog
from logging.handlers import SysLogHandler

logger = logging.getLogger('syslogTest')
logger.setLevel(logging.DEBUG)
syslog = SysLogHandler(address='/dev/log', facility=syslog.LOG_LOCAL6)
formatter = logging.Formatter('%(name)s: %(levelname)s %(message)s')
syslog.setFormatter(formatter)
logger.addHandler(syslog)

logger.debug('this is test of syslog using debug')
logger.info('this is test of syslog using info')

