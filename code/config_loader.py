import yaml

def load_config_yaml(path_to_file:str) -> yaml:
    '''
        Input:
            path_to_file:   path to the YAML config file

        Returns:
            YAML object as read by the YAML package
    '''
    with open(path_to_file,'r') as file:
        return yaml.safe_load(file)
    
config = load_config_yaml('config/sample1.yaml')