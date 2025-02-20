мой вариант 9.

Лабораторная работа № 1 (расчётная часть)
1. Для выборки А:
- указать максимальный и минимальный элементы выборки, найти размах выборки;
- построить статистический ряд и начертить полигон ряда;
- записать эмпирическую функцию распределения и построить её график;
- вычислить начальные и центральные эмпирические моменты до 4-го порядка;
- найти моду, медиану, коэффициенты асимметрии (момент 3-его порядка) и эксцесса (sum_{i=1}^{k} x_i - x_{ср})/(n*\sigma) - 3 не забыть минус три;
- сделать выводы и сформулировать гипотезы о распределении генеральной совокупности из которой извлечена выборка, оценить параметры этого распределения

2. Для выборки В:
- указать максимальный и минимальный элементы выборки, найти размах выборки;
- определить оптимальное количество интервалов группировки и длину интервала группировки;
- построить интервальный ряд и гистограмму, а также полигон ряда;
- записать эмпирическую функцию распределения и построить её график, построить кумуляту (и огиву);
- вычислить начальные и центральные эмпирические моменты до 4-го порядка;
- найти моду (отметить на гистограмме), медиану (отметить на кумуляте), коэффициенты асимметрии и эксцесса;
- сделать выводы и сформулировать гипотезы о распределении генеральной совокупности из которой извлечена выборка, оценить параметры этого распределения.

- если ряд интервальный, то функция распределения должна совпадать с кумулятой и не быть ступенчатой
- x^{*} - середина интервала


![{9A93D347-E5E7-4920-A287-AFC89A79F6E1}](https://github.com/user-attachments/assets/a9e6f9f8-f203-4d36-bfaa-dcb1c68d2aff)

![{5B061901-E43B-4997-8835-DE392FF5CD1A}](https://github.com/user-attachments/assets/2890fd71-563d-4d98-9efa-d348dac581b3)


# Результаты
## Задание 1
![alt text](https://github.com/huji-itmo/statistics-lab1/blob/main/tex/output/task1/distribution_function.png?raw=true)
![alt text](https://github.com/huji-itmo/statistics-lab1/blob/main/tex/output/task1/polygon.png?raw=true)
```
n = 79
Вариационный ряд: 0 ≤ 0 ≤ 0 ≤ 0 ≤ 0 ≤ 0 ≤ 0 ≤ 0 ≤ 0 ≤ 0 ≤ 0 ≤ 0 ≤ 0 ≤ 0 ≤ 0 ≤ 0 ≤ 0 ≤ 0 ≤ 0 ≤ 0 ≤ 1 ≤ 1 ≤ 1 ≤ 1 ≤ 1 ≤ 1 ≤ 1 ≤ 1 ≤ 1 ≤ 1 ≤ 1 ≤ 1 ≤ 2 ≤ 2 ≤ 2 ≤ 2 ≤ 2 ≤ 2 ≤ 2 ≤ 2 ≤ 2 ≤ 2 ≤ 2 ≤ 2 ≤ 2 ≤ 2 ≤ 2 ≤ 2 ≤ 2 ≤ 2 ≤ 2 ≤ 3 ≤ 3 ≤ 3 ≤ 3 ≤ 3 ≤ 3 ≤ 3 ≤ 3 ≤ 3 ≤ 3 ≤ 3 ≤ 3 ≤ 3 ≤ 3 ≤ 3 ≤ 3 ≤ 3 ≤ 3 ≤ 3 ≤ 4 ≤ 4 ≤ 4 ≤ 4 ≤ 4 ≤ 4 ≤ 4 ≤ 4 ≤ 4
min: 0 max: 4
Размах: 4.00
Статистический ряд: записаны в tex/output/task1/statistical_series.tex
Оценка математического ожидания (начальный момент): 1.8101
Стандартное отклонение0.0
Дисперсия 1.8247
Оценка выборочного среднеквадратического отклонения: 1.3508
Оценка выборочного с.к.о. (исправленная): 1.3594
Вид эмпирической функции распределения: записан в tex/output/task1/analytical_func.tex
Центральный момент 1 порядка: 0.0
Центральный момент 2 порядка: 1.8247
Центральный момент 3 порядка: 0.0209
Центральный момент 4 порядка: 5.8857
Мода: 0
Медиана: 3
Коэффициент асимметрии: 0.0209
Эксцесса: 2.8857
```

Вывод:
Данные выборки А напоминают историю студента, который планировал учиться равномерно весь семестр, но всё откладывал до последнего. Как итог — 79 попыток, 20 из которых закончились нулём (мода = 0), а к третьему дню (медиана = 3) начался аврал! Распределение асимметрично (коэффициент асимметрии ≈ 0.02) с тяжёлыми "хвостами" (эксцесс ≈ 2.89), словно студент пытался нагнать упущенное за ночь. Гипотеза: генеральная совокупность распределена по закону, близкому к биномиальному с параметром успеха p ≈ 0.45. Но, как и в сессии, здесь есть нюансы — пик на 0 и резкий рост к 3 указывают на смещение. Возможно, это отрицательное биномиальное распределение, где "неудачи" (прокрастинация) преобладают до момента прорыва.

## Задание 2
![alt text](https://github.com/huji-itmo/statistics-lab1/blob/main/tex/output/task2/cumulative_8_bins.png?raw=true)
![alt text](https://github.com/huji-itmo/statistics-lab1/blob/main/tex/output/task2/histogram_8_bins.png?raw=true)
![alt text](https://github.com/huji-itmo/statistics-lab1/blob/main/tex/output/task2/ogive_8_bins.png?raw=true)

```
n = 217
min: 28 max: 94
Размах: 66.00
Оптимальное количество интервалов (по ф. Стерджесса): 8
Длинна интервала: 8.25
Интервальный статистический ряд: записаны в tex/output/task2/statistical_interval_series_8_bins.tex
Начальный момент (среднее): 65.9614
Центральный эмпирический момент 1-того порядка: -0.0
Центральный эмпирический момент 2-того порядка: 1.0
Центральный эмпирический момент 3-того порядка: -0.028
Центральный эмпирический момент 4-того порядка: 2.6199
Коэффициент асимметрии: -0.028
Эксцесс: -0.3801
Мода: 65.125
Медиана: 65.6175
Гистограмма записана в tex/output/task2/histogram_8_bins.png
Кумулята записана в tex/output/task2/cumulative_8_bins.png
Огива записана в tex/output/task2/ogive_8_bins.png
```

Выборка В — это история кота, который пытался равномерно занять все коробки в доме (интервалы группировки), но в итоге свернулся клубком в середине (мода ≈ 65.1). Гистограмма и кумулята показывают почти симметричное распределение (среднее ≈ 65.96, медиана ≈ 65.62), словно кот нашёл идеальный баланс между игрой и сном. Лёгкий отрицательный эксцесс (-0.38) намекает, что хвосты короче, чем у нормального распределения — возможно, кот всё же предпочитает середину. Гипотеза: генеральная совокупность близка к нормальному распределению с μ ≈ 66 и σ ≈ 1.35. Однако стандартное отклонение слегка "расплывчато", как намерения кота утром.
