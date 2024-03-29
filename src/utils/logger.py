#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import time
import sys
from src.utils.common import mk_dir



class LogConfig:

    def __init__(self, path):
        """
        日志配置
        :param path: 路径
        """

        runtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        mk_dir(path + "/logs")
        logfile = path + "/logs/" + runtime + '.log'
        logfile_err = path + "/logs/" + runtime + '_error.log'

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.handlers = []

        # 第二步，创建一个handler，用于写入全部info日志文件

        fh = logging.FileHandler(logfile, mode='a+')
        fh.setLevel(logging.DEBUG)

        # 第三步，创建一个handler，用于写入错误日志文件

        fh_err = logging.FileHandler(logfile_err, mode='a+')
        fh_err.setLevel(logging.ERROR)

        # 第四步，再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO)

        # 第五步，定义handler的输出格式
        formatter = logging.Formatter("[%(asctime)s - %(filename)s - line:%(lineno)d - %(levelname)s] %(message)s")
        fh.setFormatter(formatter)
        fh_err.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 第六步，将logger添加到handler里面
        logger.addHandler(fh)
        logger.addHandler(fh_err)
        logger.addHandler(ch)


if __name__ == '__main__':
    logging.info("ass")