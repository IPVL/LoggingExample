# import logging
# import spam_applicationAux
#
# #create logger
# logger = logging.getLogger('spam_application')
# logger.setLevel(logging.DEBUG)
#
# #create file handler which logs even debug messages
#
# fh = logging.FileHandler('spam.log')
# fh.setLevel(logging.DEBUG)
#
# #create console handler with a higher log level
# ch = logging.StreamHandler()
# ch.setLevel(logging.ERROR)
#
# #create formatter and add it to the handlers
# formatter = logging.Formatter('%(asctime)s- %(name)s- %(levelname)s -: %(message)s  ')
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
#
# #add handlers to the logger
#
# logger.addHandler(fh)
# logger.addHandler(ch)
#
#
# logger.info('creating an instance of auxiliary_module.Auxiliary')
# a = spam_applicationAux.Auxilary()
# logger.info('created an instance of auxiliary module')
# logger.info('calling auxiliary_module.Auxiliary.do_something')
# a.do_someting()
# logger.info('finished auxiliary_module.Auxiliary.do_something')
# logger.info('calling auxiliary_module.some_function')
# spam_applicationAux.some_function()
# logger.info('finished auxiliary_module.some_function')

import logging
import spam_applicationAux

# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.info('creating an instance of auxiliary_module.Auxiliary')
a = spam_applicationAux.Auxiliary()
logger.info('created an instance of auxiliary_module.Auxiliary')
logger.info('calling auxiliary_module.Auxiliary.do_something')
a.do_something()
logger.info('finished auxiliary_module.Auxiliary.do_something')
logger.info('calling auxiliary_module.some_function()')
spam_applicationAux.some_function()
logger.info('done with auxiliary_module.some_function()')