#encoding:utf-8
# 主函数 url和craw

from baike_spider import url_manager, html_downloader, html_parser, html_outputer

class Spidermain(object):
    # 初始化构造函数:url管理器，网页下载器，网页解析器，输出器
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.Html_downloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.Html_outputer()
    
    def craw(self, root_url):
        try:
            count = 1   #URL计数
            self.urls.add_new_url(root_url) # 添加根url
            # 开始解析
            while self.urls.has_new_url():
                new_url = self.urls.get_new_url()    # 获取新的url
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)   # 下载url对应页面
                new_urls, new_data = self.parser.parse(new_url, html_cont)  # 解析页面并保存数据
                self.urls.add_new_urls(new_urls)    # urls添加到url_manager
                self.outputer.collect_data(new_data)    # 数据收集
                
                if count == 10:
                    break
                
                count = count + 1
        except:
            #print 'craw failed'
                
            self.outputer.output_html()

if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python"
    obj_spider = Spidermain()
    obj_spider.craw(root_url)
    