class me:
     def __init__(self, name, age, study):
        self.name = name
        self.age = age
        self.study = study

def introduce(self):
        print("안녕하세요, 저는" + self.name +"입니다. " + self.age +"살이고, 듣고 있는 강의는" +self.study +"입니다.")

yoo = me("유소희", 21, "프론트엔드 강의")
yoo.introduce()