
import sys
from automata import Automata

if __name__ == '__main__':
    stdin = sys.stdin
    input_sentence = stdin.readline().rstrip("\n")
    info = stdin.readline()
    state_count, accept_count, transition_count = info.split()
    state_count = int(state_count)
    accept_state_string = sys.stdin.readline().split()
    accept_states: set = set([int(string) for string in accept_state_string])
    automata: Automata = Automata(state_count, accept_states)

    for current_state in range(state_count):
        transition_info = stdin.readline().split()

        for transition_index in range(int(transition_info[0])):
            start_index = transition_index * 2 + 1
            symbol, to_state = transition_info[start_index], transition_info[start_index + 1]
            automata.add_transition(current_state, symbol, int(to_state))

    for symbol in input_sentence:
        automata.make_transitions(symbol)

    sys.stdout.write(automata.result_string)
