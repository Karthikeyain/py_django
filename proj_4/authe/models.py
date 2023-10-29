from django.db import models

class client(models.Model):
    cname = models.CharField(max_length=50)
    cage = models.PositiveIntegerField(3)
    cphone = models.PositiveBigIntegerField()
    cadd = models.CharField(max_length=100)
    cfees = models.PositiveBigIntegerField()

class Numfield_model(models.Model):
    num1 = models.IntegerField()
    num2 = models.PositiveSmallIntegerField()
    num3 = models.PositiveBigIntegerField()
    num4 = models.SmallIntegerField()

    
    num5 = models.BigIntegerField()
    num6 = models.DecimalField(max_digits=5,decimal_places=3)
    num7 = models.FloatField()
    num8 = models.GenericIPAddressField()
    num9 = models.PositiveIntegerField()

class Charfield_model(models.Model):
    char1 = models.CharField(max_length=20)
    char2 = models.EmailField()
    char3 = models.GenericIPAddressField()
    char4 = models.SlugField()
    char5 = models.TextField(max_length=100)
    char6 = models.JSONField()
    char7 = models.URLField()
    char8 = models.UUIDField()


class datafield_model(models.Model):
    date1 = models.DateField()
    date2 = models.TimeField()
    data3 = models.DateTimeField()
    date4 = models.DurationField()

class filemodels_model(models.Model):
    file1 = models.FileField()
    file2 = models.FilePathField()


class boolmodel_model(models.Model):
    bool1 = models.BooleanField()
    bool2 = models.BinaryField()

class constraints(models.Model):
    ID = models.SmallIntegerField(primary_key=True,unique=True) # add constraints
    phone = models.PositiveBigIntegerField() # remove constraints
    age = models.PositiveSmallIntegerField(null=True) 
    email = models.EmailField(max_length=35)  # modifying length 
    gender = models.CharField(max_length=10,default='MALE')
    c_subject = models.CharField(max_length=20,choices=[['django','django'],['python','python']]) # name chaneging  

    client= models.ForeignKey(client,on_delete=models.CASCADE)