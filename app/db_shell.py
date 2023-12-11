from app.models import  *

# exec(open(r"D:\SHRADA PYTHON B10\b10_env\Django_projects\first_project\app\db_shell.py").read())  #for reading perpose

#CRUD


#1)read


# all_emps =  employee.objects.all()
# print(all_emps)

# emp=Employee.objects.get(id=3)       # o/p madhe first name and lastname yet ahe coz apn models.py madhe __str__method mashe self.firstname ani self.lastname mention kela ahe so
# print(emp)



# for emp in all_emps:
#     print(emp.id)
# try:
#     emp=Employee.objects.get(first_name="Emp1")
#     print(emp)
# except Employee.DOESNOTExits as msg:
#     print(msg)

# emps = Employee.objets.filter(first_name__startwith="A")   #error raise nahi karta hai filter
# print(emps)

# emps = Employee.objets.filter(first_name__startwith="E")   #error raise nahi karta hai filter
# print(emps)

# emps = Employee.objets.filter(first_name__in=["Emp1","Emp2"])
# print(emps)

#contains   -- jiske first name mai 1 hai o dega

# emps = Employee.objets.filter(first_name__contains='1')
# print(emps)

# emps = Employee.objets.filter(first_name__contains='E')
# print(emps)


# emps = Employee.objets.filter(first_name__contains='E').first()
# print(emps)

# emps = Employee.objets.filter(first_name__contains='E')[0]
# print(emps)

#2)create 1

# emp=Employee(first_name="Emp6",last_name="lastname",email="emp@gmail.com",mob_no=5667678767)
# emp.save()

#another way

#create 2
#emp=Employee.objets.create(first_name="Emp7",last_name="lastname",email="emp@gmail.com",mob_no=5667678767)


#delete

# emp= Employee.objects.get(id=4)   #hard deltete #delete from database
# emp.delete()

#or

# emp= Employee.objects.get(id=4).delete()

#update

# emp_obj = Employee.objects.get(id=1)
# emp_obj.first_name = "Employee1"
# emp_obj.last_name="emplastname"
# emp_obj.save()

#chatgpt

# from django.db.models import Avg, Count, Sum

# # Calculate the average salary of all employees
# avg_salary = Employee.objects.aggregate(Avg('salary'))
# print(avg_salary)

# # Count the number of employees in each position
# position_counts = Employee.objects.values('position').annotate(count=Count('position'))
# print(position_counts)

# # Sum of salaries of all employees 
# total_salary = Employee.objects.aggregate(Sum('salary'))
# print(total_salary)

# total_count = Employee.objects.count()
# print(total_count)
 
#aggretion(): avg of all salary

# avg_sal= Employee.objects.aggregate(Avg("salary"))
# print(avg_sal)


#orderby():

# data= Employee.objects.order_by("salary")
# print(data)   # asc ordering 


# data= Employee.objects.order_by("-salary")   #only pus - sign for desc
# print(data)   # desc ordering 


#chaning:

# filtered_emp = Employee.objects.filter(first_name__startswith = "E").order_by("id")
# print(filtered_emp)


##one to one kute pn mention kela tari chalte, in any table, eka la ekch id mention karu shakto cause 1-1. on delete cascade kela tar te profile delete honar pan reverse nahi

'''create person and profile classes in models.py do makemigrations and migrate .. which will create these two table in database 
thes crete object as follows, which will insert record to these table ...perfrom get,update,delete..if u want to..then register this table 
in the admin.py.. if u want to show these tabe on front end in the app'''



from datetime import datetime

#1-create  the person and profile(migrate mule empty table query creat zali ahe i.e table tyt data insert kraych)

# p1 = Person.objects.create(first_name="shradha",last_name="bidwai")
# p5 = Person.objects.create(first_name="shraavya",last_name="pame1")


# Profile.objects.create(bio="student",birthdate=datetime(1995,1,26),Person=p1) #one way to mention person id
# Profile.objects.create(bio="student2",birthdate=datetime(1995,1,11),Person=p5)    #or person_id=p1.id



# p13 = Person.objects.create(first_name="sh13",last_name="p13")

# p13=Person.objects.get(id=13)         #fetch data
# # print(p)

# p2=person.objects.get(id=2)


