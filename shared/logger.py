import os
import logging

from datetime import datetime


log_name = '{}/../logs/{}.log'.format(os.path.dirname(os.path.abspath(__file__)),
                                      datetime.now().strftime('%Y.%m.%d.%H.%M.%S'))

logger = logging.getLogger('main')
logger.setLevel(logging.INFO)

console = logging.StreamHandler()
logger.addHandler(console)

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename=log_name)


def info(component, message):
    logger.info('[{}] {}'.format(component, message))


def error(component, message):
    logger.error('[{}] {}'.format(component, message))

