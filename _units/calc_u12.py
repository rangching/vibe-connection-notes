"""EP12 AI 能當你的朋友嗎？練習題答案。
核心式：兩個振子的相位耦合（Kuramoto 兩體）
  dθ1/dt = ω1 + K1·sin(θ2-θ1)   K1：你願意調整多少
  dθ2/dt = ω2 + K2·sin(θ1-θ2)   K2：對方願意調整多少
  可鎖頻條件 |ω2-ω1| ≤ K1+K2；鎖定後共同頻率 Ω = (K2·ω1 + K1·ω2)/(K1+K2)
  你自己移動的量 Ω-ω1 = K1/(K1+K2)·(ω2-ω1)：K1=0（只有對方在配合）時你完全不動。
數值是示意的假設值。另含全書 40 項行動的分布（Actions for Impact）。"""
import math

def locked(w1, w2, K1, K2):
    return (K2 * w1 + K1 * w2) / (K1 + K2)

def simulate(w1, w2, K1, K2, T=200.0, dt=0.001):
    t1, t2 = 0.0, 2.0
    n = int(T / dt)
    for _ in range(n):
        d1 = w1 + K1 * math.sin(t2 - t1)
        d2 = w2 + K2 * math.sin(t1 - t2)
        t1 += d1 * dt
        t2 += d2 * dt
    return d1, d2

w1, w2 = 1.0, 1.4
cases = {"雙向 K1=K2=0.3": (0.3, 0.3), "單向 K1=0,K2=0.6": (0.0, 0.6), "偏一方 K1=0.1,K2=0.5": (0.1, 0.5)}
for name, (K1, K2) in cases.items():
    Om = locked(w1, w2, K1, K2)
    d1, d2 = simulate(w1, w2, K1, K2)
    print(f"{name:<20} 理論 Ω={Om:.4f}  模擬 θ1'={d1:.4f} θ2'={d2:.4f}  你移動 {Om - w1:.4f}  你的調整占比 {K1/(K1+K2):.3f}")
print("Q3 雙向 Ω                            =", round(locked(w1, w2, 0.3, 0.3), 2))
print("Q4 偏一方時你移動的量                =", round(locked(w1, w2, 0.1, 0.5) - w1, 4))
print("Q5 Δω=0.4 時鎖頻所需最小 K1+K2       =", round(abs(w2 - w1), 2))
# 失鎖對照：K1+K2 < Δω
d1, d2 = simulate(w1, w2, 0.1, 0.2)
print(f"   K1+K2=0.3<0.4：末端 θ1'={d1:.3f} θ2'={d2:.3f}（不相等＝沒鎖住）")

# 全書 40 項行動
acts = {"點燃連結": [1, 3, 4, 3], "維繫連結": [1, 3, 3, 4], "擴大連結": [1, 4, 4, 4, 5]}
total = sum(sum(v) for v in acts.values())
for k, v in acts.items():
    print(f"   {k}: {sum(v)} 項，占 {100*sum(v)/total:.1f}%")
print("Q1 總數                              =", total)
print("Q2 擴大連結占比(%)                   =", round(100 * sum(acts['擴大連結']) / total, 1))
print("Q6 每週試 2 項，試完 40 項需幾週     =", math.ceil(40 / 2))
