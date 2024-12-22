
class FA:
    def __init__(self, alphabet):
        self.states = []
        self.transitions = {}
        self.init = None
        self.finals = []
        self.alphabet = alphabet

    def add_state(self, state, final=False):
        if state in self.states:
            print("error : state '" + state + "' already exists.")
            return
        self.transitions[state] = []
        self.states.append(state)
        if final:
            self.finals.append(state)

    def valid_symbol(self, symbol):
        return symbol in self.alphabet

    def dst_state(self, src_state, symbol):
        if src_state not in self.states:
            print("error : the state '" + src_state + "' is not an existing state.")
            return
        for (s, dst_state) in self.transitions[src_state]:
            if s == symbol:
                return dst_state
        return None

    def add_transition(self, src_state, symbol, dst_state):
        if not self.valid_symbol(symbol):
            print("error : the symbol '" + symbol + "' is not part of the alphabet.")
            return
        if src_state not in self.states:
            print("error : the state '" + src_state + "' is not an existing state.")
            return
        if dst_state not in self.states:
            print("error : the state '" + dst_state + "' is not an existing state.")
            return
        if self.dst_state(src_state, symbol) is not None:
            print("error : the transition (" + src_state + ", " + symbol + ", ...) already exists.")
            return
        self.transitions[src_state].append((symbol, dst_state))

    def generate_procedural_representation(self):
        for state in self.states:
            print(f"void Etat_{state}()\n"
                  "{\n"
                  "    char c;\n"
                  "    switch(c)\n"
                  "    {\n")
            for (sym, dest) in self.transitions[state]:
                print(f"        case '{sym}': Etat_{dest}();\n"
                      "                       break;\n")
            print("        default: ERREUR();\n"
                  "    }\n"
                  "}\n")

def lexical_analyzer(input_string, start_state, final_states, automaton):
    current_state = start_state

    for char in input_string:
        next_state = automaton.dst_state(current_state, char)
        if next_state is not None:
            current_state = next_state
        else:
            print(f"Error: No transition for symbol '{char}' from state '{current_state}'.")
            return

    if current_state in final_states:
        print("Lexical analysis successful.")
    else:
        print("Error: Final state not reached.")

def main():
    alphabet_input = input("Enter the alphabet: ")
    a = FA(alphabet_input)

    while True:
        state_input = input("Enter a state (or enter 'done' to finish): ")
        if state_input.lower() == 'done':
            break
        final_state_input = input("Is it a final state? (y/n): ").lower()
        if final_state_input == 'y':
            a.add_state(state_input, True)
        else:
            a.add_state(state_input)

    initial_state_input = input("Enter the initial state: ")
    a.init = initial_state_input

    while True:
        src_state = input("Enter the source state for a transition (or enter 'done' to finish): ")
        if src_state.lower() == 'done':
            break

        symbol = input("Enter the symbol for the transition: ")
        dst_state = input("Enter the destination state for the transition: ")

        a.add_transition(src_state, symbol, dst_state)

    print("\nAutomaton details:")
    print(a)
    print("\nProcedural Representation:")
    a.generate_procedural_representation()

    input_string = input("Enter a string for lexical analysis: ")
    lexical_analyzer(input_string, a.init, a.finals, a)

if __name__ == "__main__":
    main()