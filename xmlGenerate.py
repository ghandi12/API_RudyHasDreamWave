from xsdtojson import xsd_to_json_schema
import json

json_schema = xsd_to_json_schema("items.xsd")
#print(json_schema)

json.dumps(json_schema,indent=1, separators=(',', ': '))