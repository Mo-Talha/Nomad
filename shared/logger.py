import os
import logging

from datetime import datetime


log_name = '{}/../logs/{}.log'.format(os.path.dirname(os.path.abspath(__file__)),
                                      datetime.now().strftime('%Y.%m.%d.%H.%M.%S'))

logger = logging.getLogger('main')
logger.setLevel(logging.INFO)

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', filename=log_name)


def info(component, message):
    if component:
        logger.info('[{}] {}'.format(component, message))
    else:
        logger.info(message)


def error(component, message):
    if component:
        logger.error('[{}] {}'.format(component, message))
    else:
        logger.error(message)

