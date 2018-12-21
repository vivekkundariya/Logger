import inspect

class logger:
    __isDebug = False

    def __print(*args):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        file_array = filename.split('/')
        file_array= file_array[len(file_array)-1].split("\\")
        s = ' '.join(str(i) for i in args)
        print((file_array[len(file_array)-1], inspect.stack()[2][3], inspect.stack()[1][3]), " :-  ", s)
        return

    def enableDebug():
        print("######DEBUG ENABLED########")
        logger.__isDebug = True
        return
    
    def disableDebug():
        print("######DEBUG DISABLED########")
        logger.__isDebug = False
        return

    def debug(*args):
        if(logger.__isDebug == True):
            logger.__print(*args)
        return

    def error(*args):
        logger.__print("error",*args)
        return
    
    def log(*args):
        logger.__print(*args)
        return

def main():
    logger.disableDebug()
    logger.debug("hello")
    logger.error("hello")
    logger.log("normal", "log", "hello")
    
    logger.enableDebug()
    logger.debug("hello")
    logger.error("hello")
    return

if __name__ == "__main__":
    main()