import csv
import os

import utils

module_path = os.path.dirname(__file__)

class EmpathyMachines(object):

    def __init__(self):
        pass

    def train(self, corpus='Twitter'):
        file_path = os.path.join(module_path, 'corpora', 'aggregatedCorpusCleaned.csv')
        raw_data = utils.load_dataset(os.path.join())