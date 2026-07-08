import torch
import torch.nn as nn
from collections import deque
import gymnasium as gym
import random
import numpy as np

class Q_net(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(4, 64)
        self.output = nn.Linear(64, 2)
    def forward(self, x):
        x = torch.relu(self.hidden(x))
        return self.output(x)
def select_action(state,epsilon):
    if random.random() < epsilon:
        return env.action_space.sample()
    else:
        with torch.no_grad():
            state = torch.tensor(state, dtype=torch.float32)
            q_values = policy_net(state)
            return torch.argmax(q_values).item()
def train_step():
    batch = random.sample(buffer, batch_size)
    states, actions, rewards, next_states, dones = zip(*batch)
    states = torch.tensor(np.array(states),dtype=torch.float32)
    actions = torch.tensor(actions, dtype=torch.int64)
    rewards = torch.tensor(rewards, dtype=torch.float32)
    next_states = torch.tensor(np.array(next_states), dtype=torch.float32)
    dones = torch.tensor(dones, dtype=torch.float32)
    q_values = policy_net(states).gather(1, actions.unsqueeze(1)).squeeze(1)
    with torch.no_grad():
        max_next_q = target_net(next_states).max(1)[0]
        target = rewards + gamma * max_next_q * (1 - dones)
    loss = loss_fn(q_values, target)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

policy_net = Q_net()
target_net = Q_net()
target_net.load_state_dict(policy_net.state_dict())
env = gym.make("CartPole-v1")
optimizer = torch.optim.Adam(policy_net.parameters(), lr=0.001)
loss_fn = nn.MSELoss()
gamma = 0.99
epsilon = 0.1
batch_size = 64
num_of_episodes = 500
update_step = 10

buffer = deque(maxlen=10000)

for episode in range(num_of_episodes):
    total_reward = 0
    state, info = env.reset()
    while True:
        action = select_action(state,epsilon)
        next_state, reward, terminated, truncated, info = env.step(action) 
        done = terminated or truncated
        buffer.append((state, action, reward, next_state, done))
        state = next_state
        if len(buffer) >= batch_size: train_step() 
        total_reward += reward
        if done: break

    if episode % 20 == 0:
        print(f"episode = {episode}")
        print(f"total_reward = {total_reward}")
    if episode % update_step == 0:
        target_net.load_state_dict(policy_net.state_dict())

