# 각 종이 전체에서 몇 %를 차지하는지 구한다.

# 출력: 종의 이름을 사전순으로, 비율을 소수점 4째자리까지

# 체크할 조건
# 최대 10000개 종, 최대 1000000그루의 나무 -> 입력이 많다
# 사전순으로 출력
# 소수점 4째자리까지 출력

# 모두 담아서 비율 구해서 출력한다.

import sys

def solution():
    lines = sys.stdin.readlines()
    species = dict()
    for line in lines:
        line = line.strip()
        if not species.get(line):
            species[line] = 1
        else:
            species[line] += 1
    total = sum(species.values())
    for tree in sorted(species.keys()):
        print('{0} {1:.4f}'.format(tree, species.get(tree) / total * 100))

if __name__ == '__main__':
    solution()