# -*- coding = utf-8 -*-
# @Time : 2024/4/20 23:21
# @Author : 鬼鬼
# @File : pics_method.py
# @Software: PyCharm


import cv2
import os
from PIL import Image


class ImageMethod():

    def __init__(self):
        pass
        # 1 amplify 放大 ------ 0 reduce 缩小
        # 放大——宽、高 都大于  缩小同理

        # cv2.imread 不能读中文

    #    # file.endswith('.mp4')

        '''
        # ########################################
        # 先判断图片像素， 如果符合标准，就不做调整！！！
        # ########################################
        
        # 放大 ###########################
        flag = 0
        if pic.width < width:  
            new_width = width  # 放大的宽度
            new_height = new_width / temp  # 放大的高度
            flag = 1
    
        if flag == 1: 
            temp = new_width / new_height
            if new_height < height:
                new_height = height  # 放大的高度
                new_width = new_height * temp  # 放大的宽度
        else:
            new_height = height  # 放大的高度
            new_width = new_height * temp  # 放大的宽度
            
            
        # 缩小 ###########################
        flag = 0
        if pic.width > width:
            new_width = width  # 放大的宽度
            new_height = new_width / temp  # 放大的高度
            flag = 1
    
        if flag == 1:
            temp = new_width / new_height
            if new_height > height:
                new_height = height  # 放大的高度
                new_width = new_height * temp  # 放大的宽度
        else:
            new_height = height  # 放大的高度
            new_width = new_height * temp  # 放大的宽度
        '''



    @staticmethod  # 静态方法 # 没有使用self相关的变量
    def process_file_name(path):

        import re
        import os.path
        front_path, origin_filename = os.path.split(path)

        # 使用正则表达式匹配中文字符
        china_font = re.compile(r'[\u4e00-\u9fa5]+')

        # 查看有无中文字符
        res = re.search(china_font, origin_filename)

        if res is not None:
            # # 将 匹配到的中文字符 用】 替换
            no_chinese_filename = re.sub(china_font, "^", origin_filename)
            return front_path, origin_filename, no_chinese_filename

        return res


    @staticmethod
    def check_size_remove(path,target_size, num=1, flag_no_less=1):
        # 检测/移除 ... ...
        width, height = target_size  # 检查的像素值

        single_img = Image.open(path)
        single_img.close()
        # 不低于   >= 即太大-就缩小
        if single_img.width >= int(width) and single_img.height >= int(height) and flag_no_less == 1:
            pass
        # 不高于   <= 即太小-就放大
        elif single_img.width <= int(width) and single_img.height <= int(height) and flag_no_less == 0:
            pass
        else:
            # try:
            #     flag_remove = input("y/n?")
            #     if flag_remove == 'y':
            #         os.remove(path)
            # except:
            #     print("图片移除出错！！！", path)

            print("-共计%d张--------------需要检查像素！！！----------------" % (num + 1))
            print('图片-路径:', path)
            print("宽:" + str(single_img.width), "高:" + str(single_img.height))
            print()


    def amplify_execute(self,pic_path,target_size):

        target_width, target_height = target_size

        try:
            single_img = Image.open(pic_path)
            width, height = single_img.size  # 保存原图片的像素值
            single_img.close()
            if single_img.width >= int(target_width) and single_img.height >= int(target_height):
                pass
            else:
                print("不符合要求:", single_img.width, single_img.height)
                self.amplify_pixel_size(pic_path,height, width,target_size)

        except Exception as e:
            print("图片出错！", e)


    @staticmethod
    def amplify_pixel_size(path,height, width, target_size):
        # ********** 此函数是 调整到最符合像素的比例,即 符合标准也会调整像素 **********
        target_width, target_height = target_size

        # =====数学逻辑=====
        # ============================================
        scale = width / height  # 原图片的 宽高比例
        new_width = target_width
        new_height = int(target_width / scale)

        # 如果 高度 小于 target_height
        if new_height < target_height:
            # 就改变 高度的值，宽度 也会跟着变
            new_scale = new_width / new_height
            # 再稍微修一下 new_width , new_height 的值 ========
            new_width = int(target_height * new_scale)
            new_height = target_height
        # ============================================

        amplify_size = (int(new_width), int(new_height))  # 放大的像素
        img = Image.open(path)  # 图片
        magnified_image = img.resize(amplify_size).convert('RGB')
        magnified_image.save(path)


    def reduce_execute(self,pic_path,target_size):

        target_width, target_height = target_size

        try:
            single_img = Image.open(pic_path)
            single_img.close()
            if single_img.width <= int(target_width) and single_img.height <= int(target_height):
                pass
            else:
                print("不符合要求:", single_img.width, single_img.height)

                origin_img, height, width, result = self.get_pixel_size(pic_path)
                self.reduce_pixel_size(pic_path, origin_img, height, width, target_size, result)

        except Exception as e:
            print("图片出错！",e)


    @staticmethod
    def reduce_pixel_size(path,ori_img,height, width, target_size,result_):

        target_width, target_height = target_size

        # ====由放大修改的, 所以参数有所颠倒 =================
        scale = width / height  # 图片比例
        new_width = target_width
        new_height = int(target_width / scale)

        if new_height > target_height:  # 这里只是变了运算符
            new_scale = new_width / new_height
            # 再稍微修改 new_width , new_height 的值 ========
            new_width = int(target_height * new_scale)
            new_height = target_height
        # =================================================

        # 缩小尺寸  # img里也包含了 文件名的信息
        img = cv2.resize(ori_img, (new_width, new_height))

        if result_ is None:
            cv2.imwrite(path, img)
        else:
            path1, path2 = result_[3], result_[4]
            cv2.imwrite(path2, img)  # 存储

            os.rename(path2, path1)  # 修改文件 为 原来样子
        #print("reduce 成功！")

        '''
        # 也可以这样 ############################
        size = (int(new_width), int(new_height))  # 放大的像素
        pic = pic.resize(size).convert('RGB')
        pic.save(pic_path)
        
        '''


    @staticmethod
    def get_pixel_size_open(path):
        img = Image.open(path)
        width, height = img.size
        return width, height


    def get_pixel_size(self, path):
        # 像素大小

        # cv2.imread 不能读中文 ----------------------
        # None / front_path, origin_filename, no_chinese_filename
        res_ = self.process_file_name(path)

        # cv2.imread 不能读中文 ----------------------
        if res_ is None:
            # print("文件名内 无中文")
            origin_img_ = cv2.imread(path)  # 读取图片
        else:
            # print("文件名内 有中文 ====== 完成后等1s ！！！")
            front_path, origin_filename, no_chinese_filename = res_

            # *****************************************************
            path1 = front_path + "\\" + origin_filename  # 修改前的文件路径
            path2 = front_path + "\\" + no_chinese_filename  # 修改后的文件路径

            os.rename(path1, path2)  # 修改文件 为 变成无中文字符
            origin_img_ = cv2.imread(path2)  # 读取图片

            res_ = res_ + (path1, path2)

        # ori_img.shape = (1350, 1080, 3) #高 宽（h,w,3）,  坐标系不同(y,x,3) 是元组
        height_, width_ = origin_img_.shape[:2]  # 原始分辨率

        return origin_img_, height_, width_, res_



def main():


    Img = ImageMethod()  # 定义类

    dir_path = r"C:\Users\85317\Desktop\test\snow"
    # target_size = (400, 300)  #
    target_size = (1280, 720)
    verify_width,verify_height = 20, 20  # 可以 筛掉下载错误图片(4x8像素)

    files = os.listdir(dir_path)
    for num, f in enumerate(files):
        pic_path = os.path.join(dir_path,f)
        print(num, pic_path)

        # # 等比例缩小
        # Img.reduce_execute(pic_path,target_size)

        # 等比例放大
        #Img.amplify_execute(pic_path,target_size)

        # 检查像素
        Img.check_size_remove(pic_path,target_size,flag_no_less=0)




if __name__ == "__main__":

    main()












