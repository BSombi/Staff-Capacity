# Copyright (c) 2023, IPC and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import frappe
from frappe import _, scrub, throw
from frappe.model.naming import set_name_by_naming_series
from frappe.permissions import (
	add_user_permission,
	get_doc_permissions,
	has_permission,
	remove_user_permission,
)
from frappe.utils import cstr, getdate, today, validate_email_address
from frappe.utils.nestedset import NestedSet


class Employee(Document):
	
	def before_save(self):
		self.employee_name = " ".join(
			filter(lambda x: x, [self.first_name, self.middle_name, self.last_name])
		)