#!/usr/bin/env python

#
# Generated Wed Aug 02 23:51:03 2017 by generateDS.py version 2.28a.
#
# Command line options:
#   ('-o', 'c:\\Users\\cbpandey\\Downloads\\item.py')
#   ('-s', 'c:\\Users\\cbpandey\\Downloads\\itemsubs.py')
#
# Command line arguments:
#   Item.xsd
#
# Command line:
#   generateDS.py -o "c:\Users\cbpandey\Downloads\item.py" -s "c:\Users\cbpandey\Downloads\itemsubs.py" Item.xsd
#
# Current working directory (os.getcwd()):
#   generateDS-2.28a0
#

import sys
from lxml import etree as etree_

import item as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#


class ItemCollectionSub(supermod.ItemCollection):
    def __init__(self, item=None):
        super(ItemCollectionSub, self).__init__(item, )
supermod.ItemCollection.subclass = ItemCollectionSub
# end class ItemCollectionSub


class ItemTypeSub(supermod.ItemType):
    def __init__(self, businessUnit=None, facility=None, number=None, name=None, classType=None, shortDescription=None, longDescription=None, dimension=None, itemWeight=None, abcCategory=None, productCode=None, originCountry=None, cycleCount=None, tradingPartner=None, purchaseCost=None, unitPrice=None, bornOnDateRequired=None, expirationDateRequired=None, receiveDateRequired=None, quarantineRequired=None, inspectionRequired=None, catchWeightRequired=None, hazmat=None, hazmatCode=None, intangibleItemFlag=None, inventoryTrackingEnabled=None, lotTrackingEnabled=None, serialTrackingEnabled=None, shippable=None, purchased=None, receiveOverTolerance=None, receiveUnderTolerance=None, cycleCountFrequency=None, reorderQuantity=None, accountingType=None, defaultLedgerAccount=None, cogsAccount=None, customFields=None, extendedEntities=None, channels=None, packs=None, upcs=None, productCategory=None, styleNumber=None, styleName=None, colorName=None, colorCode=None, size=None, nmfcNumber=None, harmonizedCode=None, mixLots=None, transportationClass=None, customMappings=None, components=None, itemVendors=None, customAttribute1=None, customAttribute2=None, customAttribute3=None, customAttribute4=None, customAttribute5=None, ule=None, uleUom=None, kitOrderOnly=None, kitStockOnly=None):
        super(ItemTypeSub, self).__init__(businessUnit, facility, number, name, classType, shortDescription, longDescription, dimension, itemWeight, abcCategory, productCode, originCountry, cycleCount, tradingPartner, purchaseCost, unitPrice, bornOnDateRequired, expirationDateRequired, receiveDateRequired, quarantineRequired, inspectionRequired, catchWeightRequired, hazmat, hazmatCode, intangibleItemFlag, inventoryTrackingEnabled, lotTrackingEnabled, serialTrackingEnabled, shippable, purchased, receiveOverTolerance, receiveUnderTolerance, cycleCountFrequency, reorderQuantity, accountingType, defaultLedgerAccount, cogsAccount, customFields, extendedEntities, channels, packs, upcs, productCategory, styleNumber, styleName, colorName, colorCode, size, nmfcNumber, harmonizedCode, mixLots, transportationClass, customMappings, components, itemVendors, customAttribute1, customAttribute2, customAttribute3, customAttribute4, customAttribute5, ule, uleUom, kitOrderOnly, kitStockOnly, )
supermod.ItemType.subclass = ItemTypeSub
# end class ItemTypeSub


class KitCollectionSub(supermod.KitCollection):
    def __init__(self, component=None):
        super(KitCollectionSub, self).__init__(component, )
supermod.KitCollection.subclass = KitCollectionSub
# end class KitCollectionSub


class KitComponentTypeSub(supermod.KitComponentType):
    def __init__(self, componentItem=None, quantity=None):
        super(KitComponentTypeSub, self).__init__(componentItem, quantity, )
supermod.KitComponentType.subclass = KitComponentTypeSub
# end class KitComponentTypeSub


class PackCollectionSub(supermod.PackCollection):
    def __init__(self, pack=None):
        super(PackCollectionSub, self).__init__(pack, )
supermod.PackCollection.subclass = PackCollectionSub
# end class PackCollectionSub


class PackTypeSub(supermod.PackType):
    def __init__(self, type_=None, quantity=None, weight=None, boxTypes=None, dimension=None, upcs=None, customMappings=None):
        super(PackTypeSub, self).__init__(type_, quantity, weight, boxTypes, dimension, upcs, customMappings, )
supermod.PackType.subclass = PackTypeSub
# end class PackTypeSub


