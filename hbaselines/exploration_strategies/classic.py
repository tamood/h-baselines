"""Script containing various classic exploration strategies.

We implement the following exploration strategies here:

* TODO
"""
import numpy as np
import random

from hbaselines.exploration_strategies.base import ExplorationStrategy


class EpsilonGreedy(ExplorationStrategy):
    """Epsilon greedy exploration strategy.

    Under this strategy, The agent does random exploration occasionally with
    probability epsilon and takes the optimal action most of the time with
    probability 1 - epsilon. This epsilon value can be made to decay over time
    in order to further rely on exploitation as time progresses.

    Attributes
    ----------
    epsilon_max : bool
        TODO
    epsilon_min : bool
        TODO
    decay_rate : bool
        TODO
    decay : bool
        TODO
    """

    def __init__(self,
                 ac_space,
                 epsilon_max=1,
                 epsilon_min=0,
                 decay_rate=1e6):
        """Instantiate the exploration strategy object.

        Parameters
        ----------
        ac_space : gym.space.*
            the action space of the agent
        epsilon_max : bool
            TODO
        epsilon_min : bool
            TODO
        decay_rate : bool
            TODO
        """
        super(EpsilonGreedy, self).__init__(ac_space)

        # Run assertions.
        assert 0 <= epsilon_min <= 1, "epsilon_min must be between [0,1]."
        assert 0 <= epsilon_max <= 1, "epsilon_max must be between [0,1]."
        assert epsilon_min <= epsilon_max, \
            "epsilon_min must less than or equal to epsilon_max."

        self.epsilon_min = epsilon_min
        self.epsilon_max = epsilon_max
        self.decay_rate = decay_rate
        self.decay = 0

    def apply_noise(self, action):
        """See parent class."""
        prob_random = max(self.epsilon_min, self.epsilon_max - self.decay)
        self.decay += 1 / self.decay_rate

        if random.uniform(0, 1) < prob_random:
            # Apply random action.
            return np.array([self.ac_space.sample()])
        else:
            # Apply original action.
            return action

    def update(self):
        """Do nothing."""
        pass


class UpperConfidenceBounds(ExplorationStrategy):
    """TODO.

    """

    def __init__(self, ac_space):
        """Instantiate the exploration strategy object.

        Parameters
        ----------
        ac_space : gym.space.*
            the action space of the agent
        """
        super(UpperConfidenceBounds, self).__init__(ac_space)

    def apply_noise(self, action):
        """See parent class."""
        return action  # TODO

    def update(self):
        """Do nothing."""
        return 0


class BoltzmannExploration(ExplorationStrategy):
    """TODO.

    """

    def __init__(self, ac_space):
        """Instantiate the exploration strategy object.

        Parameters
        ----------
        ac_space : gym.space.*
            the action space of the agent
        """
        super(BoltzmannExploration, self).__init__(ac_space)

    def apply_noise(self, action):
        """See parent class."""
        return action  # TODO

    def update(self):
        """Do nothing."""
        return 0


class ThompsonSampling(ExplorationStrategy):
    """TODO.

    """

    def __init__(self, ac_space):
        """Instantiate the exploration strategy object.

        Parameters
        ----------
        ac_space : gym.space.*
            the action space of the agent
        """
        super(ThompsonSampling, self).__init__(ac_space)

    def apply_noise(self, action):
        """See parent class."""
        return action  # TODO

    def update(self):
        """Do nothing."""
        return 0


class OutputNoise(ExplorationStrategy):
    """Gaussian output noise exploration strategy.

    TODO

    Attributes
    ----------
    scale : bool
        TODO
    noise : bool
        TODO
    """

    def __init__(self, ac_space, scale):
        """Instantiate the exploration strategy object.

        Parameters
        ----------
        ac_space : gym.space.*
            the action space of the agent
        scale : bool
            TODO
        """
        super(OutputNoise, self).__init__(ac_space)

        # Run assertions.
        assert 0 <= scale <= 1, "scale must be between [0,1]."

        ac_magnitude = (self.ac_space.high - self.ac_space.low) / 2
        self.scale = scale
        self.noise = self.scale * ac_magnitude

    def apply_noise(self, action):
        """See parent class."""
        return action + np.random.normal(0, self.noise, action.shape)

    def update(self):
        """Do nothing."""
        return 0


class ParameterNoise(ExplorationStrategy):
    """TODO.

    https://arxiv.org/pdf/1706.01905.pdf

    https://arxiv.org/pdf/1706.10295.pdf
    """

    def __init__(self, ac_space):
        """Instantiate the exploration strategy object.

        Parameters
        ----------
        ac_space : gym.space.*
            the action space of the agent
        """
        super(ParameterNoise, self).__init__(ac_space)

    def apply_noise(self, action):
        """See parent class."""
        return action  # TODO

    def update(self):
        """Do nothing."""
        return 0
