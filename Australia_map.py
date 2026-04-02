import matplotlib.pyplot as plt
import networkx as nx

states = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']

neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

colors = ['red', 'green', 'blue']

def is_valid(state, color, assignment):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtracking(assignment):
    if len(assignment) == len(states):
        return assignment
    
    unassigned = [s for s in states if s not in assignment][0]
    
    for color in colors:
        if is_valid(unassigned, color, assignment):
            assignment[unassigned] = color
            
            result = backtracking(assignment)
            if result:
                return result
            
            del assignment[unassigned]
    
    return None

solution = backtracking({})

print("Australia Map Coloring Solution:\n")
for state in solution:
    print(f"{state} → {solution[state]}")

G = nx.Graph()

for state in states:
    G.add_node(state)

for state in neighbors:
    for n in neighbors[state]:
        G.add_edge(state, n)

node_colors = [solution[state] for state in G.nodes()]

plt.figure(figsize=(8,6))
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_colors,
    node_size=2000,
    font_size=12
)

plt.title("Australia Map Coloring using CSP")
plt.show()