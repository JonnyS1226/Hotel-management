# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
用于跨文件修改的全局变量
"""
import sys
from dao.dbOpStaff import Staff
from dao.dbConfig import localSourceConfig as localConfig

"""员工信息的全局变量存取"""
def _initStaff():
    global staff
    staff = Staff()
    return staff

def get_staff():
    global staff
    return staff


"""
客房信息的全局遍历
"""
















# key = 0xff


# def encrypt(src):
#     return ''.join([unichr(ord(x)^key) for x in src]).encode('utf-8').upper()
#
#
# def decrypt(src):
#     return ''.join([unichr(ord(x)^key) for x in src.decode('utf-8')])
#
# if __name__ == '__main__':
#     list_ = ['540845199705184854', '847578199711265846', '370954199711054879', '263589622522336522', '6545236653314556', '4648794654897994', '565646118797615459', '565484615613879', '625148216548415', '37098319930304591', '845478199703035687']
#     for i in list_:
#         print encrypt(i)