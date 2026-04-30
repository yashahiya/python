class person:
    def __init__(self,name):
        self.name=name

    def display(self):
        print("Name Is:",self.name)

class student(person):
    def __init__(self, name,course):
        super().__init__(name)
        self.course=course

    def show(self):
        super().display()
        print("Course:",self.course)

obj=student("Yash","B.Com")
obj.show()