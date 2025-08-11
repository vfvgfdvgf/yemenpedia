from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "إنشاء مجموعات الصلاحيات: Owner, Moderator, Writer"

    def handle(self, *args, **options):
        groups = ["Owner", "Moderator", "Writer"]
        for g in groups:
            group, created = Group.objects.get_or_create(name=g)
            if created:
                self.stdout.write(self.style.SUCCESS(f"تم إنشاء المجموعة {g}"))
            else:
                self.stdout.write(self.style.WARNING(f"المجموعة {g} موجودة بالفعل"))

        owner = Group.objects.get(name="Owner")
        owner.permissions.set(Permission.objects.all())
        owner.save()
        self.stdout.write(self.style.SUCCESS("تم إعطاء جميع الصلاحيات لمجموعة Owner"))
