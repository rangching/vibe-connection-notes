"""EP5 練習題答案：聯絡的節奏。
爆發性係數 B = (sigma - mu) / (sigma + mu)，mu、sigma 為「兩次互動間隔」的平均與（母體）標準差
（Goh & Barabási 2008：規律 B=-1、隨機泊松 B≈0、極度爆發 B→1）。
書中數字：關懷信件 3.5% → 1.8%（Motto & Bostrom 2001）、7 年後 30%／一半（Mollenhorst 等 2014）、
重新聯絡不到 1/3 寄出、90% 覺得有趣、16,000 席 43 秒售罄。"""
import math
import statistics as st

def burstiness(gaps):
    mu = st.mean(gaps)
    sigma = st.pstdev(gaps)
    return (sigma - mu) / (sigma + mu), mu, sigma

# Q1 關懷信件：相對降幅
a, b = 3.5, 1.8
print("Q1 相對降幅 (3.5-1.8)/3.5      =", round((a - b) / a * 100, 1), "%")
# Q2 絕對差距與「寄給幾人少一例」（NNT，粗估）
d = (a - b) / 100
print("Q2 絕對差距                    =", round(a - b, 1), "個百分點")
print("   1 / 絕對差距（NNT）          =", round(1 / d, 1))

# Q3 每 7 天聯絡一次（完全規律）
B, mu, sg = burstiness([7] * 10)
print("Q3 規律每週一次 B              =", round(B, 3))

# Q4 假設：一年 10 次互動，間隔（天）大多很短、偶爾很長
gaps = [1, 1, 2, 1, 120, 1, 2, 1, 1, 200]
B, mu, sg = burstiness(gaps)
print("Q4 爆發型間隔", gaps)
print("   mu =", round(mu, 2), " sigma =", round(sg, 2), " B =", round(B, 3))

# Q5 7 年後只剩一半還在生活中：假設每年保留率固定 r，r^7 = 0.5
r = 0.5 ** (1 / 7)
print("Q5 每年保留率 r                =", round(r, 4), "→ 每年流失", round((1 - r) * 100, 1), "%")
r30 = 0.3 ** (1 / 7)
print("   （同一角色 30%：每年保留率", round(r30, 4), "）")

# Q6 假設 1,000 人寫好重新聯絡的訊息，正好 1/3 寄出，其中 90% 覺得有趣
sent = 1000 / 3
print("Q6 寄出", round(sent, 1), "人；覺得有趣", round(sent * 0.9))

# Q7 Monty Python 2013：16,000 席 43 秒售罄
print("Q7 每秒售出座位                =", round(16000 / 43, 1))
