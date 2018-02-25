#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
"""
mydir.py: 一个用来展示其他模块命名空间的模块, 自己的"dir()"工具

主要使用:
- module.__dict__获取命名空间的所有属性
- 通过"__"开头判断是否为内建属性
- get(module, attr) ==> module.__dict__[attr]
"""

seplen = 60
sepchr = '-'

def listing(module, verbose=True):
    """列出模块信息主程序"""
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print('name: ', module.__name__, 'file: ', module.__file__)
        print(sepline)
        
    count = 0
    for attr in module.__dict__:
        print('<%03d> %s' %(count, attr), end=' ')
        if attr.startswith('__'):
            print('<built-in name>')
        else:
            print(getattr(module, attr))  # getattr == .__dict__[attr] 
        count += 1
        
    if verbose:
        print(sepline)
        print(module.__name__, 'has %d names' %count)
        print(sepline)

if __name__ == '__main__':
    """自我测试程序"""
    import mydir
    listing(mydir)  # 自我测试
