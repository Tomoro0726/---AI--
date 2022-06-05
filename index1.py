# 書記配列
vertical = ["1", "2", "3", "4", "5", "6", "7", "8"]
beside = ["a", "b", "c", "d", "e", "f", "g", "h"]
all = []
# マス目定義
for i in range(len(vertical)):
    for f in range(len(beside)):
        add = []
        add.append(beside[f]+vertical[i])
        add.append(0)
        all.append(add)
        f = f+1
    i = i+1
# マス目呼び出し関数


def cell(a, b):
    x = beside.index(a)+(int(b)-1)*len(vertical)
    return x


# 初期位置更新
all[cell("d", "4")][1] = 1
all[cell("e", "4")][1] = 2
all[cell("d", "5")][1] = 2
all[cell("e", "5")][1] = 1
# 打つことができる場所
# aはallを代入
# bは黒か白か


def next(a, b):
    # 返す変数設定
    x = []
    for i in range(len(vertical)):
        for i in range(len(beside)):
