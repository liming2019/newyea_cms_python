import os
import logging
import logging.handlers

host = 'http://112.74.51.178'
headers = {
    "Authorization": "Basic cGlnOnBpZw=="
}
base_path = os.path.dirname(__file__)


def init_log():
    mylog = logging.getLogger()
    mylog.setLevel(logging.DEBUG)

    sh = logging.StreamHandler()
    fh = logging.handlers.TimedRotatingFileHandler(filename=base_path + '/log/mylog.log', when='M', interval=1,
                                                   backupCount=3, encoding='utf-8')
    sh.setLevel(logging.DEBUG)
    fh.setLevel(logging.DEBUG)

    fmt = '%(levelname)s %(filename)s %(lineno)d %(asctime)s %(message)s'
    fm = logging.Formatter(fmt=fmt)
    sh.setFormatter(fm)
    fh.setFormatter(fm)

    mylog.addHandler(sh)
    mylog.addHandler(fh)