class BoxTypeCollectionSub(supermod.BoxTypeCollection):
    def __init__(self, boxType=None):
        super(BoxTypeCollectionSub, self).__init__(boxType, )
supermod.BoxTypeCollection.subclass = BoxTypeCollectionSub
# end class BoxTypeCollectionSub


class BoxTypeTypeSub(supermod.BoxTypeType):
    def __init__(self, itemNumber=None, quantity=None):
        super(BoxTypeTypeSub, self).__init__(itemNumber, quantity, )
supermod.BoxTypeType.subclass = BoxTypeTypeSub
# end class BoxTypeTypeSub


class CustomMapTypeSub(supermod.CustomMapType):
    def __init__(self, name=None, value=None):
        super(CustomMapTypeSub, self).__init__(name, value, )
supermod.CustomMapType.subclass = CustomMapTypeSub
# end class CustomMapTypeSub


class CustomMapCollectionSub(supermod.CustomMapCollection):
    def __init__(self, customMapping=None):
        super(CustomMapCollectionSub, self).__init__(customMapping, )
supermod.CustomMapCollection.subclass = CustomMapCollectionSub
# end class CustomMapCollectionSub


class DimensionTypeSub(supermod.DimensionType):
    def __init__(self, length=None, width=None, height=None, volume=None, units='Inch'):
        super(DimensionTypeSub, self).__init__(length, width, height, volume, units, )
supermod.DimensionType.subclass = DimensionTypeSub
# end class DimensionTypeSub


class WeightTypeSub(supermod.WeightType):
    def __init__(self, weight=None, units='Pound'):
        super(WeightTypeSub, self).__init__(weight, units, )
supermod.WeightType.subclass = WeightTypeSub
# end class WeightTypeSub


class CustomFieldTypeSub(supermod.CustomFieldType):
    def __init__(self, name=None, value=None, type_='String'):
        super(CustomFieldTypeSub, self).__init__(name, value, type_, )
supermod.CustomFieldType.subclass = CustomFieldTypeSub
# end class CustomFieldTypeSub


class CustomFieldCollectionSub(supermod.CustomFieldCollection):
    def __init__(self, customField=None):
        super(CustomFieldCollectionSub, self).__init__(customField, )
supermod.CustomFieldCollection.subclass = CustomFieldCollectionSub
# end class CustomFieldCollectionSub


class ChannelsCollectionSub(supermod.ChannelsCollection):
    def __init__(self, channel=None):
        super(ChannelsCollectionSub, self).__init__(channel, )
supermod.ChannelsCollection.subclass = ChannelsCollectionSub
# end class ChannelsCollectionSub


class ChannelsResourceCollectionSub(supermod.ChannelsResourceCollection):
    def __init__(self, channel=None):
        super(ChannelsResourceCollectionSub, self).__init__(channel, )
supermod.ChannelsResourceCollection.subclass = ChannelsResourceCollectionSub
# end class ChannelsResourceCollectionSub


class ChannelResourceFieldTypeSub(supermod.ChannelResourceFieldType):
    def __init__(self, businessUnit=None, businessKey=None, otherKey=None, entityType=None, feedName=None, jobName=None, ref1=None, ref2=None, ref3=None, ref4=None, ref5=None, secRef1=None, secRef2=None, secRef3=None, secRef4=None, secRef5=None, valueOf_=None):
        super(ChannelResourceFieldTypeSub, self).__init__(businessUnit, businessKey, otherKey, entityType, feedName, jobName, ref1, ref2, ref3, ref4, ref5, secRef1, secRef2, secRef3, secRef4, secRef5, valueOf_, )
supermod.ChannelResourceFieldType.subclass = ChannelResourceFieldTypeSub
# end class ChannelResourceFieldTypeSub


class ChannelFieldTypeSub(supermod.ChannelFieldType):
    def __init__(self, feedName=None, jobName=None, ref1=None, ref2=None, ref3=None, ref4=None, ref5=None, secRef1=None, secRef2=None, secRef3=None, secRef4=None, secRef5=None, valueOf_=None):
        super(ChannelFieldTypeSub, self).__init__(feedName, jobName, ref1, ref2, ref3, ref4, ref5, secRef1, secRef2, secRef3, secRef4, secRef5, valueOf_, )
supermod.ChannelFieldType.subclass = ChannelFieldTypeSub
# end class ChannelFieldTypeSub


class ExtendedEntityCollectionSub(supermod.ExtendedEntityCollection):
    def __init__(self, entity=None):
        super(ExtendedEntityCollectionSub, self).__init__(entity, )
supermod.ExtendedEntityCollection.subclass = ExtendedEntityCollectionSub
# end class ExtendedEntityCollectionSub


