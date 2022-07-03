from .models import User, TeacherProfile
from student.models import student
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff == True:
            TeacherProfile.objects.create(user=instance)
            print("saved")

        if not instance.is_staff:
            
            # s = student(user=instance)
            student.objects.create(user=instance)
            # s.save()
            print(student.objects.filter(user=instance))
            print("saved")


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created ,**kwargs):
    if instance.is_staff == True :
        #   hardcoded 
        ''' try:
            teacher_profile = TeacherProfile.objects.get(user=instance)
        except TeacherProfile.DoesNotExist:
            TeacherProfile.objects.create(user=instance)
        else:
            teacher_profile.save()'''
        # account = instance
        # print(account)
        # if User.objects.filter(user=instance).exists():
        #     print("entered")
        teacher, created = TeacherProfile.objects.update_or_create(user=instance)
        teacher.save()
    elif not instance.is_staff:
        #   hardcoded 
        ''' try:
            print("hello12")
            student_profile = student.objects.get(user=instance)
        except student.DoesNotExist:
            student.objects.create(user=instance)
            print(instance)
        else:
            student_profile.save()'''
        stu, created = student.objects.update_or_create(user=instance)
        stu.save()
        print(stu)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print(instance)
    if not instance.is_staff == True:
        try:
            
            TeacherProfile.objects.get(user=instance).delete()
        except:
            pass
    if instance.is_staff:
        try:
            
            student.objects.get(user=instance).delete()
        except:
            pass