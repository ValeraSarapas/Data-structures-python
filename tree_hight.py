# https://gist.github.com/inkoit/8454d2b56e7a9347d7fc66715449e695
# Stepik, курс "Алгоритмы: теория и практика. Структуры данных", модуль 1, задача 2
# Задача: вычислить высоту дерева
# Вход: Корневое дерево с вершинами {0,...,n−1}, заданное как последовательность parent_0,...,parent_n−1, 
# где parent_i — родитель i-й вершины.
# Выход: высота дерева
Пример.
Вход:
5
4 -1 4 1 1
Выход:
3
корень 1
Пример.
Вход:
5
-1 0 4 0 3
Выход:
4
корень 0
# Первая строка -- количество вершин
n = int(input())

# Вторая строка -- массив, задающий отношения в дереве
nodes = [[int(s), -1] for s in input().split()]


# Рекурсивная функция обхода снизу вверх с записью уже известной глубины
def depth(i):
    if nodes[i][1] == -1:
        nodes[i][1] = 1 if nodes[i][0] == -1 else 1 + depth(nodes[i][0])
    return nodes[i][1]


# Высота дерева -- максимальная глубина из глубин вершин
print(max(depth(i) for i in range(n)))

# https://github.com/nikolaygurev/Data_structures/blob/master/basic/tree_height.py
def tree_height_bottom_up(parents):
    """Time complexity: O(n), where n = len(parents)"""
    depths = [-1] * (len(parents)) + [0]

    def count_depth(i):
        if depths[i] == -1:
            depths[i] = count_depth(parents[i]) + 1
        return depths[i]

    return max(count_depth(i) for i in range(len(parents)))


def main():
    n_ = input()
    parents = [int(i) for i in input().split()]

    print(tree_height_bottom_up(parents))


if __name__ == '__main__':
    main()

Python3. Вдохновившись идеями: Игоря Фукина о рекурсии от детей к родителям - здесь  и Ольги Ларькиной об использовании списка вместо словаря для сохранения глубин вершин - здесь ﻿ получил довольно компактное решение. 
Был еще компактный вариант кода с использованием @lru_cache, но валился на 24 тесте по времени. Буду признателен, за комментарий, почему не прошел этот вариант:
    
from functools import lru_cache
@lru_cache(maxsize=None)
def count(data, i):
    return (data[i] == -1 and 1 or count(data, data[i]) + 1)
num, data = int(input()), tuple(int(i) for i in input().split())
print(max(count(data, i) for i in range(num)))

Типа стэк без рекурсии
input()
s = {}
for i, v in enumerate(map(int, input().split())):
    s.setdefault(v, []).append(i)

sm = 0
stack = s[-1]
while stack:
    child = s.get(stack[-1])
    if child:
        stack.append(child.pop())
    else:
        sm = max(sm, len(stack))
        del stack[-1]

print(sm)

Одним циклом делаем список списков детей
Вторым циклом выравниваем дерево по порядку

Python 3
n = int(input())
parents = map(int, input().split())

tree = [[] for _ in range(n+1)]
for i, parent in enumerate(parents):
    tree[parent].append(i)

ravel_tree = [(-1, 0)]
for i, k in ravel_tree:
    for j in tree[i]:
        ravel_tree.append((j, k+1))
        
print(ravel_tree[-1][-1])

Не обязательно писать рекурсию, чтобы реализовать рекурсивное решение, ведь так?
Спускаемся по уровням, и считаем уровни.

length, parents = input(), [int(parent_str) for parent_str in input().split()]
children = [[] for i in parents]
children.append([])  # to locate root vertex, by default it's parent is -1.
for i, parent in enumerate(parents):
    children[parent].append(i)

tree_depth = 0
root = children[-1]
while root:
    new_roots = []
    for vertex in root:
        new_roots.extend(children[vertex])
    root = new_roots
    tree_depth += 1

print(tree_depth)

