# Copyright (c) 2023, Ahmed Ayyash and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import uuid
from frappe.model.docstatus import DocStatus

class LibraryMember(Document):
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'
		if not self.member_id:
			self.member_id = self.member_id_generation()
	
	def member_id_generation(self):
		uuid_str = str(uuid.uuid4())
		generated_member_id =  "{}-{}-{}-{}-{}".format(uuid_str[:8], uuid_str[9:13], uuid_str[14:18], uuid_str[19:23], uuid_str[24:])
		valid_member_id = frappe.db.exists("Library Member", {"member_id": f"{generated_member_id}"})

		if valid_member_id:
			self.member_id_generation()

		return generated_member_id



		




