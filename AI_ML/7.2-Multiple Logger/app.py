import logging

## logging settings

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[ 
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("ArithmeticApp")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a}+{b}={result}")
    return result
def subtraction(a,b):
    result=a-b
    logger.debug(f"Subtraction {a}-{b}={result}")
    return result
def multiplication(a,b):
    result=a*b
    logger.debug(f"Multiplication {a}*{b}={result}")
    return result

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"Dividing {a} / {b}= {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    
add(5,3)
subtraction(2,3)
multiplication(5,5)
divide(9,0)


    
