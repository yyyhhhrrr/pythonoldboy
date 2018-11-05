#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import os
import sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE ={
    'engine':'file_txt',
    'name':'account',
    'path':'%s/db'%BASE_DIR
}

LOG_LEVEL =logging.INFO
LOG_TYPES ={
    'access':'access.log',
}
