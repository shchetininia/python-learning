import numpy as np
def epsilon_greedy(actions,eps):
    # возвращает индекс
    if np.random.random() < eps:
        return np.random.randint(0,3) # investigation
    else:
        return np.argmax(actions) # exploitation

Q = np.zeros((3,3))
eps = 0.1
s_arr = np.array([0, 1, 2]) # 0 L, 1 M, 2 H
act_arr = np.array([0, 1, 2]) # 0 down, 1 hold, 2 up
s = 0
act = 0
r = 0
count = 1000
gamma = 0.9
alpha = 0.1
num_steps = 50
eps = 0.1
while count > 0:
    step = 0
    s = np.random.choice(s_arr)
    r = 0
    for step in range(num_steps):
        s_prev = s
        act = act_arr[epsilon_greedy(Q[s],eps)]
        if act > act_arr[1]:
            s += 1

        elif act < act_arr[1]:
            s -= 1
        else:
            s += 0

        if s == s_arr[1]:
            r = 1
        else:
            r = 0
        s = np.max([np.min([s,2]),0])
        Q[s_prev, act] += alpha*(r + gamma*np.max(Q[s])-Q[s_prev,act])
    count -= 1

print(Q)
print(np.argmax(Q[0]))
print(np.argmax(Q[1]))
print(np.argmax(Q[2]))