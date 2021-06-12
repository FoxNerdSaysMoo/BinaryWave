

class State:
    def __init__(self, state="-"):
        self.state = state

    def collapse(self, state):
        self.state = state

    def __repr__(self):
        return f"<State: '{self.state}'>"

    def __str__(self):
        return self.state
