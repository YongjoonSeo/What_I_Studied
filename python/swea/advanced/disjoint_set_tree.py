def Make(char):
    return {char: char, 'rank': 0}

def Find(tree, char):
    if tree.get(char) == char:
        tree['root'] = char
        return char
    tree[char] = Find(tree, tree.get(char))
    return tree.get(char)

def Union(tree1, tree2):
    one = list(tree1.keys())[0]
    two = list(tree2.keys())[0]
    if tree1.get('rank') > tree2.get('rank'):
        tree1[Find(tree2, two)] = Find(tree1, one)
    else:
        tree2[Find(tree1, one)] = Find(tree2, two)
    if tree1.get('rank') == tree2.get('rank'):
        tree1['rank'] += 1


elements1 = ['a', 'd', 'e']
elements2 = ['b', 'f']

Tree1 = Make(elements1[0])
Union(Tree1, Make(elements1[1]))
print(Tree1)
Union(Tree1, Make(elements1[2]))

Tree2 = Make(elements2[0])
Union(Tree2, Make(elements2[1]))

print(Tree1)
print(Tree2)
print(Find(Tree1, elements1[2]))
print(Find(Tree2, elements2[1]))
