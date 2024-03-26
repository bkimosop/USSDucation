from django.db import models


class Student(models.Model):
    reg_no = models.CharField(max_length=16, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    current_year = models.IntegerField()
    current_semester = models.IntegerField()

    def __str__(self):
        return f'{self.reg_no} - {self.name} - {self.course} - {self.current_year} - {self.current_semester}'

    class Meta:
        db_table = 'student'

class CourseInfo(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course_name}"

    class Meta:
        db_table = "course_info"

class Unit_Info(models.Model):
    unit_code = models.CharField(max_length=10, unique=True, primary_key=True)
    unit_name = models.CharField(max_length=100)
    year = models.IntegerField()
    semester = models.IntegerField()
    course = models.ForeignKey(CourseInfo, max_length=100, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.unit_code} - {self.unit_name} - {self.year} - {self.semester} - {self.course}'

    class Meta:
        db_table = 'unit_info'


class Student_Units(models.Model):
    reg_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    unit_code = models.ForeignKey(Unit_Info, on_delete=models.CASCADE)
    result = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.reg_no} - {self.unit_code}'

    class Meta:
        db_table = 'student_units'


class Student_Finance(models.Model):
    reg_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    balance = models.FloatField()
    fee = models.FloatField()
    # date = models.DateField()

    def __str__(self):
        return f'{self.reg_no} - {self.balance} - {self.fee}'

    class Meta:
        db_table = 'student_finance'

