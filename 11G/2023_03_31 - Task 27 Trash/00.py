'''
    99) (Досрочный ЕГЭ-2022) В городе M расположена кольцевая автодорога длиной в N километров с движением в обе стороны. На каждом километре автодороги расположены пункты приема мусора определенной вместимости. В пределах кольцевой дороги в одном из пунктов сборки мусора собираются поставить мусороперерабатывающий завод таким образом, чтобы стоимость доставки мусора была минимальной. Стоимость доставки мусора вычисляется как вместимость пункта сбора, умноженная на расстояние от пункта сбора мусора до мусороперерабатывающего завода. Если мусороперерабатывающий завод находится рядом с пунктом сбора, расстояние считается нулевым. Пункты сбора мусора нумеруются с 1 до N. Рядом с каким пунктом сбора мусора нужно поставить мусороперерабатывающий завод?
Входные данные: Даны два входных файла: файл A (27-99a.txt) и файл B (27-99b.txt), каждый из которых содержит в первой строке натуральное число N – количество контейнеров для мусора (100 ≤ N ≤ 5000000). В каждой из следующих N строк записано одно целое число в диапазоне от 1 до 1000 – количество килограммов мусора, которое производится на одном пункте приёма мусора.
Пример входного файла:
6
8
20
5
13
7
19
Для данного примера ответ — 6 (минимальная стоимость доставки мусора 7·1 + 13·2 + 5·3 + 20·2 + 8·1 + 19·0 = 96).
В ответе укажите два числа: сначала искомый номер контейнера для файла А, затем для файла B.
'''

d = list(map(int, open('27-99b.txt').readlines()))

n = d[0]
del d[0]

ans = []
for z in range(n):
    if (z % 1 == 0):
        print(z, z/n*100)
    s = 0
    for i in range(n):
        s += d[i] * min(abs(z-i), abs(n-z+i))
    ans.append(s)
    
print(ans.index(min(ans)), min(ans), ans)

