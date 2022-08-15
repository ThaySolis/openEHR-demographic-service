# -*- coding: UTF-8 -*-
from .rm_validation import validate_DV_TEXT
from .rm_validation import validate_String
from .rm_validation import validate_PARTY_IDENTITY
from .rm_validation import validate_DV_BOOLEAN
from .rm_validation import validate_DV_INTERVAL_of_DV_DATE
from .rm_validation import validate_PARTY_RELATIONSHIP
from .rm_validation import validate_CONTACT
from .rm_validation import validate_DV_URI
from .rm_validation import validate_DV_COUNT
from .rm_validation import validate_ADDRESS
from .rm_validation import validate_DV_PROPORTION
from .rm_validation import validate_CODE_PHRASE
from .rm_validation import validate_DV_INTERVAL
from .rm_validation import validate_DV_IDENTIFIER
from .rm_validation import validate_ELEMENT
from .rm_validation import validate_DV_DATE
from .rm_validation import validate_DV_CODED_TEXT
from .rm_validation import validate_PERSON
from .rm_validation import validate_ITEM_TREE
from .rm_validation import validate_CLUSTER

def validate_archetype_DEMOGRAPHIC_ADDRESS_address_v0(obj):
    '''
    Checks if a given JSON object (Python dict) matches the archetype 'openEHR-DEMOGRAPHIC-ADDRESS.address.v0'
    
    Parameters:
        obj - The JSON object to check
        
    Returns:
        True if the object matches the arquetype, False otherwise.
    '''
    
    def validate_gen0001(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0003(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "value" not in obj["terminology_id"]:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] not in ['at0461', 'at0462', 'at0463', 'at0464', 'at0465', 'at0466']:
            return False
        return True
    
    def validate_gen0002(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0003(obj["defining_code"]):
                return False
        return True
    
    def validate_gen0004(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0006(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0000":
            return False
        return True
    
    def validate_gen0005(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0006(obj["defining_code"]):
                return False
        return True
    
    def validate_at0021(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0021":
            return False
        if "value" in obj:
            if not validate_gen0004(obj["value"]) and not validate_gen0005(obj["value"]):
                return False
        return True
    
    def validate_gen0007(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0022(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0022":
            return False
        if "value" in obj:
            if not validate_gen0007(obj["value"]):
                return False
        return True
    
    def validate_gen0008(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0023(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0023":
            return False
        if "value" in obj:
            if not validate_gen0008(obj["value"]):
                return False
        return True
    
    def validate_gen0009(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0024(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0024":
            return False
        if "value" in obj:
            if not validate_gen0009(obj["value"]):
                return False
        return True
    
    def validate_gen0010(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0025(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0025":
            return False
        if "value" in obj:
            if not validate_gen0010(obj["value"]):
                return False
        return True
    
    def validate_gen0011(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0026(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0026":
            return False
        if "value" in obj:
            if not validate_gen0011(obj["value"]):
                return False
        return True
    
    def validate_gen0012(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0014(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0001":
            return False
        return True
    
    def validate_gen0013(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0014(obj["defining_code"]):
                return False
        return True
    
    def validate_at0027(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0027":
            return False
        if "value" in obj:
            if not validate_gen0012(obj["value"]) and not validate_gen0013(obj["value"]):
                return False
        return True
    
    def validate_gen0015(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0028(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0028":
            return False
        if "value" in obj:
            if not validate_gen0015(obj["value"]):
                return False
        return True
    
    def validate_gen0016(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0029(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0029":
            return False
        if "value" in obj:
            if not validate_gen0016(obj["value"]):
                return False
        return True
    
    def validate_gen0017(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0019(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0002":
            return False
        return True
    
    def validate_gen0018(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0019(obj["defining_code"]):
                return False
        return True
    
    def validate_at0030(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0030":
            return False
        if "value" in obj:
            if not validate_gen0017(obj["value"]) and not validate_gen0018(obj["value"]):
                return False
        return True
    
    def validate_gen0020(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0031(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0031":
            return False
        if "value" in obj:
            if not validate_gen0020(obj["value"]):
                return False
        return True
    
    def validate_at0002(obj):
        if not validate_CLUSTER(obj):
            return False
        if obj["archetype_node_id"] != "at0002":
            return False
        if "items" not in obj:
            return False
        if type(obj["items"]) != list:
            return False
        counter = {'at0021': 0, 'at0022': 0, 'at0023': 0, 'at0024': 0, 'at0025': 0, 'at0026': 0, 'at0027': 0, 'at0028': 0, 'at0029': 0, 'at0030': 0, 'at0031': 0}
        for item in obj["items"]:
            if validate_at0021(item):
                counter["at0021"] += 1
            elif validate_at0022(item):
                counter["at0022"] += 1
            elif validate_at0023(item):
                counter["at0023"] += 1
            elif validate_at0024(item):
                counter["at0024"] += 1
            elif validate_at0025(item):
                counter["at0025"] += 1
            elif validate_at0026(item):
                counter["at0026"] += 1
            elif validate_at0027(item):
                counter["at0027"] += 1
            elif validate_at0028(item):
                counter["at0028"] += 1
            elif validate_at0029(item):
                counter["at0029"] += 1
            elif validate_at0030(item):
                counter["at0030"] += 1
            elif validate_at0031(item):
                counter["at0031"] += 1
            else:
                return False
        if not(0 <= counter["at0021"] and 0 <= counter["at0022"] and 0 <= counter["at0023"] and 0 <= counter["at0024"] and 0 <= counter["at0025"] and 0 <= counter["at0026"] and 0 <= counter["at0027"] and 0 <= counter["at0028"] and 0 <= counter["at0029"] and 0 <= counter["at0030"] and 0 <= counter["at0031"]):
            return False
        return True
    
    def validate_gen0021(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0003(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0003":
            return False
        if "value" in obj:
            if not validate_gen0021(obj["value"]):
                return False
        return True
    
    def validate_gen0022(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0004(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0004":
            return False
        if "value" in obj:
            if not validate_gen0022(obj["value"]):
                return False
        return True
    
    def validate_gen0023(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0005(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0005":
            return False
        if "value" in obj:
            if not validate_gen0023(obj["value"]):
                return False
        return True
    
    def validate_gen0024(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0006(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0006":
            return False
        if "value" in obj:
            if not validate_gen0024(obj["value"]):
                return False
        return True
    
    def validate_gen0025(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0007(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0007":
            return False
        if "value" in obj:
            if not validate_gen0025(obj["value"]):
                return False
        return True
    def validate_gen0027(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0003":
            return False
        return True
    
    def validate_gen0026(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0027(obj["defining_code"]):
                return False
        return True
    
    def validate_at0008(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0008":
            return False
        if "value" in obj:
            if not validate_gen0026(obj["value"]):
                return False
        return True
    def validate_gen0029(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0004":
            return False
        return True
    
    def validate_gen0028(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0029(obj["defining_code"]):
                return False
        return True
    
    def validate_at0009(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0009":
            return False
        if "value" in obj:
            if not validate_gen0028(obj["value"]):
                return False
        return True
    def validate_gen0031(obj):
        if not validate_String(obj):
            return False
        import re
        if not re.match('''^[AEU][AEU][AEU]$''',obj):
            return False
        return True
    
    def validate_gen0030(obj):
        if not validate_DV_TEXT(obj):
            return False
        if "value" in obj:
            if not validate_gen0031(obj["value"]):
                return False
        return True
    
    def validate_at0010(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0010":
            return False
        if "value" in obj:
            if not validate_gen0030(obj["value"]):
                return False
        return True
    def validate_gen0033(obj):
        if not validate_String(obj):
            return False
        import re
        if not re.match('''^[AEU][AEU][AEU]$''',obj):
            return False
        return True
    
    def validate_gen0032(obj):
        if not validate_DV_TEXT(obj):
            return False
        if "value" in obj:
            if not validate_gen0033(obj["value"]):
                return False
        return True
    
    def validate_at0011(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0011":
            return False
        if "value" in obj:
            if not validate_gen0032(obj["value"]):
                return False
        return True
    
    def validate_at0001(obj):
        if not validate_ITEM_TREE(obj):
            return False
        if obj["archetype_node_id"] != "at0001":
            return False
        if "items" in obj:
            if type(obj["items"]) != list:
                return False
            if len(obj["items"]) > 1:
                return False
            if len(obj["items"]) == 1:
                if not validate_at0002(obj["items"][0]) and not validate_at0003(obj["items"][0]) and not validate_at0004(obj["items"][0]) and not validate_at0005(obj["items"][0]) and not validate_at0006(obj["items"][0]) and not validate_at0007(obj["items"][0]) and not validate_at0008(obj["items"][0]) and not validate_at0009(obj["items"][0]) and not validate_at0010(obj["items"][0]) and not validate_at0011(obj["items"][0]):
                    return False
        return True
    
    def validate_at0000(obj):
        if not validate_ADDRESS(obj):
            return False
        if obj["archetype_node_id"] != "at0000":
            return False
        if "name" in obj:
            if not validate_gen0001(obj["name"]) and not validate_gen0002(obj["name"]):
                return False
        if "details" in obj:
            if not validate_at0001(obj["details"]):
                return False
        return True
    return validate_at0000(obj)

def validate_archetype_DEMOGRAPHIC_ADDRESS_electronic_communication_provider_v0(obj):
    '''
    Checks if a given JSON object (Python dict) matches the archetype 'openEHR-DEMOGRAPHIC-ADDRESS.electronic_communication-provider.v0'
    
    Parameters:
        obj - The JSON object to check
        
    Returns:
        True if the object matches the arquetype, False otherwise.
    '''
    
    def validate_gen0034(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0036(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "value" not in obj["terminology_id"]:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] not in ['at0020', 'at0021', 'at0022', 'at0023', 'at0024', 'at0025']:
            return False
        return True
    
    def validate_gen0035(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0036(obj["defining_code"]):
                return False
        return True
    
    def validate_gen0037(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0039(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "value" not in obj["terminology_id"]:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] not in ['at0030', 'at0031', 'at0032', 'at0033']:
            return False
        return True
    
    def validate_gen0038(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0039(obj["defining_code"]):
                return False
        return True
    
    def validate_at0003(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0003":
            return False
        if "value" in obj:
            if not validate_gen0037(obj["value"]) and not validate_gen0038(obj["value"]):
                return False
        return True
    
    def validate_gen0040(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0042(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "value" not in obj["terminology_id"]:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] not in ['at0040', 'at0041', 'at0042', 'at0043', 'at0044']:
            return False
        return True
    
    def validate_gen0041(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0042(obj["defining_code"]):
                return False
        return True
    
    def validate_at0004(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0004":
            return False
        if "value" in obj:
            if not validate_gen0040(obj["value"]) and not validate_gen0041(obj["value"]):
                return False
        return True
    
    def validate_at0012(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0009(obj):
        if not validate_DV_URI(obj):
            return False
        return True
    
    def validate_at0007(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0007":
            return False
        if "value" in obj:
            if not validate_at0012(obj["value"]) and not validate_at0009(obj["value"]):
                return False
        return True
    
    def validate_gen0043(obj):
        if not validate_DV_BOOLEAN(obj):
            return False
        return True
    
    def validate_at0_2(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0_2":
            return False
        if "value" in obj:
            if not validate_gen0043(obj["value"]):
                return False
        return True
    
    def validate_gen0044(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0_3(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0_3":
            return False
        if "value" in obj:
            if not validate_gen0044(obj["value"]):
                return False
        return True
    
    def validate_at0001(obj):
        if not validate_ITEM_TREE(obj):
            return False
        if obj["archetype_node_id"] != "at0001":
            return False
        if "items" in obj:
            if type(obj["items"]) != list:
                return False
            if len(obj["items"]) > 1:
                return False
            if len(obj["items"]) == 1:
                if not validate_at0003(obj["items"][0]) and not validate_at0004(obj["items"][0]) and not validate_at0007(obj["items"][0]) and not validate_at0_2(obj["items"][0]) and not validate_at0_3(obj["items"][0]):
                    return False
        return True
    
    def validate_at0000_1(obj):
        if not validate_ADDRESS(obj):
            return False
        if obj["archetype_node_id"] != "at0000_1":
            return False
        if "name" in obj:
            if not validate_gen0034(obj["name"]) and not validate_gen0035(obj["name"]):
                return False
        if "details" in obj:
            if not validate_at0001(obj["details"]):
                return False
        return True
    return validate_at0000_1(obj)

def validate_archetype_DEMOGRAPHIC_ADDRESS_electronic_communication_v0(obj):
    '''
    Checks if a given JSON object (Python dict) matches the archetype 'openEHR-DEMOGRAPHIC-ADDRESS.electronic_communication.v0'
    
    Parameters:
        obj - The JSON object to check
        
    Returns:
        True if the object matches the arquetype, False otherwise.
    '''
    
    def validate_gen0045(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0047(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "value" not in obj["terminology_id"]:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] not in ['at0020', 'at0021', 'at0022', 'at0023', 'at0024', 'at0025']:
            return False
        return True
    
    def validate_gen0046(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0047(obj["defining_code"]):
                return False
        return True
    
    def validate_gen0048(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0050(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "value" not in obj["terminology_id"]:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] not in ['at0030', 'at0031', 'at0032', 'at0033']:
            return False
        return True
    
    def validate_gen0049(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0050(obj["defining_code"]):
                return False
        return True
    
    def validate_at0003(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0003":
            return False
        if "value" in obj:
            if not validate_gen0048(obj["value"]) and not validate_gen0049(obj["value"]):
                return False
        return True
    
    def validate_gen0051(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0053(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "value" not in obj["terminology_id"]:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] not in ['at0040', 'at0041', 'at0042', 'at0043', 'at0044']:
            return False
        return True
    
    def validate_gen0052(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0053(obj["defining_code"]):
                return False
        return True
    
    def validate_at0004(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0004":
            return False
        if "value" in obj:
            if not validate_gen0051(obj["value"]) and not validate_gen0052(obj["value"]):
                return False
        return True
    
    def validate_at0012(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0009(obj):
        if not validate_DV_URI(obj):
            return False
        return True
    
    def validate_at0007(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0007":
            return False
        if "value" in obj:
            if not validate_at0012(obj["value"]) and not validate_at0009(obj["value"]):
                return False
        return True
    
    def validate_at0001(obj):
        if not validate_ITEM_TREE(obj):
            return False
        if obj["archetype_node_id"] != "at0001":
            return False
        if "items" in obj:
            if type(obj["items"]) != list:
                return False
            if len(obj["items"]) > 1:
                return False
            if len(obj["items"]) == 1:
                if not validate_at0003(obj["items"][0]) and not validate_at0004(obj["items"][0]) and not validate_at0007(obj["items"][0]):
                    return False
        return True
    
    def validate_at0000(obj):
        if not validate_ADDRESS(obj):
            return False
        if obj["archetype_node_id"] != "at0000":
            return False
        if "name" in obj:
            if not validate_gen0045(obj["name"]) and not validate_gen0046(obj["name"]):
                return False
        if "details" in obj:
            if not validate_at0001(obj["details"]):
                return False
        return True
    return validate_at0000(obj)

def validate_archetype_DEMOGRAPHIC_CLUSTER_birth_data_additional_detail_br_v0(obj):
    '''
    Checks if a given JSON object (Python dict) matches the archetype 'openEHR-DEMOGRAPHIC-CLUSTER.birth_data_additional_detail_br.v0'
    
    Parameters:
        obj - The JSON object to check
        
    Returns:
        True if the object matches the arquetype, False otherwise.
    '''
    
    def validate_gen0054(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0001(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0001":
            return False
        if "value" in obj:
            if not validate_gen0054(obj["value"]):
                return False
        return True
    
    def validate_gen0055(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0002(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0002":
            return False
        if "value" in obj:
            if not validate_gen0055(obj["value"]):
                return False
        return True
    
    def validate_gen0056(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0003(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0003":
            return False
        if "value" in obj:
            if not validate_gen0056(obj["value"]):
                return False
        return True
    
    def validate_at0000(obj):
        if not validate_CLUSTER(obj):
            return False
        if obj["archetype_node_id"] != "at0000":
            return False
        if "items" not in obj:
            return False
        if type(obj["items"]) != list:
            return False
        counter = {'at0001': 0, 'at0002': 0, 'at0003': 0}
        for item in obj["items"]:
            if validate_at0001(item):
                counter["at0001"] += 1
            elif validate_at0002(item):
                counter["at0002"] += 1
            elif validate_at0003(item):
                counter["at0003"] += 1
            else:
                return False
        if not(1 <= counter["at0001"] and 1 <= counter["at0002"] and 1 <= counter["at0003"]):
            return False
        return True
    return validate_at0000(obj)

def validate_archetype_DEMOGRAPHIC_CLUSTER_person_identifier_provider_v0(obj):
    '''
    Checks if a given JSON object (Python dict) matches the archetype 'openEHR-DEMOGRAPHIC-CLUSTER.person_identifier-provider.v0'
    
    Parameters:
        obj - The JSON object to check
        
    Returns:
        True if the object matches the arquetype, False otherwise.
    '''
    
    def validate_gen0057(obj):
        if not validate_DV_IDENTIFIER(obj):
            return False
        return True
    
    def validate_at0001(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0001":
            return False
        if "value" in obj:
            if not validate_gen0057(obj["value"]):
                return False
        return True
    
    def validate_gen0058(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0060(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "value" not in obj["terminology_id"]:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] not in ['at0010', 'at0011', 'at0012', 'at0013']:
            return False
        return True
    
    def validate_gen0059(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0060(obj["defining_code"]):
                return False
        return True
    
    def validate_at0002(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0002":
            return False
        if "value" in obj:
            if not validate_gen0058(obj["value"]) and not validate_gen0059(obj["value"]):
                return False
        return True
    
    def validate_gen0061(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0063(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0001":
            return False
        return True
    
    def validate_gen0062(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0063(obj["defining_code"]):
                return False
        return True
    
    def validate_at0003(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0003":
            return False
        if "value" in obj:
            if not validate_gen0061(obj["value"]) and not validate_gen0062(obj["value"]):
                return False
        return True
    def validate_gen0065(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0002":
            return False
        return True
    
    def validate_gen0064(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0065(obj["defining_code"]):
                return False
        return True
    
    def validate_at0004(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0004":
            return False
        if "value" in obj:
            if not validate_gen0064(obj["value"]):
                return False
        return True
    def validate_gen0067(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0003":
            return False
        return True
    
    def validate_gen0066(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0067(obj["defining_code"]):
                return False
        return True
    
    def validate_at0005(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0005":
            return False
        if "value" in obj:
            if not validate_gen0066(obj["value"]):
                return False
        return True
    
    def validate_gen0069(obj):
        if not validate_DV_DATE(obj):
            return False
        return True
    
    def validate_gen0070(obj):
        if not validate_DV_DATE(obj):
            return False
        return True
    
    def validate_gen0068(obj):
        if not validate_DV_INTERVAL_of_DV_DATE(obj):
            return False
        if "upper" in obj:
            if not validate_gen0069(obj["upper"]):
                return False
        if "lower" in obj:
            if not validate_gen0070(obj["lower"]):
                return False
        return True
    
    def validate_at0006(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0006":
            return False
        if "value" in obj:
            if not validate_gen0068(obj["value"]):
                return False
        return True
    
    def validate_gen0071(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0073(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0000.1":
            return False
        return True
    
    def validate_gen0072(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0073(obj["defining_code"]):
                return False
        return True
    
    def validate_at0_2(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0_2":
            return False
        if "value" in obj:
            if not validate_gen0071(obj["value"]) and not validate_gen0072(obj["value"]):
                return False
        return True
    
    def validate_gen0074(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0_30(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0_30":
            return False
        if "value" in obj:
            if not validate_gen0074(obj["value"]):
                return False
        return True
    
    def validate_gen0075(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0_31(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0_31":
            return False
        if "value" in obj:
            if not validate_gen0075(obj["value"]):
                return False
        return True
    
    def validate_gen0076(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0_32(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0_32":
            return False
        if "value" in obj:
            if not validate_gen0076(obj["value"]):
                return False
        return True
    
    def validate_gen0077(obj):
        if not validate_DV_DATE(obj):
            return False
        return True
    
    def validate_at0_33(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0_33":
            return False
        if "value" in obj:
            if not validate_gen0077(obj["value"]):
                return False
        return True
    
    def validate_gen0078(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0_34(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0_34":
            return False
        if "value" in obj:
            if not validate_gen0078(obj["value"]):
                return False
        return True
    
    def validate_at0_3(obj):
        if not validate_CLUSTER(obj):
            return False
        if obj["archetype_node_id"] != "at0_3":
            return False
        if "items" not in obj:
            return False
        if type(obj["items"]) != list:
            return False
        counter = {'at0_30': 0, 'at0_31': 0, 'at0_32': 0, 'at0_33': 0, 'at0_34': 0}
        for item in obj["items"]:
            if validate_at0_30(item):
                counter["at0_30"] += 1
            elif validate_at0_31(item):
                counter["at0_31"] += 1
            elif validate_at0_32(item):
                counter["at0_32"] += 1
            elif validate_at0_33(item):
                counter["at0_33"] += 1
            elif validate_at0_34(item):
                counter["at0_34"] += 1
            else:
                return False
        if not(0 <= counter["at0_30"] and 0 <= counter["at0_31"] and 1 <= counter["at0_32"] and 1 <= counter["at0_33"] and 1 <= counter["at0_34"]):
            return False
        return True
    
    def validate_at0000_1(obj):
        if not validate_CLUSTER(obj):
            return False
        if obj["archetype_node_id"] != "at0000_1":
            return False
        if "items" in obj:
            if type(obj["items"]) != list:
                return False
            if len(obj["items"]) > 1:
                return False
            if len(obj["items"]) == 1:
                if not validate_at0001(obj["items"][0]) and not validate_at0002(obj["items"][0]) and not validate_at0003(obj["items"][0]) and not validate_at0004(obj["items"][0]) and not validate_at0005(obj["items"][0]) and not validate_at0006(obj["items"][0]) and not validate_at0_2(obj["items"][0]) and not validate_at0_3(obj["items"][0]):
                    return False
        return True
    return validate_at0000_1(obj)

def validate_archetype_DEMOGRAPHIC_CLUSTER_person_identifier_v0(obj):
    '''
    Checks if a given JSON object (Python dict) matches the archetype 'openEHR-DEMOGRAPHIC-CLUSTER.person_identifier.v0'
    
    Parameters:
        obj - The JSON object to check
        
    Returns:
        True if the object matches the arquetype, False otherwise.
    '''
    
    def validate_gen0079(obj):
        if not validate_DV_IDENTIFIER(obj):
            return False
        return True
    
    def validate_at0001(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0001":
            return False
        if "value" in obj:
            if not validate_gen0079(obj["value"]):
                return False
        return True
    
    def validate_gen0080(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0082(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "value" not in obj["terminology_id"]:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] not in ['at0010', 'at0011', 'at0012', 'at0013']:
            return False
        return True
    
    def validate_gen0081(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0082(obj["defining_code"]):
                return False
        return True
    
    def validate_at0002(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0002":
            return False
        if "value" in obj:
            if not validate_gen0080(obj["value"]) and not validate_gen0081(obj["value"]):
                return False
        return True
    
    def validate_gen0083(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0085(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0001":
            return False
        return True
    
    def validate_gen0084(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0085(obj["defining_code"]):
                return False
        return True
    
    def validate_at0003(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0003":
            return False
        if "value" in obj:
            if not validate_gen0083(obj["value"]) and not validate_gen0084(obj["value"]):
                return False
        return True
    def validate_gen0087(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0002":
            return False
        return True
    
    def validate_gen0086(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0087(obj["defining_code"]):
                return False
        return True
    
    def validate_at0004(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0004":
            return False
        if "value" in obj:
            if not validate_gen0086(obj["value"]):
                return False
        return True
    def validate_gen0089(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0003":
            return False
        return True
    
    def validate_gen0088(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0089(obj["defining_code"]):
                return False
        return True
    
    def validate_at0005(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0005":
            return False
        if "value" in obj:
            if not validate_gen0088(obj["value"]):
                return False
        return True
    
    def validate_gen0091(obj):
        if not validate_DV_DATE(obj):
            return False
        return True
    
    def validate_gen0092(obj):
        if not validate_DV_DATE(obj):
            return False
        return True
    
    def validate_gen0090(obj):
        if not validate_DV_INTERVAL_of_DV_DATE(obj):
            return False
        if "upper" in obj:
            if not validate_gen0091(obj["upper"]):
                return False
        if "lower" in obj:
            if not validate_gen0092(obj["lower"]):
                return False
        return True
    
    def validate_at0006(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0006":
            return False
        if "value" in obj:
            if not validate_gen0090(obj["value"]):
                return False
        return True
    
    def validate_at0000(obj):
        if not validate_CLUSTER(obj):
            return False
        if obj["archetype_node_id"] != "at0000":
            return False
        if "items" not in obj:
            return False
        if type(obj["items"]) != list:
            return False
        counter = {'at0001': 0, 'at0002': 0, 'at0003': 0, 'at0004': 0, 'at0005': 0, 'at0006': 0}
        for item in obj["items"]:
            if validate_at0001(item):
                counter["at0001"] += 1
            elif validate_at0002(item):
                counter["at0002"] += 1
            elif validate_at0003(item):
                counter["at0003"] += 1
            elif validate_at0004(item):
                counter["at0004"] += 1
            elif validate_at0005(item):
                counter["at0005"] += 1
            elif validate_at0006(item):
                counter["at0006"] += 1
            else:
                return False
        if not(1 <= counter["at0001"] and 1 <= counter["at0002"] and 0 <= counter["at0003"] and 0 <= counter["at0004"] and 0 <= counter["at0005"] and 0 <= counter["at0006"]):
            return False
        return True
    return validate_at0000(obj)

def validate_archetype_DEMOGRAPHIC_ITEM_TREE_person_details_v0(obj):
    '''
    Checks if a given JSON object (Python dict) matches the archetype 'openEHR-DEMOGRAPHIC-ITEM_TREE.person_details.v0'
    
    Parameters:
        obj - The JSON object to check
        
    Returns:
        True if the object matches the arquetype, False otherwise.
    '''
    
    def validate_gen0093(obj):
        if not validate_DV_DATE(obj):
            return False
        return True
    
    def validate_at0010(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0010":
            return False
        if "value" in obj:
            if not validate_gen0093(obj["value"]):
                return False
        return True
    
    def validate_gen0094(obj):
        if not validate_DV_BOOLEAN(obj):
            return False
        return True
    
    def validate_at0011(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0011":
            return False
        if "value" in obj:
            if not validate_gen0094(obj["value"]):
                return False
        return True
    def validate_gen0096(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0001":
            return False
        return True
    
    def validate_gen0095(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0096(obj["defining_code"]):
                return False
        return True
    
    def validate_at0012(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0012":
            return False
        if "value" in obj:
            if not validate_gen0095(obj["value"]):
                return False
        return True
    def validate_gen0098(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0002":
            return False
        return True
    
    def validate_gen0097(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0098(obj["defining_code"]):
                return False
        return True
    
    def validate_at0013(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0013":
            return False
        if "value" in obj:
            if not validate_gen0097(obj["value"]):
                return False
        return True
    def validate_gen0100(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0003":
            return False
        return True
    
    def validate_gen0099(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0100(obj["defining_code"]):
                return False
        return True
    
    def validate_at0014(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0014":
            return False
        if "value" in obj:
            if not validate_gen0099(obj["value"]):
                return False
        return True
    
    def validate_gen0101(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0103(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0004":
            return False
        return True
    
    def validate_gen0102(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0103(obj["defining_code"]):
                return False
        return True
    
    def validate_at0015(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0015":
            return False
        if "value" in obj:
            if not validate_gen0101(obj["value"]) and not validate_gen0102(obj["value"]):
                return False
        return True
    
    def validate_gen0104(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0106(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0005":
            return False
        return True
    
    def validate_gen0105(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0106(obj["defining_code"]):
                return False
        return True
    
    def validate_at0016(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0016":
            return False
        if "value" in obj:
            if not validate_gen0104(obj["value"]) and not validate_gen0105(obj["value"]):
                return False
        return True
    
    def validate_gen0107(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0109(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "value" not in obj["terminology_id"]:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] not in ['at0310', 'at0311', 'at0312', 'at0313']:
            return False
        return True
    
    def validate_gen0108(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0109(obj["defining_code"]):
                return False
        return True
    
    def validate_at0017(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0017":
            return False
        if "value" in obj:
            if not validate_gen0107(obj["value"]) and not validate_gen0108(obj["value"]):
                return False
        return True
    
    def validate_gen0110(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0018(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0018":
            return False
        if "value" in obj:
            if not validate_gen0110(obj["value"]):
                return False
        return True
    
    def validate_at0006(obj):
        if validate_archetype_DEMOGRAPHIC_CLUSTER_birth_data_additional_detail_br_v0(obj):
            return True
        return False
    
    def validate_at0001(obj):
        if not validate_CLUSTER(obj):
            return False
        if obj["archetype_node_id"] != "at0001":
            return False
        if "items" in obj:
            if type(obj["items"]) != list:
                return False
            if len(obj["items"]) > 1:
                return False
            if len(obj["items"]) == 1:
                if not validate_at0010(obj["items"][0]) and not validate_at0011(obj["items"][0]) and not validate_at0012(obj["items"][0]) and not validate_at0013(obj["items"][0]) and not validate_at0014(obj["items"][0]) and not validate_at0015(obj["items"][0]) and not validate_at0016(obj["items"][0]) and not validate_at0017(obj["items"][0]) and not validate_at0018(obj["items"][0]) and not validate_at0006(obj["items"][0]):
                    return False
        return True
    
    def validate_gen0111(obj):
        if not validate_DV_DATE(obj):
            return False
        return True
    
    def validate_at0021(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0021":
            return False
        if "value" in obj:
            if not validate_gen0111(obj["value"]):
                return False
        return True
    
    def validate_gen0112(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0114(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "value" not in obj["terminology_id"]:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] not in ['at0220', 'at0221', 'at0222', 'at0223', 'at0224']:
            return False
        return True
    
    def validate_gen0113(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0114(obj["defining_code"]):
                return False
        return True
    
    def validate_at0022(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0022":
            return False
        if "value" in obj:
            if not validate_gen0112(obj["value"]) and not validate_gen0113(obj["value"]):
                return False
        return True
    def validate_gen0116(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0001":
            return False
        return True
    
    def validate_gen0115(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0116(obj["defining_code"]):
                return False
        return True
    
    def validate_at0023(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0023":
            return False
        if "value" in obj:
            if not validate_gen0115(obj["value"]):
                return False
        return True
    def validate_gen0118(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0002":
            return False
        return True
    
    def validate_gen0117(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0118(obj["defining_code"]):
                return False
        return True
    
    def validate_at0024(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0024":
            return False
        if "value" in obj:
            if not validate_gen0117(obj["value"]):
                return False
        return True
    
    def validate_gen0119(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0121(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0003":
            return False
        return True
    
    def validate_gen0120(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0121(obj["defining_code"]):
                return False
        return True
    
    def validate_at0025(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0025":
            return False
        if "value" in obj:
            if not validate_gen0119(obj["value"]) and not validate_gen0120(obj["value"]):
                return False
        return True
    
    def validate_gen0122(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0026(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0026":
            return False
        if "value" in obj:
            if not validate_gen0122(obj["value"]):
                return False
        return True
    
    def validate_at0002(obj):
        if not validate_CLUSTER(obj):
            return False
        if obj["archetype_node_id"] != "at0002":
            return False
        if "items" in obj:
            if type(obj["items"]) != list:
                return False
            if len(obj["items"]) > 1:
                return False
            if len(obj["items"]) == 1:
                if not validate_at0021(obj["items"][0]) and not validate_at0022(obj["items"][0]) and not validate_at0023(obj["items"][0]) and not validate_at0024(obj["items"][0]) and not validate_at0025(obj["items"][0]) and not validate_at0026(obj["items"][0]):
                    return False
        return True
    
    def validate_gen0123(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0125(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "value" not in obj["terminology_id"]:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] not in ['at0410', 'at0411', 'at0412', 'at0413', 'at0414', 'at0415', 'at0416', 'at0417', 'at0418', 'at0419', 'at0420', 'at0421', 'at0422', 'at0423', 'at0424', 'at0425']:
            return False
        return True
    
    def validate_gen0124(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0125(obj["defining_code"]):
                return False
        return True
    
    def validate_at0041(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0041":
            return False
        if "value" in obj:
            if not validate_gen0123(obj["value"]) and not validate_gen0124(obj["value"]):
                return False
        return True
    
    def validate_gen0126(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0042(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0042":
            return False
        if "value" in obj:
            if not validate_gen0126(obj["value"]):
                return False
        return True
    
    def validate_gen0127(obj):
        if not validate_DV_PROPORTION(obj):
            return False
        return True
    
    def validate_at0043(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0043":
            return False
        if "value" in obj:
            if not validate_gen0127(obj["value"]):
                return False
        return True
    
    def validate_gen0128(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0044(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0044":
            return False
        if "value" in obj:
            if not validate_gen0128(obj["value"]):
                return False
        return True
    
    def validate_gen0129(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0131(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0008":
            return False
        return True
    
    def validate_gen0130(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0131(obj["defining_code"]):
                return False
        return True
    
    def validate_at0045(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0045":
            return False
        if "value" in obj:
            if not validate_gen0129(obj["value"]) and not validate_gen0130(obj["value"]):
                return False
        return True
    
    def validate_gen0132(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0046(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0046":
            return False
        if "value" in obj:
            if not validate_gen0132(obj["value"]):
                return False
        return True
    
    def validate_gen0133(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0047(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0047":
            return False
        if "value" in obj:
            if not validate_gen0133(obj["value"]):
                return False
        return True
    
    def validate_gen0134(obj):
        if not validate_DV_DATE(obj):
            return False
        return True
    
    def validate_at0048(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0048":
            return False
        if "value" in obj:
            if not validate_gen0134(obj["value"]):
                return False
        return True
    
    def validate_at0004(obj):
        if not validate_CLUSTER(obj):
            return False
        if obj["archetype_node_id"] != "at0004":
            return False
        if "items" in obj:
            if type(obj["items"]) != list:
                return False
            if len(obj["items"]) > 1:
                return False
            if len(obj["items"]) == 1:
                if not validate_at0041(obj["items"][0]) and not validate_at0042(obj["items"][0]) and not validate_at0043(obj["items"][0]) and not validate_at0044(obj["items"][0]) and not validate_at0045(obj["items"][0]) and not validate_at0046(obj["items"][0]) and not validate_at0047(obj["items"][0]) and not validate_at0048(obj["items"][0]):
                    return False
        return True
    
    def validate_gen0135(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0137(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "value" not in obj["terminology_id"]:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] not in ['at0310', 'at0311', 'at0312', 'at0313']:
            return False
        return True
    
    def validate_gen0136(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0137(obj["defining_code"]):
                return False
        return True
    
    def validate_at0031(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0031":
            return False
        if "value" in obj:
            if not validate_gen0135(obj["value"]) and not validate_gen0136(obj["value"]):
                return False
        return True
    
    def validate_gen0138(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0032(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0032":
            return False
        if "value" in obj:
            if not validate_gen0138(obj["value"]):
                return False
        return True
    
    def validate_gen0139(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0141(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0006":
            return False
        return True
    
    def validate_gen0140(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0141(obj["defining_code"]):
                return False
        return True
    
    def validate_at0033(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0033":
            return False
        if "value" in obj:
            if not validate_gen0139(obj["value"]) and not validate_gen0140(obj["value"]):
                return False
        return True
    
    def validate_gen0142(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0144(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0007":
            return False
        return True
    
    def validate_gen0143(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0144(obj["defining_code"]):
                return False
        return True
    
    def validate_at0034(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0034":
            return False
        if "value" in obj:
            if not validate_gen0142(obj["value"]) and not validate_gen0143(obj["value"]):
                return False
        return True
    
    def validate_gen0145(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0035(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0035":
            return False
        if "value" in obj:
            if not validate_gen0145(obj["value"]):
                return False
        return True
    
    def validate_at0005(obj):
        if validate_archetype_DEMOGRAPHIC_CLUSTER_person_identifier_provider_v0(obj):
            return True
        if validate_archetype_DEMOGRAPHIC_CLUSTER_person_identifier_v0(obj):
            return True
        return False
    
    def validate_at0000(obj):
        if not validate_ITEM_TREE(obj):
            return False
        if obj["archetype_node_id"] != "at0000":
            return False
        if "items" not in obj:
            return False
        if type(obj["items"]) != list:
            return False
        counter = {'at0001': 0, 'at0002': 0, 'at0004': 0, 'at0031': 0, 'at0032': 0, 'at0033': 0, 'at0034': 0, 'at0035': 0, 'at0005': 0}
        for item in obj["items"]:
            if validate_at0001(item):
                counter["at0001"] += 1
            elif validate_at0002(item):
                counter["at0002"] += 1
            elif validate_at0004(item):
                counter["at0004"] += 1
            elif validate_at0031(item):
                counter["at0031"] += 1
            elif validate_at0032(item):
                counter["at0032"] += 1
            elif validate_at0033(item):
                counter["at0033"] += 1
            elif validate_at0034(item):
                counter["at0034"] += 1
            elif validate_at0035(item):
                counter["at0035"] += 1
            elif validate_at0005(item):
                counter["at0005"] += 1
            else:
                return False
        if not(1 <= counter["at0001"] and 1 <= counter["at0002"] and 1 <= counter["at0004"] and 0 <= counter["at0031"] and 0 <= counter["at0032"] and 0 <= counter["at0033"] and 0 <= counter["at0034"] and 0 <= counter["at0035"] and 0 <= counter["at0005"]):
            return False
        return True
    return validate_at0000(obj)

def validate_archetype_DEMOGRAPHIC_PARTY_IDENTITY_person_name_individual_provider_v0(obj):
    '''
    Checks if a given JSON object (Python dict) matches the archetype 'openEHR-DEMOGRAPHIC-PARTY_IDENTITY.person_name-individual_provider.v0'
    
    Parameters:
        obj - The JSON object to check
        
    Returns:
        True if the object matches the arquetype, False otherwise.
    '''
    
    def validate_gen0146(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0010(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0010":
            return False
        if "value" in obj:
            if not validate_gen0146(obj["value"]):
                return False
        return True
    
    def validate_gen0147(obj):
        if not validate_DV_COUNT(obj):
            return False
        return True
    
    def validate_at0011(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0011":
            return False
        if "value" in obj:
            if not validate_gen0147(obj["value"]):
                return False
        return True
    
    def validate_at0002(obj):
        if not validate_CLUSTER(obj):
            return False
        if obj["archetype_node_id"] != "at0002":
            return False
        if "items" not in obj:
            return False
        if type(obj["items"]) != list:
            return False
        counter = {'at0010': 0, 'at0011': 0}
        for item in obj["items"]:
            if validate_at0010(item):
                counter["at0010"] += 1
            elif validate_at0011(item):
                counter["at0011"] += 1
            else:
                return False
        if not(1 <= counter["at0010"] and 1 <= counter["at0011"]):
            return False
        return True
    
    def validate_gen0148(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0012(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0012":
            return False
        if "value" in obj:
            if not validate_gen0148(obj["value"]):
                return False
        return True
    
    def validate_gen0149(obj):
        if not validate_DV_COUNT(obj):
            return False
        return True
    
    def validate_at0013(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0013":
            return False
        if "value" in obj:
            if not validate_gen0149(obj["value"]):
                return False
        return True
    
    def validate_at0003(obj):
        if not validate_CLUSTER(obj):
            return False
        if obj["archetype_node_id"] != "at0003":
            return False
        if "items" not in obj:
            return False
        if type(obj["items"]) != list:
            return False
        counter = {'at0012': 0, 'at0013': 0}
        for item in obj["items"]:
            if validate_at0012(item):
                counter["at0012"] += 1
            elif validate_at0013(item):
                counter["at0013"] += 1
            else:
                return False
        if not(1 <= counter["at0012"] and 1 <= counter["at0013"]):
            return False
        return True
    def validate_gen0151(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0000":
            return False
        return True
    
    def validate_gen0150(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0151(obj["defining_code"]):
                return False
        return True
    
    def validate_at0014(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0014":
            return False
        if "value" in obj:
            if not validate_gen0150(obj["value"]):
                return False
        return True
    
    def validate_gen0152(obj):
        if not validate_DV_COUNT(obj):
            return False
        return True
    
    def validate_at0015(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0015":
            return False
        if "value" in obj:
            if not validate_gen0152(obj["value"]):
                return False
        return True
    
    def validate_at0004(obj):
        if not validate_CLUSTER(obj):
            return False
        if obj["archetype_node_id"] != "at0004":
            return False
        if "items" not in obj:
            return False
        if type(obj["items"]) != list:
            return False
        counter = {'at0014': 0, 'at0015': 0}
        for item in obj["items"]:
            if validate_at0014(item):
                counter["at0014"] += 1
            elif validate_at0015(item):
                counter["at0015"] += 1
            else:
                return False
        if not(1 <= counter["at0014"] and 1 <= counter["at0015"]):
            return False
        return True
    def validate_gen0154(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0001":
            return False
        return True
    
    def validate_gen0153(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0154(obj["defining_code"]):
                return False
        return True
    
    def validate_at0016(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0016":
            return False
        if "value" in obj:
            if not validate_gen0153(obj["value"]):
                return False
        return True
    
    def validate_gen0155(obj):
        if not validate_DV_COUNT(obj):
            return False
        return True
    
    def validate_at0017(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0017":
            return False
        if "value" in obj:
            if not validate_gen0155(obj["value"]):
                return False
        return True
    
    def validate_at0005(obj):
        if not validate_CLUSTER(obj):
            return False
        if obj["archetype_node_id"] != "at0005":
            return False
        if "items" not in obj:
            return False
        if type(obj["items"]) != list:
            return False
        counter = {'at0016': 0, 'at0017': 0}
        for item in obj["items"]:
            if validate_at0016(item):
                counter["at0016"] += 1
            elif validate_at0017(item):
                counter["at0017"] += 1
            else:
                return False
        if not(1 <= counter["at0016"] and 1 <= counter["at0017"]):
            return False
        return True
    def validate_gen0157(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "value" not in obj["terminology_id"]:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] not in ['at0023', 'at0024', 'at0025', 'at0026', 'at0027', 'at0028']:
            return False
        return True
    
    def validate_gen0156(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0157(obj["defining_code"]):
                return False
        return True
    
    def validate_at0018(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0018":
            return False
        if "value" in obj:
            if not validate_gen0156(obj["value"]):
                return False
        return True
    
    def validate_gen0158(obj):
        if not validate_DV_INTERVAL_of_DV_DATE(obj):
            return False
        return True
    
    def validate_at0019(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0019":
            return False
        if "value" in obj:
            if not validate_gen0158(obj["value"]):
                return False
        return True
    
    def validate_gen0159(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0020(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0020":
            return False
        if "value" in obj:
            if not validate_gen0159(obj["value"]):
                return False
        return True
    
    def validate_at0006(obj):
        if not validate_CLUSTER(obj):
            return False
        if obj["archetype_node_id"] != "at0006":
            return False
        if "items" not in obj:
            return False
        if type(obj["items"]) != list:
            return False
        counter = {'at0018': 0, 'at0019': 0, 'at0020': 0}
        for item in obj["items"]:
            if validate_at0018(item):
                counter["at0018"] += 1
            elif validate_at0019(item):
                counter["at0019"] += 1
            elif validate_at0020(item):
                counter["at0020"] += 1
            else:
                return False
        if not(1 <= counter["at0018"] and 1 <= counter["at0019"] and 0 <= counter["at0020"]):
            return False
        return True
    def validate_gen0161(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0002":
            return False
        return True
    
    def validate_gen0160(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0161(obj["defining_code"]):
                return False
        return True
    
    def validate_at0021(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0021":
            return False
        if "value" in obj:
            if not validate_gen0160(obj["value"]):
                return False
        return True
    
    def validate_gen0162(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0022(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0022":
            return False
        if "value" in obj:
            if not validate_gen0162(obj["value"]):
                return False
        return True
    
    def validate_at0007(obj):
        if not validate_CLUSTER(obj):
            return False
        if obj["archetype_node_id"] != "at0007":
            return False
        if "items" not in obj:
            return False
        if type(obj["items"]) != list:
            return False
        counter = {'at0021': 0, 'at0022': 0}
        for item in obj["items"]:
            if validate_at0021(item):
                counter["at0021"] += 1
            elif validate_at0022(item):
                counter["at0022"] += 1
            else:
                return False
        if not(1 <= counter["at0021"] and 1 <= counter["at0022"]):
            return False
        return True
    
    def validate_gen0163(obj):
        if not validate_DV_BOOLEAN(obj):
            return False
        return True
    
    def validate_at0008(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0008":
            return False
        if "value" in obj:
            if not validate_gen0163(obj["value"]):
                return False
        return True
    def validate_gen0165(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "value" not in obj["terminology_id"]:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] not in ['at0031', 'at0032', 'at0033', 'at0034', 'at0035', 'at0036']:
            return False
        return True
    
    def validate_gen0164(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0165(obj["defining_code"]):
                return False
        return True
    
    def validate_at0009_1(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0009_1":
            return False
        if "value" in obj:
            if not validate_gen0164(obj["value"]):
                return False
        return True
    
    def validate_at0_3(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0_3":
            return False
        return True
    
    def validate_gen0166(obj):
        if not validate_DV_INTERVAL(obj):
            return False
        return True
    
    def validate_at0_4(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0_4":
            return False
        if "value" in obj:
            if not validate_gen0166(obj["value"]):
                return False
        return True
    
    def validate_gen0167(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0_5(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0_5":
            return False
        if "value" in obj:
            if not validate_gen0167(obj["value"]):
                return False
        return True
    
    def validate_at0_2(obj):
        if not validate_CLUSTER(obj):
            return False
        if obj["archetype_node_id"] != "at0_2":
            return False
        if "items" not in obj:
            return False
        if type(obj["items"]) != list:
            return False
        counter = {'at0_3': 0, 'at0_4': 0, 'at0_5': 0}
        for item in obj["items"]:
            if validate_at0_3(item):
                counter["at0_3"] += 1
            elif validate_at0_4(item):
                counter["at0_4"] += 1
            elif validate_at0_5(item):
                counter["at0_5"] += 1
            else:
                return False
        if not(1 <= counter["at0_3"] and 1 <= counter["at0_4"] and 0 <= counter["at0_5"]):
            return False
        return True
    
    def validate_at0001(obj):
        if not validate_ITEM_TREE(obj):
            return False
        if obj["archetype_node_id"] != "at0001":
            return False
        if "items" not in obj:
            return False
        if type(obj["items"]) != list:
            return False
        counter = {'at0002': 0, 'at0003': 0, 'at0004': 0, 'at0005': 0, 'at0006': 0, 'at0007': 0, 'at0008': 0, 'at0009_1': 0, 'at0_2': 0}
        for item in obj["items"]:
            if validate_at0002(item):
                counter["at0002"] += 1
            elif validate_at0003(item):
                counter["at0003"] += 1
            elif validate_at0004(item):
                counter["at0004"] += 1
            elif validate_at0005(item):
                counter["at0005"] += 1
            elif validate_at0006(item):
                counter["at0006"] += 1
            elif validate_at0007(item):
                counter["at0007"] += 1
            elif validate_at0008(item):
                counter["at0008"] += 1
            elif validate_at0009_1(item):
                counter["at0009_1"] += 1
            elif validate_at0_2(item):
                counter["at0_2"] += 1
            else:
                return False
        if not(0 <= counter["at0002"] and 1 <= counter["at0003"] and 0 <= counter["at0004"] and 0 <= counter["at0005"] and 1 <= counter["at0006"] and 0 <= counter["at0007"] and 1 <= counter["at0008"] and 0 <= counter["at0009_1"] and 0 <= counter["at0_2"]):
            return False
        return True
    
    def validate_at0000_1(obj):
        if not validate_PARTY_IDENTITY(obj):
            return False
        if obj["archetype_node_id"] != "at0000_1":
            return False
        if "details" in obj:
            if not validate_at0001(obj["details"]):
                return False
        return True
    return validate_at0000_1(obj)

def validate_archetype_DEMOGRAPHIC_PARTY_IDENTITY_person_name_v0(obj):
    '''
    Checks if a given JSON object (Python dict) matches the archetype 'openEHR-DEMOGRAPHIC-PARTY_IDENTITY.person_name.v0'
    
    Parameters:
        obj - The JSON object to check
        
    Returns:
        True if the object matches the arquetype, False otherwise.
    '''
    
    def validate_gen0168(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0170(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "value" not in obj["terminology_id"]:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] not in ['at0023', 'at0024', 'at0025', 'at0026', 'at0027', 'at0028']:
            return False
        return True
    
    def validate_gen0169(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0170(obj["defining_code"]):
                return False
        return True
    
    def validate_gen0171(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0002(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0002":
            return False
        if "value" in obj:
            if not validate_gen0171(obj["value"]):
                return False
        return True
    
    def validate_gen0172(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0003(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0003":
            return False
        if "value" in obj:
            if not validate_gen0172(obj["value"]):
                return False
        return True
    
    def validate_gen0173(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0004(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0004":
            return False
        if "value" in obj:
            if not validate_gen0173(obj["value"]):
                return False
        return True
    
    def validate_gen0174(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0005(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0005":
            return False
        if "value" in obj:
            if not validate_gen0174(obj["value"]):
                return False
        return True
    
    def validate_gen0175(obj):
        if not validate_DV_INTERVAL_of_DV_DATE(obj):
            return False
        return True
    
    def validate_at0019(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0019":
            return False
        if "value" in obj:
            if not validate_gen0175(obj["value"]):
                return False
        return True
    
    def validate_gen0176(obj):
        if not validate_DV_IDENTIFIER(obj):
            return False
        return True
    
    def validate_at0020(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0020":
            return False
        if "value" in obj:
            if not validate_gen0176(obj["value"]):
                return False
        return True
    
    def validate_gen0177(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0021(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0021":
            return False
        if "value" in obj:
            if not validate_gen0177(obj["value"]):
                return False
        return True
    
    def validate_gen0178(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0022(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0022":
            return False
        if "value" in obj:
            if not validate_gen0178(obj["value"]):
                return False
        return True
    
    def validate_at0007(obj):
        if not validate_CLUSTER(obj):
            return False
        if obj["archetype_node_id"] != "at0007":
            return False
        if "items" not in obj:
            return False
        if type(obj["items"]) != list:
            return False
        counter = {'at0021': 0, 'at0022': 0}
        for item in obj["items"]:
            if validate_at0021(item):
                counter["at0021"] += 1
            elif validate_at0022(item):
                counter["at0022"] += 1
            else:
                return False
        if not(1 <= counter["at0021"] and 1 <= counter["at0022"]):
            return False
        return True
    
    def validate_gen0179(obj):
        if not validate_DV_BOOLEAN(obj):
            return False
        return True
    
    def validate_at0008(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0008":
            return False
        if "value" in obj:
            if not validate_gen0179(obj["value"]):
                return False
        return True
    
    def validate_gen0180(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0182(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "value" not in obj["terminology_id"]:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] not in ['at0031', 'at0032', 'at0033', 'at0034', 'at0035', 'at0036']:
            return False
        return True
    
    def validate_gen0181(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0182(obj["defining_code"]):
                return False
        return True
    
    def validate_at0009(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0009":
            return False
        if "value" in obj:
            if not validate_gen0180(obj["value"]) and not validate_gen0181(obj["value"]):
                return False
        return True
    
    def validate_gen0183(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    
    def validate_at0010(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0010":
            return False
        if "value" in obj:
            if not validate_gen0183(obj["value"]):
                return False
        return True
    
    def validate_at0001(obj):
        if not validate_ITEM_TREE(obj):
            return False
        if obj["archetype_node_id"] != "at0001":
            return False
        if "items" not in obj:
            return False
        if type(obj["items"]) != list:
            return False
        counter = {'at0002': 0, 'at0003': 0, 'at0004': 0, 'at0005': 0, 'at0019': 0, 'at0020': 0, 'at0007': 0, 'at0008': 0, 'at0009': 0, 'at0010': 0}
        for item in obj["items"]:
            if validate_at0002(item):
                counter["at0002"] += 1
            elif validate_at0003(item):
                counter["at0003"] += 1
            elif validate_at0004(item):
                counter["at0004"] += 1
            elif validate_at0005(item):
                counter["at0005"] += 1
            elif validate_at0019(item):
                counter["at0019"] += 1
            elif validate_at0020(item):
                counter["at0020"] += 1
            elif validate_at0007(item):
                counter["at0007"] += 1
            elif validate_at0008(item):
                counter["at0008"] += 1
            elif validate_at0009(item):
                counter["at0009"] += 1
            elif validate_at0010(item):
                counter["at0010"] += 1
            else:
                return False
        if not(0 <= counter["at0002"] and 0 <= counter["at0003"] and 0 <= counter["at0004"] and 0 <= counter["at0005"] and 0 <= counter["at0019"] and 0 <= counter["at0020"] and 0 <= counter["at0007"] and 1 <= counter["at0008"] and 0 <= counter["at0009"] and 0 <= counter["at0010"]):
            return False
        return True
    
    def validate_at0000(obj):
        if not validate_PARTY_IDENTITY(obj):
            return False
        if obj["archetype_node_id"] != "at0000":
            return False
        if "name" in obj:
            if not validate_gen0168(obj["name"]) and not validate_gen0169(obj["name"]):
                return False
        if "details" in obj:
            if not validate_at0001(obj["details"]):
                return False
        return True
    return validate_at0000(obj)

def validate_archetype_DEMOGRAPHIC_PERSON_person_patient_v0(obj):
    '''
    Checks if a given JSON object (Python dict) matches the archetype 'openEHR-DEMOGRAPHIC-PERSON.person-patient.v0'
    
    Parameters:
        obj - The JSON object to check
        
    Returns:
        True if the object matches the arquetype, False otherwise.
    '''
    
    def validate_at0001(obj):
        if validate_archetype_DEMOGRAPHIC_ITEM_TREE_person_details_v0(obj):
            return True
        return False
    
    def validate_at0002_1(obj):
        if validate_archetype_DEMOGRAPHIC_PARTY_IDENTITY_person_name_individual_provider_v0(obj):
            return True
        if validate_archetype_DEMOGRAPHIC_PARTY_IDENTITY_person_name_v0(obj):
            return True
        return False
    
    def validate_at0030(obj):
        if validate_archetype_DEMOGRAPHIC_ADDRESS_address_v0(obj):
            return True
        if validate_archetype_DEMOGRAPHIC_ADDRESS_electronic_communication_provider_v0(obj):
            return True
        if validate_archetype_DEMOGRAPHIC_ADDRESS_electronic_communication_v0(obj):
            return True
        return False
    
    def validate_at0003_1(obj):
        if not validate_CONTACT(obj):
            return False
        if obj["archetype_node_id"] != "at0003_1":
            return False
        if "addresses" in obj:
            if type(obj["addresses"]) != list:
                return False
            if len(obj["addresses"]) > 1:
                return False
            if len(obj["addresses"]) == 1:
                if not validate_at0030(obj["addresses"][0]):
                    return False
        return True
    
    def validate_gen0184(obj):
        if not validate_DV_TEXT(obj):
            return False
        return True
    def validate_gen0186(obj):
        if not validate_CODE_PHRASE(obj):
            return False
        if "terminology_id" not in obj:
            return False
        if "code_string" not in obj:
            return False
        if obj["terminology_id"]["value"] != "local":
            return False
        if obj["code_string"] != "ac0000":
            return False
        return True
    
    def validate_gen0185(obj):
        if not validate_DV_CODED_TEXT(obj):
            return False
        if "defining_code" in obj:
            if not validate_gen0186(obj["defining_code"]):
                return False
        return True
    
    def validate_at0040(obj):
        if not validate_ELEMENT(obj):
            return False
        if obj["archetype_node_id"] != "at0040":
            return False
        if "value" in obj:
            if not validate_gen0184(obj["value"]) and not validate_gen0185(obj["value"]):
                return False
        return True
    
    def validate_at0_40(obj):
        if not validate_ITEM_TREE(obj):
            return False
        if obj["archetype_node_id"] != "at0_40":
            return False
        if "items" in obj:
            if type(obj["items"]) != list:
                return False
            if len(obj["items"]) > 1:
                return False
            if len(obj["items"]) == 1:
                if not validate_at0040(obj["items"][0]):
                    return False
        return True
    
    def validate_at0004_1(obj):
        if not validate_PARTY_RELATIONSHIP(obj):
            return False
        if obj["archetype_node_id"] != "at0004_1":
            return False
        if "details" in obj:
            if not validate_at0_40(obj["details"]):
                return False
        return True
    
    def validate_at0_21(obj):
        if validate_archetype_DEMOGRAPHIC_CLUSTER_person_identifier_provider_v0(obj):
            return True
        if validate_archetype_DEMOGRAPHIC_CLUSTER_person_identifier_v0(obj):
            return True
        return False
    
    def validate_at0_20(obj):
        if not validate_ITEM_TREE(obj):
            return False
        if obj["archetype_node_id"] != "at0_20":
            return False
        if "items" in obj:
            if type(obj["items"]) != list:
                return False
            if len(obj["items"]) > 1:
                return False
            if len(obj["items"]) == 1:
                if not validate_at0_21(obj["items"][0]):
                    return False
        return True
    
    def validate_at0_2(obj):
        if not validate_PARTY_RELATIONSHIP(obj):
            return False
        if obj["archetype_node_id"] != "at0_2":
            return False
        if "details" in obj:
            if not validate_at0_20(obj["details"]):
                return False
        return True
    
    def validate_at0_31(obj):
        if validate_archetype_DEMOGRAPHIC_CLUSTER_person_identifier_provider_v0(obj):
            return True
        if validate_archetype_DEMOGRAPHIC_CLUSTER_person_identifier_v0(obj):
            return True
        return False
    
    def validate_at0_30(obj):
        if not validate_ITEM_TREE(obj):
            return False
        if obj["archetype_node_id"] != "at0_30":
            return False
        if "items" in obj:
            if type(obj["items"]) != list:
                return False
            if len(obj["items"]) > 1:
                return False
            if len(obj["items"]) == 1:
                if not validate_at0_31(obj["items"][0]):
                    return False
        return True
    
    def validate_at0_3(obj):
        if not validate_PARTY_RELATIONSHIP(obj):
            return False
        if obj["archetype_node_id"] != "at0_3":
            return False
        if "details" in obj:
            if not validate_at0_30(obj["details"]):
                return False
        return True
    
    def validate_at0000_1(obj):
        if not validate_PERSON(obj):
            return False
        if obj["archetype_node_id"] != "at0000_1":
            return False
        if "details" in obj:
            if not validate_at0001(obj["details"]):
                return False
        if "identities" in obj:
            if type(obj["identities"]) != list:
                return False
            if len(obj["identities"]) > 1:
                return False
            if len(obj["identities"]) == 1:
                if not validate_at0002_1(obj["identities"][0]):
                    return False
        if "contacts" in obj:
            if type(obj["contacts"]) != list:
                return False
            if len(obj["contacts"]) > 1:
                return False
            if len(obj["contacts"]) == 1:
                if not validate_at0003_1(obj["contacts"][0]):
                    return False
        if "relationships" in obj:
            if type(obj["relationships"]) != list:
                return False
            if len(obj["relationships"]) > 1:
                return False
            if len(obj["relationships"]) == 1:
                if not validate_at0004_1(obj["relationships"][0]) and not validate_at0_2(obj["relationships"][0]) and not validate_at0_3(obj["relationships"][0]):
                    return False
        return True
    return validate_at0000_1(obj)
