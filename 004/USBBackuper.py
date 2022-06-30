#!/usr/bin/env python3
#-*- coding: utf-8 -*-


from window import run_window
from log import Log


if __name__ == '__main__':
    Log('============程序开始运行============')
    Log('载入窗口')
    run_window()
    Log('============程序关闭============')