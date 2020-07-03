#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: bing.wei
# Email: weibing@missfresh.cn
from __future__ import print_function, division
import sys
# import here

# from multiprocessing import Queue
from mac.support import MultiProcessingQueue as Queue
import multiprocessing

# 默认-1，传任意多个值，直到消息满了
q = Queue(3, ctx=multiprocessing.get_context())

q.put('1')
q.put('2')
q.put('3')

print('qsize:%s' % q.qsize())

print(q.full())
print(q.empty())