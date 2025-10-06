import random
import matplotlib
import matplotlib.animation as animation
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

"""
图形化目标
1. 以柱状图显示数组内数据情况
2. 当前变量会被高亮未黄色
3. 被交换的两个变量标记成绿色
4. 已经安置好的变量标记为紫色
"""
matplotlib.use('TkAgg')

fig = plt.figure(figsize=(20, 6))
ax = fig.subplots()
s = random.sample(range(100), 20)
bars = ax.bar(range(0, len(s) * 2, 2), s, width=1.5)
ax.set_title("Bubble Sort Visualization")
ax.set_xlabel("Index")
ax.set_ylabel("Value")
texts = []
# 给每根柱子添加数值标签
for bar, val in zip(bars, s):
    height = bar.get_height()
    txt = ax.text(bar.get_x() + bar.get_width() / 2,
                  height + 1,
                  str(val),
                  ha='center',
                  va='bottom')
    texts.append(txt)


# 冒泡排序算法
def bubble_sort(t: list):
    for i in range(len(t) - 1):
        for j in range(len(t) - i - 1):
            # 返回当前列表、当前索引、尚未排序好的项的数量、是否交换
            yield t, j, len(t) - i, False
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]
                yield t, j, len(t) - i, True


# 动画更新函数
def update(frame):
    arr, pivot, border, swapped = frame

    # 重置每根柱子的颜色
    for i in range(len(arr)):
        bars[i].set_color("blue")
    bars[pivot].set_color("yellow")
    for i in range(border, len(arr)):
        bars[i].set_color("purple")
    if swapped:
        # 让被交换的两个柱子的数值、高度和颜色一起被修改
        bars[pivot].set_color("green")
        texts[pivot].set_text(arr[pivot])
        texts[pivot].set_y(arr[pivot] + 1)
        bars[pivot + 1].set_color("green")
        texts[pivot + 1].set_y(arr[pivot + 1] + 1)
        texts[pivot + 1].set_text(arr[pivot + 1])

    for bar_, val_ in zip(bars, arr):
        bar_.set_height(val_)

    return bars


if __name__ == '__main__':
    ani = FuncAnimation(fig, update, frames=bubble_sort(s), interval=500)
    plt.show()
