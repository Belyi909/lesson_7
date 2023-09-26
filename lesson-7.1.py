# coding=windows-1251
# 7 урок 1 задача
word = str(input())
a = word[:: -1]
if word == a:
    print("yes")
else:
    print("no")