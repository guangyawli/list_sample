# This is a sample Python script.
from itertools import count

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

demolist2 = ['芭樂', '鳳梨']
demolist3 = ['柳丁', '蘋果']


def list_sample():
    # 宣告空集合
    demolist = []
    samplelist = ['梨子']

    demolist.append('西瓜')
    print('使用 append 加入元素:')
    print(demolist)
    print('使用 append 加入串列:')
    samplelist.append(demolist3)
    print(samplelist)

    print('使用 extend 加入元素:')
    demolist.extend(demolist2)
    print(demolist)
    print()

    print('以 加法 使用串列 :')
    demolist = demolist2 + demolist3
    print(demolist)
    print('以 乘法 使用串列:')
    demolist = demolist2 * 3
    print(demolist)

    print()
    print('以 insert() 加入元素 :')
    demolist.insert(3, '芒果')
    print(demolist)

    print('以 remove() 移除元素 :')
    demolist.remove('芭樂')
    print(demolist)

    print()
    print('以 count 計算元素  芭樂 在串列中出現幾次:')
    print(demolist.count('芭樂'))

    print()
    #清除 list
    demolist.clear()
    print('以 clear() 移除元素 :')
    print(demolist)

    if demolist :
        print('demolist is not empty')
    else:
        print('demolist is empty')

    # 刪除串列 del
    print()
    del demolist
    print('以 del 移除list :')
    try:
        demolist
    except NameError:
        print('demolist is not exist')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list_sample()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
