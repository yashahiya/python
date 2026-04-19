class studinfo:
    #private
    __stid=14
    __stnm="Yash"

    def __getdata(self):  #private
        print("Id Is:",self.__stid)
        print("Name Is:",self.__stnm)

    def printdata(self):
        self.__getdata()


st=studinfo()
st.printdata()