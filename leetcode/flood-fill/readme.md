## Problem
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

## Approach
1. 어떤 위치의 coords를 받고 그 위치의 색깔이 바꾸는 조건에 부합하는지
결정하고 색을 바꾼다.
- 타일의 coords가 valid한가(sr, sc가 0보다 크고 최대 길이보다 짧은가)
- 전에 바꾼 타일과 인접하는 위치에 있는가
- 전에 바꾼 타일의 원래 색과 같은 색을 가지고 있는가

2. 1번 과정을 함수로 만들고 인접 타일 4개에 대해 재귀적으로 실행한다.
