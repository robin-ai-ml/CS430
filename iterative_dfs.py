"""
iterative_dfs.py

Implements an iterative depth-first search on a graph using a stack.

This iterative DFS matches the behavior of a recursive DFS traversal, 
ensuring each node is visited only once by keeping track of nodes 
already visited.

A dictionary tracks the parent of each node to represent the DFS 
forest. The same DFS order and forest structure as recursive DFS is 
generated.

Author: Project Group#10 (Team members: Qiuping, Bin Zou, Xiaonan Peng)
"""


from collections import defaultdict

## @brief implement a iterative DFS using stack in a linear time
#  @param graph
#  @param start_node
#  @return pre_ordered list
#          parent map     parent[adjacent node] -> parent node set
def iterative_dfs(graph, start_node):
    stack = [str(start_node)]
    visited_node_list = set()
    adjacent2parent_dict = defaultdict(lambda: None)
    pre_order = []
    post_order = []

    while stack:
        current_node = stack[-1]
       
        if current_node not in visited_node_list:
            visited_node_list.add(current_node)
            pre_order.append(current_node)

            if current_node in graph:
                
                for adjacent_node in graph[current_node][::-1]:
                    if adjacent_node not in visited_node_list:
                        adjacent2parent_dict[adjacent_node] = current_node
                        stack.append(adjacent_node)
        else:
            node = stack.pop()
            if node not in post_order:
              post_order.append(node)
              
    return post_order, pre_order, adjacent2parent_dict


## @brief   Reads an input file and returns a graph and a source node for DFS.
#  @param   file_name (str): The name of the input file.
#  @param   graph (list): A list of lists representing the graph. 
#           Each inner list contains the nodes connected to the corresponding node.
#  @return s (int): The source node for DFS.
##
def read_input(file_name):
    graph = {}
    with open(file_name, 'r') as file:
        n = int(file.readline().strip()) #First line - n (number of nodes)
        m = int(file.readline().strip()) #Second line - m (number of edges)

        for _ in range(m):  #Next m lines - u<space>v, where (u, v) ∈ E and 0 ≤ u, v ≤ n − 1
            u, v = file.readline().strip().split()
            if(u in graph): 
               graph[u].append(v)
            else: 
               graph[u] = [v]  
              
        s = int(file.readline().strip()) #Last line - s (Source node for DFS), where 0 ≤ s ≤ n − 1
        file.close()
    return graph, s


def write_output(file_name, pre_order, post_order):
    with open(file_name, 'w') as file:
        for node in pre_order: #First n lines - Pre-order of DFS
            file.write(f"{node}\n")
        for node in post_order:#Next n lines - Post-order of DFS
            file.write(f"{node}\n")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Iterative DFS Traversal")
    parser.add_argument("-i", "--input", help="input file name", required=True)
    args = parser.parse_args()
    input_file = args.input
    output_file = f"{input_file.split('.')[0]}_output.txt"

    graph, start_node = read_input(input_file)
    print("graph:",graph, "start_node:",start_node)
    post_order, pre_order, parent_map = iterative_dfs(graph, start_node)
    write_output(output_file, pre_order, post_order)
    print("pre_order:", pre_order,"post_order:", post_order)
