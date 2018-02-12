#!/usr/bin/python

import os
import sys

q_num = 1

class question:
    def __init__(self, line):

        tab = line.split("\t")
        
        self.num = q_num
        self.ID = ID
        self.question = question
        self.t_rep = true_rep
        self.f_rep_1 = false_rep_1
        self.f_rep_2 = false_rep_2
        self.f_rep_3 = false_rep_3
        self.f_rep_4 = false_rep_4
        self.f_rep_5 = false_rep_5
        q_num += 1

def main():

    fd = open("question.tsv", "r")
    
    line = fd.readline()
    qtn = question(line)
    
    
    dest = open("test.txt", "w")
    dest.write("ta geule\n")
    dest.close()



if __name__ == '__main__':
    main()
