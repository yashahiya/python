class studinfo :
    stid=12
    stname="Yash"

    def getdata(self):
        print("This Is Get Data")

    def getsum(self,a,b):
        print("Sum Is : ",a+b)

#object of class

st=studinfo()

print("ID:",st.stid)
print("Name:",st.stname)

st.getdata()
st.getsum(12,45)