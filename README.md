# Spiral-of-polar-coordinates
## 素数の螺旋

#### 参考サイト
https://www.youtube.com/watch?v=EK32jo7i5LQ&ab_channel=3Blue1Brown <br>
https://math.stackexchange.com/questions/885879/meaning-of-rays-in-polar-plot-of-prime-numbers/885894

#### 概要
3Blue1Brownにて紹介されている「素数の螺旋」というものを検証するためのプログラム.


#### 関数の説明
- [x] judge_prime_number(n)
引数`n`が素数であるかを判別する関数.<br>
`n`が素数である場合は`True`，`n`が素数ではない場合は`False`を返す．<br>

- [x] polar_coordinates(max_value)<br>
`judge_prime_number(n)`を用いて，

$$
(r, \theta) = (p, p) \quad p \text{ is a prime number}
$$

が成り立つ極座標`(r, θ)`をリストに追加する関数．


- [x] plot_polar_coordinates(polar_coords)
リスト`polar_coords`を極座標として`(x, y)`平面に描画する関数.

