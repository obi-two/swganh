#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/building/corellia/shared_skyscraper_corellia_style_02.iff"
	is_prototype = False
	
	def create(self, params):
		result = Building()
	
		result.template = "object/building/corellia/shared_skyscraper_corellia_style_02.iff"
		result.attribute_template_id = -1
		result.stfName("skyscraper_corellia_style_2","building_name")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())