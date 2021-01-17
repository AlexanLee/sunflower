import scrapy
import os
import re
import time


class SunFlowerSpider(scrapy.Spider):
    name = 'sun_flower'
    allowed_domains = ['wsjkw.hebei.gov.cn']

    # start_urls = ['http://wsjkw.hebei.gov.cn/syyctplj/375192.jhtml']
    # start_urls = ['http://wsjkw.hebei.gov.cn/']

    def start_requests(self):
        urls = [
            # 'http://wsjkw.hebei.gov.cn/syyctplj/375192.jhtml',
            # 'http://wsjkw.hebei.gov.cn/syyctplj/375221.jhtml',
            # 'http://wsjkw.hebei.gov.cn/syyctplj/375261.jhtml',
            # 'http://wsjkw.hebei.gov.cn/syyctplj/375333.jhtml',
            # 'http://wsjkw.hebei.gov.cn/syyctplj/375294.jhtml',
            # 'http://wsjkw.hebei.gov.cn/syyctplj/375478.jhtml',
            # 'http://wsjkw.hebei.gov.cn/syyctplj/375429.jhtml',
            # 'http://wsjkw.hebei.gov.cn/syyctplj/375391.jhtml',
            # 'http://wsjkw.hebei.gov.cn/syyctplj/375501.jhtml',
            # 'http://wsjkw.hebei.gov.cn/syyctplj/375370.jhtml',
            # 'http://wsjkw.hebei.gov.cn/syyctplj/375583.jhtml',
            # 'http://wsjkw.hebei.gov.cn/syyctplj/375501.jhtml',
            # 'http://wsjkw.hebei.gov.cn/syyctplj/375548.jhtml',
            # 'http://wsjkw.hebei.gov.cn/syyctplj/375583.jhtml',
            'http://wsjkw.hebei.gov.cn/syyctplj/375619.jhtml'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        relative_path = "../data/sjz/"
        page = response.url.split("/")[-1].split(".")[0]
        filename = f'sjz-{page}.html'
        with open(os.path.join(relative_path, filename), 'wb') as f:
            f.write(response.body)
        title = response.xpath('/html/head/title/text()').extract_first()
        time_release = response.xpath('// *[ @ id = "container"] / div[3] / div / div[1] / span[1]/node()') \
            .extract_first()
        content = response.xpath('// *[ @ id = "zoom"] / p / span / text()').extract()
        # content = response.xpath('// *[ @ id = "zoom"] / p / span/ span / span / text()').extract() #6、7是3个span
        contents = '\n'.join(content)

        # 以下方法可以抽取所有文本，但是没有分割，不是太好。
        # contents = response.xpath('// *[ @ id = "zoom"]')
        # content = contents.xpath('string(.)').extract()[0]

        print(title)
        print(time_release)
        pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
        date_certain = ''.join(pattern.findall(time_release))
        print(date_certain)
        # print(time_release.split(" ")[0].split("：")[1])
        print(contents)
        with open(os.path.join(relative_path, 'text/' + date_certain+'.txt'), 'wb') as f:
            f.write(contents.encode())

        self.log(f'Saved file {filename}')
        time.sleep(3)
        pass
