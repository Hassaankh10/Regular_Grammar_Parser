def parse_grammar(rules):
    grammar = {}
    for rule in rules:
        if "->" not in rule:
            raise ValueError(f"Invalid rule format: {rule}")
        head, productions = rule.split("->", 1)
        head = head.strip()
        if not head:
            raise ValueError(f"Invalid rule with empty head: {rule}")
        grammar[head] = [prod.strip() for prod in productions.strip().split("|")]
    return grammar

def grammar_to_nfa(grammar):
    nfa = {}
    for head, productions in grammar.items():
        nfa.setdefault(head, {})
        for prod in productions:
            if prod == 'ε':
                nfa[head].setdefault('ε', []).append('ACCEPT')
            elif len(prod) == 1:
                # Terminal only (goes to ACCEPT)
                symbol = prod
                nfa[head].setdefault(symbol, []).append('ACCEPT')
            elif len(prod) > 1:
                symbol, next_state = prod[0], prod[1:]
                nfa[head].setdefault(symbol, []).append(next_state)
            else:
                raise ValueError(f"Invalid production: {prod}")
    return nfa