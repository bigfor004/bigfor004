class Member:    #父類別
    def __init__(self, new_gender, new_major, new_id):
        def __init__(self, new_gender, new_major, new_id):
            self.__gender = new_gender  # 選告此方法為私有只能在此類別執行__
            self.major = new_major
            self.id = new_id

    def get_gender(self): #c回傳private屬性
        return self.__gender

    def set_gender(self, new_gender):
        if new_gender == 'M' or new_gender == 'F':
            self.__gender = new_gender
        else:
            print('====請傳入"M"或"F"====')

    def borrow_resources(self):
        pass
    def check_auth(self):
        pass

class Student(Member):   #子類別
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)

    def borrow_resources(self):
        print('student borrow')

    def join_class(self):   #self負責傳自己本身
        pass

    def quit_class(self):
        pass

class Professor(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)

    def borrow_resources(self):
        print('professor borrow')

studentA = Student('M','工管系','B10721004')   #類別實體化物件
studentB = Student('F','文資系','B107232008')
professorC = Professor('f','經濟系','T10532054')
professorD = Professor('M','會計系','t10624074')

ls = [studentA, studentB, professorC, professorD]

for item in ls:
    item.borrow_resources()

studentA.__gender = "K"
print(studentA.__gender)     #印出物件student1的gender
studentA.set_gender('F')
print(studentA.__gender)
studentA.join_class()      #呼叫物件的join_class方法