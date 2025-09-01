# 2. Multiple Inheritance

class Father:
    def F_skills(self):
        print("Father: Driving")
    
class Mother:
    def M_skills(self):
        print("Mother: Cooking")

class child(Father,Mother):
    def more_skills(self):
        print("Child : Programming")

obj = child()
obj.F_skills()
obj.M_skills()
obj.more_skills()