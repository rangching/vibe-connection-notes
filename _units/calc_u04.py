"""EP4 練習題答案：第一印象的樣本太小。
樣本均值 mu_hat = (1/n) sum x_i，標準誤 SE = sigma / sqrt(n)。
數字來源：0.1 秒（Willis & Todorov 2006）、15 分鐘（Frieder 等 2016）、
夏令營每個孩子平均 167 小時（Shoda, Mischel, Wright 1994）、Inklings 每週聚會 16 年（書中）。"""
import math
from itertools import combinations

# Q1 夏令營觀察時數 vs 看臉 0.1 秒
camp_s = 167 * 3600
print("Q1 167 小時 ÷ 0.1 秒           =", round(camp_s / 0.1))

# Q2 夏令營觀察時數 vs 面試 15 分鐘
print("Q2 167 小時 ÷ 15 分鐘          =", round(167 * 60 / 15))

# Q3 觀察次數從 4 次增加到 100 次，標準誤變成原來的幾分之幾
print("Q3 SE(100)/SE(4)               =", round(math.sqrt(4 / 100), 4))

# Q4 從 n=10 開始，要把誤差減半需要幾次觀察
n0 = 10
n_half = round(n0 / 0.5 ** 2)   # sigma/sqrt(n) = 0.5 * sigma/sqrt(n0)
print("Q4 誤差減半所需 n              =", n_half)

# Q5 假設：某營隊孩子只在 5 種情境中的 1 種（被大人處罰）會攻擊。
#     隨機看他 3 種「不同」情境，至少看到一次攻擊的機率
situations = list(range(5))      # 0 = 被大人處罰
combos = list(combinations(situations, 3))
hit = sum(1 for c in combos if 0 in c)
print("Q5 至少看到一次攻擊的機率       =", round(hit / len(combos), 4), f"({hit}/{len(combos)})")
print("   只看 1 種情境時的機率        =", 1 / 5)

# Q6 假設：同一情境重複看 n 次，偏誤不會變小（示範）
true_scores = [1, 1, 1, 1, -1]   # 4 種情境友善(+1)、1 種攻擊(-1)
true_mean = sum(true_scores) / len(true_scores)
print("Q6 真實平均（各情境等權）       =", true_mean)
print("   只在『被處罰』情境看 100 次的估計 =", -1.0, "→ 偏誤", round(-1.0 - true_mean, 2))

# Q7 Inklings：每週一次、16 年（假設每年 52 週）
print("Q7 Inklings 聚會次數（約）      =", 16 * 52)

# Q8 自我擴展：兩個圓半徑都變 1.5 倍，面積變幾倍
print("Q8 半徑 ×1.5 的面積倍數         =", round(1.5 ** 2, 2))
