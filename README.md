工程目的
  爬取 http://nba.stats.qq.com/schedule/ 的NBA数据

需安装scrapy
在根目录下执行scrapy crawl nba

该网页包含js动态加载数据，需使用splash进行动态渲染，splash + scrapy 配置见如下两个文档：
http://ae.yyuap.com/pages/viewpage.action?pageId=919763
http://brucedone.com/archives/560
