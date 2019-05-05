from functools import wraps
from time import time
from commons.loggy import set_up_logging
logger = set_up_logging()


def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = 0
        start = int(round(time() * 1000))
        end_ = 0
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"Total execution time for ", args[0].path, ":", func.__name__, ":", end_ , "ms")
            result = args[0].path + " " + func.__name__ + " " + str(end_)
            logger.info("Total execution time: for {} ms".format(result))
    return _time_it


def measure_all_class_methods(Cls):
    class NewCls(object):
        def __init__(self,*args,**kwargs):
            self.oInstance = Cls(*args,**kwargs)

        def __getattribute__(self,s):
            """
            this is called whenever any attribute of a NewCls object is accessed. This function first tries to
            get the attribute off NewCls. If it fails then it tries to fetch the attribute from self.oInstance (an
            instance of the decorated class). If it manages to fetch the attribute from self.oInstance, and
            the attribute is an instance method then `time_this` is applied.
            """
            try:
                x = super(NewCls,self).__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x
            x = self.oInstance.__getattribute__(s)
            if type(x) == type(self.__init__): # it is an instance method
                return measure(x)                 # this is equivalent of just decorating the method with time_this
            else:
                return x
    return NewCls
