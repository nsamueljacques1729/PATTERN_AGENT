class PatternAgent:
    """Original Agent: Finds Standard Hamiltonian Patterns (Dots cannot be reused)."""
    def __init__(self, min_length=4, max_length=9):
        self.min_length = min_length
        self.max_length = max_length
        self.skip_nodes = {
            (0, 2): 1, (2, 0): 1, (0, 6): 3, (6, 0): 3,
            (0, 8): 4, (8, 0): 4, (1, 7): 4, (7, 1): 4,
            (2, 6): 4, (6, 2): 4, (2, 8): 5, (8, 2): 5,
            (3, 5): 4, (5, 3): 4, (6, 8): 7, (8, 6): 7
        }
        self.collected_patterns = []

    def _is_valid_move(self, current_node, next_node, visited):
        if next_node in visited: return False
        jump_pair = (current_node, next_node)
        if jump_pair in self.skip_nodes:
            if self.skip_nodes[jump_pair] not in visited: return False
        return True

    def _dfs(self, current_node, current_path, visited):
        if len(current_path) >= self.min_length:
            self.collected_patterns.append(list(current_path))
        if len(current_path) == self.max_length: return

        for next_node in range(9):
            if self._is_valid_move(current_node, next_node, visited):
                visited.add(next_node)
                current_path.append(next_node)
                self._dfs(next_node, current_path, visited)
                current_path.pop()
                visited.remove(next_node)

    def collect_all_patterns(self):
        self.collected_patterns = []
        for start_node in range(9):
            self._dfs(start_node, [start_node], {start_node})
        return self.collected_patterns


class EulerianPatternAgent:
    """Eulerian Agent: Finds paths where LINES cannot be reused, but DOTS can be."""
    def __init__(self, min_length=4, max_length=9, max_collected=200000):
        self.min_length = min_length
        self.max_length = max_length
        self.max_collected = max_collected
        self.skip_nodes = PatternAgent().skip_nodes # Borrow the same lookup table
        self.collected_patterns = []

    def _is_valid_move(self, current_node, next_node, visited_edges, visited_nodes):
        edge = tuple(sorted((current_node, next_node)))
        if edge in visited_edges: return False
            
        jump_pair = (current_node, next_node)
        if jump_pair in self.skip_nodes:
            if self.skip_nodes[jump_pair] not in visited_nodes: return False
        return True

    def _dfs(self, current_node, current_path, visited_edges, visited_nodes):
        if len(self.collected_patterns) >= self.max_collected: return

        if len(current_path) >= self.min_length:
            self.collected_patterns.append(list(current_path))
            
        if len(current_path) == self.max_length: return

        for next_node in range(9):
            if self._is_valid_move(current_node, next_node, visited_edges, visited_nodes):
                edge = tuple(sorted((current_node, next_node)))
                
                visited_edges.add(edge)
                added_new_node = False
                if next_node not in visited_nodes:
                    visited_nodes.add(next_node)
                    added_new_node = True
                    
                current_path.append(next_node)
                
                self._dfs(next_node, current_path, visited_edges, visited_nodes)
                
                current_path.pop()
                visited_edges.remove(edge)
                if added_new_node:
                    visited_nodes.remove(next_node)

    def collect_all_patterns(self):
        self.collected_patterns = []
        for start_node in range(9):
            visited_edges = set()
            visited_nodes = {start_node}
            self._dfs(start_node, [start_node], visited_edges, visited_nodes)
            if len(self.collected_patterns) >= self.max_collected:
                print(f"\n[!] SAFETY LIMIT REACHED: Stopped Eulerian search at {self.max_collected:,} patterns to save RAM.")
                break
        return self.collected_patterns

# --- Interactive Terminal Menu ---
if __name__ == "__main__":
    print("=========================================")
    print("  GRID PATTERN MINER AI  ")
    print("=========================================")
    print("Which mathematical model would you like to run?")
    print("  1. Standard Hamiltonian (Strict Dots - Max 389,112)")
    print("  2. Eulerian (Reusable Dots - Explodes exponentially!)")
    
    choice = input("\nEnter 1 or 2: ")
    
    if choice == '1':
        agent = PatternAgent(min_length=4, max_length=9)
        print("\nAgent is collecting Hamiltonian pattern combinations... Please wait.")
        all_patterns = agent.collect_all_patterns()
    elif choice == '2':
        # Setting max_length to 9 dots to keep the comparison fair
        agent = EulerianPatternAgent(min_length=4, max_length=9, max_collected=200000)
        print("\nEulerian Agent is collecting edge combinations... Please wait.")
        all_patterns = agent.collect_all_patterns()
    else:
        print("\nInvalid choice. Exiting.")
        exit()
        
    print(f"\nSuccess! Total valid combinations collected: {len(all_patterns):,}")
    print("\nSample Patterns (Grid Indices 0-8):")
    for i in [0, 500, 50000, 150000, len(all_patterns) - 1]:
        if i < len(all_patterns):
            print(f"Pattern #{i}: {all_patterns[i]}")