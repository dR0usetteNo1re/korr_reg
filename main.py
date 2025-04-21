from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

# 4 4 6 7 7 8 9 10 10 11
# 21 26 21 26 31 33 30 37 38 41
x = list(map(int, input("Введите ранжированный x - ").split()))
y = list(map(int, input("Введите ранжированный (относительно x) y - ").split()))
x_sq = [i ** 2 for i in x]
y_sq = [i ** 2 for i in y]
x_y = [x[i] * y[i] for i in range(len(x))]

print("Этап 1: Корреляция")

print("x y x*y x**2 y**2\n------------------")
for i in range(len(x)):
    print(x[i], y[i], x_y[i], x_sq[i], y_sq[i])

print(
    f"\n{sum(x)} {sum(y)} {sum(x_y)} {sum(x_sq)} {sum(y_sq)} - Итого")
print(
    f"{sum(x) / len(x)} {sum(y) / len(y)} {sum(x_y) / len(x)} {sum(x_sq) / len(x)} {sum(y_sq) / len(y)} - Среднее значение")

disp_x = round(sum(x_sq) / len(x) - pow(sum(x) / len(x), 2), 2)
disp_y = round(sum(y_sq) / len(y) - pow(sum(y) / len(y), 2), 2)
print(f"Дисперсия x = {disp_x}\nДисперсия y = {disp_y}")

sko_x = sqrt(disp_x)
sko_y = sqrt(disp_y)
print(f"СКО x = {sko_x}\nСКО y = {sko_y}")

korr = round(((sum(x_y) / len(x)) - (sum(x) / len(x)) * (sum(y) / len(y))) / (sko_x * sko_y), 2)
print(f"Коэффициент Корреляции = {korr}")

determ = pow(korr, 2) * 100
print(f"Коэффициент Детерминации = {round(determ, 2)}%")

if 0 < korr < 1:
    conn, zav = "ПРЯМАЯ", "УВЕЛИЧИТСЯ"
elif -1 < korr < 0:
    conn, zav = "ОБРАТНАЯ", "УМЕНЬШИТСЯ"
elif korr == abs(1):
    conn, zav = "ФУНКЦИОНАЛЬНАЯ", "ЗАВИСИТ ОТ (x)"
else:
    conn, zav = "ОТСУТСТВУЕТ", ""

if abs(korr) < 0.1:
    tesn = "ПОЧТИ ОТСУТСТВУЕТ"
elif 0.1 < abs(korr) < 0.3:
    tesn = "СЛАБАЯ"
elif 0.3 < korr < 0.5:
    tesn = "УМЕРЕННАЯ"
elif 0.5 < korr < 0.7:
    tesn = "ЗАМЕТНАЯ"
else:
    tesn = "СИЛЬНАЯ"

print(f"Таким образом, связь между x и y - {conn} и {tesn}")

print('\n')
print("Этап 2: Регрессия")

delta = len(x) * sum(x_sq) - sum(x) * sum(x)
delta_a0 = sum(y) * sum(x_sq) - sum(x) * sum(x_y)
delta_a1 = len(x) * sum(x_y) - sum(y) * sum(x)

print(f"Дельта = {delta}, Дельта а0 = {delta_a0} Дельта а1 = {delta_a1}")
a_0 = delta_a0 / delta
a_1 = delta_a1 / delta

ellast = a_1 * (sum(x) / len(x)) / (sum(y) / len(y))
print(f"Коэффициент Элластичности = {ellast}")

print(
    f"Тренд = {[round(a_0 + (i * a_1), 3) for i in x]}\nСумма тренда = {sum([round(a_0 + (i * a_1), 3) for i in x])}, Итого y = {sum(y)}")

print(f"Экономический смысл a1 - Если (х) увеличить на 1%, то (у) {zav} примерно на {round(a_1, 3)}")
print(f"Если (х) увеличить на 1%, то (у) {zav} примерно на {round(ellast, 3)}%")

plt.plot(x, y, color='green', marker='o', markersize=7)
plt.show()
