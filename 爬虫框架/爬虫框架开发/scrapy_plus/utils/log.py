import sys
import logging



from scrapy_plus.conf.settings import DEFAULT_LOG_FMT,DEFAULT_LOG_DATEFMT,\
    DEFAULT_LOG_FILENAME,DEFAULT_LOG_LEVEL


class Logger():

    def __init__(self):
        # 1.获取一个logger对象
        self._logger = logging.getLogger()
        # 2.设置format对象
        self.formatter = logging.Formatter(fmt=DEFAULT_LOG_FMT,datefmt=DEFAULT_LOG_DATEFMT)
        # 3.设置日志输出
        # 3.1设置文件日志模式
        self._logger.addHandler(self._get_file_handler(DEFAULT_LOG_FILENAME))
        # 3.2设置终端日志模式
        self._logger.addHandler(self._get_consile_handler())
        # 4.设置日志等级
        self._logger.setLevel(DEFAULT_LOG_LEVEL)


    def _get_file_handler(self,filename):
        """返回一个日志handler"""
        # 1.    获取一个文件日志handler
        filehandler = logging.FileHandler(filename=filename,encoding="utf8")
        # 2.    设置日志格式
        filehandler.setFormatter(self.formatter)
        # 3.    返回
        return filehandler

    def _get_consile_handler(self):
        """返回一个数据到终端日志handler"""
        # 1. 获取一个输出到终端日志的handler
        console_handler = logging.StreamHandler(sys.stdout)
        # 2. 设置日志格式
        console_handler.setFormatter(self.formatter)
        # 3. 返回handler
        return console_handler

    @property
    def logger(self):
        return self._logger



logger = Logger().logger


if __name__ == '__main__':
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
