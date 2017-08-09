import json
from collections import OrderedDict
import jsonschema_model
import pyodbc
import requests
import jsonmerge

server = 'bentexmssql.cmuxg5zfat9e.eu-west-2.rds.amazonaws.com'
database = 'bentexmssql'
username = 'dreamwave1234'
password = 'dreamwave1234'
#driver= '{ODBC Driver 11 for SQL Server}'
cnxn = pyodbc.connect("DRIVER={SQL Server};SERVER=bentexmssql.cmuxg5zfat9e.eu-west-2.rds.amazonaws.com,1433;DATABASE=tempdb;UID=dreamwave1234;PWD=dreamwave1234")

url = "https://prod-ua.deposco.com/integration/RBY/items/"

headers = {
    'authorization': "Basic YmVudGV4OmJlbnRleHRlc3Q=",
    'cache-control': "no-cache",
    'Content-Type': 'application/xml',
    'Accept-Encoding': "gzip,deflate",
    'Host': 'prod-ua.deposco.com',
    'Content-Length': '3200',
    'Accept-Encoding': 'gzip,deflate'
    }

cursor = cnxn.cursor()

cursor.execute('SELECT * FROM dbo.items')
rows = cursor.fetchall()
field_names = [i[0] for i in cursor.description]

itemSchemaHead = {'required': ['ItemCollection'], 'properties': OrderedDict([('ItemCollection', OrderedDict([('properties', OrderedDict([('item', {'type': 'string'})])), ('required', ['item'])]))])}
itemSchemabody = {'required': ['ItemType'],
              'properties': OrderedDict(
              [('ItemType', OrderedDict(
                  [('properties', OrderedDict(
                      [('businessUnit', {'type': 'string'}),
                       ('facility', {'type': 'string'}),
                       ('number', {'type': 'string'}),
                       ('name', {'type': 'string'}),
                       ('classType', {'type': 'string'}),
                       ('shortDescription', {'type': 'string'}),
                       ('longDescription', {'type': 'string'}),
                       ('dimension', {'type': 'string'}),
                       ('itemWeight', {'type': 'string'}),
                       ('abcCategory', OrderedDict()),
                       ('productCode', {'type': 'string'}),
                       ('originCountry', {'type': 'string'}),
                       ('cycleCount', {'type': 'string'}),
                       ('tradingPartner', {'type': 'string'}),
                       ('purchaseCost', {'type': 'string'}),
                       ('unitPrice', {'type': 'string'}),
                       ('bornOnDateRequired', {'type': 'string'}),
                       ('expirationDateRequired', {'type': 'string'}),
                       ('receiveDateRequired', {'type': 'string'}),
                       ('quarantineRequired', {'type': 'string'}),
                       ('inspectionRequired', {'type': 'string'}),
                       ('catchWeightRequired', {'type': 'string'}),
                       ('hazmat', {'type': 'string'}),
                       ('hazmatCode', {'type': 'string'}),
                       ('intangibleItemFlag', {'type': 'string'}),
                       ('inventoryTrackingEnabled', {'type': 'string'}),
                       ('lotTrackingEnabled', {'type': 'string'}),
                       ('serialTrackingEnabled', {'type': 'string'}),
                       ('shippable', {'type': 'string'}),
                       ('purchased', {'type': 'string'}),
                       ('receiveOverTolerance', {'type': 'string'}),
                       ('receiveUnderTolerance', {'type': 'string'}),
                       ('cycleCountFrequency', {'type': 'string'}),
                       ('reorderQuantity', {'type': 'string'}),
                       ('accountingType', {'type': 'string'}),
                       ('defaultLedgerAccount', {'type': 'string'}),
                       ('cogsAccount', {'type': 'string'}),
                       ('customFields', {'type': 'string'}),
                       ('extendedEntities', {'type': 'string'}),
                       ('channels', {'type': 'string'}),
                       ('packs', {'type': 'string'}),
                       ('upcs', {'type': 'string'}),
                       ('productCategory', {'type': 'string'}),
                       ('styleNumber', {'type': 'string'}),
                       ('styleName', {'type': 'string'}),
                       ('colorName', {'type': 'string'}),
                       ('colorCode', {'type': 'string'}),
                       ('size', {'type': 'string'}),
                       ('nmfcNumber', {'type': 'string'}),
                       ('harmonizedCode', {'type': 'string'}),
                       ('mixLots', {'type': 'string'}),
                       ('transportationClass', {'type': 'string'}),
                       ('customMappings', {'type': 'string'}),
                       ('components', {'type': 'string'}),
                       ('itemVendors', {'type': 'string'}),
                       ('customAttribute1', {'type': 'string'}),
                       ('customAttribute2', {'type': 'string'}),
                       ('customAttribute3', {'type': 'string'}),
                       ('customAttribute4', {'type': 'string'}),
                       ('customAttribute5', {'type': 'string'}),
                       ('ule', {'type': 'string'}),
                       ('uleUom', {'type': 'string'}),
                       ('kitOrderOnly', {'type': 'string'}),
                       ('kitStockOnly', {'type': 'string'})])),
                   ('required', ['number', 'name', 'classType', 'shortDescription', 'longDescription',
                                 'dimension', 'itemWeight', 'abcCategory', 'productCode', 'originCountry',
                                 'cycleCount', 'tradingPartner', 'purchaseCost', 'unitPrice', 'bornOnDateRequired',
                                 'expirationDateRequired', 'receiveDateRequired', 'quarantineRequired',
                                 'inspectionRequired', 'catchWeightRequired', 'hazmat', 'hazmatCode',
                                 'intangibleItemFlag', 'inventoryTrackingEnabled', 'lotTrackingEnabled',
                                 'serialTrackingEnabled', 'shippable', 'purchased', 'receiveOverTolerance',
                                 'receiveUnderTolerance', 'cycleCountFrequency', 'reorderQuantity', 'customFields',
                                 'packs', 'upcs', 'nmfcNumber', 'harmonizedCode', 'mixLots', 'transportationClass',
                                 'customMappings', 'components', 'itemVendors'])]))])}


