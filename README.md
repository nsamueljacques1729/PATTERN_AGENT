# Pattern Agent

This repository explores pattern search agents on a 3x3 grid, inspired by Android-style unlock patterns.

## Projects

### `eep First Search (DFS) backtracking agent.py`
- Implements a standard DFS/backtracking agent for valid grid patterns.
- Treats the pattern as a Hamiltonian-style path where each dot can be used once.
- Enforces jump restrictions: moves that skip over an intermediate dot are only allowed if that dot has already been visited.
- Collects all valid patterns between a configurable `min_length` and `max_length`.

### `Eulerian Agent.py`
- A variant that explores Eulerian-style paths on the same 3x3 grid.
- In this model, edges between dots cannot be reused, but nodes may be revisited.
- Still keeps the same intermediate-dot jump restrictions used by the standard agent.
- Useful for studying how line-based constraints change the search space.

### `EulerianPatternAgent.py`
- Contains both the original Hamiltonian-like `PatternAgent` and the Eulerian `EulerianPatternAgent`.
- Includes an interactive terminal menu to run either search model and compare results.
- Adds a safety limit for the Eulerian search to avoid excessive memory use when patterns explode exponentially.

## Grid layout

The 3x3 grid is represented as indices:

```
0 1 2
3 4 5
6 7 8
```

This index mapping is used throughout the code for moves and sample output.

## Usage

Run the scripts from the repository root with Python:

```bash
git clone <repo>
cd PATTERN_AGENT
python3 "eep First Search (DFS) backtracking agent.py"
python3 "Eulerian Agent.py"
python3 EulerianPatternAgent.py
```

## Notes

- The DFS agent enumerates valid unlock patterns with a configurable minimum and maximum length.
- The Eulerian version explores a different mathematical model: no line is drawn twice, but dots can be reused.
- The skip-node logic ensures diagonal and long straight-line moves follow real pattern-lock rules.

## License

No license is specified in this repository.
