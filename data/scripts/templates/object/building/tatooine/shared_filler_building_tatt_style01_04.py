#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/building/tatooine/shared_filler_building_tatt_style01_04.iff"
	is_prototype = False
	
	def create(self, params):
		result = Building()
	
		result.template = "object/building/tatooine/shared_filler_building_tatt_style01_04.iff"
		result.attribute_template_id = -1
		result.stfName("filler_building_tatt_style01_04","building_name")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())