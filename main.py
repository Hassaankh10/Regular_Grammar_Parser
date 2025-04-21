from custom_parser import parse_grammar, grammar_to_nfa
from validator import validate_string
from visualizer import draw_nfa

if __name__ == '__main__':
    print("Enter grammar rules (e.g., S -> aA | bB). Type 'done' to finish:")
    rules = []
    while True:
        line = input().strip()
        if line.lower() == 'done':
            break
        rules.append(line)

    try:
        grammar = parse_grammar(rules)
        nfa = grammar_to_nfa(grammar)
        draw_nfa(nfa)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

    while True:
        test_str = input("Enter string to validate (or 'exit' to quit): ").strip()
        if test_str.lower() == 'exit':
            break
        result = validate_string(nfa, 'S', test_str)
        print("Accepted" if result else "Rejected")
