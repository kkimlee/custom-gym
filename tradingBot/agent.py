# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:11:22 2021

@author: user
"""

import random

class TradingAgent:
    def __init__(self):
        self.asset = 100000
        self.invertory = []
        
    def act(self, state, action_size):
        return random.randrange(1,action_size)