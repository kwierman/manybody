from .base import Algorithm

import xgboost as xgb

class BoostedDecisionTrees(Algorithm):
    tasks = ['regression', 'classification']

    workflows = ['training', 'inference']

    def __init__(self):
        pass

    def train(self, dataset):
        pass
        
