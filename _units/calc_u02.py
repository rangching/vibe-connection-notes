"""EP2 練習題答案：社會關係模型（SRM）變異分解與書中倍數。
X_ij = μ + α_i + β_j + γ_ij + ε_ij；關係變異占比 = σ_γ² / (σ_α²+σ_β²+σ_γ²+σ_ε²)。"""
import random, statistics as st

# Q1 假設變異量（虛構情境）：行動者 0.20、對象 0.15、關係 0.55、誤差 0.10
va, vb, vg, ve = 0.20, 0.15, 0.55, 0.10
tot = va+vb+vg+ve
print("Q1 關係（這一對）占比          =", round(vg/tot, 3))
print("Q2 個人特質（行動者+對象）占比 =", round((va+vb)/tot, 3))

# 模擬驗證：20 人兩兩互評，看估計值是否接近設定（固定亂數種子）
random.seed(1)
N = 20
a = [random.gauss(0, va**.5) for _ in range(N)]
b = [random.gauss(0, vb**.5) for _ in range(N)]
X = {}
for i in range(N):
    for j in range(N):
        if i != j:
            X[i, j] = a[i]+b[j]+random.gauss(0, (vg+ve)**.5)
rows = [st.mean(X[i, j] for j in range(N) if j != i) for i in range(N)]
cols = [st.mean(X[i, j] for i in range(N) if i != j) for j in range(N)]
res = [X[i, j]-rows[i]-cols[j] for (i, j) in X]
print("   模擬：列平均變異≈", round(st.pvariance(rows), 3), " 殘差變異≈", round(st.pvariance(res), 3))

print("Q3 每項研究平均人數 35,000/300 =", round(35000/300, 1))
print("Q4 印度近一半 vs 美國 6%（以 0.5 計）倍數 =", round(0.5/0.06, 2))
print("Q5 假設隔四戶被點名機率 5%，隔壁（4 倍）=", 5*4, "%")
print("Q6 假設黨派敵意 60 分，降約 10% 後 =", round(60*0.9, 1))
print("補 三個內圈（盟友、玩伴、知己）的非空組合 =", 2**3-1, "；兩兩交集 =", 3)
