"""
Created on Nov. 14, 2021
@author: Heng-Sheng (Hanson) Chang
"""

import numpy as np
from _rod_tool import StaticRod

class Algorithm(object):
    def __init__(self, rod, algo_config):

        self.static_rod = StaticRod.get_rod(rod)
        self.config = algo_config

        self.ds = self.static_rod.rest_lengths / np.sum(self.static_rod.rest_lengths)
        self.s = np.insert(np.cumsum(self.ds), 0, 0)
        self.s_position = self.s.copy()
        self.s_director = (self.s[:-1] + self.s[1:])/2
        self.s_sigma = (self.s[:-1] + self.s[1:])/2
        self.s_kappa = self.s[1:-1]

    def run(self, **kwargs):
        raise NotImplementedError