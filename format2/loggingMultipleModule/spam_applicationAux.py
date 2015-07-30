
# import logging
#
# #create logger
#
# module_logger = logging.getLogger('spam_application_aux')
#
# class Auxilary:
#     def __init__(self):
#         self.logger = logging.getLogger('spam_application_aux.Auxiliary')
#         self.logger.error('there is no error in Auxiliary')
#         self.logger.info('creating an instance of Auxiliary')
#
#     def do_someting(self):
#         self.logger.info('doing something')
#         a = 1 + 1
#         self.logger.error('there is no error in do_something')
#         self.logger.info('done doing something')
#
# def some_function():
#     module_logger.info('received a call to "some_function"')
#     module_logger.error('there is no error in some_function')
#
# # spam_application_aux.py
import logging

# create logger
module_logger = logging.getLogger('spam_application.auxiliary')

class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger('spam_application.auxiliary.Auxiliary')
        self.logger.error('there is no error in Auxiliary')
        self.logger.info('creating an instance of Auxiliary')
    def do_something(self):
        self.logger.info('doing something')
        a = 1 + 1
        self.logger.info('done doing something')
        self.logger.error('there is no error in do_something')

def some_function():
    module_logger.info('received a call to "some_function"')
    module_logger.error('there is no error in some_function')