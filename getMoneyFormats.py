#!/usr/bin/env python3
# coding=utf-8

"""
说明:
python-学习手册-24章-使用带有__name__的命令行
两个函数
- commas为数字添加逗号
- money为表示金钱的数字格式化, 添加逗号, 和保留两位有效值
"""

def commas(N):
	"""为数字添加逗号"""
	digits = str(N)
	assert(digits.isdigit())
	result = ''
	while digits:
		"""将digits分片, 前部分和后3个数字 """
		digits, last3 = digits[:-3], digits[-3:]
		result = (last3 + ',' + result) if result else last3
	return result
	
def money(N, width=0):	
	sign = '-' if N < 0 else ''
	N = abs(N)
	whole = commas(int(N))  # whole 取N的整数
	fract = ('%.2f' % N)[-2:]
	format = '%s%s.%s' %(sign, whole, fract)
	return '$%*s' %(width, format)    # width为对齐位数
	
if __name__ == '__main__':
	def selftest():
		tests = 0, 1
		tests += 12, 123, 1234, 12345, 123456, 1234567
		tests += 2 ** 32, 2 ** 100
		for test in tests:
			print(commas(test))
		print('')
		test = 0, 1, -2, 1.23, 3.1, 4.55
		tests += 12.34, 12.344, 12.34567
		tests += 2 ** 32, (2 ** 32 + .56789)
		test += 1.234, 1.2, 0.2345
		test += -(2 ** 100), -(2 ** 32 + .345)
		for test in tests:
			print('%s [%s]' % (money(test, 17), test))
			
import sys
if len(sys.argv) == 1:
	selftest()
else:
	print(money(float(sys.argv[1]), int(sys.argv[2])))



"""
一个测试
========================================================================

result = (last3 + ',' + result) if result else last3

==>

if result:
	result = last3 + ',' + result
else:
	result = last3
	
------------------------------------------------------------------------

In [5]: def commas(N):
   ...:     digits = str(N)
   ...:     assert(digits.isdigit())
   ...:     result = ''
   ...:     while digits:
   ...:         digits, last3 = digits[:-3], digits[-3:]
   ...:         print('=>' + digits)
   ...:         print('==>' + last3)
   ...:         result = (last3 + ',' + result) if result else last3
   ...:         print('===>' + result)
   ...:     print('^^^' + result)
   ...:     

In [6]: commas(123)
=>
==>123
===>123
^^^123

In [7]: commas(1234)
=>1
==>234
===>234
=>
==>1
===>1,234
^^^1,234

In [8]: commas(1234567)
=>1234
==>567
===>567
=>1
==>234
===>234,567
=>
==>1
===>1,234,567
^^^1,234,567

"""
