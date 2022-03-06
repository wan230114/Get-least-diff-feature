#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# @ Author: Chen Jun
# @ Author Email: 1170101471@qq.com
# @ Created Date: 2022-03-06, 21:41:05
# @ Modified By: Chen Jun
# @ Last Modified: 2022-03-06, 22:11:17
#############################################

# %%

import itertools
import pandas as pd

in_file = "./a.txt"

df = pd.read_table(in_file, index_col=0)
df

# %%
# 测试两者的是否不同
# 区分 1 和 2
df.iloc[:, 0] != df.iloc[:, 1]
# 区分 2 和 3
df.iloc[:, 0] != df.iloc[:, 1]
dict(df.iloc[:, 0] != df.iloc[:, 1])

# %%
# 获取两者对比且不同的新矩阵
D = {}
for x, y in itertools.combinations(list(df.columns), 2):
    # D[(x, y)] = df[df.loc[:, x] != df.loc[:, y]].index.values
    D[f"{x} vs {y}"] = dict(df.loc[:, x] != df.loc[:, y])

tezheng = pd.DataFrame(D)
tezheng = tezheng.astype("int")

tezheng.to_csv("tezheng.csv", index_label="compare diff stat")
tezheng
# %%
# 找出矩阵中哪些行满足尽可能多的不同
c = tezheng.sum().sort_values(ascending=False)
r = tezheng.sum(axis=1).sort_values(ascending=False)

tezheng = tezheng.loc[r.index, c.index]
tezheng.to_csv("tezheng.sort.csv", index_label="compare diff stat")

# %%
cutoff = 0

(tezheng.iloc[:2, :].sum(axis=0) == 0).sum()
(tezheng.iloc[:2, :].sum(axis=0) == 0).sum() <= cutoff

# %%
# 计算和直到列之和满足至少大于1
for x in range(1, tezheng.shape[0]):
    stat = (tezheng.iloc[:x, :].sum(axis=0) == 0).sum() <= cutoff
    if stat:
        print(*tezheng.index[:x], sep="\n")
        break

# %%
