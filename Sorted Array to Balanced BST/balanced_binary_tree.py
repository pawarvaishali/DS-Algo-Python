# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:32:14 2020

@author: VSP021

Balanced binary tree
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
def inorder(temp):
    if not temp:
        return None
    if temp:
        inorder(temp.left)
        print(temp.key, end=' ')
        inorder(temp.right)
    
def balanced_tree(arr, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    root = Node(arr[mid])
    root.left = balanced_tree(arr, start, mid-1)
    root.right = balanced_tree(arr, mid+1, end)
    return root
        
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    root = balanced_tree(arr, 0, len(arr)-1)
    print("Inorder : ")
    inorder(root)