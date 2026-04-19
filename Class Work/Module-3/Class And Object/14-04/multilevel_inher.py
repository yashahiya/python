class yash:
    yid:int
    ytech:str

    def y_getdata(self):
        self.yid=input("Enter Yash's Id:")
        self.ytech=input("Enter Yash's Technology:")

class mohit(yash):
    mid:int
    mtech:str

    def m_getdata(self):
        self.mid=input("Enter Mohit's Id:")
        self.mtech=input("Enter Mohit's Technology:")

class dhara(mohit):
    did:int
    dtech:str

    def d_getdata(self):
        self.did=input("Enter Dhara's Id:")
        self.dtech=input("Enter Dhara's Technology:")

class vandna(dhara):
    vid:int
    vtech:str

    def v_getdata(self):
        self.vid=input("Enter Vandna's Id:")
        self.vtech=input("Enter Vandna's Technology:")


class ahiya(vandna):
    def printdata(self):
        print("------Yash Information-------")
        print("Yash's Id Is:",self.yid)
        print("Yash's Technology Is:",self.ytech)
        print("------Mohit Information-------")
        print("Mohit's Id Is:",self.mid)
        print("Mohit's Technology Is:",self.mtech)
        print("------Dhara Information-------")
        print("Yash's Id Is:",self.did)
        print("Yash's Technology Is:",self.dtech)
        print("------Vandna Information-------")
        print("Yash's Id Is:",self.vid)
        print("Yash's Technology Is:",self.vtech)


nm=ahiya()
nm.y_getdata()
nm.m_getdata()
nm.d_getdata()
nm.v_getdata()
nm.printdata()
