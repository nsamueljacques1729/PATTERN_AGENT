class PatternAgent:
    def __init__(self, min_length=4, max_length=9):
        self.min_length = min_length
        self.max_length = max_length
        
        # Define the 3x3 grid indices:
        # 0  1  2
        # 3  4  5
        # 6  7  8
        
        # Lookup table for 'illegal jumps' and the intermediate node they require.
        self.skip_nodes = {
            (0, 2): 1, (2, 0): 1,
            (0, 6): 3, (6, 0): 3,
            (0, 8): 4, (8, 0): 4,
            (1, 7): 4, (7, 1): 4,
            (2, 6): 4, (6, 2): 4,
            (2, 8): 5, (8, 2): 5,
            (3, 5): 4, (5, 3): 4,
            (6, 8): 7, (8, 6): 7
        }
        
        self.collected_patterns = []

    def _is_valid_move(self, current_node, next_node, visited):
        """Checks if moving from current_node to next_node is valid."""
        if next_node in visited:
            return False
        
        # Check if there is a node between them that hasn't been visited yet
        jump_pair = (current_node, next_node)
        if jump_pair in self.skip_nodes:
            required_node = self.skip_nodes[jump_pair]
            if required_node not in visited:
                return False # Invalid: skipped over an unvisited node
                
        return True

    def _dfs(self, current_node, current_path, visited):
        """Backtracking agent logic to explore paths."""
        # Collect pattern if it meets the minimum length requirement
        if len(current_path) >= self.min_length:
            self.collected_patterns.append(list(current_path))
            
        # Stop exploring if we reached max length
        if len(current_path) == self.max_length:
            return

        # Try moving to all possible 9 nodes
        for next_node in range(9):
            if self._is_valid_move(current_node, next_node, visited):
                # Action
                visited.add(next_node)
                current_path.append(next_node)
                
                # Recursion
                self._dfs(next_node, current_path, visited)
                
                # Backtrack (Undo action)
                current_path.pop()
                visited.remove(next_node)

    def collect_all_patterns(self):
        """Triggers the agent to collect patterns from all starting positions."""
        self.collected_patterns = []
        for start_node in range(9):
            visited = {start_node}
            self._dfs(start_node, [start_node], visited)
        return self.collected_patterns

# --- Execution ---
if __name__ == "__main__":
    agent = PatternAgent(min_length=4, max_length=9)
    print("Agent is collecting pattern combinations... Please wait.")
    all_patterns = agent.collect_all_patterns()
    
    print(f"\nSuccess! Total valid pattern combinations collected: {len(all_patterns):,}")
    
    # Showcase a few patterns of different lengths
    print("\nSample Patterns (Grid Indices 0-8):")
    for i in [0, 5000, 50000, 140000, len(all_patterns) - 1]:
        if i < len(all_patterns):
            print(f"Pattern #{i}: {all_patterns[i]}")