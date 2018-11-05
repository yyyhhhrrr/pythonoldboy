#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import logging
from conf import settings
import time
def logger(log_type,message):
    time_format="%Y-%m-%d %X"
    time_current=time.strftime(time_format)
    with open(settings.BASE_DIR+"\\log\\%s.log"%log_type,"a+") as f:
        f.write("\n"+time_current+message)
    f.close()