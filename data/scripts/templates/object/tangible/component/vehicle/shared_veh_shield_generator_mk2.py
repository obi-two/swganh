#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/component/vehicle/shared_veh_shield_generator_mk2.iff"
	is_prototype = False
	
	def create(self, params):
		result = Tangible()
	
		result.template = "object/tangible/component/vehicle/shared_veh_shield_generator_mk2.iff"
		result.attribute_template_id = -1
		result.stfName("veh_shield_generator_mk2","craft_item_ingredients_n")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())