#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/ship/crafted/armor/shared_adv_durasteel_plating.iff"
	is_prototype = False
	
	def create(self, params):
		result = Tangible()
	
		result.template = "object/tangible/ship/crafted/armor/shared_adv_durasteel_plating.iff"
		result.attribute_template_id = 8
		result.stfName("adv_durasteel_plating","space_crafting_n")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())