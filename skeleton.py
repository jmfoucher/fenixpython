#-*- coding:utf-8 -*-
# AUTHOR:   foucher
# FILE:     skeleton.py
# ROLE:     TODO (some explanation)
# CREATED:  2020-12-08 21:43:08
# MODIFIED: 2020-12-08 21:43:08

# Logs

#import logging
#logging.basicConfig(
#    format='%(asctime)s:%(levelname)s:%(name)s: %(message)s',
#    datefmt='%y/%m/%d %H:%M:%S')

#loggerName = __file__.split('.')[0]

#from logger import createHandler
#handler = createHandler(loggerName)
#log = logging.getLogger(loggerName)
#log.addHandler(handler)
#
#logging.root.setLevel(logging.DEBUG)
##logging.root.setLevel(logging.INFO)


from logger import getLogger
#log = getLogger(loggerName)
log = getLogger(__file__)

# Imports


# Global variables


# Class declarations


# Function declarations


# Main body


def main():

    import argparse
    from argparse import RawTextHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)

    parser.add_argument('-v', '--verbose',
        dest='verbose', help='increase verbosity',
        action='store_true')

    parser.add_argument('-a', '--args',
        dest='args', help="""Set arguments.
Format: key=value,key=value,etc...

Available Keys:
- key1
    explanation1
- ...

Example: -a key1=value

""",
        nargs='?',
        metavar=('key=value,...',),
        default='')

    args = parser.parse_args()

    if args.args:
        kw = dict(item.split("=") for item in args.args.split(","))
        for k,v in kw.items():
            try:
                v = float(v)
                kw[k] = v
                continue
            except: pass
            try:
                v = int(v)
                kw[k] = v
                continue
            except: pass

    # TODO

    # END OF MAIN



if __name__ == "__main__":
    log.info("START...")
    #log.debug("Debug log message")
    #log.debug("pyPiqDetection.version = %.1f" % pd.version)
    main()
    log.info("...END.")
