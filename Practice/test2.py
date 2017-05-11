# print(all([True, False]))
# print(all([True, True]))
# print(all([False, False]))
# print(any([True, False]))
# print(any([False, False]))
# print(bin(10101))
# print(ascii('jim'), type(ascii('jim')))
# print(bool([False, True]))
# print(bool([]))
# print(bool([False]))
# # print(bytearray('jim', str.encode('utf-8')), type(bytearray('jim', str.encode('utf-8'))))
# print(bytes(9), type(bytes(9)))
# print(bytes(8), type(bytes(8)))
# print(chr(1000))
# a = [1, 2, 4]
# # delattr(x=a)
# # print(a)
# print(divmod(x=1, y=2))



# import bs4
# print(dir(bs4.BeautifulSoup))
# print([n for n in dir(bs4.BeautifulSoup) if not n.startswith("_")])
# print(bs4.__all__)
# print(help(bs4.BeautifulSoup))
# n_list = dir(copy)
# for n in n_list:
#     if not n.startswith("_"):
#         arrage = [n].append(n)
        # print([n])
        # n_arrage = [n].append(n)
        # print(n_arrage)

# import urllib.request
# print([n for n in dir(urllib.request) if not n.startswith("_")])
# help(urllib.request.urlparse)
#
# import logging
# print(dir(logging))
# print(n for n in dir(logging) if not n.startswith("_"))
# help(logging.getLogger)

test_dict = {'a': 'b', 'b': 'c'}
if 'c' in test_dict:
    print('yes')
else:
    print("no")