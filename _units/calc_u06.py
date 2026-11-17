"""EP6 練習題答案：亦敵亦友。
矛盾指數（Griffin 公式，Thompson, Zanna & Griffin 1995）：A = (P + N)/2 - |P - N|，
P = 正面感受強度、N = 負面感受強度（此處用 1–5 分的假設評分）。
書中數字：Gottman 69% 永久問題、Rasheed 驅逐 5→0、禁賽 7→0、勝率 61%→77%、
Ginsburg 與 Scalia 在 5–4 判決中 93% 對立、Allison 預留 37 分鐘 vs 作者遲到 37 秒。"""

def ambivalence(P, N):
    return (P + N) / 2 - abs(P - N)

quadrants = {
    "正面（優點高、缺點低）": (5, 1),
    "負面（優點低、缺點高）": (1, 5),
    "冷漠（兩者都低）": (1, 1),
    "矛盾（兩者都高）": (5, 5),
}
for name, (P, N) in quadrants.items():
    print(f"Q1 {name:<14} P={P} N={N}  A = {ambivalence(P, N)}")

# Q2 假設：P=4、N=3 的同事
print("Q2 A(4,3)                      =", ambivalence(4, 3))

# Q3 Gottman：100 次衝突中的永久問題，以及永久：可解 的比值
print("Q3 100 次衝突中的永久問題        =", round(100 * 0.69))
print("   永久 / 可解                  =", round(69 / 31, 2))

# Q4 活塞隊勝率 61% → 77%：換算成 82 場例行賽（假設整季都維持該勝率）
w0, w1 = 82 * 0.61, 82 * 0.77
print("Q4 82 場勝場", round(w0, 1), "→", round(w1, 1), "，多", round(w1 - w0, 1), "場")
print("   勝率提升（百分點）            =", 77 - 61)

# Q5 Ginsburg 與 Scalia：假設某年有 20 件 5–4 判決
print("Q5 20 件中對立的件數（期望值）    =", round(20 * 0.93, 1))

# Q6 Allison 預留 37 分鐘，作者遲到 37 秒就不高興：緩衝是遲到的幾倍
print("Q6 37 分鐘 ÷ 37 秒              =", 37 * 60 // 37)
