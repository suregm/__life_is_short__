import scrapy

# Scrapy爬虫框架结构
# “5+2”结构
# engine
# spider 出Request，入Response
# downloader
# scheduler
# item pipelines
# spider和engine中间件Middleware
# engine和downloader中间件Middleware
# 用户修改的部分：spider, item pipelines, downloader middleware

# Scrapy命令行格式
# scrapy <command> [options][args]
# 常用<command>
# startproject 新建工程 scrapy startproject <name> [dir]
# genspider 创建爬虫 scrapy genspider [options] <name> <domain>
# settings 获得爬虫的配置信息 scrapy settings [options]
# crawl 运行一个爬虫 scrapy crawl <spider>
# list 列出所有爬虫 scrapy list
# shell 启动URL调试命令行 scrapy shell [url]

# 工程目录结构
# python_demo/  外层目录
#     scrapy.cfg    部署爬虫的配置文件
#     python_demo/  用户自定义Python代码
#         __init__.py   初始化脚本
#         items.py  Items代码模版（继承类）
#         middlewares.py    Middlewares代码模版（继承类）
#         pipelines.py  Pipelines代码模版（继承类）
#         settings.py   Scrapy爬虫的配置文件
#         spiders/  Spiders代码模版目录（继承类）
#             __init__.py   初始文件，无需修改
#             __pycache__/  缓存目录，无需修改
#             demo.py

class DemoSpider(scrapy.spider)
