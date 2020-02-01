# File: statements.py
# Template file for Informatics 2A Assignment 2:
# 'A Natural Language Query System in Python/NLTK'

# John Longley, November 2012
# Revised November 2013 and November 2014 with help from Nikolay Bogoychev
# Revised November 2015 by Toms Bergmanis
# Revised October 2017 by Chunchuan Lyu


# PART A: Processing statements

def add(lst,item):
    if (item not in lst):
        lst.insert(len(lst),item)

class Lexicon:
    """stores known word stems of various part-of-speech categories"""
    # "P" Personal pronoun
    # "N" Common Nouns
    # "A" Adjectives
    # "I" Intransitive verbs
    # "T" Transitive verbs
    def __init__(self):
        #declares the list where (stem,cat) are stored
        self.w_list = []
    def add(self,stem,cat):
        #appends the (stem,cat) to the list
        self.w_list.append((stem,cat))
    def getAll(self,cat):
        #returns all the words POS tag of cat
        cat_list = []
        for i in range(len(self.w_list)):
            #checks for duplicates and checks whether it equals cat
            if(self.w_list[i][1] == cat and self.w_list[i][0] not in cat_list):
                cat_list.append(self.w_list[i][0])

        return cat_list

class FactBase:
    """stores unary and binary relational facts"""
    def __init__(self):
        #creates two lists, to store unary facts and binary facts
        self.unary_list = []
        self.binary_list = []
    def addUnary(self,pred,e1):
        #appends the unary fact to the list unary_list
        self.unary_list.append([pred,e1])
    def addBinary(self,pred,e1,e2):
        #appends the binary fact to the list binary_list
        self.binary_list.append([pred,e1,e2])
    def queryUnary(self,pred,e1):
        #checks whether it exists in unary list
        is_query = 0
        query = [pred,e1]
        #creates a for loop to go through all the queries
        for i in range (len(self.unary_list)):
            #checks whether the query is in the list
            if(query in self.unary_list):
                is_query = 1
        return bool(is_query)
    def queryBinary(self,pred,e1,e2):
        #checks whether it exists in binary list
        is_query = 0
        query = [pred,e1,e2]
        #creates a for loop to go through all the queries
        for i in range (len(self.binary_list)):
            #checks whether the query is in the list
            if(query in self.binary_list):
                is_query = 1

        return bool(is_query)
import re
from nltk.corpus import brown
verblist = [(w,t) for (w,t) in brown.tagged_words() if t == "VBZ" or t == "VB"]
def verb_stem(s):
    """extracts the stem from the 3sg form of a verb, or returns empty string"""
    stem = ""
    #stem  ends in anything except s,x,y,z,xh,sh or a vowel then add s
    if(re.match("[A-z]+([^aeiousxyzh]|[^cs]h)s",s)):
        stem = s[:-1]
    #stem ends in y preceded by a vowel, simply add s
    elif(re.match("[A-z]*(a|e|i|o|u)ys",s)):
        stem = s[:-1]
    #stem ends in y preceded by a non-vowel and contains at least three letters, change the y to ies
    elif(re.match("[A-z]+(b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z)ies",s)):
        stem = s[:-3]
        stem = stem+'y'
    #stem is of the form Xie where X is a single letter other than a vowel,simply add s
    elif(re.match("(b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z)ies",s)):
        stem = s[:-1]
    #stem ends in o,x,ch,sh,ss or zz, add es
    elif(re.match("[A-z]+(o|x|ch|sh|ss|zz)es",s)):
        stem = s[:-2]
    #stem ends in se or ze but not in sse or zze, add s
    elif re.match("[A-z]+([^s]se|[^z]ze)",s):
        stem = s[:-1]
    # stem is have, its 3s form is has.
    elif(re.match("has",s)):
        stem = "have"
    #stem ends in e not preceded by i,o,s,x,z,ch,sh, just add s
    elif(re.match("[A-z]+([^iosxz]|[^cs]h)es",s)):
        stem = s[:-1]
    else:
        stem = ""

    stemlist =[w for (w,t) in verblist if w == stem or w == s]
    #checks wheather verb is in list.
    if(stemlist):
        return stem
    else:
         return ""


def add_proper_name (w,lx):
    """adds a name to a lexicon, checking if first letter is uppercase"""
    if ('A' <= w[0] and w[0] <= 'Z'):
        lx.add(w,'P')
        return ''
    else:
        return (w + " isn't a proper name")

def process_statement (lx,wlist,fb):
    """analyses a statement and updates lexicon and fact base accordingly;
       returns '' if successful, or error message if not."""
    # Grammar for the statement language is:
    #   S  -> P is AR Ns | P is A | P Is | P Ts P
    #   AR -> a | an
    # We parse this in an ad hoc way.
    msg = add_proper_name (wlist[0],lx)
    if (msg == ''):
        if (wlist[1] == 'is'):
            if (wlist[2] in ['a','an']):
                lx.add (wlist[3],'N')
                fb.addUnary ('N_'+wlist[3],wlist[0])
            else:
                lx.add (wlist[2],'A')
                fb.addUnary ('A_'+wlist[2],wlist[0])
        else:
            stem = verb_stem(wlist[1])
            if (len(wlist) == 2):
                lx.add (stem,'I')
                fb.addUnary ('I_'+stem,wlist[0])
            else:
                msg = add_proper_name (wlist[2],lx)
                if (msg == ''):
                    lx.add (stem,'T')
                    fb.addBinary ('T_'+stem,wlist[0],wlist[2])
    return msg

# End of PART A.

# print verb_stem("tells")
# print verb_stem("bathes"
# print verb_stem("unifies")
# print verb_stem("tells")
# print verb_stem("matches")
# print verb_stem("pays")
# print verb_stem("flies")
# print verb_stem("ties")
# print verb_stem("unties")
# print verb_stem("attaches")
# print verb_stem("analyzes")
# print verb_stem("has")
# print verb_stem("hates")
# print verb_stem("flys")
# print verb_stem("laughs")
