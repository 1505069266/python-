from urllib import request  # 模拟http请求的python包
import re


class Spider:

    def __init__(self, url, root_pattern, name_pattern, number_pattern):
        self.url = url
        self.name_pattern = name_pattern
        self.number_pattern = number_pattern
        self.root_pattern = root_pattern

    # 模拟http请求
    def __fetch_content(self):
        r = request.urlopen(self.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        r = re.findall(self.root_pattern, htmls)

        anchors = []
        for html in r:
            name = re.findall(self.name_pattern, html)
            number = re.findall(self.number_pattern, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)

        return anchors

    def __refine(self, anchors):
        l = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'number': anchor['number'][0]
        }

        return map(l, anchors)

    def __sort(self, anchors):
        # filter
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)

        return anchors

    def __sort_seed(self, anchor):
        r = re.findall('\d*', anchor['number'])

        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000

        return number

    def __show(self, anchors):
        for rank in range(0, len(anchors)):
            print('rank ' + str(rank + 1) + ":" + anchors[rank]['name'] + '  ' + anchors[rank]['number'])

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


spider = Spider('https://www.huya.com/g/lol','<li class="game-live-item" gid="1">([\s\S]*?)</li>','<i class="nick" title="([\s\S]*?)">[\s\S]*?</i>','<i class="js-num">([\s\S]*?)</i>')

spider.go()
