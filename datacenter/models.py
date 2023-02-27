import datetime
import django

from django.db import models


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def get_duration(visit):
    entry_time = visit.entered_at
    exit_time = django.utils.timezone.localtime(visit.leaved_at)
    return exit_time - entry_time


def format_duration(duration):
    duration_total_sec = int(duration.total_seconds())
    duration_hours = duration_total_sec // 3600
    rest_sec = duration_total_sec % 3600
    duration_min = rest_sec // 60
    duration_sec = rest_sec%60
    return f'{duration_hours}:{duration_min}:{duration_sec}'


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return duration > datetime.timedelta(minutes=minutes)
  