

class Pattern:
    def __init__(self, pat: str):
        """
        Pattern class for binary wave function

        :param pat: string of chars [0, 1, -]: 0 for binary literal 0, 1 for binary literal 1, - for either 0 or 1
        """
        self.pattern = pat

    def check(self, section: str) -> bool:
        for ind, char in enumerate(self.pattern):
            if char in "01":
                if ind >= len(section):
                    return True
                if section[ind] != char and section[ind] != '-':
                    return False
        return True

    def collapse(self, wave, index, collapse=False):
        section = ''.join([str(x) for x in wave.wave[index:]])
        if self.check(section):
            if collapse:
                for ind, state in enumerate(wave.wave[index:]):
                    if ind < len(self.pattern):
                        state.collapse(self.pattern[ind])
            return True
        return False
