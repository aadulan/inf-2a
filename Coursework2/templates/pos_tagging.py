# File: pos_tagging.py
# Template file for Informatics 2A Assignment 2:
# 'A Natural Language Query System in Python/NLTK'

# John Longley, November 2012
# Revised November 2013 and November 2014 with help from Nikolay Bogoychev
# Revised November 2015 by Toms Bergmanis


# PART B: POS tagging

from statements import *

# The tagset we shall use is:
# P  A  Ns  Np  Is  Ip  Ts  Tp  BEs  BEp  DOs  DOp  AR  AND  WHO  WHICH  ?

# Tags for words playing a special role in the grammar:

function_words_tags = [('a','AR'), ('an','AR'), ('and','AND'),
     ('is','BEs'), ('are','BEp'), ('does','DOs'), ('do','DOp'),
     ('who','WHO'), ('which','WHICH'), ('Who','WHO'), ('Which','WHICH'), ('?','?')]
     # upper or lowercase tolerated at start of question.

function_words = [p[0] for p in function_words_tags]

def unchanging_plurals():
    with open("sentences.txt", "r") as f:
        sen = [] #puts the words in tuples of the word and tag
        for line in f:
             l = line.split() #splits each line by a space so word|tag
             sen += [tuple(x.split('|')) for x in l] #combines two lists of (word,tag)

        n = [w for (w,t) in sen if t == "NN"] #lists of words with tag NN

        ns = [w for (w,t) in sen if t == "NNS"] #lists of words with tag NNS

        return list(set(n).intersection(ns)) #intersects both lists as sets and turn into a list
#import time
#t=time.time()
unchanging_plurals_list = unchanging_plurals()
#print sorted(unchanging_plurals_list)
#print time.time()-t
def noun_stem (s):
    """extracts the stem from a plural noun, or returns empty string"""
    stem = ""
    if( s in unchanging_plurals_list):
        stem = s
    elif(re.match("[a-z]*men",s)):
        stem = s[:-3] + "man"
    elif(re.match("[a-z]+([^aeiousxyzh]|[^cs]h)s",s)):
        stem = s[:-1]
    #stem ends in y preceded by a vowel, simply add s
    elif(re.match("[a-z]*(a|e|i|o|u)ys",s)):
        stem = s[:-1]
    #stem ends in y preceded by a non-vowel and contains at least three letters, change the y to ies
    elif(re.match("[a-z]+(b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z)ies",s)):
        stem = s[:-3]
        stem = stem+'y'
    #stem is of the form Xie where X is a single letter other than a vowel,simply add s
    elif(re.match("(b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z)ies",s)):
        stem = s[:-1]
    #stem ends in o,x,ch,sh,ss or zz, add es
    elif(re.match(r"[a-z]+(o|x|ch|sh|ss|zz)es",s)):
        stem = s[:-2]
    #stem ends in se or ze but not in sse or zze, add s
    elif re.match("[a-z]+[^s]se|[^z]ze",s):
        stem = s[:-1]
    #stem ends in e not preceded by i,o,s,x,z,ch,sh, just add s
    elif(re.match("[a-z]+([^iosxz]|[^cs]h)es",s)):
        stem = s[:-1]
    else:
        stem = ""

    return stem


def tag_word (lx,wd):
    """returns a list of all possible tags for wd relative to lx"""
    tags=[]

    p = lx.getAll("P")
    a = lx.getAll("A")
    n = lx.getAll("N")
    i = lx.getAll("I")
    t = lx.getAll("T")

    if wd in p:
        tags.append("P")
    if wd in a:
        tags.append("A")


    if (wd in unchanging_plurals_list):
        tags.append("Ns")
        tags.append("Np")
    elif noun_stem(wd) in n:
            tags.append("Np")
    elif wd in n :
            tags.append("Ns")

    if verb_stem(wd) in i:
        tags.append("Is")
    if wd in i:
        tags.append("Ip")
    if verb_stem(wd) in t:
        tags.append("Ts")
    if wd in t:
        tags.append("Tp")

    function = [t for (w,t) in function_words_tags if w == wd]
    tags = tags + function


    return tags

def tag_words (lx, wds):
    """returns a list of all possible taggings for a list of words"""
    if (wds == []):
        return [[]]
    else:
        tag_first = tag_word (lx, wds[0])
        tag_rest = tag_words (lx, wds[1:])
        return [[fst] + rst for fst in tag_first for rst in tag_rest]

#End of PART B.
# print noun_stem("peas")
# print noun_stem("bears")
# print noun_stem("salmon")
# print noun_stem("choleras")
# print noun_stem("doormat")
# print noun_stem("chocolates")
# print noun_stem("monkey-men")
# print noun_stem("ashes")
# lx = Lexicon()
# lx.add("John","P")
# lx.add("Mary","P")
# lx.add("like","T")
# lx.add("orange","A")
# lx.add("orange","N")
# lx.add("fish","N")
# lx.add("fish","T")
# lx.add("fish","I")
# lx.add("duck","N")
# print tag_word(lx,'duck')
# print tag_word(lx,'fish')
# print tag_words(lx,['John','fish'])
