# -*- coding: utf-8 -*-
# Copyright (c) 2017, Dirk Chang and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class IOTLicense(Document):
	def validate(self):
		self.type_value = frappe.get_value("IOT License Type", self.type, "value")
