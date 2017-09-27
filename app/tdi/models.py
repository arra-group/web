'''
    Copyright (C) 2017 Gitcoin Core 

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from economy.models import SuperModel


class AccessCodes(SuperModel):
    invitecode = models.CharField(max_length=30)
    maxuses = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.invitecode

    @property
    def uses(self):
        return WhitepaperAccess.objects.filter(invitecode=self.invitecode).count()


class WhitepaperAccess(SuperModel):
    invitecode = models.CharField(max_length=30)
    email = models.CharField(max_length=255)
    ip = models.CharField(max_length=30)

    def __str__(self):
        return "{} / {} / {} on {}".format(self.email, self.invitecode, self.ip, self.created_on)


class WhitepaperAccessRequest(SuperModel):
    comments = models.TextField(max_length=5000)
    email = models.CharField(max_length=30)
    role = models.CharField(max_length=255)
    ip = models.CharField(max_length=30)

    def __str__(self):
        return "{} / {} / {} on {}".format(self.email, self.role, self.ip, self.created_on)

