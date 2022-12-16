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