ModelHead = jsonschema_model.model_factory(itemSchemaHead)
objHead = ModelHead()

ModelBody = jsonschema_model.model_factory(itemSchemabody)
obj = ModelBody()

for row in rows:
    obj.businessUnit = str(row.businessUnit)
    obj.facility = str(row.facility)
    obj.number = str(row.number)
    obj.name = str(row.name)
    obj.classType = str(row.classType)
    obj.shortDescription = str(row.shortDescription)
    obj.longDescription = str(row.longDescription)
    obj.dimension = str(row.dimension)
    obj.itemWeight = str(row.itemWeight)
    obj.abcCategory = str(row.abcCategory)
    obj.productCode = str(row.productCode)
    obj.originCountry = str(row.originCountry)
    obj.cycleCount = str(row.cycleCount)
    obj.tradingPartner = str(row.tradingPartner)
    obj.purchaseCost = str(row.purchaseCost)
    obj.unitPrice = str(row.unitPrice)
    obj.bornOndateRequired = str(row.bornOndateRequired)
    obj.expirationDateRequired = str(row.expirationDateRequired)
    obj.receiveDateRequired = str(row.receiveDateRequired)
    obj.quarantineRequired = str(row.quarantineRequired)
    obj.inspectionRequired = str(row.inspectionRequired)
    obj.catchWeightRequired = str(row.catchWeightRequired)
    obj.hazmat = str(row.hazmat)
    obj.hazmatCode = str(row.hazmatCode)
    obj.intangibleItemFlag = str(row.intangibleItemFlag)
    obj.inventoryTrackingEnabled = str(row.inventoryTrackingEnabled)
    obj.lotTrackingEnabled = str(row.lotTrackingEnabled)
    obj.serialTrackingEnabled = str(row.serialTrackingEnabled)
    obj.shippable = str(row.shippable)
    obj.purchased = str(row.purchased)
    obj.receiveOverTolerance = str(row.receiveOverTolerance)
    obj.receiveUnderTolerance = str(row.receiveUnderTolerance)
    obj.cycleCountFrequency = str(row.cycleCountFrequency)
    obj.reorderQuantity = str(row.reorderQuantity)
    obj.accountingType = str(row.accountingType)
    obj.defaultLedgerAccount = str(row.defaultLedgerAccount)
    obj.cogsAccount = str(row.cogsAccount)
    obj.customFields = str(row.customFields)
    obj.extendedEntities = str(row.extendedEntities)
    obj.channels = str(row.channels)
    obj.packs = str(row.packs)
    obj.upcs = str(row.upcs)
    obj.productCategory = str(row.productCategory)
    obj.styleNumber = str(row.styleNumber)
    obj.styleName = str(row.styleName)
    obj.colorName = str(row.colorName)
    obj.size = str(row.size)
    obj.nmfcNumber = str(row.nmfcNumber)
    obj.ule = str(row.ule)
    obj.uleUom = str(row.uleUom)
    obj.kitOrderOnly = str(row.kitOrderOnly)
    obj.kitStockOnly = str(row.kitStockOnly)
    obj.KitCollection = str(row.KitCollection)
    obj.KitComponentType = str(row.KitComponentType)


#print(obj)
objHead.Item = obj
jsoninput = json.dumps(objHead)
print(jsoninput)

# Sent API POST request
response = requests.request("POST", url, headers=headers, data=jsoninput)
print(response)