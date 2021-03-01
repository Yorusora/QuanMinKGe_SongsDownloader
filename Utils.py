import requests
import time
import WConio2

def progressbar(url, path, songInfo): # 进度条
    start = time.time()  # 下载开始时间
    response = requests.get(url, stream=True)
    size = 0    # 初始化已下载大小
    chunk_size = 1024  # 每次下载的数据大小
    content_size = int(response.headers['content-length'])  # 下载文件总大小
    try:
        if response.status_code == 200:   # 判断是否响应成功
            # 开始下载，显示下载文件大小
            print('Start downloading [' + songInfo + '], File size:{size:.2f} MB'.format(size=content_size / chunk_size / 1024))
            with open(path, 'wb') as file:   # 显示进度条
                WConio2.textcolor(WConio2.YELLOW)
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    size += len(data)
                    print('\r'+'Progress:[%s%.2f%%' % ('>'*int(round(size*50 / content_size, 0)) + ' '*int(round(50 - size*50 / content_size, 0)) + '] ',float(size / content_size * 100)), end=' ')
        end = time.time()   # 下载结束时间
        WConio2.textcolor(WConio2.GREEN)
        print('\nDownload completed! Time: %.2fsec' % (end - start))  # 输出下载用时时间
        WConio2.textcolor(WConio2.WHITE)
    except:
        WConio2.textcolor(WConio2.RED)
        print('Progressbar Error!')
        WConio2.textcolor(WConio2.WHITE)

def characterChange(originstr): # 替换windows非法字符
    return str(originstr).replace(":", "：").replace("*", "_").replace("?", "_").replace("\"", "_").replace("<", "_").replace(">", "_").replace("|", "_").replace("\\", "_").replace("/", "_")
