# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 23:51:10 2020

@author: VSP021
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickestWayUp function below.
# def quickestWayUp(ladders, snakes):
from collections import deque

# Complete the quickestWayUp function below.
def quickestWayUp(ladders, snakes):
  paths = {}
  for s,d in ladders + snakes:
    paths[s] = d

  q = deque([(1, 0)])
  visited = set()
  while q:
    sq, rolls = q.popleft()
    if 100 == sq:
      return rolls

    visited.add(sq)
    for i in range(1, 7):
      next = sq + i
      if next in visited or next > 100: continue
      print("----------")
      print(next in paths and paths[next] or next, rolls + 1)
      q.append((next in paths and paths[next] or next, rolls + 1))
  return -1

if __name__ == '__main__':

    ladders = [[2,78], [5,80], [15, 98], [45, 100]]
    snakes = [[80, 44], [97, 25], [93, 37], [79, 27], [75, 19], [49, 47], [67, 17]]
    result = quickestWayUp(ladders, snakes)

    print(result)
    '''
    ladders = [[32, 62], [42, 68], [12, 98]]
    snakes = [[95, 13], [97, 25], [93, 37], [79, 27], [75, 19], [49, 47], [67, 17]]
    result = quickestWayUp(ladders, snakes)

    print(result)
    
    ladders = [[8, 52], [6, 80], [26, 42], [2, 72]]
    snakes = [[51, 19], [39, 11], [37, 29], [81, 3], [59, 5], [79, 23], [53, 7], [43, 33], [77, 21]]
    
    result = quickestWayUp(ladders, snakes)

    print(result)
    '''    
    '''
    t = int(input())
    for t_itr in range(t):
        n = int(input())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        print(result)
    '''