#!/usr/bin/env python3
# coding=utf-8

"""
reloadall.py: 过渡性重载嵌套模块

说明:

- 使用模块-"types"的"ModuleType"属性判断对象是否为模块
- 使用模块-"imp"的"reload()"方法进行重载
"""

import types
from imp import reload

def status(module):
    print('reloading ' + module.__name__)
    
def transitive_reload(module, visited):
    """过渡性重载
    
    查看提供的模块, 进行reload重载
    检测被重载过的模块属性中是否有模块存在, 如果有模块存在, 再次调用本函数transitive_reload
    """
    if not module in visited:
        status(module)
        reload(module)  # 重载模块
        visited[module] = None  # 将重载的模块值改为None
        for attrobj in module.__dict__.values():
            if type(attrobj) == types.ModuleType:  # 判断相应属性如果是模块, 就将属性再此传入重载
                transitive_reload(attrobj, visited)

def reload_all(*args):
    """重载主程序
    
    根据提供的参数, 判断是否为模块, 然后调用函数transitive_reload
    """
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)

if __name__ == '__main__':
    """自我检测程序"""
    import reloadall
    reload_all(reloadall)
