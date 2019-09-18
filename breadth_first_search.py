# File breadth_first_search.py
# Author(s): xingqil, xxxx

# 1.a (function definition)
'''
def BFS(G, root, target): # Pythonish pseudocode
   S.add(root)
   T.add(root, None)      # value, parent
   Q = [root]
   while Q:
      cur = Q.pop(0)
      if cur is target:
         return cur parent list
      for v in G[cur]:
         if v not in S:
            S.add(v)
            T.add(v, cur)
            Q += [v]
'''

def BFS(G, root, target):
    S = {root}
    T = {root: None}
    Q = [root]

    while Q:
        cur = Q.pop(0)

        if cur == target:
            res_list = []
            while cur is not None:
                res_list.append(cur)
                cur = T[cur]
            res_list.reverse()

            return res_list

        for v in G[cur]:
            if v not in S:
                S.add(v)
                T[v] = cur
                Q.append(v)


# 1.c (function definitions)
def BFS_con_comps(G):
    # return a list of connected components in G,
    # where each connected component is a sorted
    # list of nodes

    all_node_set = set(G.keys())

    res_list = []
    while all_node_set:
        root = all_node_set.pop()

        S = {root}
        Q = [root]

        while Q:
            cur = Q.pop(0)

            for v in G[cur]:
                if v not in S:
                    S.add(v)
                    Q.append(v)
                    all_node_set.remove(v)

        res_list.append(list(sorted(S)))

    res_list = sorted(res_list, key=lambda x: x[0])
    return res_list
   

def print_con_comps(G_cc):  # display connected components
    print('graph contains', len(G_cc), 'connected components:')
    for x, y in enumerate(G_cc):
        print("\t{}: {}".format(x + 1, y))


def main():

    # 1.a (test code)
    G = { 'A' : [ 'B', 'J', 'Me' ],
          'B' : [ 'A' ],
          'C' : [ 'D', 'P' ],
          'D' : [ 'C', 'O' ],
          'E' : [ 'F', 'J', 'K' ],
          'F' : [ 'E', 'M' ],
          'G' : [ 'K', 'S', 'Ed' ],
          'H' : [ 'O', 'U' ],
          'Me': [ 'A', 'I', 'N', 'V' ],
          'I' : [ 'Me', 'Q' ],
          'J' : [ 'A', 'E', 'L', 'Q', 'W' ],
          'K' : [ 'E', 'G' ],
          'L' : [ 'J', 'W' ],
          'M' : [ 'E', 'S', 'T' ],
          'N' : [ 'Me', 'V' ],
          'O' : [ 'H', 'D' ],
          'P' : [ 'C', 'U' ],
          'Q' : [ 'I', 'J', 'X', 'Y' ],
          'R' : [ 'Ed' ],
          'S' : [ 'G', 'M', 'Y', 'Z' ],
          'T' : [ 'M' ],
          'U' : [ 'H', 'P' ],
          'V' : [ 'Me', 'N' ],
          'W' : [ 'J', 'L' ],
          'X' : [ 'Q', 'Y' ],
          'Y' : [ 'Q', 'S', 'X', 'Z' ],
          'Ed': [ 'G', 'R', 'Z' ],
          'Z' : [ 'S', 'Y', 'Ed' ] }
    print('Shortest path from Me to Ed:', BFS(G, 'Me', 'Ed'))

    # 1.b (test code)
    print('Shortest path from A to I:  ', BFS(G, 'A', 'I'))
    print('Shortest path from B to R:  ', BFS(G, 'B', 'R'))
    print('Shortest path from C to H:  ', BFS(G, 'C', 'H'))
    print('Shortest path from M to T:  ', BFS(G, 'M', 'T'))

    # 1.c (test code)
    # connected components tests:
    G2 = { 'A': ['B', 'C'],
          'C': ['A'],
          'E': ['F'],
          'D': [],
          'B': ['A'],
          'F': ['E'] }
    G2_cc = BFS_con_comps(G2)
    print_con_comps(G2_cc)
    G_cc = BFS_con_comps(G)
    print_con_comps(G_cc)


if __name__ == '__main__':
    main()
