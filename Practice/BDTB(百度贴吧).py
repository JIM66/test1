from urllib.request import urlopen
from urllib.request import Request
from urllib.request import URLError
from bs4 import BeautifulSoup
import re
# 初始化，传入基地址，是否只看楼主的参数


class BDTB:
    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self, baserUrl, seeLZ):
        self.baseURL = baserUrl
        self.seeLZ = "?see_lz"+str(seeLZ)

    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = Request(url)
            html = urlopen(request)
            bsobj = BeautifulSoup(html.read(), "html.parser")
            # print(bsobj)
            return bsobj.read()
        except URLError as e:
            if hasattr(e, "reason"):
                print(u"链接百度贴吧失败，错误原因", e.reason)
                return None
    # 获取帖子标题

    # def getTitle(self):
    #     page = self.getPage(1).read
    #     pattern = re.compile('<h3 class="core_title_txt pull-left text-overflow.*?>(.*?)</h3>', re.S)
    #     result = re.search(pattern, page)
    #     if result:
    #         print(result.group(1))
    #         return (result.group(1).strip())
    #     else:
    #         return None
    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt pull-left text-overflow.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        if result:
            print(result.group(1))



baseURL = "http://tieba.baidu.com/p/3138733512"
bdtb = BDTB(baseURL, 1)

# print(bdtb.getPage(1).prettify())  # prettify格式化输出html
# print(bdtb.getTitle())   # 不知道为什么会输出这么多
print(type())



# # 测试语句
# baseURL = "http://tieba.baidu.com/p/3138733512"
# bdtb = BDTB(baseURL, 1)
# # print(bdtb.getPage(1).prettify())
# title_list = bdtb.getPage(1).find_all('h3', {'class': 'core_title_txt pull-left text-overflow '}) # class方法有问题,已经解决
# title_list2 = bdtb.getPage(1).find('h3', {'class': 'core_title_txt pull-left text-overflow '})
# title2 = bdtb.getPage(1).h3.string
# # print(title)
# print(title_list2.get_text())
# for title in title_list:
#     print(title.get_text())
# print(type(title_list))   # 返回类型是结果集
# print(type(title_list2))   # 返回的类型的标签
# print(type(title))
# print(type(title2))


