from graphviz import Digraph

def draw_nfa(nfa):
    dot = Digraph()
    dot.attr(rankdir='LR')
    dot.node('S', shape='circle')
    dot.node('ACCEPT', shape='doublecircle')

    for state in nfa:
        dot.node(state, shape='circle')
        for symbol, next_states in nfa[state].items():
            for next_state in next_states:
                label = symbol if symbol else 'ε'
                dot.edge(state, next_state, label=label)

    dot.render('nfa', format='png', cleanup=True)
    print("NFA visual saved as nfa.png")

