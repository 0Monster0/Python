# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 19:28
# @File    : ShellSort.py
# detail

from generateArrayHelper import generateArray
from InsertSort import insert_sort

'''
希尔排序(Shell Sort)是插入排序的一种。(也叫“最小增量排序”)
也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。
希尔排序是非稳定排序算法。该方法因DL．Shell于1959年提出而得名。
希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
'''
def shell_sort(lists):
    step = 2
    gap = len(lists) / step
    while gap > 0:
        for startpostion in range(gap):
            insert_sort(lists, startpostion, gap)
            print("After increments of size", gap,
                  "The list is", lists)
        gap //= step
    return lists

# def shell_sort(lists):
#     count = len(lists)
#     step = 2
#     group = count / step
#     while group > 0:
#         for i in range(0, group):
#             j = i + group
#             while j < count:
#                 k = j - group
#                 key = lists[j]
#                 while k >= 0:
#                     if lists[k] > key:
#                         lists[k+group] = lists[k]
#                         lists[k] = key
#                     k -= group
#                 j += group
#         group /=step
#     return lists

new_lists = shell_sort(generateArray(10))
print(new_lists)

