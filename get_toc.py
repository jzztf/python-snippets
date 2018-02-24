#!/usr/bin/env python3
# coding=utf-8

"""
获取当前目录, 追加到README以便说明片段
"""

import os

def get_toc(dir):
	l = os.listdir(dir)
	l_ignore = ['.git', '.gitignore','README.md']
	for x in l_ignore:
		l.remove(x)
	with open('README.md') as f_old:
		line_old = f_old.readlines()
	toc = open('README.md', 'a+')
	for f in l:
		f = '- ' + f + '\n'
		if f not in line_old:
			toc.write(f)
		else:
			continue
	toc.close()
	with open('README.md') as f:
		for x in f.readlines():
			print(x)	
		

get_toc('.')
