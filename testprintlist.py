"""
Program: testprintlist.py
Author: My

This program tests printAll(seq) function and add code to trace the argument on each call.
"""
seq = ["Hello", "welcome", "to", "my", "world"]

def printAll(seq):
    if seq == []:
        return 
    else:
        print(seq[0])
        seq.pop(0)
        return printAll(seq)
             
printAll(seq)
