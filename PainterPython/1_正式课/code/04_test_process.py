#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 14:46:12 2023

@author: lilianli
"""

import multiprocessing

import time

    
import os
import subprocess

def print_numbers(name, start, end):
    for i in range(start, end):
        print(name, i)
    
if __name__ == "__main__":
    num_processes = 4
    processes = []

    for i in range(num_processes):
        process = multiprocessing.Process(target=print_numbers, args=("process " + str(i), 1, 100))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print("All processes have finished.")
    


    # 启动一个子进程并执行命令
    proc = subprocess.Popen(['ping', 'www.google.com'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # 获取子进程的PID
    pid = proc.pid
    print(f"子进程的PID：{pid}")
    
    # 使用os模块获取进程的信息
    try:
        proc_info = os.waitid(os.P_PID, pid, os.WEXITED | os.WNOWAIT)
        print(f"进程的返回码：{proc_info.si_status}")
        print(f"进程是否退出：{os.WIFEXITED(proc_info.si_status)}")
        print(f"进程是否被信号中断：{os.WIFSIGNALED(proc_info.si_status)}")
        print(f"进程是否暂停：{os.WIFSTOPPED(proc_info.si_status)}")
    except ChildProcessError:
        print("子进程还在运行")
    
    # 等待子进程执行结束
    stdout, stderr = proc.communicate()
    print(f"子进程的输出：{stdout.decode()}")

    