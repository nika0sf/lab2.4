#!/usr/bin/env python3
# -*- coding: utf-8 -*-

arr = [-1, 3, 5, -3, 0, 7, 14]
print(arr)
print('Количество элементов массива, равных нулю', arr.count(0))
print('Сумма элементов массива, расположенных после минимального элемента', sum(arr[arr.index(min(arr))+1:]))
arr.sort(key=abs)
print(arr)