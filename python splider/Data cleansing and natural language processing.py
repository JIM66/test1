# import requests
# from bs4 import BeautifulSoup
# import re
# import string
# from collections import OrderedDict
#
#
# def clean_content(contens):
#     contens = re.sub('\n+', " ", contens)
#     contens = re.sub('\[[0-9]*\]', "", contens)
#     contens = re.sub(" +", ' ', contens)
#     result = []
#     contens = contens.split(' ')
#     for item in contens:
#         item = item.strip(string.punctuation)
#         if len(item) > 1 or (item.lower() == 'a' or item.lower == 'i'):
#             result.append(item)
#     return result
#
#
# def ngrams(contens, n):
#     result = []
#     contens = clean_content(contens)
#     for i in range(len(contens)-n+1):
#         result.append(contens[i:i+n])
#     return result
# url = 'http://en.wikipedia.org/wiki/Python_(programming_language)'
# req = requests.get(url)
# bsObj = BeautifulSoup(req.text, 'html.parser')
# content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
# # ngrams = ngrams(content, 3)
# # print(ngrams)
# ngrams = ngrams(content, 2)
# # print(ngrams[0])
#
# # ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reversed=True))
# # b = OrderedDict(sorted(ngrams.items(), key=lambda x: x[1], reverse=True))
# ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
# print(ngrams)
#
# # for a in a_list:
# #     print(a)
# # for a in ngrams:
# #     print(a)
# # print("2-grams count is: "+str(len(ngrams)))
#
# # test_text = '作为一名优秀的\n程 序员，你可 能会问：“为什 么不自动 地对输 入的信息进行清洗，去掉非'
# # test_text2 = 'jiang shao bing'
# # test_list = ngrams(test_text, 2)
# # test_list2 = ngrams(test_text2, 3)
# # for i in test_list2:
# #     print(i)
# # # b = clean_content(a)
# # # print(len(b))
# # # print(b)
# # for i in test_list:
# #     print(i)
#
#
# def clean_text(text):
#     text = re.sub('\n+', '', text)
#     text = re.sub(' +', '', text)
#     text = re.sub('\d', '', text)
#     return text
#
#
# def seg_text(text, n):
#     result = []
#     text = clean_text(text)
#     # print(text)
#     for i in range(len(text)-n+1):
#         result.append(text[i:i+n])
#     return result
#
# # # a = '作为一名优秀的\n程 序员，你可 能会问：“为什 么123不自动 地对输 入的信息进行清洗，去掉非'
# # # print(clean_text(a))
# # # list1 = seg_text(a, 2)
# # # for i in list1:
# # #     print(i)
# # #
# # # b = clean_text(a)
# # # list2 = seg_text(b, 2)
# # # for j in list2:
# # #     print(j)
# # c = '作为一名优秀的程序员，你可能会问：“为什么不自动地对输入的信息进行清洗，去掉非'
# # list3 = seg_text(c,2)
# # for i in list3:
# #     print(i)


# 范例
# from bs4 import BeautifulSoup
# import re
# from urllib.request import urlopen
# import string
# from collections import OrderedDict
#
#
# def cleanInput(input):
#     input = re.sub('\n+', " ", input)
#     input = re.sub('\[[0-9]*\]', "", input)
#     input = re.sub(' +', " ", input)
#     input = bytes(input, "UTF-8")
#     input = input.decode("ascii", "ignore")
#     cleanInput = []
#     input = input.split(' ')
#     for item in input:
#         item = item.strip(string.punctuation)
#         if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
#             cleanInput.append(item)
#     return cleanInput
#
#
# def getNgrams(input, n):
#     input = cleanInput(input)
#     output = dict()
#     for i in range(len(input)-n+1):
#         newNGram = " ".join(input[i:i+n])
#         if newNGram in output:
#             output[newNGram] += 1
#         else:
#             output[newNGram] = 1
#     return output
#
# html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
# bsObj = BeautifulSoup(html, "html.parser")
# content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
# #ngrams = getNgrams(content, 2)
# #print(ngrams)
# #print("2-grams count is: "+str(len(ngrams)))
#
# ngrams = getNgrams(content, 2)
# print(ngrams)
# b = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
# print(b)

#
import requests
# from random import randint
# from urllib.request import urlopen
#
# def wordListSum(wordlist):
#     sum = 0
#     for word, value in wordlist.items():
#         sum += value
#     return sum
#
#
#
#
# def retrieveRandomWord(wordlist):
#     randIndex = randint(1, wordListSum(wordlist))
#     for word, value in wordlist.items():
#         randIndex -= value
#         if randIndex <= 0:
#             return word
#
#
#
#
# def buildWordDict(text):
#     text = text.replace("\n", " ")
#     text = text.replace("\"", "")
#     # 保证每个标点符号都和前面的单词在一起
#     # 这样不会被剔除，保留在马可夫链中
#     punctuation = [',', '.', ';', ':']
#     for symbol in punctuation:
#         text = text.replace(symbol, " "+symbol+" ")
#
#     words = text.split(" ")
#     # 过滤空单词
#     words = [word for word in words if word != ""]
#     wordDict = {}
#     for i in range(1, len(words)):
#         if words[i-1] not in wordDict:
#             wordDict[words[i-1]] = {}
#         if words[i] not in wordDict[words[i-1]]:
#             wordDict[words[i-1]][words[i]] = 0
#         wordDict[words[i-1]][words[i]] += 1
#
#     return wordDict
#
# # req = requests.get("http://pythonscraping.com/files/inaugurationSpeech.txt")
# # text = req.text
# text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
# wordDict = buildWordDict(text)
# length = 100
# chain = ""
# currentword = 'I'
# for i in range(0, length):
#     chain += currentword+" "
#     print(wordDict[currentword])
#     currentword = retrieveRandomWord(wordDict[currentword])
# print(chain)


# from urllib.request import urlopen
# from random import randint
#
# def wordListSum(wordList):
#     sum = 0
#     for word, value in wordList.items():
#         sum += value
#     return sum
#
# def retrieveRandomWord(wordList):
#
#     randIndex = randint(1, wordListSum(wordList))
#     for word, value in wordList.items():
#         randIndex -= value
#         if randIndex <= 0:
#             return word
#
# def buildWordDict(text):
#     #Remove newlines and quotes
#     text = text.replace("\n", " ")
#     text = text.replace("\"", "")
#
#     #Make sure puncuation are treated as their own "word," so they will be included
#     #in the Markov chain
#     punctuation = [',','.',';',':']
#     for symbol in punctuation:
#         text = text.replace(symbol, " "+symbol+" ")
#
#     words = text.split(" ")
#     #Filter out empty words
#     words = [word for word in words if word != ""]
#
#     wordDict = {}
#     for i in range(1, len(words)):
#         if words[i-1] not in wordDict:
#             #Create a new dictionary for this word
#             wordDict[words[i-1]] = {}
#         if words[i] not in wordDict[words[i-1]]:
#             wordDict[words[i-1]][words[i]] = 0
#         wordDict[words[i-1]][words[i]] += 1
#
#     return wordDict
#
# text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
# wordDict = buildWordDict(text)
#
# #Generate a Markov chain of length 100
# length = 100
# chain = ""
# currentWord = "I"
# for i in range(0, length):
#     chain += currentWord+" "
#     #print(wordDict[currentWord])
#     currentWord = retrieveRandomWord(wordDict[currentWord])
#
# print(chain)

#

import csv
import json
f = open('F:\学习\新新贷\网贷之家.csv', 'r')
f_list = csv.reader(f)
head = next(f_list)
for i in f_list:
    if i:
        print(i[0])


