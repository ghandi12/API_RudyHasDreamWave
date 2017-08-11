import json
from collections import OrderedDict
import collections
import pyodbc
import requests
from marshmallow import Schema, fields, pprint
import http.client

server = 'bentexmssql.cmuxg5zfat9e.eu-west-2.rds.amazonaws.com'
database = 'bentexmssql'
username = 'dreamwave1234'
password = 'dreamwave1234'
#driver= '{ODBC Driver 11 for SQL Server}'
cnxn = pyodbc.connect("DRIVER={SQL Server};SERVER=bentexmssql.cmuxg5zfat9e.eu-west-2.rds.amazonaws.com,1433;DATABASE=tempdb;UID=dreamwave1234;PWD=dreamwave1234")

conn = http.client.HTTPSConnection("prod-ua.deposco.com")

headers = {
    'authorization': "Basic YmVudGV4OmJlbnRleHRlc3Q=",
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

cursor = cnxn.cursor()

cursor.execute('SELECT * FROM dbo.items')
rows = cursor.fetchall()
field_names = [i[0] for i in cursor.description]

class ItemDimensionSchema(Schema):
    length = fields.Str()
    width = fields.Str()
    height = fields.Str()
    units = fields.Str()

class itemWeightSchema(Schema):
    weight = fields.Str()
    units = fields.Str()

class PackDimensionSchema(Schema):
    length = fields.Str()
    width = fields.Str()
    height = fields.Str()
    units = fields.Str()

class PackSchema(Schema):
    type = fields.Str()
    quantity = fields.Str()
    weight = fields.Str()
    dimension = fields.Nested(PackDimensionSchema)
    customMappings = fields.Str()

class ItemSchema(Schema):
    class Meta:
        fields = ("businessUnit","facility","number","name","classType","shortDescription","longDescription","dimension",
                    "itemWeight","abcCategory","productCode","originCountry","cycleCount","tradingPartner","purchaseCost",
                    "unitPrice","bornOndateRequired","expirationDateRequired","receiveDateRequired","quarantineRequired",
                    "inspectionRequired","catchWeightRequired","hazmat","hazmatCode","intangibleItemFlag","inventoryTrackingEnabled",
                    "lotTrackingEnabled","serialTrackingEnabled","shippable","purchased","receiveOverTolerance","receiveUnderTolerance",
                    "cycleCountFrequency","reorderQuantity","accountingType","defaultLedgerAccount","cogsAccount","customFields",
                    "extendedEntities","channels","packs","upcs","productCategory","styleNumber","styleName","colorName","size",
                    "nmfcNumber","ule","uleUom","kitOrderOnly","kitStockOnly","KitCollection","KitComponentType")
        ordered = True
    businessUnit = fields.Str()
    facility = fields.Str()
    number = fields.Str()
    name = fields.Str()
    classType = fields.Str()
    shortDescription = fields.Str()
    longDescription = fields.Str()
    dimension = fields.Nested(ItemDimensionSchema())
    itemWeight = fields.Nested(itemWeightSchema())
    abcCategory = fields.Str()
    productCode = fields.Str()
    originCountry = fields.Str()
    cycleCount = fields.Str()
    tradingPartner = fields.Str()
    purchaseCost = fields.Str()
    unitPrice = fields.Str()
    bornOndateRequired = fields.Str()
    expirationDateRequired = fields.Str()
    receiveDateRequired = fields.Str()
    quarantineRequired = fields.Str()
    inspectionRequired = fields.Str()
    catchWeightRequired = fields.Str()
    hazmat = fields.Str()
    hazmatCode = fields.Str()
    intangibleItemFlag = fields.Str()
    inventoryTrackingEnabled = fields.Str()
    lotTrackingEnabled = fields.Str()
    serialTrackingEnabled = fields.Str()
    shippable = fields.Str()
    purchased = fields.Str()
    receiveOverTolerance = fields.Str()
    receiveUnderTolerance = fields.Str()
    cycleCountFrequency = fields.Str()
    reorderQuantity = fields.Str()
    accountingType = fields.Str()
    defaultLedgerAccount = fields.Str()
    cogsAccount = fields.Str()
    customFields = fields.Str()
    extendedEntities = fields.Str()
    channels = fields.Str()
    packs = fields.Nested(PackSchema())
    upcs = fields.Str()
    productCategory = fields.Str()
    styleNumber = fields.Str()
    styleName = fields.Str()
    colorName = fields.Str()
    size = fields.Str()
    nmfcNumber = fields.Str()
    ule = fields.Str()
    uleUom = fields.Str()
    kitOrderOnly = fields.Str()
    kitStockOnly = fields.Str()
    KitCollection = fields.Str()
    KitComponentType = fields.Str()

class FinalItemSchema(Schema):
    item = fields.Nested(ItemSchema())
    class Meta:
        ordered = True

for row in rows:
    itemDimension = OrderedDict(
        length = "10",
        width = "10",
        height = "10",
        units = "10"
    )
    itemWeight = OrderedDict(
        weight = "10",
        units = "10"
    )
    packDimension = OrderedDict(
        length = "30",
        width = "20",
        height = "20",
        units = "40"
    )
    packsItem = OrderedDict(
        type = "test",
        quantity = "10",
        weight = "10",
        dimension = packDimension,
        customMappings = "test"
    )
    packsDict = OrderedDict(
        pack = packsItem
    )
    itemdict = OrderedDict(
        businessUnit = str(row.businessUnit),
        facility = str(row.facility),
        number = str(row.number),
        name = str(row.name),
        classType = str(row.classType),
        shortDescription = str(row.shortDescription),
        longDescription = str(row.longDescription),
        dimension = itemDimension,
        itemWeight = itemWeight,
        productCode = str(row.productCode),
        originCountry = str(row.originCountry),
        cycleCount = str(row.cycleCount),
        tradingPartner = str(row.tradingPartner),
        purchaseCost = str(row.purchaseCost),
        unitPrice = str(row.unitPrice),
        bornOndateRequired = str(row.bornOndateRequired),
        expirationDateRequired = str(row.expirationDateRequired),
        receiveDateRequired = str(row.receiveDateRequired),
        quarantineRequired = str(row.quarantineRequired),
        inspectionRequired = str(row.inspectionRequired),
        catchWeightRequired = str(row.catchWeightRequired),
        hazmat = str(row.hazmat),
        hazmatCode = str(row.hazmatCode),
        intangibleItemFlag = str(row.intangibleItemFlag),
        inventoryTrackingEnabled = str(row.inventoryTrackingEnabled),
        lotTrackingEnabled = str(row.lotTrackingEnabled),
        serialTrackingEnabled = str(row.serialTrackingEnabled),
        shippable = str(row.shippable),
        purchased = str(row.purchased),
        receiveOverTolerance = str(row.receiveOverTolerance),
        receiveUnderTolerance = str(row.receiveUnderTolerance),
        cycleCountFrequency = str(row.cycleCountFrequency),
        reorderQuantity = str(row.reorderQuantity),
        accountingType = str(row.accountingType),
        defaultLedgerAccount = str(row.defaultLedgerAccount),
        cogsAccount = str(row.cogsAccount),
        customFields = str(row.customFields),
        extendedEntities = str(row.extendedEntities),
        channels = str(row.channels),
        packs = packsItem,
        upcs = str(row.upcs),
        productCategory = str(row.productCategory),
        styleNumber = str(row.styleNumber),
        styleName = str(row.styleName),
        colorName = str(row.colorName),
        size = str(row.size),
        nmfcNumber = str(row.nmfcNumber),
        ule = str(row.ule),
        uleUom = str(row.uleUom),
        kitOrderOnly = str(row.kitOrderOnly),
        kitStockOnly = str(row.kitStockOnly),
        KitCollection = str(row.KitCollection),
        KitComponentType = str(row.KitComponentType),
    )

    finalItem = OrderedDict(item = itemdict)
    schema = FinalItemSchema()
    result = schema.dump(finalItem)
    #print(json.dumps(result.data))
    payload = json.dumps(result.data)
    print(payload)

    # Sent API POST request
    response = conn.request("POST", "/integration/RBY/items/",  payload, headers)
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))