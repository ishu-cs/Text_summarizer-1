import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

# Function to read yaml
@ensure_annotations

def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ Reads the yaml file and returns a ConfigBox
    Args : 
       path_to_yaml (str): Path like input
    Raises : 
        ValueError : if yaml file is empty
        e: empty file    
    Returns :
        ConfigBox : ConfigBox type
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path_to_yaml} is loaded successfully")
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f'{path_to_yaml} is empty')
    except Exception as e:
        raise e
    
# Function to create the dirs
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """ Create list of directories

    Args : 
            path_to_directories (list): list of the paths to directories
            ignore_log(bool,optional): ignore if multiple directories to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at {path}")  
    
# Function to return the size of a file
    
@ensure_annotations
def get_file_size(path: Path) -> str:
    """ Get size of a file in KB

    Args : 
            path (Path): path to the file
    returns : 
            str : Size in kb 
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"
