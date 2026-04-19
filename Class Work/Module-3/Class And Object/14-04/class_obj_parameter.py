class studinfo:
    def getdata(self,stid,stnm):
        print("Id Is:",stid)
        print("Name Is:",stnm)

st=studinfo()
#st.getdata(1427,"Yash")

id=input("Enter Your Id:")
name=input("Enter Your Name:")

st.getdata(id,name)