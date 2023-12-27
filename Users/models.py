from django.db import models

# Create your models here.



class User(models.Model):
    SEXE = (
        ('male','male'),
        ('female','female'),
    )
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    sexe = models.CharField(max_length=6,choices=SEXE,)
    dateOfBirth = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.lastName + ' ' + self.firstName
    
    
# Doctor Model --
    
class Doctor(models.Model,):
    idUser = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)
    specialty = models.CharField(max_length=45, null=False)
    scheduledTherapySessions = models.IntegerField(null=False)
    cv = models.FileField(upload_to='assets/files/', null=True)
     
    
    # def checkUser(self):
    #     from Patient.models import Patient
    #     existing_patient = Patient.objects.filter(idUser=self.idUser).exists()
    #     if existing_patient:
    #         raise ValidationError("This user is already associated with a doctor.")


    # def __str__(self):
    #     return self.idUser.lastName + ' ' + self.idUser.firstName
    
    
    
# Patient Model -- 


class Patient(models.Model):
    idUser = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)
    levelOfAddiction = models.DecimalField(max_digits=4,decimal_places=2)
    averageHoursOfGammingPerWeek = models.DecimalField(max_digits=5,decimal_places=2)
    averageHoursOfGammingPerMounth = models.DecimalField(max_digits=5,decimal_places=2)
    insomniaScore = models.DecimalField(max_digits=4,decimal_places=2)
    excessiveSleepinessScore = models.DecimalField(max_digits=4,decimal_places=2)
    anxietyScore = models.DecimalField(max_digits=4,decimal_places=2)
    depressionScore = models.DecimalField(max_digits=4,decimal_places=2)
    
    
    # def checkUser(self):
    #     from Doctor.models import Doctor
    #     existing_doctor = Doctor.objects.filter(idUser=self.idUser).exists()
    #     if existing_doctor:
    #         raise ValidationError("This user is already associated with a doctor.")
    
    
    # def __str__(self):
    #     return self.idUser.lastName + ' ' + self.idUser.firstName
    

# Admin Model -- 


class Admin(models.Model):
    ROLE= ()
    PERMISSIONS = (
        ('Doctor','Doctor'),
        ('Patient','Patient'),
        ('Admin','Admin'),
    )
    idUser = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)
    role = models.CharField(max_length=45,null=False,choices=ROLE)
    permissions = models.CharField(max_length=45,null=False,choices=PERMISSIONS)
    
    
