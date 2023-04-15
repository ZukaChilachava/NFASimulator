
class Automata:

    def __init__(self, state_count: int, accept_states: set):
        self.transitions = {}
        self.current_states = {0}
        self.accept_states = accept_states
        self.result_string = ""
        for i in range(state_count):
            self.transitions[i] = {}

    def add_transition(self, from_state, with_symbol, to_state) -> None:
        # ex. {0: {a: 1,
        #          b: 0}}
        if with_symbol not in self.transitions[from_state]:
            self.transitions[from_state][with_symbol] = [to_state]
        else:
            self.transitions[from_state][with_symbol].append(to_state)

    def __get_transition(self, from_state, with_symbol) -> str:
        # return None if transition for a symbol isn't described else return  new state
        return self.transitions[from_state].get(with_symbol, None)

    def make_transitions(self, with_symbol):
        substring_accepted = False
        temporary_current_states = set()

        for state in self.current_states:
            destination_states = self.__get_transition(state, with_symbol)
            if destination_states is None:
                continue

            for destination_state in destination_states:
                # if there is a transition from the state using the current symbol
                # append the new state to l + 1 step states
                temporary_current_states.add(destination_state)

                # if at least one of the new states is an accept state set the flag for appending "Y" to the answer
                if destination_state in self.accept_states:
                    substring_accepted = True

        # append the current substring answer to the overall answer
        self.result_string += "Y" if substring_accepted else "N"
        # update the previous state with the new l + 1 states
        self.current_states = temporary_current_states
