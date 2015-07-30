import logging, sys
from logging import config

loggerName = 'mylog'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(name)s-%(levelname)s %(module)s P%(process)d T%(thread)d %(message)s'
            },
        },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose',
            },
        'sys-logger6': {
            'class': 'logging.handlers.SysLogHandler',
            'address': '/dev/log',
            'facility': "local6",
            'formatter': 'verbose',
            },
        },
    'loggers': {
        loggerName: {
            'handlers': ['sys-logger6','stdout'],
            'level': logging.DEBUG,
            'propagate': True,
            },
        }
    }

config.dictConfig(LOGGING)


logger = logging.getLogger(loggerName)

logger.debug('this is test of syslog using debug')
logger.info('this is test of syslog using info')
logger.debug("this is Debug")
logger.info("this is  Info")
logger.warn("this is  Warn")
logger.error("this is Error")
logger.critical("this is Critical")