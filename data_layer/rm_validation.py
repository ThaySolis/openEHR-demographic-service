def validate_ACTOR(actor):
    if '_type' not in actor:
        return False
    if actor['_type'] not in ['AGENT','ORGANISATION','GROUP','PERSON']:
        return False
    if 'name' not in actor:
        return False
    if not validate_DV_TEXT(actor['name']):
        return False
    if 'archetype_node_id' not in actor:
        return False
    if not validate_String(actor['archetype_node_id']):
        return False
    if 'uid' in actor:
        if not validate_UID_BASED_ID(actor['uid']):
            return False
    if 'links' in actor:
        if type(actor['links']) != list:
            return False
        for element in actor['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in actor:
        if not validate_ARCHETYPED(actor['archetype_details']):
            return False
    if 'feeder_audit' in actor:
        if not validate_FEEDER_AUDIT(actor['feeder_audit']):
            return False
    if 'identities' not in actor:
        return False
    if type(actor['identities']) != list:
        return False
    if len(actor['identities']) == 0:
        return False
    for element in actor['identities']:
        if not validate_PARTY_IDENTITY(element):
            return False
    if 'contacts' in actor:
        if type(actor['contacts']) != list:
            return False
        for element in actor['contacts']:
            if not validate_CONTACT(element):
                return False
    if 'details' in actor:
        if not validate_ITEM_STRUCTURE(actor['details']):
            return False
    if 'reverse_relationships' in actor:
        if type(actor['reverse_relationships']) != list:
            return False
        for element in actor['reverse_relationships']:
            if not validate_PARTY_RELATIONSHIP(element):
                return False
    if 'relationships' in actor:
        if type(actor['relationships']) != list:
            return False
        for element in actor['relationships']:
            if not validate_PARTY_RELATIONSHIP(element):
                return False
    if 'languages' in actor:
        if type(actor['languages']) != list:
            return False
        for element in actor['languages']:
            if not validate_DV_TEXT(element):
                return False
    if 'roles' in actor:
        if type(actor['roles']) != list:
            return False
        for element in actor['roles']:
            if not validate_ROLE(element):
                return False
    if actor['_type']=='AGENT':
        if not validate_AGENT(actor):
            return False
    if actor['_type']=='ORGANISATION':
        if not validate_ORGANISATION(actor):
            return False
    if actor['_type']=='GROUP':
        if not validate_GROUP(actor):
            return False
    if actor['_type']=='PERSON':
        if not validate_PERSON(actor):
            return False
    return True
def validate_ADDRESS(address):
    if 'name' not in address:
        return False
    if not validate_DV_TEXT(address['name']):
        return False
    if 'archetype_node_id' not in address:
        return False
    if not validate_String(address['archetype_node_id']):
        return False
    if 'uid' in address:
        if not validate_UID_BASED_ID(address['uid']):
            return False
    if 'links' in address:
        if type(address['links']) != list:
            return False
        for element in address['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in address:
        if not validate_ARCHETYPED(address['archetype_details']):
            return False
    if 'feeder_audit' in address:
        if not validate_FEEDER_AUDIT(address['feeder_audit']):
            return False
    if 'details' not in address:
        return False
    if not validate_ITEM_STRUCTURE(address['details']):
        return False
    return True
def validate_AGENT(agent):
    if 'name' not in agent:
        return False
    if not validate_DV_TEXT(agent['name']):
        return False
    if 'archetype_node_id' not in agent:
        return False
    if not validate_String(agent['archetype_node_id']):
        return False
    if 'uid' in agent:
        if not validate_UID_BASED_ID(agent['uid']):
            return False
    if 'links' in agent:
        if type(agent['links']) != list:
            return False
        for element in agent['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in agent:
        if not validate_ARCHETYPED(agent['archetype_details']):
            return False
    if 'feeder_audit' in agent:
        if not validate_FEEDER_AUDIT(agent['feeder_audit']):
            return False
    if 'identities' not in agent:
        return False
    if type(agent['identities']) != list:
        return False
    if len(agent['identities']) == 0:
        return False
    for element in agent['identities']:
        if not validate_PARTY_IDENTITY(element):
            return False
    if 'contacts' in agent:
        if type(agent['contacts']) != list:
            return False
        for element in agent['contacts']:
            if not validate_CONTACT(element):
                return False
    if 'details' in agent:
        if not validate_ITEM_STRUCTURE(agent['details']):
            return False
    if 'reverse_relationships' in agent:
        if type(agent['reverse_relationships']) != list:
            return False
        for element in agent['reverse_relationships']:
            if not validate_PARTY_RELATIONSHIP(element):
                return False
    if 'relationships' in agent:
        if type(agent['relationships']) != list:
            return False
        for element in agent['relationships']:
            if not validate_PARTY_RELATIONSHIP(element):
                return False
    if 'languages' in agent:
        if type(agent['languages']) != list:
            return False
        for element in agent['languages']:
            if not validate_DV_TEXT(element):
                return False
    if 'roles' in agent:
        if type(agent['roles']) != list:
            return False
        for element in agent['roles']:
            if not validate_ROLE(element):
                return False
    return True
def validate_ARCHETYPED(archetyped):
    if 'archetype_id' not in archetyped:
        return False
    if not validate_ARCHETYPE_ID(archetyped['archetype_id']):
        return False
    if 'template_id' in archetyped:
        if not validate_TEMPLATE_ID(archetyped['template_id']):
            return False
    if 'rm_version' not in archetyped:
        return False
    if not validate_String(archetyped['rm_version']):
        return False
    return True
def validate_ARCHETYPE_ID(archetype_id):
    if 'value' not in archetype_id:
        return False
    if not validate_String(archetype_id['value']):
        return False
    return True
def validate_CAPABILITY(capability):
    if 'name' not in capability:
        return False
    if not validate_DV_TEXT(capability['name']):
        return False
    if 'archetype_node_id' not in capability:
        return False
    if not validate_String(capability['archetype_node_id']):
        return False
    if 'uid' in capability:
        if not validate_UID_BASED_ID(capability['uid']):
            return False
    if 'links' in capability:
        if type(capability['links']) != list:
            return False
        for element in capability['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in capability:
        if not validate_ARCHETYPED(capability['archetype_details']):
            return False
    if 'feeder_audit' in capability:
        if not validate_FEEDER_AUDIT(capability['feeder_audit']):
            return False
    if 'credentials' not in capability:
        return False
    if not validate_ITEM_STRUCTURE(capability['credentials']):
        return False
    if 'time_validity' in capability:
        if not validate_DV_INTERVAL_of_DV_DATE(capability['time_validity']):
            return False
    return True
def validate_CLUSTER(cluster):
    if 'name' not in cluster:
        return False
    if not validate_DV_TEXT(cluster['name']):
        return False
    if 'archetype_node_id' not in cluster:
        return False
    if not validate_String(cluster['archetype_node_id']):
        return False
    if 'uid' in cluster:
        if not validate_UID_BASED_ID(cluster['uid']):
            return False
    if 'links' in cluster:
        if type(cluster['links']) != list:
            return False
        for element in cluster['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in cluster:
        if not validate_ARCHETYPED(cluster['archetype_details']):
            return False
    if 'feeder_audit' in cluster:
        if not validate_FEEDER_AUDIT(cluster['feeder_audit']):
            return False
    if 'items' not in cluster:
        return False
    if type(cluster['items']) != list:
        return False
    if len(cluster['items']) == 0:
        return False
    for element in cluster['items']:
        if not validate_ITEM(element):
            return False
    return True
def validate_CODE_PHRASE(code_phrase):
    if 'terminology_id' not in code_phrase:
        return False
    if not validate_TERMINOLOGY_ID(code_phrase['terminology_id']):
        return False
    if 'code_string' not in code_phrase:
        return False
    if not validate_String(code_phrase['code_string']):
        return False
    if 'preferred_term' in code_phrase:
        if not validate_String(code_phrase['preferred_term']):
            return False
    return True
def validate_CONTACT(contact):
    if 'name' not in contact:
        return False
    if not validate_DV_TEXT(contact['name']):
        return False
    if 'archetype_node_id' not in contact:
        return False
    if not validate_String(contact['archetype_node_id']):
        return False
    if 'uid' in contact:
        if not validate_UID_BASED_ID(contact['uid']):
            return False
    if 'links' in contact:
        if type(contact['links']) != list:
            return False
        for element in contact['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in contact:
        if not validate_ARCHETYPED(contact['archetype_details']):
            return False
    if 'feeder_audit' in contact:
        if not validate_FEEDER_AUDIT(contact['feeder_audit']):
            return False
    if 'addresses' not in contact:
        return False
    if type(contact['addresses']) != list:
        return False
    if len(contact['addresses']) == 0:
        return False
    for element in contact['addresses']:
        if not validate_ADDRESS(element):
            return False
    if 'time_validity' in contact:
        if not validate_DV_INTERVAL_of_DV_DATE(contact['time_validity']):
            return False
    return True
def validate_DATA_VALUE(data_value):
    if '_type' not in data_value:
        return False
    if data_value['_type'] not in ['DV_BOOLEAN','DV_STATE','DV_IDENTIFIER','DV_PARAGRAPH','DV_TEXT','DV_INTERVAL','DV_URI','DV_MULTIMEDIA','DV_PARSABLE','DV_CODED_TEXT','DV_ORDINAL','DV_SCALE','DV_PROPORTION','DV_QUANTITY','DV_COUNT','DV_DURATION','DV_DATE','DV_TIME','DV_DATE_TIME','DV_INTERVAL<DV_DATE_TIME>','DV_INTERVAL<DV_DATE>','DV_INTERVAL<DV_QUANTITY>','DV_INTERVAL<DV_COUNT>','DV_INTERVAL<DV_PROPORTION>','DV_PERIODIC_TIME_SPECIFICATION','DV_GENERAL_TIME_SPECIFICATION','DV_EHR_URI']:
        return False
    if data_value['_type']=='DV_BOOLEAN':
        if not validate_DV_BOOLEAN(data_value):
            return False
    if data_value['_type']=='DV_STATE':
        if not validate_DV_STATE(data_value):
            return False
    if data_value['_type']=='DV_IDENTIFIER':
        if not validate_DV_IDENTIFIER(data_value):
            return False
    if data_value['_type']=='DV_PARAGRAPH':
        if not validate_DV_PARAGRAPH(data_value):
            return False
    if data_value['_type']=='DV_TEXT':
        if not validate_DV_TEXT(data_value):
            return False
    if data_value['_type']=='DV_INTERVAL':
        if not validate_DV_INTERVAL(data_value):
            return False
    if data_value['_type']=='DV_URI':
        if not validate_DV_URI(data_value):
            return False
    if data_value['_type']=='DV_MULTIMEDIA':
        if not validate_DV_MULTIMEDIA(data_value):
            return False
    if data_value['_type']=='DV_PARSABLE':
        if not validate_DV_PARSABLE(data_value):
            return False
    if data_value['_type']=='DV_CODED_TEXT':
        if not validate_DV_CODED_TEXT(data_value):
            return False
    if data_value['_type']=='DV_ORDINAL':
        if not validate_DV_ORDINAL(data_value):
            return False
    if data_value['_type']=='DV_SCALE':
        if not validate_DV_SCALE(data_value):
            return False
    if data_value['_type']=='DV_PROPORTION':
        if not validate_DV_PROPORTION(data_value):
            return False
    if data_value['_type']=='DV_QUANTITY':
        if not validate_DV_QUANTITY(data_value):
            return False
    if data_value['_type']=='DV_COUNT':
        if not validate_DV_COUNT(data_value):
            return False
    if data_value['_type']=='DV_DURATION':
        if not validate_DV_DURATION(data_value):
            return False
    if data_value['_type']=='DV_DATE':
        if not validate_DV_DATE(data_value):
            return False
    if data_value['_type']=='DV_TIME':
        if not validate_DV_TIME(data_value):
            return False
    if data_value['_type']=='DV_DATE_TIME':
        if not validate_DV_DATE_TIME(data_value):
            return False
    if data_value['_type']=='DV_INTERVAL<DV_DATE_TIME>':
        if not validate_DV_INTERVAL_of_DV_DATE_TIME(data_value):
            return False
    if data_value['_type']=='DV_INTERVAL<DV_DATE>':
        if not validate_DV_INTERVAL_of_DV_DATE(data_value):
            return False
    if data_value['_type']=='DV_INTERVAL<DV_QUANTITY>':
        if not validate_DV_INTERVAL_of_DV_QUANTITY(data_value):
            return False
    if data_value['_type']=='DV_INTERVAL<DV_COUNT>':
        if not validate_DV_INTERVAL_of_DV_COUNT(data_value):
            return False
    if data_value['_type']=='DV_INTERVAL<DV_PROPORTION>':
        if not validate_DV_INTERVAL_of_DV_PROPORTION(data_value):
            return False
    if data_value['_type']=='DV_PERIODIC_TIME_SPECIFICATION':
        if not validate_DV_PERIODIC_TIME_SPECIFICATION(data_value):
            return False
    if data_value['_type']=='DV_GENERAL_TIME_SPECIFICATION':
        if not validate_DV_GENERAL_TIME_SPECIFICATION(data_value):
            return False
    if data_value['_type']=='DV_EHR_URI':
        if not validate_DV_EHR_URI(data_value):
            return False
    return True
def validate_DV_BOOLEAN(dv_boolean):
    if 'value' not in dv_boolean:
        return False
    if not validate_Boolean(dv_boolean['value']):
        return False
    return True
def validate_DV_CODED_TEXT(dv_coded_text):
    if 'value' not in dv_coded_text:
        return False
    if not validate_String(dv_coded_text['value']):
        return False
    if 'hyperlink' in dv_coded_text:
        if not validate_DV_URI(dv_coded_text['hyperlink']):
            return False
    if 'formatting' in dv_coded_text:
        if not validate_String(dv_coded_text['formatting']):
            return False
    if 'mappings' in dv_coded_text:
        if type(dv_coded_text['mappings']) != list:
            return False
        for element in dv_coded_text['mappings']:
            if not validate_TERM_MAPPING(element):
                return False
    if 'language' in dv_coded_text:
        if not validate_CODE_PHRASE(dv_coded_text['language']):
            return False
    if 'encoding' in dv_coded_text:
        if not validate_CODE_PHRASE(dv_coded_text['encoding']):
            return False
    if 'defining_code' not in dv_coded_text:
        return False
    if not validate_CODE_PHRASE(dv_coded_text['defining_code']):
        return False
    return True
def validate_DV_COUNT(dv_count):
    if 'normal_status' in dv_count:
        if not validate_CODE_PHRASE(dv_count['normal_status']):
            return False
    if 'normal_range' in dv_count:
        if not validate_DV_INTERVAL_of_DV_COUNT(dv_count['normal_range']):
            return False
    if 'other_reference_ranges' in dv_count:
        if type(dv_count['other_reference_ranges']) != list:
            return False
        for element in dv_count['other_reference_ranges']:
            if not validate_REFERENCE_RANGE_of_DV_COUNT(element):
                return False
    if 'magnitude_status' in dv_count:
        if not validate_String(dv_count['magnitude_status']):
            return False
    if 'accuracy' in dv_count:
        if not validate_Real(dv_count['accuracy']):
            return False
    if 'accuracy_is_percent' in dv_count:
        if not validate_Boolean(dv_count['accuracy_is_percent']):
            return False
    if 'magnitude' not in dv_count:
        return False
    if not validate_Integer64(dv_count['magnitude']):
        return False
    return True
def validate_DV_DATE(dv_date):
    if 'value' not in dv_date:
        return False
    if not validate_String(dv_date['value']):
        return False
    if 'normal_status' in dv_date:
        if not validate_CODE_PHRASE(dv_date['normal_status']):
            return False
    if 'normal_range' in dv_date:
        if not validate_DV_INTERVAL(dv_date['normal_range']):
            return False
    if 'other_reference_ranges' in dv_date:
        if type(dv_date['other_reference_ranges']) != list:
            return False
        for element in dv_date['other_reference_ranges']:
            if not validate_REFERENCE_RANGE(element):
                return False
    if 'magnitude_status' in dv_date:
        if not validate_String(dv_date['magnitude_status']):
            return False
    if 'accuracy' in dv_date:
        if not validate_DV_DURATION(dv_date['accuracy']):
            return False
    return True
def validate_DV_DATE_TIME(dv_date_time):
    if 'value' not in dv_date_time:
        return False
    if not validate_String(dv_date_time['value']):
        return False
    if 'normal_status' in dv_date_time:
        if not validate_CODE_PHRASE(dv_date_time['normal_status']):
            return False
    if 'normal_range' in dv_date_time:
        if not validate_DV_INTERVAL(dv_date_time['normal_range']):
            return False
    if 'other_reference_ranges' in dv_date_time:
        if type(dv_date_time['other_reference_ranges']) != list:
            return False
        for element in dv_date_time['other_reference_ranges']:
            if not validate_REFERENCE_RANGE(element):
                return False
    if 'magnitude_status' in dv_date_time:
        if not validate_String(dv_date_time['magnitude_status']):
            return False
    if 'accuracy' in dv_date_time:
        if not validate_DV_DURATION(dv_date_time['accuracy']):
            return False
    return True
def validate_DV_DURATION(dv_duration):
    if 'value' not in dv_duration:
        return False
    if not validate_String(dv_duration['value']):
        return False
    if 'normal_status' in dv_duration:
        if not validate_CODE_PHRASE(dv_duration['normal_status']):
            return False
    if 'normal_range' in dv_duration:
        if not validate_DV_INTERVAL(dv_duration['normal_range']):
            return False
    if 'other_reference_ranges' in dv_duration:
        if type(dv_duration['other_reference_ranges']) != list:
            return False
        for element in dv_duration['other_reference_ranges']:
            if not validate_REFERENCE_RANGE(element):
                return False
    if 'magnitude_status' in dv_duration:
        if not validate_String(dv_duration['magnitude_status']):
            return False
    if 'accuracy' in dv_duration:
        if not validate_Real(dv_duration['accuracy']):
            return False
    if 'accuracy_is_percent' in dv_duration:
        if not validate_Boolean(dv_duration['accuracy_is_percent']):
            return False
    return True
def validate_DV_EHR_URI(dv_ehr_uri):
    if 'value' not in dv_ehr_uri:
        return False
    if not validate_String(dv_ehr_uri['value']):
        return False
    return True
def validate_DV_ENCAPSULATED(dv_encapsulated):
    if '_type' not in dv_encapsulated:
        return False
    if dv_encapsulated['_type'] not in ['DV_MULTIMEDIA','DV_PARSABLE']:
        return False
    if 'charset' in dv_encapsulated:
        if not validate_CODE_PHRASE(dv_encapsulated['charset']):
            return False
    if 'language' in dv_encapsulated:
        if not validate_CODE_PHRASE(dv_encapsulated['language']):
            return False
    if dv_encapsulated['_type']=='DV_MULTIMEDIA':
        if not validate_DV_MULTIMEDIA(dv_encapsulated):
            return False
    if dv_encapsulated['_type']=='DV_PARSABLE':
        if not validate_DV_PARSABLE(dv_encapsulated):
            return False
    return True
def validate_DV_GENERAL_TIME_SPECIFICATION(dv_general_time_specification):
    if 'value' not in dv_general_time_specification:
        return False
    if not validate_DV_PARSABLE(dv_general_time_specification['value']):
        return False
    return True
def validate_DV_IDENTIFIER(dv_identifier):
    if 'issuer' in dv_identifier:
        if not validate_String(dv_identifier['issuer']):
            return False
    if 'assigner' in dv_identifier:
        if not validate_String(dv_identifier['assigner']):
            return False
    if 'id' not in dv_identifier:
        return False
    if not validate_String(dv_identifier['id']):
        return False
    if 'type' in dv_identifier:
        if not validate_String(dv_identifier['type']):
            return False
    return True
def validate_DV_INTERVAL(dv_interval):
    if '_type' in dv_interval:
        if dv_interval['_type'] not in ['DV_INTERVAL','DV_INTERVAL<DV_DATE_TIME>','DV_INTERVAL<DV_DATE>','DV_INTERVAL<DV_QUANTITY>','DV_INTERVAL<DV_COUNT>','DV_INTERVAL<DV_PROPORTION>']:
            return False
    if 'lower_unbounded' not in dv_interval:
        return False
    if not validate_Boolean(dv_interval['lower_unbounded']):
        return False
    if 'upper_unbounded' not in dv_interval:
        return False
    if not validate_Boolean(dv_interval['upper_unbounded']):
        return False
    if 'lower_included' not in dv_interval:
        return False
    if not validate_Boolean(dv_interval['lower_included']):
        return False
    if 'upper_included' not in dv_interval:
        return False
    if not validate_Boolean(dv_interval['upper_included']):
        return False
    return True
def validate_DV_INTERVAL_of_DV_COUNT(dv_interval_of_dv_count):
    if 'lower' in dv_interval_of_dv_count:
        if not validate_DV_COUNT(dv_interval_of_dv_count['lower']):
            return False
    if 'upper' in dv_interval_of_dv_count:
        if not validate_DV_COUNT(dv_interval_of_dv_count['upper']):
            return False
    if 'lower_unbounded' not in dv_interval_of_dv_count:
        return False
    if not validate_Boolean(dv_interval_of_dv_count['lower_unbounded']):
        return False
    if 'upper_unbounded' not in dv_interval_of_dv_count:
        return False
    if not validate_Boolean(dv_interval_of_dv_count['upper_unbounded']):
        return False
    if 'lower_included' not in dv_interval_of_dv_count:
        return False
    if not validate_Boolean(dv_interval_of_dv_count['lower_included']):
        return False
    if 'upper_included' not in dv_interval_of_dv_count:
        return False
    if not validate_Boolean(dv_interval_of_dv_count['upper_included']):
        return False
    return True
def validate_DV_INTERVAL_of_DV_DATE(dv_interval_of_dv_date):
    if 'lower_unbounded' not in dv_interval_of_dv_date:
        return False
    if not validate_Boolean(dv_interval_of_dv_date['lower_unbounded']):
        return False
    if 'upper_unbounded' not in dv_interval_of_dv_date:
        return False
    if not validate_Boolean(dv_interval_of_dv_date['upper_unbounded']):
        return False
    if 'lower_included' not in dv_interval_of_dv_date:
        return False
    if not validate_Boolean(dv_interval_of_dv_date['lower_included']):
        return False
    if 'upper_included' not in dv_interval_of_dv_date:
        return False
    if not validate_Boolean(dv_interval_of_dv_date['upper_included']):
        return False
    return True
def validate_DV_INTERVAL_of_DV_DATE_TIME(dv_interval_of_dv_date_time):
    if 'lower' in dv_interval_of_dv_date_time:
        if not validate_DV_DATE_TIME(dv_interval_of_dv_date_time['lower']):
            return False
    if 'upper' in dv_interval_of_dv_date_time:
        if not validate_DV_DATE_TIME(dv_interval_of_dv_date_time['upper']):
            return False
    if 'lower_unbounded' not in dv_interval_of_dv_date_time:
        return False
    if not validate_Boolean(dv_interval_of_dv_date_time['lower_unbounded']):
        return False
    if 'upper_unbounded' not in dv_interval_of_dv_date_time:
        return False
    if not validate_Boolean(dv_interval_of_dv_date_time['upper_unbounded']):
        return False
    if 'lower_included' not in dv_interval_of_dv_date_time:
        return False
    if not validate_Boolean(dv_interval_of_dv_date_time['lower_included']):
        return False
    if 'upper_included' not in dv_interval_of_dv_date_time:
        return False
    if not validate_Boolean(dv_interval_of_dv_date_time['upper_included']):
        return False
    return True
def validate_DV_INTERVAL_of_DV_PROPORTION(dv_interval_of_dv_proportion):
    if 'lower' in dv_interval_of_dv_proportion:
        if not validate_DV_PROPORTION(dv_interval_of_dv_proportion['lower']):
            return False
    if 'upper' in dv_interval_of_dv_proportion:
        if not validate_DV_PROPORTION(dv_interval_of_dv_proportion['upper']):
            return False
    if 'lower_unbounded' not in dv_interval_of_dv_proportion:
        return False
    if not validate_Boolean(dv_interval_of_dv_proportion['lower_unbounded']):
        return False
    if 'upper_unbounded' not in dv_interval_of_dv_proportion:
        return False
    if not validate_Boolean(dv_interval_of_dv_proportion['upper_unbounded']):
        return False
    if 'lower_included' not in dv_interval_of_dv_proportion:
        return False
    if not validate_Boolean(dv_interval_of_dv_proportion['lower_included']):
        return False
    if 'upper_included' not in dv_interval_of_dv_proportion:
        return False
    if not validate_Boolean(dv_interval_of_dv_proportion['upper_included']):
        return False
    return True
def validate_DV_INTERVAL_of_DV_QUANTITY(dv_interval_of_dv_quantity):
    if 'lower' in dv_interval_of_dv_quantity:
        if not validate_DV_QUANTITY(dv_interval_of_dv_quantity['lower']):
            return False
    if 'upper' in dv_interval_of_dv_quantity:
        if not validate_DV_QUANTITY(dv_interval_of_dv_quantity['upper']):
            return False
    if 'lower_unbounded' not in dv_interval_of_dv_quantity:
        return False
    if not validate_Boolean(dv_interval_of_dv_quantity['lower_unbounded']):
        return False
    if 'upper_unbounded' not in dv_interval_of_dv_quantity:
        return False
    if not validate_Boolean(dv_interval_of_dv_quantity['upper_unbounded']):
        return False
    if 'lower_included' not in dv_interval_of_dv_quantity:
        return False
    if not validate_Boolean(dv_interval_of_dv_quantity['lower_included']):
        return False
    if 'upper_included' not in dv_interval_of_dv_quantity:
        return False
    if not validate_Boolean(dv_interval_of_dv_quantity['upper_included']):
        return False
    return True
def validate_DV_MULTIMEDIA(dv_multimedia):
    if 'charset' in dv_multimedia:
        if not validate_CODE_PHRASE(dv_multimedia['charset']):
            return False
    if 'language' in dv_multimedia:
        if not validate_CODE_PHRASE(dv_multimedia['language']):
            return False
    if 'alternate_text' in dv_multimedia:
        if not validate_String(dv_multimedia['alternate_text']):
            return False
    if 'uri' in dv_multimedia:
        if not validate_DV_URI(dv_multimedia['uri']):
            return False
    if 'data' in dv_multimedia:
        if type(dv_multimedia['data']) != list:
            return False
        for element in dv_multimedia['data']:
            if not validate_Character(element):
                return False
    if 'media_type' not in dv_multimedia:
        return False
    if not validate_CODE_PHRASE(dv_multimedia['media_type']):
        return False
    if 'compression_algorithm' in dv_multimedia:
        if not validate_CODE_PHRASE(dv_multimedia['compression_algorithm']):
            return False
    if 'integrity_check' in dv_multimedia:
        if type(dv_multimedia['integrity_check']) != list:
            return False
        for element in dv_multimedia['integrity_check']:
            if not validate_Character(element):
                return False
    if 'integrity_check_algorithm' in dv_multimedia:
        if not validate_CODE_PHRASE(dv_multimedia['integrity_check_algorithm']):
            return False
    if 'thumbnail' in dv_multimedia:
        if not validate_DV_MULTIMEDIA(dv_multimedia['thumbnail']):
            return False
    if 'size' not in dv_multimedia:
        return False
    if not validate_Integer(dv_multimedia['size']):
        return False
    return True
def validate_DV_ORDINAL(dv_ordinal):
    if 'normal_status' in dv_ordinal:
        if not validate_CODE_PHRASE(dv_ordinal['normal_status']):
            return False
    if 'normal_range' in dv_ordinal:
        if not validate_DV_INTERVAL(dv_ordinal['normal_range']):
            return False
    if 'other_reference_ranges' in dv_ordinal:
        if type(dv_ordinal['other_reference_ranges']) != list:
            return False
        for element in dv_ordinal['other_reference_ranges']:
            if not validate_REFERENCE_RANGE(element):
                return False
    if 'symbol' not in dv_ordinal:
        return False
    if not validate_DV_CODED_TEXT(dv_ordinal['symbol']):
        return False
    if 'value' not in dv_ordinal:
        return False
    if not validate_Integer(dv_ordinal['value']):
        return False
    return True
def validate_DV_PARAGRAPH(dv_paragraph):
    if 'items' not in dv_paragraph:
        return False
    if type(dv_paragraph['items']) != list:
        return False
    if len(dv_paragraph['items']) == 0:
        return False
    for element in dv_paragraph['items']:
        if not validate_DV_TEXT(element):
            return False
    return True
def validate_DV_PARSABLE(dv_parsable):
    if 'charset' in dv_parsable:
        if not validate_CODE_PHRASE(dv_parsable['charset']):
            return False
    if 'language' in dv_parsable:
        if not validate_CODE_PHRASE(dv_parsable['language']):
            return False
    if 'value' not in dv_parsable:
        return False
    if not validate_String(dv_parsable['value']):
        return False
    if 'formalism' not in dv_parsable:
        return False
    if not validate_String(dv_parsable['formalism']):
        return False
    return True
def validate_DV_PERIODIC_TIME_SPECIFICATION(dv_periodic_time_specification):
    if 'value' not in dv_periodic_time_specification:
        return False
    if not validate_DV_PARSABLE(dv_periodic_time_specification['value']):
        return False
    return True
def validate_DV_PROPORTION(dv_proportion):
    if 'normal_status' in dv_proportion:
        if not validate_CODE_PHRASE(dv_proportion['normal_status']):
            return False
    if 'normal_range' in dv_proportion:
        if not validate_DV_INTERVAL_of_DV_PROPORTION(dv_proportion['normal_range']):
            return False
    if 'other_reference_ranges' in dv_proportion:
        if type(dv_proportion['other_reference_ranges']) != list:
            return False
        for element in dv_proportion['other_reference_ranges']:
            if not validate_REFERENCE_RANGE_of_DV_PROPORTION(element):
                return False
    if 'magnitude_status' in dv_proportion:
        if not validate_String(dv_proportion['magnitude_status']):
            return False
    if 'accuracy' in dv_proportion:
        if not validate_Real(dv_proportion['accuracy']):
            return False
    if 'accuracy_is_percent' in dv_proportion:
        if not validate_Boolean(dv_proportion['accuracy_is_percent']):
            return False
    if 'numerator' not in dv_proportion:
        return False
    if not validate_Real(dv_proportion['numerator']):
        return False
    if 'denominator' not in dv_proportion:
        return False
    if not validate_Real(dv_proportion['denominator']):
        return False
    if 'type' not in dv_proportion:
        return False
    if not validate_Integer(dv_proportion['type']):
        return False
    if 'precision' in dv_proportion:
        if not validate_Integer(dv_proportion['precision']):
            return False
    return True
def validate_DV_QUANTITY(dv_quantity):
    if 'normal_status' in dv_quantity:
        if not validate_CODE_PHRASE(dv_quantity['normal_status']):
            return False
    if 'normal_range' in dv_quantity:
        if not validate_DV_INTERVAL_of_DV_QUANTITY(dv_quantity['normal_range']):
            return False
    if 'other_reference_ranges' in dv_quantity:
        if type(dv_quantity['other_reference_ranges']) != list:
            return False
        for element in dv_quantity['other_reference_ranges']:
            if not validate_REFERENCE_RANGE_of_DV_QUANTITY(element):
                return False
    if 'magnitude_status' in dv_quantity:
        if not validate_String(dv_quantity['magnitude_status']):
            return False
    if 'accuracy' in dv_quantity:
        if not validate_Real(dv_quantity['accuracy']):
            return False
    if 'accuracy_is_percent' in dv_quantity:
        if not validate_Boolean(dv_quantity['accuracy_is_percent']):
            return False
    if 'magnitude' not in dv_quantity:
        return False
    if not validate_Real(dv_quantity['magnitude']):
        return False
    if 'precision' in dv_quantity:
        if not validate_Integer(dv_quantity['precision']):
            return False
    if 'units' not in dv_quantity:
        return False
    if not validate_String(dv_quantity['units']):
        return False
    if 'units_system' in dv_quantity:
        if not validate_String(dv_quantity['units_system']):
            return False
    if 'units_display_name' in dv_quantity:
        if not validate_String(dv_quantity['units_display_name']):
            return False
    return True
def validate_DV_SCALE(dv_scale):
    if 'normal_status' in dv_scale:
        if not validate_CODE_PHRASE(dv_scale['normal_status']):
            return False
    if 'normal_range' in dv_scale:
        if not validate_DV_INTERVAL(dv_scale['normal_range']):
            return False
    if 'other_reference_ranges' in dv_scale:
        if type(dv_scale['other_reference_ranges']) != list:
            return False
        for element in dv_scale['other_reference_ranges']:
            if not validate_REFERENCE_RANGE(element):
                return False
    if 'symbol' not in dv_scale:
        return False
    if not validate_DV_CODED_TEXT(dv_scale['symbol']):
        return False
    if 'value' not in dv_scale:
        return False
    if not validate_Real(dv_scale['value']):
        return False
    return True
def validate_DV_STATE(dv_state):
    if 'value' not in dv_state:
        return False
    if not validate_DV_CODED_TEXT(dv_state['value']):
        return False
    if 'is_terminal' not in dv_state:
        return False
    if not validate_Boolean(dv_state['is_terminal']):
        return False
    return True
def validate_DV_TEXT(dv_text):
    if '_type' in dv_text:
        if dv_text['_type'] not in ['DV_TEXT','DV_CODED_TEXT']:
            return False
    if 'value' not in dv_text:
        return False
    if not validate_String(dv_text['value']):
        return False
    if 'hyperlink' in dv_text:
        if not validate_DV_URI(dv_text['hyperlink']):
            return False
    if 'formatting' in dv_text:
        if not validate_String(dv_text['formatting']):
            return False
    if 'mappings' in dv_text:
        if type(dv_text['mappings']) != list:
            return False
        for element in dv_text['mappings']:
            if not validate_TERM_MAPPING(element):
                return False
    if 'language' in dv_text:
        if not validate_CODE_PHRASE(dv_text['language']):
            return False
    if 'encoding' in dv_text:
        if not validate_CODE_PHRASE(dv_text['encoding']):
            return False
    return True
def validate_DV_TIME(dv_time):
    if 'value' not in dv_time:
        return False
    if not validate_String(dv_time['value']):
        return False
    if 'normal_status' in dv_time:
        if not validate_CODE_PHRASE(dv_time['normal_status']):
            return False
    if 'normal_range' in dv_time:
        if not validate_DV_INTERVAL(dv_time['normal_range']):
            return False
    if 'other_reference_ranges' in dv_time:
        if type(dv_time['other_reference_ranges']) != list:
            return False
        for element in dv_time['other_reference_ranges']:
            if not validate_REFERENCE_RANGE(element):
                return False
    if 'magnitude_status' in dv_time:
        if not validate_String(dv_time['magnitude_status']):
            return False
    if 'accuracy' in dv_time:
        if not validate_DV_DURATION(dv_time['accuracy']):
            return False
    return True
def validate_DV_URI(dv_uri):
    if '_type' in dv_uri:
        if dv_uri['_type'] not in ['DV_URI','DV_EHR_URI']:
            return False
    if 'value' not in dv_uri:
        return False
    if not validate_String(dv_uri['value']):
        return False
    return True
def validate_ELEMENT(element):
    if 'name' not in element:
        return False
    if not validate_DV_TEXT(element['name']):
        return False
    if 'archetype_node_id' not in element:
        return False
    if not validate_String(element['archetype_node_id']):
        return False
    if 'uid' in element:
        if not validate_UID_BASED_ID(element['uid']):
            return False
    if 'links' in element:
        if type(element['links']) != list:
            return False
        for element in element['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in element:
        if not validate_ARCHETYPED(element['archetype_details']):
            return False
    if 'feeder_audit' in element:
        if not validate_FEEDER_AUDIT(element['feeder_audit']):
            return False
    if 'null_flavour' in element:
        if not validate_DV_CODED_TEXT(element['null_flavour']):
            return False
    if 'value' in element:
        if not validate_DATA_VALUE(element['value']):
            return False
    if 'null_reason' in element:
        if not validate_DV_TEXT(element['null_reason']):
            return False
    return True
def validate_FEEDER_AUDIT(feeder_audit):
    if 'originating_system_item_ids' in feeder_audit:
        if type(feeder_audit['originating_system_item_ids']) != list:
            return False
        for element in feeder_audit['originating_system_item_ids']:
            if not validate_DV_IDENTIFIER(element):
                return False
    if 'feeder_system_item_ids' in feeder_audit:
        if type(feeder_audit['feeder_system_item_ids']) != list:
            return False
        for element in feeder_audit['feeder_system_item_ids']:
            if not validate_DV_IDENTIFIER(element):
                return False
    if 'original_content' in feeder_audit:
        if not validate_DV_ENCAPSULATED(feeder_audit['original_content']):
            return False
    if 'originating_system_audit' not in feeder_audit:
        return False
    if not validate_FEEDER_AUDIT_DETAILS(feeder_audit['originating_system_audit']):
        return False
    if 'feeder_system_audit' in feeder_audit:
        if not validate_FEEDER_AUDIT_DETAILS(feeder_audit['feeder_system_audit']):
            return False
    return True
def validate_FEEDER_AUDIT_DETAILS(feeder_audit_details):
    if 'system_id' not in feeder_audit_details:
        return False
    if not validate_String(feeder_audit_details['system_id']):
        return False
    if 'location' in feeder_audit_details:
        if not validate_PARTY_IDENTIFIED(feeder_audit_details['location']):
            return False
    if 'subject' in feeder_audit_details:
        if not validate_PARTY_PROXY(feeder_audit_details['subject']):
            return False
    if 'provider' in feeder_audit_details:
        if not validate_PARTY_IDENTIFIED(feeder_audit_details['provider']):
            return False
    if 'time' in feeder_audit_details:
        if not validate_DV_DATE_TIME(feeder_audit_details['time']):
            return False
    if 'version_id' in feeder_audit_details:
        if not validate_String(feeder_audit_details['version_id']):
            return False
    if 'other_details' in feeder_audit_details:
        if not validate_ITEM_STRUCTURE(feeder_audit_details['other_details']):
            return False
    return True
def validate_GENERIC_ID(generic_id):
    if 'value' not in generic_id:
        return False
    if not validate_String(generic_id['value']):
        return False
    if 'scheme' not in generic_id:
        return False
    if not validate_String(generic_id['scheme']):
        return False
    return True
def validate_GROUP(group):
    if 'name' not in group:
        return False
    if not validate_DV_TEXT(group['name']):
        return False
    if 'archetype_node_id' not in group:
        return False
    if not validate_String(group['archetype_node_id']):
        return False
    if 'uid' in group:
        if not validate_UID_BASED_ID(group['uid']):
            return False
    if 'links' in group:
        if type(group['links']) != list:
            return False
        for element in group['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in group:
        if not validate_ARCHETYPED(group['archetype_details']):
            return False
    if 'feeder_audit' in group:
        if not validate_FEEDER_AUDIT(group['feeder_audit']):
            return False
    if 'identities' not in group:
        return False
    if type(group['identities']) != list:
        return False
    if len(group['identities']) == 0:
        return False
    for element in group['identities']:
        if not validate_PARTY_IDENTITY(element):
            return False
    if 'contacts' in group:
        if type(group['contacts']) != list:
            return False
        for element in group['contacts']:
            if not validate_CONTACT(element):
                return False
    if 'details' in group:
        if not validate_ITEM_STRUCTURE(group['details']):
            return False
    if 'reverse_relationships' in group:
        if type(group['reverse_relationships']) != list:
            return False
        for element in group['reverse_relationships']:
            if not validate_PARTY_RELATIONSHIP(element):
                return False
    if 'relationships' in group:
        if type(group['relationships']) != list:
            return False
        for element in group['relationships']:
            if not validate_PARTY_RELATIONSHIP(element):
                return False
    if 'languages' in group:
        if type(group['languages']) != list:
            return False
        for element in group['languages']:
            if not validate_DV_TEXT(element):
                return False
    if 'roles' in group:
        if type(group['roles']) != list:
            return False
        for element in group['roles']:
            if not validate_ROLE(element):
                return False
    return True
def validate_HIER_OBJECT_ID(hier_object_id):
    if 'value' not in hier_object_id:
        return False
    if not validate_String(hier_object_id['value']):
        return False
    return True
def validate_ITEM(item):
    if '_type' not in item:
        return False
    if item['_type'] not in ['CLUSTER','ELEMENT']:
        return False
    if 'name' not in item:
        return False
    if not validate_DV_TEXT(item['name']):
        return False
    if 'archetype_node_id' not in item:
        return False
    if not validate_String(item['archetype_node_id']):
        return False
    if 'uid' in item:
        if not validate_UID_BASED_ID(item['uid']):
            return False
    if 'links' in item:
        if type(item['links']) != list:
            return False
        for element in item['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in item:
        if not validate_ARCHETYPED(item['archetype_details']):
            return False
    if 'feeder_audit' in item:
        if not validate_FEEDER_AUDIT(item['feeder_audit']):
            return False
    if item['_type']=='CLUSTER':
        if not validate_CLUSTER(item):
            return False
    if item['_type']=='ELEMENT':
        if not validate_ELEMENT(item):
            return False
    return True
def validate_ITEM_LIST(item_list):
    if 'name' not in item_list:
        return False
    if not validate_DV_TEXT(item_list['name']):
        return False
    if 'archetype_node_id' not in item_list:
        return False
    if not validate_String(item_list['archetype_node_id']):
        return False
    if 'uid' in item_list:
        if not validate_UID_BASED_ID(item_list['uid']):
            return False
    if 'links' in item_list:
        if type(item_list['links']) != list:
            return False
        for element in item_list['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in item_list:
        if not validate_ARCHETYPED(item_list['archetype_details']):
            return False
    if 'feeder_audit' in item_list:
        if not validate_FEEDER_AUDIT(item_list['feeder_audit']):
            return False
    if 'items' in item_list:
        if type(item_list['items']) != list:
            return False
        for element in item_list['items']:
            if not validate_ELEMENT(element):
                return False
    return True
def validate_ITEM_SINGLE(item_single):
    if 'name' not in item_single:
        return False
    if not validate_DV_TEXT(item_single['name']):
        return False
    if 'archetype_node_id' not in item_single:
        return False
    if not validate_String(item_single['archetype_node_id']):
        return False
    if 'uid' in item_single:
        if not validate_UID_BASED_ID(item_single['uid']):
            return False
    if 'links' in item_single:
        if type(item_single['links']) != list:
            return False
        for element in item_single['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in item_single:
        if not validate_ARCHETYPED(item_single['archetype_details']):
            return False
    if 'feeder_audit' in item_single:
        if not validate_FEEDER_AUDIT(item_single['feeder_audit']):
            return False
    if 'item' not in item_single:
        return False
    if not validate_ELEMENT(item_single['item']):
        return False
    return True
def validate_ITEM_STRUCTURE(item_structure):
    if '_type' not in item_structure:
        return False
    if item_structure['_type'] not in ['ITEM_TREE','ITEM_SINGLE','ITEM_TABLE','ITEM_LIST']:
        return False
    if 'name' not in item_structure:
        return False
    if not validate_DV_TEXT(item_structure['name']):
        return False
    if 'archetype_node_id' not in item_structure:
        return False
    if not validate_String(item_structure['archetype_node_id']):
        return False
    if 'uid' in item_structure:
        if not validate_UID_BASED_ID(item_structure['uid']):
            return False
    if 'links' in item_structure:
        if type(item_structure['links']) != list:
            return False
        for element in item_structure['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in item_structure:
        if not validate_ARCHETYPED(item_structure['archetype_details']):
            return False
    if 'feeder_audit' in item_structure:
        if not validate_FEEDER_AUDIT(item_structure['feeder_audit']):
            return False
    if item_structure['_type']=='ITEM_TREE':
        if not validate_ITEM_TREE(item_structure):
            return False
    if item_structure['_type']=='ITEM_SINGLE':
        if not validate_ITEM_SINGLE(item_structure):
            return False
    if item_structure['_type']=='ITEM_TABLE':
        if not validate_ITEM_TABLE(item_structure):
            return False
    if item_structure['_type']=='ITEM_LIST':
        if not validate_ITEM_LIST(item_structure):
            return False
    return True
def validate_ITEM_TABLE(item_table):
    if 'name' not in item_table:
        return False
    if not validate_DV_TEXT(item_table['name']):
        return False
    if 'archetype_node_id' not in item_table:
        return False
    if not validate_String(item_table['archetype_node_id']):
        return False
    if 'uid' in item_table:
        if not validate_UID_BASED_ID(item_table['uid']):
            return False
    if 'links' in item_table:
        if type(item_table['links']) != list:
            return False
        for element in item_table['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in item_table:
        if not validate_ARCHETYPED(item_table['archetype_details']):
            return False
    if 'feeder_audit' in item_table:
        if not validate_FEEDER_AUDIT(item_table['feeder_audit']):
            return False
    if 'rows' in item_table:
        if type(item_table['rows']) != list:
            return False
        for element in item_table['rows']:
            if not validate_CLUSTER(element):
                return False
    return True
def validate_ITEM_TREE(item_tree):
    if 'name' not in item_tree:
        return False
    if not validate_DV_TEXT(item_tree['name']):
        return False
    if 'archetype_node_id' not in item_tree:
        return False
    if not validate_String(item_tree['archetype_node_id']):
        return False
    if 'uid' in item_tree:
        if not validate_UID_BASED_ID(item_tree['uid']):
            return False
    if 'links' in item_tree:
        if type(item_tree['links']) != list:
            return False
        for element in item_tree['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in item_tree:
        if not validate_ARCHETYPED(item_tree['archetype_details']):
            return False
    if 'feeder_audit' in item_tree:
        if not validate_FEEDER_AUDIT(item_tree['feeder_audit']):
            return False
    if 'items' in item_tree:
        if type(item_tree['items']) != list:
            return False
        for element in item_tree['items']:
            if not validate_ITEM(element):
                return False
    return True
def validate_LINK(link):
    if 'meaning' not in link:
        return False
    if not validate_DV_TEXT(link['meaning']):
        return False
    if 'type' not in link:
        return False
    if not validate_DV_TEXT(link['type']):
        return False
    if 'target' not in link:
        return False
    if not validate_DV_EHR_URI(link['target']):
        return False
    return True
def validate_OBJECT_ID(object_id):
    if '_type' not in object_id:
        return False
    if object_id['_type'] not in ['ARCHETYPE_ID','GENERIC_ID','TERMINOLOGY_ID','TEMPLATE_ID','HIER_OBJECT_ID','OBJECT_VERSION_ID']:
        return False
    if 'value' not in object_id:
        return False
    if not validate_String(object_id['value']):
        return False
    if object_id['_type']=='ARCHETYPE_ID':
        if not validate_ARCHETYPE_ID(object_id):
            return False
    if object_id['_type']=='GENERIC_ID':
        if not validate_GENERIC_ID(object_id):
            return False
    if object_id['_type']=='TERMINOLOGY_ID':
        if not validate_TERMINOLOGY_ID(object_id):
            return False
    if object_id['_type']=='TEMPLATE_ID':
        if not validate_TEMPLATE_ID(object_id):
            return False
    if object_id['_type']=='HIER_OBJECT_ID':
        if not validate_HIER_OBJECT_ID(object_id):
            return False
    if object_id['_type']=='OBJECT_VERSION_ID':
        if not validate_OBJECT_VERSION_ID(object_id):
            return False
    return True
def validate_OBJECT_VERSION_ID(object_version_id):
    if 'value' not in object_version_id:
        return False
    if not validate_String(object_version_id['value']):
        return False
    return True
def validate_ORGANISATION(organisation):
    if 'name' not in organisation:
        return False
    if not validate_DV_TEXT(organisation['name']):
        return False
    if 'archetype_node_id' not in organisation:
        return False
    if not validate_String(organisation['archetype_node_id']):
        return False
    if 'uid' in organisation:
        if not validate_UID_BASED_ID(organisation['uid']):
            return False
    if 'links' in organisation:
        if type(organisation['links']) != list:
            return False
        for element in organisation['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in organisation:
        if not validate_ARCHETYPED(organisation['archetype_details']):
            return False
    if 'feeder_audit' in organisation:
        if not validate_FEEDER_AUDIT(organisation['feeder_audit']):
            return False
    if 'identities' not in organisation:
        return False
    if type(organisation['identities']) != list:
        return False
    if len(organisation['identities']) == 0:
        return False
    for element in organisation['identities']:
        if not validate_PARTY_IDENTITY(element):
            return False
    if 'contacts' in organisation:
        if type(organisation['contacts']) != list:
            return False
        for element in organisation['contacts']:
            if not validate_CONTACT(element):
                return False
    if 'details' in organisation:
        if not validate_ITEM_STRUCTURE(organisation['details']):
            return False
    if 'reverse_relationships' in organisation:
        if type(organisation['reverse_relationships']) != list:
            return False
        for element in organisation['reverse_relationships']:
            if not validate_PARTY_RELATIONSHIP(element):
                return False
    if 'relationships' in organisation:
        if type(organisation['relationships']) != list:
            return False
        for element in organisation['relationships']:
            if not validate_PARTY_RELATIONSHIP(element):
                return False
    if 'languages' in organisation:
        if type(organisation['languages']) != list:
            return False
        for element in organisation['languages']:
            if not validate_DV_TEXT(element):
                return False
    if 'roles' in organisation:
        if type(organisation['roles']) != list:
            return False
        for element in organisation['roles']:
            if not validate_ROLE(element):
                return False
    return True
def validate_PARTY(party):
    if '_type' not in party:
        return False
    if party['_type'] not in ['ROLE','AGENT','ORGANISATION','GROUP','PERSON']:
        return False
    if 'name' not in party:
        return False
    if not validate_DV_TEXT(party['name']):
        return False
    if 'archetype_node_id' not in party:
        return False
    if not validate_String(party['archetype_node_id']):
        return False
    if 'uid' in party:
        if not validate_UID_BASED_ID(party['uid']):
            return False
    if 'links' in party:
        if type(party['links']) != list:
            return False
        for element in party['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in party:
        if not validate_ARCHETYPED(party['archetype_details']):
            return False
    if 'feeder_audit' in party:
        if not validate_FEEDER_AUDIT(party['feeder_audit']):
            return False
    if 'identities' not in party:
        return False
    if type(party['identities']) != list:
        return False
    if len(party['identities']) == 0:
        return False
    for element in party['identities']:
        if not validate_PARTY_IDENTITY(element):
            return False
    if 'contacts' in party:
        if type(party['contacts']) != list:
            return False
        for element in party['contacts']:
            if not validate_CONTACT(element):
                return False
    if 'details' in party:
        if not validate_ITEM_STRUCTURE(party['details']):
            return False
    if 'reverse_relationships' in party:
        if type(party['reverse_relationships']) != list:
            return False
        for element in party['reverse_relationships']:
            if not validate_PARTY_RELATIONSHIP(element):
                return False
    if 'relationships' in party:
        if type(party['relationships']) != list:
            return False
        for element in party['relationships']:
            if not validate_PARTY_RELATIONSHIP(element):
                return False
    if party['_type']=='ROLE':
        if not validate_ROLE(party):
            return False
    if party['_type']=='AGENT':
        if not validate_AGENT(party):
            return False
    if party['_type']=='ORGANISATION':
        if not validate_ORGANISATION(party):
            return False
    if party['_type']=='GROUP':
        if not validate_GROUP(party):
            return False
    if party['_type']=='PERSON':
        if not validate_PERSON(party):
            return False
    return True
def validate_PARTY_IDENTIFIED(party_identified):
    if '_type' in party_identified:
        if party_identified['_type'] not in ['PARTY_IDENTIFIED','PARTY_RELATED']:
            return False
    if 'external_ref' in party_identified:
        if not validate_PARTY_REF(party_identified['external_ref']):
            return False
    if 'name' in party_identified:
        if not validate_String(party_identified['name']):
            return False
    if 'identifiers' in party_identified:
        if type(party_identified['identifiers']) != list:
            return False
        for element in party_identified['identifiers']:
            if not validate_DV_IDENTIFIER(element):
                return False
    return True
def validate_PARTY_IDENTITY(party_identity):
    if 'name' not in party_identity:
        return False
    if not validate_DV_TEXT(party_identity['name']):
        return False
    if 'archetype_node_id' not in party_identity:
        return False
    if not validate_String(party_identity['archetype_node_id']):
        return False
    if 'uid' in party_identity:
        if not validate_UID_BASED_ID(party_identity['uid']):
            return False
    if 'links' in party_identity:
        if type(party_identity['links']) != list:
            return False
        for element in party_identity['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in party_identity:
        if not validate_ARCHETYPED(party_identity['archetype_details']):
            return False
    if 'feeder_audit' in party_identity:
        if not validate_FEEDER_AUDIT(party_identity['feeder_audit']):
            return False
    if 'details' not in party_identity:
        return False
    if not validate_ITEM_STRUCTURE(party_identity['details']):
        return False
    return True
def validate_PARTY_PROXY(party_proxy):
    if '_type' not in party_proxy:
        return False
    if party_proxy['_type'] not in ['PARTY_IDENTIFIED','PARTY_SELF','PARTY_RELATED']:
        return False
    if 'external_ref' in party_proxy:
        if not validate_PARTY_REF(party_proxy['external_ref']):
            return False
    if party_proxy['_type']=='PARTY_IDENTIFIED':
        if not validate_PARTY_IDENTIFIED(party_proxy):
            return False
    if party_proxy['_type']=='PARTY_SELF':
        if not validate_PARTY_SELF(party_proxy):
            return False
    if party_proxy['_type']=='PARTY_RELATED':
        if not validate_PARTY_RELATED(party_proxy):
            return False
    return True
def validate_PARTY_REF(party_ref):
    if 'namespace' not in party_ref:
        return False
    if not validate_String(party_ref['namespace']):
        return False
    if 'type' not in party_ref:
        return False
    if not validate_String(party_ref['type']):
        return False
    if 'id' not in party_ref:
        return False
    if not validate_OBJECT_ID(party_ref['id']):
        return False
    return True
def validate_PARTY_RELATED(party_related):
    if 'external_ref' in party_related:
        if not validate_PARTY_REF(party_related['external_ref']):
            return False
    if 'name' in party_related:
        if not validate_String(party_related['name']):
            return False
    if 'identifiers' in party_related:
        if type(party_related['identifiers']) != list:
            return False
        for element in party_related['identifiers']:
            if not validate_DV_IDENTIFIER(element):
                return False
    if 'relationship' not in party_related:
        return False
    if not validate_DV_CODED_TEXT(party_related['relationship']):
        return False
    return True
def validate_PARTY_RELATIONSHIP(party_relationship):
    if 'name' not in party_relationship:
        return False
    if not validate_DV_TEXT(party_relationship['name']):
        return False
    if 'archetype_node_id' not in party_relationship:
        return False
    if not validate_String(party_relationship['archetype_node_id']):
        return False
    if 'uid' in party_relationship:
        if not validate_UID_BASED_ID(party_relationship['uid']):
            return False
    if 'links' in party_relationship:
        if type(party_relationship['links']) != list:
            return False
        for element in party_relationship['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in party_relationship:
        if not validate_ARCHETYPED(party_relationship['archetype_details']):
            return False
    if 'feeder_audit' in party_relationship:
        if not validate_FEEDER_AUDIT(party_relationship['feeder_audit']):
            return False
    if 'details' in party_relationship:
        if not validate_ITEM_STRUCTURE(party_relationship['details']):
            return False
    if 'target' not in party_relationship:
        return False
    if not validate_PARTY(party_relationship['target']):
        return False
    if 'time_validity' in party_relationship:
        if not validate_DV_INTERVAL_of_DV_DATE(party_relationship['time_validity']):
            return False
    if 'source' not in party_relationship:
        return False
    if not validate_PARTY(party_relationship['source']):
        return False
    return True
def validate_PARTY_SELF(party_self):
    if 'external_ref' in party_self:
        if not validate_PARTY_REF(party_self['external_ref']):
            return False
    return True
def validate_PERSON(person):
    if 'name' not in person:
        return False
    if not validate_DV_TEXT(person['name']):
        return False
    if 'archetype_node_id' not in person:
        return False
    if not validate_String(person['archetype_node_id']):
        return False
    if 'uid' in person:
        if not validate_UID_BASED_ID(person['uid']):
            return False
    if 'links' in person:
        if type(person['links']) != list:
            return False
        for element in person['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in person:
        if not validate_ARCHETYPED(person['archetype_details']):
            return False
    if 'feeder_audit' in person:
        if not validate_FEEDER_AUDIT(person['feeder_audit']):
            return False
    if 'identities' not in person:
        return False
    if type(person['identities']) != list:
        return False
    if len(person['identities']) == 0:
        return False
    for element in person['identities']:
        if not validate_PARTY_IDENTITY(element):
            return False
    if 'contacts' in person:
        if type(person['contacts']) != list:
            return False
        for element in person['contacts']:
            if not validate_CONTACT(element):
                return False
    if 'details' in person:
        if not validate_ITEM_STRUCTURE(person['details']):
            return False
    if 'reverse_relationships' in person:
        if type(person['reverse_relationships']) != list:
            return False
        for element in person['reverse_relationships']:
            if not validate_PARTY_RELATIONSHIP(element):
                return False
    if 'relationships' in person:
        if type(person['relationships']) != list:
            return False
        for element in person['relationships']:
            if not validate_PARTY_RELATIONSHIP(element):
                return False
    if 'languages' in person:
        if type(person['languages']) != list:
            return False
        for element in person['languages']:
            if not validate_DV_TEXT(element):
                return False
    if 'roles' in person:
        if type(person['roles']) != list:
            return False
        for element in person['roles']:
            if not validate_ROLE(element):
                return False
    return True
def validate_REFERENCE_RANGE(reference_range):
    if '_type' in reference_range:
        if reference_range['_type'] not in ['REFERENCE_RANGE','REFERENCE_RANGE<DV_QUANTITY>','REFERENCE_RANGE<DV_COUNT>','REFERENCE_RANGE<DV_PROPORTION>','REFERENCE_RANGE<DV_ORDINAL>']:
            return False
    if 'meaning' not in reference_range:
        return False
    if not validate_DV_TEXT(reference_range['meaning']):
        return False
    if 'range' not in reference_range:
        return False
    if not validate_DV_INTERVAL(reference_range['range']):
        return False
    return True
def validate_REFERENCE_RANGE_of_DV_COUNT(reference_range_of_dv_count):
    if 'meaning' not in reference_range_of_dv_count:
        return False
    if not validate_DV_TEXT(reference_range_of_dv_count['meaning']):
        return False
    if 'range' not in reference_range_of_dv_count:
        return False
    if not validate_DV_INTERVAL(reference_range_of_dv_count['range']):
        return False
    return True
def validate_REFERENCE_RANGE_of_DV_PROPORTION(reference_range_of_dv_proportion):
    if 'meaning' not in reference_range_of_dv_proportion:
        return False
    if not validate_DV_TEXT(reference_range_of_dv_proportion['meaning']):
        return False
    if 'range' not in reference_range_of_dv_proportion:
        return False
    if not validate_DV_INTERVAL(reference_range_of_dv_proportion['range']):
        return False
    return True
def validate_REFERENCE_RANGE_of_DV_QUANTITY(reference_range_of_dv_quantity):
    if 'meaning' not in reference_range_of_dv_quantity:
        return False
    if not validate_DV_TEXT(reference_range_of_dv_quantity['meaning']):
        return False
    if 'range' not in reference_range_of_dv_quantity:
        return False
    if not validate_DV_INTERVAL(reference_range_of_dv_quantity['range']):
        return False
    return True
def validate_ROLE(role):
    if 'name' not in role:
        return False
    if not validate_DV_TEXT(role['name']):
        return False
    if 'archetype_node_id' not in role:
        return False
    if not validate_String(role['archetype_node_id']):
        return False
    if 'uid' in role:
        if not validate_UID_BASED_ID(role['uid']):
            return False
    if 'links' in role:
        if type(role['links']) != list:
            return False
        for element in role['links']:
            if not validate_LINK(element):
                return False
    if 'archetype_details' in role:
        if not validate_ARCHETYPED(role['archetype_details']):
            return False
    if 'feeder_audit' in role:
        if not validate_FEEDER_AUDIT(role['feeder_audit']):
            return False
    if 'identities' not in role:
        return False
    if type(role['identities']) != list:
        return False
    if len(role['identities']) == 0:
        return False
    for element in role['identities']:
        if not validate_PARTY_IDENTITY(element):
            return False
    if 'contacts' in role:
        if type(role['contacts']) != list:
            return False
        for element in role['contacts']:
            if not validate_CONTACT(element):
                return False
    if 'details' in role:
        if not validate_ITEM_STRUCTURE(role['details']):
            return False
    if 'reverse_relationships' in role:
        if type(role['reverse_relationships']) != list:
            return False
        for element in role['reverse_relationships']:
            if not validate_PARTY_RELATIONSHIP(element):
                return False
    if 'relationships' in role:
        if type(role['relationships']) != list:
            return False
        for element in role['relationships']:
            if not validate_PARTY_RELATIONSHIP(element):
                return False
    if 'time_validity' in role:
        if not validate_DV_INTERVAL_of_DV_DATE(role['time_validity']):
            return False
    if 'performer' not in role:
        return False
    if not validate_ACTOR(role['performer']):
        return False
    if 'capabilities' in role:
        if type(role['capabilities']) != list:
            return False
        for element in role['capabilities']:
            if not validate_CAPABILITY(element):
                return False
    return True
def validate_TEMPLATE_ID(template_id):
    if 'value' not in template_id:
        return False
    if not validate_String(template_id['value']):
        return False
    return True
def validate_TERMINOLOGY_ID(terminology_id):
    if 'value' not in terminology_id:
        return False
    if not validate_String(terminology_id['value']):
        return False
    return True
def validate_TERM_MAPPING(term_mapping):
    if 'match' not in term_mapping:
        return False
    if not validate_Character(term_mapping['match']):
        return False
    if 'purpose' in term_mapping:
        if not validate_DV_CODED_TEXT(term_mapping['purpose']):
            return False
    if 'target' not in term_mapping:
        return False
    if not validate_CODE_PHRASE(term_mapping['target']):
        return False
    return True
def validate_UID_BASED_ID(uid_based_id):
    if '_type' not in uid_based_id:
        return False
    if uid_based_id['_type'] not in ['HIER_OBJECT_ID','OBJECT_VERSION_ID']:
        return False
    if 'value' not in uid_based_id:
        return False
    if not validate_String(uid_based_id['value']):
        return False
    if uid_based_id['_type']=='HIER_OBJECT_ID':
        if not validate_HIER_OBJECT_ID(uid_based_id):
            return False
    if uid_based_id['_type']=='OBJECT_VERSION_ID':
        if not validate_OBJECT_VERSION_ID(uid_based_id):
            return False
    return True
def validate_String(parameter):
    return type(parameter) == str
def validate_Character(parameter):
    return type(parameter)==str and len(parameter)==1
def validate_Boolean(parameter):
    return type(parameter)==bool
def validate_Double(parameter):
    return type(parameter)==float or type(parameter)==int
def validate_Integer(parameter):
    return type(parameter)==int
def validate_Integer64(parameter):
    return type(parameter)==int
def validate_Real(parameter):
    return type(parameter)==float or type(parameter)==int
