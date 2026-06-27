def _is_valid_move(self, current_node, next_node, visited_edges):
        """Eulerian version: Checks if the line segment has been used."""
        # Represent the edge as a sorted tuple so direction doesn't matter
        # (e.g., moving 0->1 is the same edge as 1->0)
        edge = tuple(sorted((current_node, next_node)))
        
        if edge in visited_edges:
            return False # Line already drawn!
            
        # Keep the skip_nodes logic for jumping over unvisited intermediate dots
        jump_pair = (current_node, next_node)
        if jump_pair in self.skip_nodes:
            required_node = self.skip_nodes[jump_pair]
            # In an Eulerian system, we check if the intermediate node has been 
            # touched yet by looking at the edge history, or we maintain a separate node tracker.
            
        return True