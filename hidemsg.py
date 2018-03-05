#!/usr/bin/env python
#coding=utf-8

"""
hidemsg.py: 根据英文对应的unicode码进行转译,提取

ASCII码值:
        A-Z: 65-90
        a-z: 97-122
"""

def hide(norm_string,lucky_num):
    """两个参数: 要转译的字符串,和自己定的幸运数字(23-86)),也是加密数字;
    同样的加密数字,才能解出相同的加密信息"""
    secrect_string = ""
    for char in norm_string:
        secrect_string += str(ord(char)-int(lucky_num))
    return secrect_string

def show(secrect_string,lucky_num):
    """两个参数: 加密数字,幸运数字(23-86);
    只有自己的幸运数字才能解出自己的加密信息"""    
    norm_string = ""
    for i in range(0,len(secrect_string)-1,2):
        char_code = secrect_string[i] + secrect_string[i+1]
        norm_string += chr(int(char_code)+int(lucky_num))
    
    return norm_string

if __name__ == '__main__':
    print("Secrect Message: ",hide("hello",23))
    print("Hide Message: ",show("8178858588",23))
