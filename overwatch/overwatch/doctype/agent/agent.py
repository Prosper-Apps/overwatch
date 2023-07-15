# Copyright (c) 2023, Flexcom Systems and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Agent(Document):
	def autoname(self):
		if self.agent:
			self.name = self.agent
