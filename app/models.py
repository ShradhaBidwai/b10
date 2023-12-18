from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email= models.EmailField(max_length=100,unique=True)
    mob_no = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    salary= models.IntegerField(default=25000)

    def __str__(self):
        return f"{self.first_name}"

#one to one relationship

class Person(models.Model):

    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    #Profile=models.OneToOneField(Profile,on_delete=models.CASCADE)  # profileid

    def __str__(self):
        return f"{self.first_name}"


class Meta:
    db_table= "Person"       #changing the table name by using this query as like alter(show table name Person , update name by using this query)


# if we are create this product table but we doesnt use now , but use in future perpose toh we write class Meta: abstarct=True
# class product(models.Model):
#     name=models.CharField(max_length=30)
                                            
#     class Meta:
#         abstract = True


class Address(models.Model): 
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    postal_code=models.CharField(max_length=10)
    person=models.ForeignKey(Person,on_delete=models.SET_NULL,null=True)  #person id


    def __str__(self):
        return f"{self.street}"


class Meta:
    db_table= "address"


class Profile(models.Model):
    bio= models.TextField()
    birthdate=models.DateField()
    Person=models.OneToOneField(Person,on_delete=models.CASCADE)  # person id


    def __str__(self):
        return f"{self.bio}"


class FuelType(models.Model):
    name=models.CharField(max_length=255)


    def __str__(self):
        return self.name

    class Meta:
        db_table="fuel"

class CarModel(models.Model):
    name=models.CharField(max_length=255)
    fueltype=models.ManyToManyField(FuelType, related_name="models")
  

    def __str__(self):
        return self.name

    class Meta:
        db_table="car"





# Employee.objects.all()


#creating mutiple models

#ORM-- (object relational mapper)  object oriented API.   --------JUST LIKE A WETER
#django ORM 




# person:   #one to one relationship
# id firstname,last_name

# profile:
# bio id   person id  student birthdate
        


class employee(models.model):
    first_name = models.CharField(max_length=50)
    