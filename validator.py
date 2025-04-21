def epsilon_closure(nfa, states):
    closure = set(states)
    stack = list(states)
    
    while stack:
        state = stack.pop()
        for next_state in nfa.get(state, {}).get('ε', []):
            if next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)
    return closure

def validate_string(nfa, start_state, input_string):
    current_states = epsilon_closure(nfa, [start_state])

    for char in input_string:
        next_states = set()
        for state in current_states:
            for target in nfa.get(state, {}).get(char, []):
                next_states.add(target)
        current_states = epsilon_closure(nfa, next_states)

    return 'ACCEPT' in current_states