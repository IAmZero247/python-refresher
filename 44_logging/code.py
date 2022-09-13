import logging

print(dir(logging))

#Level		Numeric Value
#************************
#notset		0
#debug		10
#info		20
#warning	30     Default
#error		40
#critical	50


#1 Create & Configure logger:
log_format = "%(levelname)s %(asctime)s - %(message)s"

#2 Create & Configure logger:
#  filemode='w'

#3 Create & Configure logger: #Default logging level for basicConfig ==> 30
logging.basicConfig(filename="../logging/pythonlogs.log" , format=log_format, filemode='w')
logger = logging.getLogger()

#4 Setting the log level to DEBUG:
logger.setLevel(logging.DEBUG)

#Test the Logger
logger.debug("This is my debug logger")
logger.info("This is my info logger")
logger.warning("This is my warning logger")
logger.error("This is my error logger")
logger.critical("This is my critical logger")
print(logger.level)
