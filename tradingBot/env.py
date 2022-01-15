# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:48:58 2021

@author: user
"""
import gym
from tradingBot.agent import TradingAgent
import tradingBot.utils as utils

class TradingEnv(gym.Env):
    # 초기화
    def __init__(self):
        super(TradingEnv, self).__init__()
        
        # 플레이어
        self.agent = TradingAgent()
        
        # 데이터
        self.stock_data = utils.get_stock_data('tradingBot/data/data.csv') # 주식 데이터 가져오기
        self.data_length = len(self.stock_data) # 주식 데이터의 길이 계산
        self.state_size = len(self.stock_data.columns) # 지표 개수 계산
        
        # 행동
        self.action_size = 3 # 0: HOLD, 1: LONG, 2: SHORT
        self.reward = 0 # 행동에 대한 보상
        
        # 상태
        self.t = 0 # 시간
        self.state = self.stock_data.iloc[self.t] # 상태
        self.done = False # 끝 체크
        
    def step(self, action):
        # 끝이면 그냥 종료
        if self.done:
            return
        
        # 다음 시점의 데이터 읽어오기
        self.next_state = self.stock_data.iloc[self.t+1]
        # agent의 행동에 대한 보상 계산
        self.reward = self.act(action)
        # 시각화
        self.render()
        
        # 시점 증가
        self.t += 1
        if self.t == self.data_length-1:
            # 마지막 시점까지 온 경우 
            self.done = True
        
        # 디버깅을 위한 정보
        info = None
        
        self.state = self.next_state
        
        return [self.state, self.next_state], self.reward, self.done, info
    
    # 행동에 대한 보상
    def act(self, action):
        # HOLD 보상 계산
        if action == 0:
            # 다음 시점에서 가격이 올랐을 경우 - 보상
            # 다음 시점에서 가격이 내렸을 경우 + 보상
            self.reward = self.state['Close'] - self.next_state['Close']
            return self.reward
        # LONG 보상 계산
        elif action == 1:
            # 다음 시점에서 가격이 올랐을 경우 + 보상
            # 다음 시점에서 가격이 내렸을 경우 - 보상
            self.reward = self.next_state['Close'] - self.state['Close']
            return self.reward
        # SHORT 보상 계산
        elif action == 2:
            # 다음 시점에서 가격이 올랐을 경우 + 보상
            # 다음 시점에서 가격이 내렸을 경우 - 보상
            self.reward = self.state['Close'] - self.next_state['Close']
            return self.reward
    
    # 진행 상황 시각화
    def render(self):
        print(self.t+1, 'th result: ', self.reward)
    
    # 초기 상태로 
    def reset(self):
        self.state = None
        self.t = 0
        self.done = False