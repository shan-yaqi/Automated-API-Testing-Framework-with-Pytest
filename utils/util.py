import yaml
import os
import requests
import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler
from utils.colors import ColoredFormatter
Coloredformatter = ColoredFormatter()

class RequestUtil:
    BASE_DIR_d = os.path.dirname(os.path.abspath(__file__))
    BASE_DIR = os.path.dirname(BASE_DIR_d)
    LOG_DIR = os.path.join(os.path.join(BASE_DIR, "results"),"logs")
    TIMESTAMP = datetime.now().strftime("%Y%m%d_%H_%M_%S")
    BASEURL = "https://reqres.in/"

    os.makedirs(LOG_DIR, exist_ok=True)

    @staticmethod
    def send_requests(method,url,data=None):
        header = {
            'Content-Type': 'application/json',
            'x-api-key': 'pub_50e4576a07d3a071e4d80ac14b4e94081a063005c265227806ff5fc562550d5f'
        }
        session = requests.Session()
        if isinstance(data,dict):
            response = session.request(method=method, url=url, headers=header, json=data)
        else:
            response = session.request(method=method, url=url, headers=header, data=data)
        return response

    @staticmethod
    def read_yaml(data_path):
        with open(data_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return data

    # @staticmethod
    # def resquest_safe(method,url,data=None):
    #     try:
    #         response = RequestUtil.send_requests(method,url,data)
    #         if response.status_code == 200:
    #             return response
    #         elif response.status_code >= 500:

    @staticmethod
    def get_logger(LOG_DIR,TIMESTAMP,name="auto_test_logger"):
        """
        Create and return a pre-configured Logger object.
        """
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        log_file = os.path.join(LOG_DIR, f"run{TIMESTAMP}.log")

        if not logger.handlers:  # 防止重复添加handler
            file_handler  = RotatingFileHandler(
                filename=log_file,  # when = "midnight"
                maxBytes=5 * 1024 * 1024,
                backupCount=5,
                mode='a',
                encoding="utf-8"
            )
            file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
            logger.addHandler(file_handler )

            console_handler = logging.StreamHandler()
            console_formatter = ColoredFormatter(
                "%(asctime)s [%(levelname)s] %(message)s"
            )
            console_handler.setFormatter(console_formatter)
            logger.addHandler(console_handler)
        return logger


