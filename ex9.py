class newclass():
    protec="smit"
    _protec2="vekariya"
    __priva="nikunjbhai"
    def __init__(self,protec,protec2,priva):
        self.protec=protec
        self._protec2=protec2
        self.__priva=priva
    def display(self):
        print(self.protec+" "+self._protec2+" "+self.__priva)
    
stu=newclass()
stu.display()