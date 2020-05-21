def pre(key):
    global result1
    if key != '.':
        result1 += key
    children = tree.get(key)
    if children:
        pre(children[0])
        pre(children[1])

def inorder(key):
    global result2
    children = tree.get(key)
    if children:
        inorder(children[0])
    if key != '.':
        result2 += key
    if children:
        inorder(children[1])

def post(key):
    global result3
    children = tree.get(key)
    if children:
        post(children[0])
        post(children[1])
    if key != '.':
        result3 += key

N = int(input())
tree = dict()
for i in range(N):
    temp = list(input().split())
    tree[temp[0]] = temp[1:]
result1 = result2 = result3 = ''

pre('A')
inorder('A')
post('A')

print(result1)
print(result2)
print(result3)