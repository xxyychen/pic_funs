# -*- coding = utf-8 -*-
# @Time : 2024/4/17 14:32
# @Author : 鬼鬼
# @File : pics_inf.py
# @Software: PyCharm

class ImageInfo():

    def __init__(self):
        pass


    def employ_memory(self,image_path):
        # 占用内存
        import os
        imagesize = os.path.getsize(image_path)

        imagesize /= 1024  # Kb
        if imagesize // 1024 == 0: # 不到1M
            print("图片占内存: %.1fkb" % imagesize)
        else:
            t = imagesize / 1024
            print("图片占内存: %.1fM" % t)





if __name__ == "__main__":

    ImageInfo().employ_memory(r'C:\Users\85317\Desktop\test\2.jpg')


