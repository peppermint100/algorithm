## Problem
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

## Approach
고등학생 때 어디선가 접해본 문제였다. 처음에 바로 생각나지 않았지만 어떤 점에서의 최단 경로의 개수는 그 점의 위까지의 최단 경로 개수 + 그 점 왼쪽의 최단 경로의 개수인것을 알아내고 풀었다.