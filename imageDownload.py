# -*- coding = utf-8 -*-
# @Time : 2024/4/16 20:22
# @Author : 鬼鬼
# @File : imageDownload.py
# @Software: PyCharm

import os

class ImageDownload():

    def __init__(self, postfix='.jpg',keyword=""):

        self.postfix = postfix
        self.keyword = keyword # "生活照"
        path_desktop = os.path.join(os.path.expanduser("~"), 'Desktop')
        self.path_Desktop = path_desktop
        # pic_url  k  pic_string
        # pic_string = 路径 + k + _ + pic_title + .jpg


    def down_pic_get(self, pic_url,k=1, pic_string=""):

        import requests
        # import urllib3
        # urllib3.disable_warnings()

        requests.packages.urllib3.disable_warnings()


        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",

        }

        try:
            r = requests.get(pic_url, headers=headers, timeout=3, verify=False)
            # ===================================
            if r.status_code == 200:
                # *********************************************************************
                if pic_string == "":# 没有输入下载路径
                    pic_string = os.path.join(self.path_Desktop, str(k) + self.postfix)
                # *********************************************************************
                try:
                    with open(pic_string, 'wb') as f:
                        f.write(r.content)  # 写入二进制内容
                except:
                    f = open(pic_string, 'wb')
                    f.write(r.content)
                    f.close()
            else:
                print("下载出错！ " + str(r.status_code), end="")
            # ===================================
        except Exception as e:
            if str(e) == "check_hostname requires server_hostname":
                print("下载出错！" + "   -----关掉VPN试试-----", end="")
            else:
                print("下载出错！", e, end="")



    # urlretrieve
    def down_pic_urlretrieve(self,pic_url,k=1,pic_string=""):

        from urllib import request
        import urllib.request

        opener = request.build_opener()
        opener.addheaders = [('User-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'),
                             ('accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')]

        request.install_opener(opener)

        try:
            import urllib
            import socket
            from urllib.request import urlretrieve
            # *********************************************************************
            if pic_string == "":  # 没有输入下载路径
                pic_string = os.path.join(self.path_Desktop, str(k) + self.postfix)
            # *********************************************************************
            socket.setdefaulttimeout(2)  # 解决下载不完全问题且避免陷入死循环
            urllib.request.urlretrieve(pic_url,pic_string)
        except Exception as e:
             #print(e)
             print("第%d张图片下载错误" % k, "img_url=", pic_url,e)
        finally:
            pass
            # time.sleep(random.randint(0, 3) + random.random()) # 休息数秒，预防IP被禁
            # time.sleep(random.randint(1,5))  # 每批次下载完成多休息几秒


    '''
        图片标题有时候会出现非法字符
        规范字符串，方便成功重命名
    '''
    def rename_file_name(self,pic_name):

        # \ / : * ? " < > |
        char_list = ["?","\\","/",":","*",'"',">","<","|"]

        for cha in char_list:
            pic_name = pic_name.replace(cha, '-')

        return pic_name



if __name__ == "__main__":


    url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTH6790B7c4xlFK6BDSG2F2vQxVRZkO1qbC7g&usqp=CAU"
    # url = "https://img.vmeiji.com/uploads/allimg/1807/1-1PF6143424.jpg"

    # url = "https://img5.tmdpic.com/2020-12-31/1136263686.jpg"
    # url = "https://i.ssjz8.com/upload/1/img0.baidu.com%2Fit%2Fu%3D1823161109%2C143162006%26fm%3D26%26fmt%3Dauto"

    Image = ImageDownload()





    pic_url = "https://img5.tmdpic.com/2020-12-31/1136263686.jpg"

    Image.down_pic_get(pic_url,5)
    Image.down_pic_urlretrieve(pic_url,3)










