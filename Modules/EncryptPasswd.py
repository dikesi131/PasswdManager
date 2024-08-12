########################################################################
 # $ @Author: d1k3si
 # $ @Date: 2024-08-08 11:13:28
 # $ @LastEditors: d1k3si
 # $ @LastEditTime: 2024-08-08 11:42:46
 # $ @email:2098415680@qq.com
 # $ @Copyright (c) 2024 by d1k3si
########################################################################
import pyAesCrypt

def Encryption(input_file_path:str, output_file_path:str, key:str):
    buffer_size = 64 * 1024  # 缓冲区大小(64KB)
    pyAesCrypt.encryptFile(input_file_path, output_file_path, key,buffer_size)

def Decryption(input_file_path:str, output_file_path:str, key:str):
    buffer_size = 64 * 1024  # 缓冲区大小(64KB)
    pyAesCrypt.decryptFile(input_file_path, output_file_path, key,buffer_size)