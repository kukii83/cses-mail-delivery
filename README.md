# cses-mail-delivery
Assignment 3 for Informatics ITS Graph Theory Class Group 5

## Fleury

---

## Hierholzer
Hierholzer's algorithm is an efficient linear-time algorithm used to find an Eulerian circuit or path in a graph. It operates by traversing unvisited edges to construct an initial cycle and iteratively discovering sub-tours from vertices with remaining unvisited edges. These sub-tours are then spliced directly into the main route until all edges in the graph have been visited exactly once.
To efficiently construct the circuit without expensive bridge checks, the algorithm utilizes a Hierholzer stack/DFS traversal technique. Prior to execution, the algorithm verifies that all vertex degrees are even and that all edges belong to a single connected component; if a vertex has an odd degree or the graph is disconnected, the algorithm terminates immediately and returns IMPOSSIBLE

### Prerequisites
- Python 3.x interpreter installed
- Standard Python built-in libraries

### Instructions
- Copy the code
- Open your compiler(make sure it's not DevC++ or anything since this is a Phyton code)
- Paste the code
- Run the code
- Copy the sample input from the problem set given in the assignment

### Results
Here are the results from the graph in the assignment:

- **Initial State** |
The graph consists of 6 vertices (1, 2, 3, 4, 5, 6) and 8 edges. Pre-check verifies all degrees are even (1:2, 2:4, 3:4, 4:2, 5:2, 6:2) and all edges are connected. The algorithm targets traversing all 8 edges starting from Node 1.   

- **Iteration 1: Edge (1, 2)** |
Starting from Node 1, the algorithm traverses the first available unvisited edge (1, 2). Node 1 is pushed to the path stack, moving current position to Node 2.   

- **Iteration 2: Edge (2, 3)** |
At Node 2, candidate edges are (2-3, 2-4, 2-6). The algorithm selects edge (2, 3). Node 2 is pushed, moving current position to Node 3.   

- **Iteration 3: Edge (3, 5)** |
At Node 3, candidate edges are (3-5, 3-6). The algorithm selects edge (3, 5). Node 3 is pushed, moving current position to Node 5.   

- **Iteration 4: Edge (5, 4)** |
At Node 5, the only available unvisited edge is (5, 4). The algorithm takes edge (5, 4), pushing Node 5 and moving current position to Node 4.   

- **Iteration 5: Edge (4, 2)** |
At Node 4, the only available unvisited edge is (4, 2). The algorithm takes edge (4, 2), pushing Node 4 and returning to Node 2.   

- **Iteration 6: Edge (2, 6)** |
Back at Node 2, the main tour encounters remaining unvisited edges (2-6). The algorithm initiates a sub-tour along edge (2, 6), pushing Node 2 and moving current position to Node 6.   

- **Iteration 7: Edge (6, 3)** |
At Node 6, the only available unvisited edge is (6, 3). The algorithm takes edge (6, 3), pushing Node 6 and moving current position to Node 3.   

- **Iteration 8: Edge (3, 1)** |
At Node 3, the final remaining edge (3, 1) is taken. The algorithm returns to start Node 1, completing and splicing the sub-tour into the main circuit.   

- **Iteration 9: Complete** |
With all 8 edges traversed, no unvisited edges remain across any vertex. The stack unfolds to construct the final Eulerian circuit: 1 $\rightarrow$ 2 $\rightarrow$ 3 $\rightarrow$ 5 $\rightarrow$ 4 $\rightarrow$ 2 $\rightarrow$ 6 $\rightarrow$ 3 $\rightarrow$ 1. The process terminates successfully.


---

HUSSEIN THIS IS YOUR SPOT

---

AI tools usage disclosure:

https://claude.ai/share/630bca29-ed64-4040-8697-890326603d80

