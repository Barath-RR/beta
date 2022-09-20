from django.db import models

class Courthouse(models.Model):
    __tablename__ = 'courthouse'
    id = models.AutoField(primary_key=True)
    court_type = models.CharField(max_length=250,blank=False)
    court_location = models.CharField(max_length=250,blank=False)
    users = models.ManyToManyField('User')
    number_of_cases_per_day = models.CharField(max_length=250,blank=False, default=5)
    # fixed_case_dates = models.relationship('FixedCaseDate', backref='Courthouse')

    def __str__(self):
        return self.id

class User(models.Model):
    __tablename__ = 'user'
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250,blank=False)
    password = models.CharField(max_length=250,blank=False)
    full_name = models.CharField(max_length=250,blank=False)
    city_of_origin = models.CharField(max_length=250,blank=False)
    court_house = models.ForeignKey(Courthouse,blank=False,on_delete=models.CASCADE)
    role = models.CharField(max_length=250,blank=False)
    # cases = models.relationship('Case', backref='user')
    # fixed_case_dates = models.relationship('FixedCaseDate', backref='user')

    def __repr__(self):
        return str(self.id)

class RequestHandler(models.Model):
    __tablename__ = 'request'
    id =models.AutoField(primary_key=True)
    from_user =models.ForeignKey(User, blank=False,on_delete=models.CASCADE, related_name='from_user')
    to_user =models.ForeignKey(User, blank=False,on_delete=models.CASCADE, related_name='to_user')
    request_type =models.CharField(max_length=250,blank=False)
    request_data =models.CharField(max_length=250,blank=False)
    status =models.CharField(max_length=250,blank=False)
    # created_on =models.CharField(
    #     max_length=250, default=getDateTimeInMillis(), blank=False)

    def __repr__(self):
        return str(self.id)

class Case(models.Model):
    __tablename__ = 'case'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=False)
    assigned_advocate = models.CharField(max_length=250, blank=False)
    affidavit = models.CharField(max_length=250, blank=False)
    charge_sheet = models.CharField(max_length=250, blank=False)
    casefiles = models.CharField(max_length=250, blank=False)
    # case_created_time = models.CharField(
    #     max_length=250, default=getDateTimeInMillis(), blank=False)
    # last_modified = models.CharField(
    #     max_length=250, default=getDateTimeInMillis(), blank=False)
    case_status = models.CharField(max_length=250, blank=False, default="Not yet assigned")
    severity_index = models.CharField(max_length=250, blank=False, default="0.1")
    assigned_by =models.ForeignKey(User, blank=False,on_delete=models.CASCADE)
    # fixed_case_date = db.relationship("FixedCaseDate", backref="Case")

    def __repr__(self):
        return self.id

class FixedCaseDate(models.Model):
    __tablename__ = 'fixed_case_date'
    id = models.AutoField(primary_key=True)
    case = models.ForeignKey(Case,blank=False,on_delete=models.CASCADE)
    date = models.CharField(max_length=250, blank=False)
    created_by = models.ForeignKey(User, blank=False,on_delete=models.CASCADE)
    created_on = models.CharField(max_length=250, blank=False)
    courthouse = models.ForeignKey(Courthouse, blank=False,on_delete=models.CASCADE)
    type = models.CharField(max_length=250, blank=False)

    def __repr__(self):
        return self.id

class JudgeCasePreference(models.Model):
    __tablename__ = 'judge_case_preference'
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,blank=False,on_delete=models.CASCADE)
    section = models.CharField(max_length=250, blank=False)
    preference_order = models.CharField(max_length=250, blank=False)

    def __repr__(self):
        return self.user + self.preferenceOrder