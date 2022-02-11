"""
finite state machine module
"""

class Transition:
    """
    Template class for transitions. To be declared then added in StateManager instance with add_transition()
    """
    def __init__(self, origin_state, target_state):
        self.origin_state = origin_state
        self.target_state = target_state

    def execute(self):
        pass

class State:
    """
    Template class for states. To be declared then added in StateManager instance with add_state()
    """
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def enter(self):
        pass

    def execute(self):
        pass

    def exit(self):
        pass

class StateManager:
    """
    Manages all states of one entity.
    To be declared in entity __init__.
    ! Don't forget to add states/transitions
    ! Don't forget to set current_state with start()
    """
    def __init__(self):
        self.states = {}
        self.prev_state = None
        self.cur_state = None
        self.trans = None

    def add_state(self, state):
        self.states[state.name] = state

    def add_transition(self, transition):
        self.states[transition.origin_state].transitions[transition.target_state] = transition

    def start(self, start_state_name):
        self.cur_state = self.states[start_state_name]
        self.cur_state.enter()

    def change_state(self, target_state_name):
        try:
            self.trans = self.cur_state.transitions[target_state_name]
        except:
            print("Transition not found")
        # TODO CHECK PREV STATE

    def loop(self):
        """
        To be put in entity loop.
        """
        if self.trans:
            self.cur_state.exit()
            self.cur_state.transitions[self.trans.target_state].execute()

            self.prev_state = self.cur_state
            self.cur_state = self.states[self.trans.target_state]

            self.cur_state.enter()
            self.trans = None
        else:
            self.cur_state.execute()
