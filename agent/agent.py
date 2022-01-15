# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:11:22 2021

@author: user
"""

import random

class Agent:
    def __init__(self):
        self.asset = 100000
        self.invertory = []
    
    def get_state(self, state):
        self.state = state
    
    def act(self):
        return random.randrange(1,3)