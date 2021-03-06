from django.db import models


class Principal_investigator(models.Model):
    P_Dept = models.CharField(max_length=100)
    P_designation = models.CharField(max_length=100)
    principal_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
         return str(self.principal_id)


class Co_Investigator(models.Model):
    Co_name = models.CharField(max_length=100)
    Co_designation = models.CharField(max_length=100)
    Co_contact_no = models.CharField(max_length=20)
    Co_email = models.EmailField(max_length=100, unique=True, null=True, blank=True)