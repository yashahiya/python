class studeinfo:
    stid=1427
    stnm="Yash"
    def getdata(self):
        print("Id Is : ",self.stid)
        print("Name Is : ",self.stnm)

    def getsum(self,a,b):
            return a+b
        
#calling via object

st=studeinfo()
st.getdata()
st.stid=2714
st.stnm="Mohit"
st.getdata()


#calling via instance

studeinfo().getdata()
studeinfo().stid=2714
studeinfo().stnm="Mohit"
studeinfo().getdata()
x=studeinfo().getsum()