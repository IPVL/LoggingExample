# myApp/myapp
import logging

from myApp import mylib
from AppDirectory1 import dirLogTest

def main():
    # logging.basicConfig(filename='test.log',format='%(levelname)s: %(asctime)s %(message)s', filemode='w',level=logging.DEBUG)
    logging.getLogger('myApp')
    logging.basicConfig(filename='test.log',format='%(levelname)s: %(asctime)s %(message)s',level=logging.DEBUG)
    logging.getLogger('myApp')
    logging.debug('This message should go to the log file')
    logging.warning('Watch out!ddd')
    mylib.do_something()
    dirLogTest.do_something_in_dir()
    logging.info("I told you so...")


if __name__ == '__main__':
    main()