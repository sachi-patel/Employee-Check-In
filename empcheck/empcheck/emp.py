from __future__ import unicode_literals
import frappe
import json


def custom_validate(self,method):
    emp = frappe.get_doc('Employee',self.employee)
    print('employe====================',emp.latitude,emp.longitude)
    if self.longitude and self.latitude:
            print("1234567890",self.longitude,self.latitude)
            coords = []
            coords.append(self.longitude)
            coords.append(self.latitude)
            # coords.append(emp.latitude)
            # coords.append(emp.longitude)
            print("gsg",coords)
            line = {"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":coords}}]}
            print(line)
            line_string = json.dumps(line)
            self.map = line_string