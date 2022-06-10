class Tester():

    def __init__(self, fun):
        self.fun = fun

    def __call__(self, suite, allowed = []):
        flag = 0
        for i in suite:
            try:
                self.fun(*i)
            except Exception as exp:
                if type(exp) in allowed or Exception in allowed: flag = -1
                else: return 1
        return flag