class ExtendedEntityTypeSub(supermod.ExtendedEntityType):
    def __init__(self, name=None, key_field=None, key_value=None, field=None):
        super(ExtendedEntityTypeSub, self).__init__(name, key_field, key_value, field, )
supermod.ExtendedEntityType.subclass = ExtendedEntityTypeSub
# end class ExtendedEntityTypeSub


class ExtendedFieldTypeSub(supermod.ExtendedFieldType):
    def __init__(self, name=None, valueOf_=None):
        super(ExtendedFieldTypeSub, self).__init__(name, valueOf_, )
supermod.ExtendedFieldType.subclass = ExtendedFieldTypeSub
# end class ExtendedFieldTypeSub


class CustomAttributeCollectionSub(supermod.CustomAttributeCollection):
    def __init__(self, customAttribute=None):
        super(CustomAttributeCollectionSub, self).__init__(customAttribute, )
supermod.CustomAttributeCollection.subclass = CustomAttributeCollectionSub
# end class CustomAttributeCollectionSub


class CustomAttributeTypeSub(supermod.CustomAttributeType):
    def __init__(self, name=None, value=None):
        super(CustomAttributeTypeSub, self).__init__(name, value, )
supermod.CustomAttributeType.subclass = CustomAttributeTypeSub
# end class CustomAttributeTypeSub


class AddressTypeSub(supermod.AddressType):
    def __init__(self, name=None, contactName=None, attention=None, email=None, phone=None, phone2=None, addressLine1=None, addressLine2=None, addressLine3=None, addressLine4=None, city=None, stateProvinceCode=None, postalCode=None, countryCode=None):
        super(AddressTypeSub, self).__init__(name, contactName, attention, email, phone, phone2, addressLine1, addressLine2, addressLine3, addressLine4, city, stateProvinceCode, postalCode, countryCode, )
supermod.AddressType.subclass = AddressTypeSub
# end class AddressTypeSub


class FreightTypeSub(supermod.FreightType):
    def __init__(self, termsType=None, account=None, billToPartner=None, billToAddress=None):
        super(FreightTypeSub, self).__init__(termsType, account, billToPartner, billToAddress, )
supermod.FreightType.subclass = FreightTypeSub
# end class FreightTypeSub


class NoteTypeSub(supermod.NoteType):
    def __init__(self, source='Internal', title=None, body=None):
        super(NoteTypeSub, self).__init__(source, title, body, )
supermod.NoteType.subclass = NoteTypeSub
# end class NoteTypeSub


class NoteCollectionSub(supermod.NoteCollection):
    def __init__(self, note=None):
        super(NoteCollectionSub, self).__init__(note, )
supermod.NoteCollection.subclass = NoteCollectionSub
# end class NoteCollectionSub


class LinkTypeSub(supermod.LinkType):
    def __init__(self, rel=None, href=None, type_=None):
        super(LinkTypeSub, self).__init__(rel, href, type_, )
supermod.LinkType.subclass = LinkTypeSub
# end class LinkTypeSub


class UPCCollectionSub(supermod.UPCCollection):
    def __init__(self, upc=None, source=None):
        super(UPCCollectionSub, self).__init__(upc, source, )
supermod.UPCCollection.subclass = UPCCollectionSub
# end class UPCCollectionSub


class ItemVendorCollectionSub(supermod.ItemVendorCollection):
    def __init__(self, itemVendor=None):
        super(ItemVendorCollectionSub, self).__init__(itemVendor, )
supermod.ItemVendorCollection.subclass = ItemVendorCollectionSub
# end class ItemVendorCollectionSub


class ItemVendorTypeSub(supermod.ItemVendorType):
    def __init__(self, businessUnit=None, itemNumber=None, item=None, shortDescription=None, longDescription=None, tradingPartnerCode=None, reorderQuantity=None, reorderPoint=None, reorderLeadTime=None, unitCost=None, fulfillmentType=None, isPreferred=None, isInventorySyncEnabled=None, itemSkuUpc=None, additionalCost=None, quantity=None, importReference1=None, importReference2=None, reorderLot=None):
        super(ItemVendorTypeSub, self).__init__(businessUnit, itemNumber, item, shortDescription, longDescription, tradingPartnerCode, reorderQuantity, reorderPoint, reorderLeadTime, unitCost, fulfillmentType, isPreferred, isInventorySyncEnabled, itemSkuUpc, additionalCost, quantity, importReference1, importReference2, reorderLot, )
supermod.ItemVendorType.subclass = ItemVendorTypeSub
# end class ItemVendorTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ItemCollection'
        rootClass = supermod.ItemCollection
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ItemCollection'
        rootClass = supermod.ItemCollection
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ItemCollection'
        rootClass = supermod.ItemCollection
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ItemCollection'
        rootClass = supermod.ItemCollection
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
