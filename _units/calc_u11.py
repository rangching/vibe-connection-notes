"""EP11 家庭傳統：練習題答案與「家族樹變豆莖」驗算。
書中句子（〈Everything Is Relative〉）：父母生兩個而不是三個、我們也一樣，孩子少 1 個手足，但少 5 個堂表兄弟姊妹。
書中沒寫計算假設，這裡用三種模型驗算：
  (A) 固定家庭人數，只算父母一方：手足 m-1，堂表 (m-1)·m
  (B) 固定家庭人數，父母雙方都算（配偶家也生 m 個）：堂表 2(m-1)·m
  (C) 家庭人數隨機（Poisson，平均 m），隨機抽一個孩子，只算父母一方：
      大家庭的孩子比較容易被抽到（大小偏差），期望手足數 = E[N²]/E[N]-1 = m，
      父母的期望手足數也是 m，每人平均生 m 個 → 期望堂表數 = m²
"""
import random

def det(m):
    sib = m - 1
    return sib, (m - 1) * m, 2 * (m - 1) * m

for m in (3, 2):
    s, c1, c2 = det(m)
    print(f"(A/B) m={m}: 手足 {s}，堂表 單邊 {c1}、雙邊 {c2}；(C) 手足 {m}，單邊堂表 {m*m}")

dA = det(3)[1] - det(2)[1]
dB = det(3)[2] - det(2)[2]
dC = 3 * 3 - 2 * 2
print("Q1 模型 A 少幾個堂表                 =", dA)
print("Q2 模型 B 少幾個堂表                 =", dB)
print("Q3 模型 C 少幾個堂表 3²-2²           =", dC)

def poisson(lam, rng):
    # Knuth 演算法
    import math
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1

def simulate(m, n_fam=200_000, seed=1):
    rng = random.Random(seed)
    tot_sib = tot_cous = n_kids = 0
    for _ in range(n_fam):
        parents_kids = [poisson(m, rng) for _ in range(poisson(m, rng))]  # 祖父母的每個孩子各生幾個
        total = sum(parents_kids)
        for i, k in enumerate(parents_kids):
            cous = total - k
            tot_sib += k * (k - 1)
            tot_cous += k * cous
            n_kids += k
    return tot_sib / n_kids, tot_cous / n_kids

for m in (3, 2):
    s, c = simulate(m)
    print(f"   蒙地卡羅 (C) m={m}: 平均手足 {s:.2f}，平均單邊堂表 {c:.2f}")

# 家庭晚餐：典型一頓約 18 分鐘
print("Q4 每天一起吃，一週分鐘數 18×7      =", 18 * 7)
print("   每週一頓愉快晚餐占天天吃的比例(%) =", round(100 / 7, 1))
# 81% 延續舊傳統、74% 引入新傳統：假設 200 人
print("Q5 200 人中延續舊傳統的人數          =", round(200 * 0.81))
print("   200 人中引入新傳統的人數          =", round(200 * 0.74))
# 感恩練習：每週一次 vs 每天，一年次數
print("Q6 一年 每天 365 次 ÷ 每週 52 次    =", round(365 / 52, 2))
