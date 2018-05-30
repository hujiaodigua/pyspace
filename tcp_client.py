#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import socket
import os
import sys
import struct
import time

def socket_client_recv():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('192.168.0.103',6666))
        except socket.error as msg:
            print(msg)
            sys.exit(1)
        print("connecting service...")
        
        data_from_service = s.recv(64)
        print(data_from_service)
        
        data_from_service = s.recv(64)
        print(data_from_service)
        
        time.sleep(1)

        while 1:
            data_from_service = s.recv(64)
            if(data_from_service):
                print(data_from_service)


if __name__ == '__main__':
        socket_client_recv()
    

