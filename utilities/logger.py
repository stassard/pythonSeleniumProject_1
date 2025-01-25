import datetime
from loguru import logger

file_name = f"D:\\PythonEducation\\autoProjectOnlineStore\\logs\\log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"


logger.add(file_name, format="{time} - {level} - {message}", rotation="10 MB", backtrace=False, retention=10)