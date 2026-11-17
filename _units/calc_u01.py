"""EP1 練習題答案：Kuramoto 秩序參數與四種波長的組合數。
r e^{iψ} = (1/N) Σ e^{iθ_j}；兩振子相差 Δ 時 r = |cos(Δ/2)|；
Lorentz 分布（半寬 γ）的平均場解：K_c = 2γ，K > K_c 時 r = sqrt(1 - K_c/K)。"""
import cmath, math
from itertools import combinations

def order(thetas_deg):
    z = sum(cmath.exp(1j*math.radians(t)) for t in thetas_deg)/len(thetas_deg)
    return abs(z)

print("Q1 兩振子相差 60°，r        =", round(order([0, 60]), 3))
print("Q2 四振子 0/90/180/270°，r  =", round(order([0, 90, 180, 270]), 3))
print("Q3 三振子 0/0/90°，r         =", round(order([0, 0, 90]), 3))
g = 0.5; Kc = 2*g
print("Q4 γ=0.5 的臨界耦合 K_c     =", Kc)
print("Q5 γ=0.5、K=2 時 r          =", round(math.sqrt(1-Kc/2), 3))
n_sub = sum(1 for k in range(1, 5) for _ in combinations(range(4), k))
print("Q6 四種波長至少共振一種的組合數 =", n_sub, "（2^4 - 1）")
print("補 ATUS 男性 18%→27% 相對增幅 =", round((27-18)/18*100, 1), "%")
print("補 ATUS 女性 16%→25% 相對增幅 =", round((25-16)/16*100, 1), "%")
print("補 假設每段對話錯頻機率 0.5、獨立，5 段至少一次錯頻 =", round(1-0.5**5, 4))
