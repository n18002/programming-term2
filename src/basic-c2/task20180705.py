#　値段
sake_n = 200
tumami_n = 100
tori_n = 100
# 個数
sake_k = 2
tumami_k = 1
tori_k = 2
#　割引率
rate = 0.8
point = 150
# 計算
kaikei = (sake_n * sake_k) + (tumami_n) + ((tori_n * tori_k) * rate) - (point)
#　結果
print("買い物の合計は", kaikei, "円です")
