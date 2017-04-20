import numpy as np
import pandas as pd


class QLearningAgent:
    def __init__(self, actions):
        # actions = [0, 1, 2, 3]
        self.actions = actions
        self.learning_rate = 0.01
        self.discount_factor = 0.9
        self.epsilon = 0.9
        self.q_table = pd.DataFrame(columns=self.actions)

        # check whether the state was visited
        # if this is first visitation, then initialize the q function of the state

    def check_state_exist(self, state):
        if state not in self.q_table.index:
            self.q_table = self.q_table.append(
                pd.Series(
                    [0] * len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )

    # update q function with sample <s, a, r, s'>
    def learn(self, state, action, reward, next_state):
        self.check_state_exist(next_state)
        q_1 = self.q_table.ix[state, action]
        # using Bellman Optimality Equation to update q function
        q_2 = reward + self.discount_factor * self.q_table.ix[next_state, :].max()
        self.q_table.ix[state, action] += self.learning_rate * (q_2 - q_1)

    # get action for the state according to the q function table
    # agent pick action of epsilon-greedy policy
    def get_action(self, state):
        self.check_state_exist(state)

        if np.random.rand() > self.epsilon:
            # take random action
            action = np.random.choice(self.actions)
        else:
            # take action according to the q function table
            state_action = self.q_table.ix[state, :]
            state_action = state_action.reindex(np.random.permutation(state_action.index))
            action = state_action.argmax()

        return action
