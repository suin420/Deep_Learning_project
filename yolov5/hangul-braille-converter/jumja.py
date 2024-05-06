#!/usr/bin/env python
# coding: utf-8
# %%
import hbcvt


# %%
def to_vector(result):
    result = hbcvt.h2b.text(result)
    for i in range(len(result)):
        for j in (result[i][1]):
            print(j)


# %%


def to_jumja(result):
    result = hbcvt.h2b.text(result)
    jum_lst = []

    for i in range(len(result)):
        for j in (result[i][1]):
            #print(j[1])
            if j[1] !=1:

                for l in range(len(j[1])):
                    jum = j[1][l]

                    jum = ['○' if x==0 else '●' for x in jum]
                    jum_lst.append(jum)


    for i in range(len(jum_lst)):
        try:
            print(f"{jum_lst[i][0]} {jum_lst[i][3]}")
            print(f"{jum_lst[i][1]} {jum_lst[i][4]}")
            print(f"{jum_lst[i][2]} {jum_lst[i][5]}")
            
        except:
            continue

