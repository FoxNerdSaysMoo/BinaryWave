from .pattern import Pattern
from .state import State

import typing as t
import random


class Wave:
    def __init__(self, length: int, patterns: t.List[Pattern], seed: t.Optional[str] = None):
        """
        Binary wave function

        :param length: Length of wave.

        :param patterns: List of patterns for wave

        :param seed: Optional starting seed for wave
        """
        self.length = length
        self.patterns = patterns
        if seed is None:
            seed = ""
        self.seed = seed
        self.wave = []

    def get_state(self, index):
        return self.wave[index]

    def collapse(self, default='0'):
        self.wave = [State() for _ in range(self.length)]
        for i, x in enumerate(self.seed):
            self.wave[i] = State(x)

        for i in range(self.length):
            possible = []
            for pat in self.patterns:
                if pat.collapse(self, i):
                    possible.append(pat)

            if len(possible) == 0:
                continue
            random.choice(possible).collapse(self, i, True)

        return self.wave
