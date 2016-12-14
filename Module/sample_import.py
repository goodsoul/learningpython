#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
#默认情况下，Python解释器会搜索当前目录、
#所有已安装的内置模块
#和第三方模块，搜索路径存放在sys模块的path变量中

print(sys.path)
print('\n')

#直接修改sys.path，添加要搜索的目录：
sys.path.append('/Users/michael/my_py_scripts')
print(sys.path)