import matplotlib.pyplot as plt
import networkx as nx

districts = [
    'Adilabad','Komaram Bheem','Nirmal','Mancherial','Nizamabad',
    'Jagitial','Peddapalli','Karimnagar','Rajanna Sircilla','Kamareddy',
    'Sangareddy','Medak','Siddipet','Jangaon','Warangal Urban',
    'Warangal Rural','Mahabubabad','Khammam','Bhadradri','Mulugu',
    'Jayashankar','Hanamkonda','Yadadri','Medchal','Hyderabad',
    'Ranga Reddy','Vikarabad','Mahabubnagar','Nagarkurnool',
    'Wanaparthy','Jogulamba','Narayanpet'
]

neighbors = {
    'Adilabad': ['Komaram Bheem','Nirmal'],
    'Komaram Bheem': ['Adilabad','Mancherial'],
    'Nirmal': ['Adilabad','Nizamabad'],
    'Mancherial': ['Komaram Bheem','Peddapalli'],
    'Nizamabad': ['Nirmal','Kamareddy'],
    'Jagitial': ['Karimnagar','Peddapalli'],
    'Peddapalli': ['Mancherial','Jagitial'],
    'Karimnagar': ['Jagitial','Rajanna Sircilla'],
    'Rajanna Sircilla': ['Karimnagar','Kamareddy'],
    'Kamareddy': ['Nizamabad','Rajanna Sircilla','Medak'],
    'Medak': ['Kamareddy','Sangareddy'],
    'Sangareddy': ['Medak','Ranga Reddy'],
    'Siddipet': ['Medak','Jangaon'],
    'Jangaon': ['Siddipet','Warangal Urban'],
    'Warangal Urban': ['Jangaon','Warangal Rural','Hanamkonda'],
    'Warangal Rural': ['Warangal Urban','Mahabubabad'],
    'Mahabubabad': ['Warangal Rural','Khammam'],
    'Khammam': ['Mahabubabad','Bhadradri'],
    'Bhadradri': ['Khammam','Mulugu'],
    'Mulugu': ['Bhadradri','Jayashankar'],
    'Jayashankar': ['Mulugu','Hanamkonda'],
    'Hanamkonda': ['Warangal Urban','Jayashankar'],
    'Yadadri': ['Medchal','Jangaon'],
    'Medchal': ['Hyderabad','Yadadri'],
    'Hyderabad': ['Medchal','Ranga Reddy'],
    'Ranga Reddy': ['Hyderabad','Vikarabad','Mahabubnagar'],
    'Vikarabad': ['Ranga Reddy','Sangareddy'],
    'Mahabubnagar': ['Ranga Reddy','Nagarkurnool','Narayanpet'],
    'Nagarkurnool': ['Mahabubnagar','Wanaparthy'],
    'Wanaparthy': ['Nagarkurnool','Jogulamba'],
    'Jogulamba': ['Wanaparthy','Narayanpet'],
    'Narayanpet': ['Mahabubnagar','Jogulamba']
}

colors = ['red','green','blue','yellow']

def is_valid(state, color, assignment):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtracking(assignment):
    if len(assignment) == len(districts):
        return assignment
    
    unassigned = [d for d in districts if d not in assignment][0]
    
    for color in colors:
        if is_valid(unassigned, color, assignment):
            assignment[unassigned] = color
            
            result = backtracking(assignment)
            if result:
                return result
            
            del assignment[unassigned]
    
    return None

solution = backtracking({})

print("\nTelangana Map Coloring Solution:\n")
for d in solution:
    print(f"{d} → {solution[d]}")

G = nx.Graph()

for d in districts:
    G.add_node(d)

for d in neighbors:
    for n in neighbors[d]:
        G.add_edge(d, n)

node_colors = [solution[node] for node in G.nodes()]

plt.figure(figsize=(12,10))
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_colors,
    node_size=800,
    font_size=8
)

plt.title("Telangana Map Coloring using CSP")
plt.show()