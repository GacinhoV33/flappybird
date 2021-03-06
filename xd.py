#!/usr/bin/python
# -*- coding: utf-8 -*-


with open("highscore.txt", 'r', encoding='UTF-8') as f:
    print(f.readline())
    print(f.readline())
    f.close()

with open("highscore.txt", "w", encoding='UTF-8') as f:
    f.write(" \n")
    f.write("33")
    f.close()