# p3=Person.objects.get(id=3)
# p3.delete()


# p1=Person.objects.create(first_name="shradha1",last_name="b1")

# Address.objects.filter(id__in=[1,2]).update(person=p1)

#or

# Address.objects.get(id=1)
# Address.objects.get(id=2)


#2.fetch(get) person ka address 
p1=Person.objects.get(id=4)
# print(dir(p1))
# print(p1.address_set.all())

#address se person fetch karna hai(means alredy datahai o read karne ke liye)

# adr1=Address.objects.get(id=16)  # if we want person belong to that perticular  address
# print(adr1.person)

#so forward direction (in 1-m) madhe yetana....set all karaw lagte ani backword direction la just .person

# Address.objects.create(street="dp road",city="pune",state="MH",postal_code=431714,person=p3)
# Address.objects.create(street="wakad road",city="pune",state="MH",postal_code=431714,person_id=p3.id)

# p4=Person.objects.get(id=4)   


# Address.objects.create(street="dp road",city="pune",state="MH",postal_code=431714,person=p4)
# Address.objects.create(street="wakad road",city="pune",state="MH",postal_code=431714,person_id=p4.id)


#3.update all records
# Profile.objects.all().update(birthdate= datetime(1995, 8, 29))



#--------------many to many relationship( many car model used many fuel type and many fules used in one car or car model can run on diffrent fule type)------------
    # in any table relationship mention karu shakto...association table create nahi karaw lagat in django it will create automatically gets created
    #fuletype=models.ManyToManyField(FuleType)



#add car model (crate car model record)

#c100=CarModel.objects.create(name="c100")
#c200=CarModel.objects.create(name="c200")
# print(CarModel.objects.all())

# exec(open(r"D:\SHRADA PYTHON B10\b10_env\Django_projects\first_project\app\db_shell.py").read())  #run on cmd

#add fuletype(create fule type to insert data into table)

# gas=FuleType.objects.create(name="Gas")
# diesel=FuleType.objects.create(name="Diesel")
# hybrid=FuleType.objects.create(name="Hybrid")
# print(FuleType.objects.all())

#relationship (associate the carmodel with a fuletype)
##c100 = CarModel.objects.get(name="c100")  #id=1
# c200= CarModel.objects.get(name="c200") 

#g= FuelType.objects.get(name="Gas")    #id=1
# d=FuelType.objects.get(name="Diesel")
# h=FuelType.objects.get(name="Hybrid")


#define a relatinship between these two table ,it insert entry in associted table

# c100.fueltype.add(g)     #carmodelobject.FuleType.add(Fuletypeobject)
# c100.fueltype.add(d) 
# c100.fueltype.add(h) 

#anothrway by using tuple
# c200.fueltype.add(g,d,h)  


#remove all relatinship between table
# c100.fuletype.clear()
# c100.fuletype.remove(h)


# c200.fueltype.create(name="bio diesel")    #car model che fule type kadle
# print(g.models.all())

# print(c100.fueltype.all())   #get all fuletype of c100

#get all models of fule gas
# print(g.carmodel set.all())   #ani jar clss madhe feild nasel tar, obj.small latter madhe tya class ch nav


#related name
#models.py madhe ...related name mention kela tar backward direction a traverser kartana _set.all(), te related name karu shakto

# print(g.car_rel_nm.all())   #it gives all cars who are using gas
#print(h.car_rel_nm.all())     #it gives all cars who are using hybrid


#filtering records--- filtering use kartana classname.objects.filter karaycha.... obj use nahi karaycha

# p=CarModel.objects.filter(fueltype__name__startswith="G")   # ashya cars havya ahet jyncha fule typt G pasun start hoil
# print(p)

# f=FuelType.objects.filter(models__name__startswith="c100")
# print(f)

# f=FuelType.objects.filter(models__name__startswith="c200")
# print(f)

# f=FuelType.objects.filter(models__name__startswith="c100").distinct()
# print(f)

# f=FuelType.objects.filter(models__name__startswith="c200").distinct()
# print(f)

# c100.FuelType.all()
# c100.fueltype.remove(g)
# c100.fueltype.all()

# c100.fueltype.clear()


# #delete some car models.
# cars= CarModel.objects.filter(fuletype__name__startswith="p")
# cars.delete()














