#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/creature/npc/droid/crafted/shared_cll_8_binary_load_lifter.iff"
	is_prototype = False
	
	def create(self, params):
		result = Creature()
	
		result.template = "object/creature/npc/droid/crafted/shared_cll_8_binary_load_lifter.iff"
		result.attribute_template_id = 3
		result.stfName("cll_8_binary_load_lifter_crafted","droid_name")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())