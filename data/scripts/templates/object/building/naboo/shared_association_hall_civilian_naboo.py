#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/building/naboo/shared_association_hall_civilian_naboo.iff"
	is_prototype = False
	
	def create(self, params):
		result = Building()
	
		result.template = "object/building/naboo/shared_association_hall_civilian_naboo.iff"
		result.attribute_template_id = -1
		result.stfName("association_hall_civilian_naboo","building_name")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())