# *************************************
# SpeedCollect
# Web Service
# 'collections_utilities.py'
# Author: Juan Carlos Juárez
# Contact: speedcollect@outlook.com
# *************************************

import utilities.constants as constants
import re

def valid_collection_name(collection_name) -> bool:

    # Validate that 'collection_name' is a string
    if(type(collection_name) != str): return False
    
    # Validate 'collection_name' according to alphanumeric or underscore characters between the minumum and maximum size for a collection_name
    collection_name_pattern_string = "^[a-zA-Z0-9_]{{{0},{1}}}$".format(constants.MIN_COLLECTION_NAME_SIZE, constants.MAX_COLLECTION_NAME_SIZE)
    collection_name_pattern = re.compile(collection_name_pattern_string)
    if(not collection_name_pattern.match(collection_name)): return False
    
    # 'collection_name' is acceptable
    return True

def valid_collection_type(collection_type) -> bool:

    # Validate that 'collection_type' is a string
    if(type(collection_type) != str): return False
    
    # Validate 'collection_type' according to any characters between the minum and maximum size for a collection_type
    collection_type_pattern_string = "^.{{{0},{1}}}$".format(constants.MIN_COLLECTION_TYPE_SIZE, constants.MAX_COLLECTION_TYPE_SIZE)
    collection_type_pattern = re.compile(collection_type_pattern_string)
    if(not collection_type_pattern.match(collection_type)): return False
    
    # 'collection_type' is acceptable
    return True

def valid_collection_description(collection_description) -> bool:

    # Validate that 'collection_description' is a string
    if(type(collection_description) != str): return False
    
    # Validate 'collection_description' according to any characters between the minum and maximum size for a collection_description
    collection_description_pattern_string = "^.{{{0},{1}}}$".format(constants.MIN_COLLECTION_DESCRIPTION_SIZE, constants.MAX_COLLECTION_DESCRIPTION_SIZE)
    collection_description_pattern = re.compile(collection_description_pattern_string)
    if(not collection_description_pattern.match(collection_description)): return False
    
    # 'collection_description' is acceptable
    return True
    