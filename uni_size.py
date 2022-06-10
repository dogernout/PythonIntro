import copy


class sizer:

    def __init__(self, cls):
        self.size = 0
        self.cls = cls

    def __call__(self, *args):
        if not args: arz = ''
        else: arz = copy.deepcopy(*args)
        if '__len__' in dir(self.cls):
            try:
                len(self.cls)
            except Exception:
                if 'keys' in dir(self.cls): self.cls.size = len(dict(arz))
                elif 'intersection' in dir(self.cls): self.cls.size = len(set(arz))
                elif 'append' in dir(self.cls): self.cls.size = len(list(arz))
                else:
                    if not args:
                        self.cls.size = self.cls.__len__(args)
                    else: self.cls.size = self.cls.__len__(*args)#len(*args)
        elif '__abs__' in dir(self.cls):
            if not args: self.cls.size = self.cls.__abs__(args)
            else: self.cls.size = abs(*args)
        else: self.cls.size = 0
        return self.cls.__call__(*args)
