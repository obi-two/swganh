#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/tangible/wearables/armor/kashyyykian_black_mtn/shared_armor_kashyyykian_black_mtn_bracer_l.iff"
	is_prototype = False
	
	def create(self, params):
		result = Tangible()
	
		result.template = "object/tangible/wearables/armor/kashyyykian_black_mtn/shared_armor_kashyyykian_black_mtn_bracer_l.iff"
		result.attribute_template_id = 0
		result.stfName("armor_kashyyykian_black_mtn_bracer_l","wearables_name")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())