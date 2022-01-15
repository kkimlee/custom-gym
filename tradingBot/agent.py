# -*- coding: utf-8 -*-
import random

class TradingAgent:
    def __init__(self):
        self.asset = 100000
        self.invertory = []
        
    def act(self, state, action_size):
        
        return random.randrange(1,action_size)