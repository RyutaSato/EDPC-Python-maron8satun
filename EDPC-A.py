
"""
title: Educational DP Contest / DP まとめコンテスト / A Frog1
問題URL: https://atcoder.jp/contests/dp/tasks/dp_a

N個の足場があって、i番目の足場の高さは hiです。
最初、足場1にカエルがいて、ぴょんぴょん跳ねながら足場 Nへと向かいます。カエルは足場 iにいるときに
・足場 iから足場 i+1へと移動する (そのコストは |hi−hi+1|)
・足場 iから足場 i+2へと移動する (そのコストは |hi−hi+2|)
のいずれかの行動を選べます。カエルが足場 1から足場 Nへと移動するのに必要な最小コストを求めよ。

the answer is made by maron8satun(http://maron8satun.com/)
"""


def Solve1(h: list):

    lh = len(h)
    one_step = [abs(h[i] - h[i + 1]) for i in range(lh - 1)]
    two_step = [abs(h[i] - h[i + 2]) for i in range(lh - 2)]
    DP = [0, one_step[0]]
    for i in range(1, lh - 1):
        DP.append(min(DP[i] + one_step[i], DP[i - 1] + two_step[i - 1]))
    print(DP[-1])


def Solve2(h: list):
    dp = [0 for _ in range(len(h))]  # dpを0埋め

    for i in range(1, len(h)):
        dp[i] = dp[i - 1] + abs(h[i] - h[i - 1])  # 1つ前からジャンプ
        if i > 1:
            dp[i] = min(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]))  # 2つ前からジャンプ

    print(dp[-1])  # answer


_ = int(input())
h = [int(i) for i in input().split()]

n = 6
h = [30, 10, 60, 10, 60, 50]
Solve1(h)
Solve2(h)
# >> 40
