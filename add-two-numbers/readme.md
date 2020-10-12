## Problem
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Approach
거꾸로 더하는게 풀이의 난이도를 낮췄다. 재귀함수의 인수로 두 링크드리스트와
다음으로 연결할 링크드 리스트 그리고 올림수 값을 받아서 두 링크드리스트의 val 값 그리고 carry 값을 더하여 계산하고 다음 리스트를 미리 연결해 놓는다.  

중간중간 조건을 거는 것이 헷갈렸는데, 재귀함수의 종료 조건에 carry 값이 존재하면 sum 값이 존재할 수 있다는점과 다음 연결리스트의 존재 조건을 마지막에 정해주지 않으면 끝에 쓰레기 값의 링크드리스트가 더해진다.