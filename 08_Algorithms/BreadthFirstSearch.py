# find the shortest path between places where all steps are the same length (not weighted)
# visualisation in README.md

graph = {
    "A": ["B", "D"],
    "B": ["A", "C", "E"],
    "C": ["B", "F"],
    "D": ["A", "E"],
    "E": ["B", "D", "F","H"],
    "F": ["C", "E", "H", "G", "I"],
    "G": ["F", "I"],
    "H": ["E", "F", "I"],
    "I": ["F", "G", "H"]
}

def shortest_path(start, end):
    queue = [[start]] 
    visited = set() 
    
    while queue:
        path = queue.pop(0)  
        node = path[-1]      

        if node == end:
            return path 
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:  
                new_path = path + [neighbor] 
                queue.append(new_path)  

print("Available locations:")
for i, j in graph.items():
    print(f"{i}: {j}")

start = input(f"Where would you like to start?\n").upper()
end = input(f"Where do you want to go?\n").upper()
path = shortest_path(start, end)

print(f"The shortest path from {start} to {end} is: {' -> '.join(path)}")
