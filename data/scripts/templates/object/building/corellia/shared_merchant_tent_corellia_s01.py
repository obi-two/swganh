#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/building/corellia/shared_merchant_tent_corellia_s01.iff"
	is_prototype = False
	
	def create(self, params):
		result = Building()
	
		result.template = "object/building/corellia/shared_merchant_tent_corellia_s01.iff"
		result.attribute_template_id = -1
		result.stfName("merchant_tent_tato_s01","building_name")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())