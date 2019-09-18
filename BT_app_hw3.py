# File BT_app_hw3.py
# Author(s): xingqil, xxx

import BinaryTree_hw3 as bt

bt1 = bt.BinaryTree()     # an empty BinaryTree
bt1.insert(12)
bt1.insert(7)
bt1.insert(13)
bt1.insert(-4)

bt2 = bt.BinaryTree()     # an empty tree
print('bt2:', bt2)        # bt2:

print('bt1:', bt1)        # bt1: -4 7 12 13

print('bt1.sum():', bt1.sum())   # bt1.sum(): 28

bt3 = bt.BinaryTree()
bt3.insert(9)
bt3.insert(18)
bt3.insert(12)
bt3.insert(22)
bt3.insert(10)
bt3.insert(4)
bt3.insert(-1)
bt3.insert(7)
bt3.insert(8)
bt3.insert(8)        # should ignore duplicate
bt3.insert(8)        # should ignore duplicate
bt3.insert(10)
bt3.insert(6)
print('bt3:', bt3)

print('bt3.sum():', bt3.sum())

# 1.b
print('bt2.size():', bt2.size())    # should display 0
print('bt1.size():', bt1.size())    # should display 4
print('bt3.size():', bt3.size())    # should display 10

# 1.c
bt4 = bt.BinaryTree()
for k in range(5):
    bt4.insert(k)       # insert in ascending order!
print('\nbt2.print_pretty():')
bt2.print_pretty()      # should display no output

print('\nbt1.print_pretty():')
bt1.print_pretty()      # should display:
                        #         13
                        # 12
                        #         7
                        #                 -4

print('\nbt4.print_pretty():')
bt4.print_pretty()      # should display:
                        #                                 4
                        #                         3
                        #                 2
                        #         1
                        # 0

print('\nbt3.print_pretty():')
bt3.print_pretty()      # does the output make sense, given the
                        # order of inserts into bt3? Ans: The ouput do make sense

# 1.d
print('bt2.depth():', bt2.depth())    # should display 0
print('bt1.depth():', bt1.depth())    # should display 3
print('bt4.depth():', bt4.depth())    # should display 5
print('bt3.depth():', bt3.depth())    # does the output make sense? Ans: The output do make sense

# 1.e
print('bt1 == bt2:', bt1 == bt2)      # should be False
print('bt1 == bt1:', bt1 == bt1)      # should be True
bt5 = bt3          # bt5 and bt3 refer to the same tree!
print('bt5 == bt3:', bt5 == bt3)

# 1.f
print('bt1.min():', bt1.min())
print('bt1.max():', bt1.max())
print('bt1.mean():', bt1.mean())
print('bt2.min():', bt2.min())
print('bt2.max():', bt2.max())
print('bt2.mean():', bt2.mean())
print('bt3.min():', bt3.min())
print('bt3.max():', bt3.max())
print('bt3.mean():', bt3.mean())
print('bt4.min():', bt4.min())
print('bt4.max():', bt4.max())
print('bt4.mean():', bt4.mean())

# 3.a
print('18 in bt3:', 18 in bt3)
print('21 in bt3:', 21 in bt3)
print('13 in bt1:', 13 in bt1)
print('13 in bt3:', 13 in bt2)

# 3.b
bt3r = bt3           # copy or reference?
print('\nbt3r.print_pretty():')
bt3r.print_pretty()
print('bt3r == bt3:', bt3r == bt3)
print('bt3r is bt3:', bt3r is bt3)
bt3c = bt3.copy()    # copy or reference?
print('\nbt3c.print_pretty():')
bt3c.print_pretty()
print('bt3c == bt3:', bt3c == bt3)
print('bt3c is bt3:', bt3c is bt3)

# 3.c
bt3.negate()
print('\nbt3c.print_pretty():')
bt3.print_pretty()
