import datetime
from django.db import models
from django.db.models import base
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import BaseValidator, RegexValidator, MaxValueValidator, MinValueValidator

from college.models import *
