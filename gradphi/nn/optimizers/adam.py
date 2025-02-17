import numpy as np


class Adam:
    def __init__(self, params, lr=0.01, betas=(0.9, 0.999), epsilon=1e-8):
        self.params = params
        self.lr = lr
        self.betas = betas
        self.epsilon = epsilon

        self.m = [np.zeros_like(param.data) for param in self.params]
        self.v = [np.zeros_like(param.data) for param in self.params]

        self.t = 0

    def step(self):
        self.t += 1
        for i, param in enumerate(self.params):
            if param.grad is None:
                continue

            self.m[i] = self.betas[0] * self.m[i] + \
                (1 - self.betas[0]) * param.grad
            self.v[i] = self.betas[1] * self.v[i] + \
                (1 - self.betas[1]) * param.grad ** 2

            m_hat = self.m[i] / (1 - self.betas[0] ** self.t)
            v_hat = self.v[i] / (1 - self.betas[1] ** self.t)

            param.data -= self.lr * m_hat / (np.sqrt(v_hat) + self.epsilon)

    def zero_grad(self):
        for param in self.params:
            param.grad = None if param.grad is None else np.zeros_like(
                param.grad)
