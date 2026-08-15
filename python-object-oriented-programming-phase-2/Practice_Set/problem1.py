class Programmers:
    company ="Microsoft"
    def __init__(self,name,salary,pincode):
        self.name = name
        self.salary = salary
        self.pincode =pincode

p = Programmers("alex",12000,31332)
print(p.name,p.company,p.salary,p.pincode)

r = Programmers("ralex",12000,3122332)
print(r.name,r.company,r.salary,r.pincode)