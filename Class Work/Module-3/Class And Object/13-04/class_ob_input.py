class studinfo:
    stid:int
    stnm:str

    def getdata(self):
        self.stid=input("Enter An Id:")
        self.stnm=input("Enter A Name:")

    def printdata(self):
        print("Id Is:",self.stid)
        print("Name Is:",self.stnm)

st=studinfo()
st.getdata()
st.printdata()