import os
import logging
class Log:

    @staticmethod
    def error(message:str,trace:any):
        log = logging.getLogger(__name__)
        appName = os.getenv('APP_ENV','Application')
        logFile = os.getenv('AGENDATE_DIR')+ '/src/Storage/Log/' +appName.replace(' ','_')+".log"
        logging.basicConfig(filename=logFile,format='%(asctime)s - %(name)s - %(levelname)s => %(message)s',level=logging.ERROR,encoding="utf-8")
        logging.error(message + "\n" + str(trace))

    @staticmethod
    def debug(message:str,trace:any):
        log = logging.getLogger(__name__)
        appName = os.getenv('APP_ENV','Application')
        logFile = os.getenv('AGENDATE_DIR')+ '/src/Storage/Log/' +appName.replace(' ','_')+".log"
        logging.basicConfig(filename=logFile,format='%(asctime)s - %(name)s - %(levelname)s => %(message)s',level=logging.DEBUG,encoding="utf-8")
        log.info(message + "\n" + str(trace))


