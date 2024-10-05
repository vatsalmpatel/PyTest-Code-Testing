from code.config_loader import load_config_yaml

# reading the sample1.yaml file, which will be used to write tests on
config = load_config_yaml('config/sample1.yaml')

def test_app_config():
    '''
        Testing the 'app' configuration of the configuration file
    '''
    app_config = config["app"]
    assert app_config["name"] == "MyApp"
    assert app_config["version"] == "1.0.0"
    assert app_config["debug"] is True

def test_server_config():
    '''
        Testing the 'server' configuration of the configuration YAML file
    '''
    server_config = config["server"]
    assert server_config["host"] == "127.0.0.1"
    assert server_config["port"] == 8080
    assert server_config["ssl"] is False

def test_database_config():
    '''
        Testing the 'database' configuration of the configuration YAML file
    '''
    db_config = config["database"]
    assert db_config["type"] == "postgresql"
    assert db_config["host"] == "localhost"
    assert db_config["port"] == 5432
    assert db_config["username"] == "admin"
    assert db_config["password"] == "secret"
    assert db_config["name"] == "myapp_db"

def test_log_config():
    '''
        Testing the "logging" configuration of the YAML file
    '''
    log_config = config["logging"]
    assert log_config["level"] == "INFO"
    assert log_config["file"] == "/var/log/myapp.log"

def test_feature_config():
    '''
        Testing the 'features' configuration of the YAML file
    '''
    features_config = config["features"]
    assert features_config["enable_signup"] is True
    assert features_config["enable_notifications"] is False

def test_user_config():
    '''
        Testing the 'users' and its related configurations in the YAMl file
    '''
    users = config["users"]
    
    # testing the first user
    user1 = users[0]
    assert user1["username"] == "john_doe"
    assert user1["email"] == "john@example.com"
    assert "admin" in user1["roles"]
    assert "editor" in user1["roles"]

    # testing the second user 
    user2 = users[1]
    assert user2["username"] == "jane_smith"
    assert user2["email"] == "jane@example.com"
    assert "editor" in user2["roles"]
    assert "admin" not in user2["roles"]