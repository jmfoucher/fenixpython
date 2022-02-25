#-*- coding:utf-8 -*-
#cython: language_level=3
# AUTHOR:   foucher
# FILE:     logger.py
# ROLE:     logger
# CREATED:  2020-12-08 21:43:08
# MODIFIED: 2020-12-08 21:43:08

"""
Module documentation.
"""

# Imports

import logging
import gzip
import os
import shutil
import sys
from logging import handlers

# Logs

# Global variables

#fileHandler = TimedRotatingFileHandler(
#    filename=filename, when='h', interval=12, backupCount=10
#    )
#fileHandler.setFormatter(formatter)
#logger = logging.getLogger(logger_name)

formatter = logging.Formatter(fmt='%(asctime)s:%(levelname)s:%(name)s: %(message)s',
                              datefmt='%y/%m/%d %H:%M:%S')

# Class declarations

class TimedRotatingFileHandler(handlers.TimedRotatingFileHandler):


    def __init__(self, filename="", when="midnight", interval=1,
                 backupCount=14
                 ):
        #print("filename = " + filename)
        super(TimedRotatingFileHandler, self).__init__(
            filename=filename,
            when=when,
            interval=int(interval),
            backupCount=int(backupCount)
        )


    def doRollover(self):
        super(TimedRotatingFileHandler, self).doRollover()
        log_dir = os.path.dirname(self.baseFilename)
        to_compress = [
            os.path.join(log_dir, f) for f in os.listdir(log_dir) if f.startswith(
                os.path.basename(os.path.splitext(self.baseFilename)[0])
            ) and not f.endswith((".gz", ".log"))
        ]
        for f in to_compress:
            if os.path.exists(f):
                with open(f, "rb") as _old, gzip.open(f + ".gz", "wb") as _new:
                    shutil.copyfileobj(_old, _new)
                os.remove(f)

# Function declarations

def createHandler(loggerName):

    dirName, baseName = os.path.split(loggerName)
    dirNameBackup = dirName
    dirName = os.path.join(dirName, 'logs')
    if not os.path.isdir(dirName):
        try:
            os.mkdir(dirName)
        except OSError:
           print("Creation of the directory %s failed" % dirName)
           dirName = dirNameBackup
       #else:
       #    print("Successfully created the directory %s " % dirName)

    loggerName = os.path.join(dirName, baseName)


    fileHandler = TimedRotatingFileHandler(
        filename=loggerName+'.log', 
        #filename=loggerName+'.log', 
        when='h', interval=12, backupCount=10
        )
    fileHandler.setFormatter(formatter)
    return fileHandler


def getName(filename):
    name = filename.split('.')[0]
    paths = []
    for path in sys.path:
        if path in filename:
            paths.append(path)

    if paths:
        minPath = min(paths)
        name = filename.replace(minPath, '')
        if name.startswith('/'):
            name = name[1:]
        name = name.replace('/', '.')
    return name


def getLogger(filename, level=logging.DEBUG):
    name = getName(filename)
    handler = createHandler(name)
    log = logging.getLogger(name)
    log.addHandler(handler)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    streamHandler.setLevel(level)
    log.addHandler(streamHandler)
    logging.root.setLevel(level)
    return log


# Main body


