'''
参考サイト
https://math.stackexchange.com/questions/885879/meaning-of-rays-in-polar-plot-of-prime-numbers/885894
https://www.youtube.com/watch?v=CJpyguRJfeM&t=118s&ab_channel=3Blue1BrownJapan
'''

import math
import matplotlib.pyplot as plt



def judge_prime_number(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def polar_coordinates(max_value):
    coordinates = []
    theta = 0
    while theta <= max_value:
        r = theta
        if judge_prime_number(r):
            coordinates.append((r, theta))
        theta += 1  # 角度を1ずつ増やす
    return coordinates


def plot_polar_coordinates(polar_coords):
    x_coords = [r * math.cos(theta) for r, theta in polar_coords]
    y_coords = [r * math.sin(theta) for r, theta in polar_coords]

    plt.figure(figsize=(12, 12), facecolor='#1f1f1f')
    plt.scatter(x_coords, y_coords, c='#00bfff', marker='o', s=1)  # 明るい青系の色に変更
    plt.xlabel('X', color='white')
    plt.ylabel('Y', color='white')
    plt.title('Polar Coordinates (r, θ) (r = θ)', color='white')
    plt.grid(True, color='white')
    plt.gca().set_facecolor('#1f1f1f')
    plt.gca().tick_params(colors='white')  # x, y座標の数値を白にする
    plt.axis('equal')
    plt.show()



if __name__ == "__main__":
    MAX = 1000 # MAXまでの素数を求める
    result = polar_coordinates(MAX)
    print(result)

    plot_polar_coordinates(result)
