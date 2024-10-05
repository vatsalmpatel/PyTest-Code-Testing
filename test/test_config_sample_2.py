import pytest
from code.config_loader import load_config_yaml
import logging

@pytest.fixture(scope='session')
def config():
    '''
        Loading the config file once for the entire test file
    '''
    return load_config_yaml('config/sample2.yaml')

@pytest.mark.parametrize("env",["development","production"])
def test_server_config(env,config):
    '''
        Using the parametrize functionality of pytest, to use both environments
        while testing, which is "development" and "production"
    '''
    server_config = config["server"][env]
    assert server_config["host"], "Host should be defined in server config"
    assert server_config["port"] > 0, "Port should be a positive integer"
    assert "workers" in server_config, f"Workers must be configured for {env}"

    # writing env specific tests such as for production and others
    if env == "production":
        assert server_config["ssl"] is True, "SSL should be enabled in production"
        assert "cert_path" in server_config, "SSL cert_path must be defined in production"
        assert "key_path" in server_config, "SSL key_path must be defined in production"
    else:
        assert server_config["ssl"] is False, "SSL should be disabled in development"

def test_db_config(config):
    '''
        Testing the database configuration in the YAML file
    '''
    dev_db = config["database"]["development"]
    prod_db = config["database"]["production"]

    assert dev_db["type"] == prod_db["type"] == "postgresql"
    assert dev_db["port"] == prod_db["port"] == 5432
    assert dev_db["username"] == prod_db["username"] == "admin"
    assert dev_db["password"] == prod_db["password"] == "supersecret"

    assert dev_db["host"] == "localhost"
    assert dev_db["name"] == "myapp_dev_db"
    assert prod_db["host"] == "db.myapp.com"
    assert prod_db["name"] == "myapp_prod_db"

def test_auth_config(config):
    '''
        Testing the authentication configuration in the YAMl file
    '''
    auth_config = config["authentication"]

    assert "jwt_secret" in auth_config
    assert len(auth_config["jwt_secret"]) >= 16, "JWT secret should be at least 16 characters long"
    assert auth_config["token_expiration_minutes"] == 60
    assert auth_config["refresh_token_expiration_days"] == 7

    allowed_providers = auth_config["allowed_providers"]
    assert "google" in allowed_providers
    assert "facebook" in allowed_providers

    oauth2_providers = auth_config["oauth2_providers"]
    assert "google" in oauth2_providers
    assert "client_id" in oauth2_providers["google"]
    assert "client_secret" in oauth2_providers["google"]

def test_cache_config(config):
    '''
        Testing Caching configuration in the YAML file
    '''
    assert config["caching"]["enabled"] is True, "Caching should be enabled"
    dev_cache = config["caching"]["development"]
    prod_cache = config["caching"]["production"]

    assert dev_cache["host"] == "localhost"
    assert dev_cache["ttl_seconds"] == 600

    assert prod_cache["host"] == "cache.myapp.com"
    assert prod_cache["ttl_seconds"] == 3600

def test_log_config(config,caplog):
    '''
        Testing the Logging config in the YAML file, using caplog, which will 
        capture logging information in and then use it for testing purposes
    '''
    logging_config = config["logging"]
    assert logging_config["version"] == 1

    assert "handlers" in logging_config
    assert "console" in logging_config["handlers"]
    assert "file" in logging_config["handlers"]

    with caplog.at_level("INFO"):
        caplog.clear()
        logging.info("INFO This is a log message")

    assert "This is a log message" in caplog.text

@pytest.mark.parametrize("admin_user", [
    {"username": "alice_admin", "email": "alice@myapp.com", "roles": ["superuser", "admin"]},
    {"username": "bob_manager", "email": "bob@myapp.com", "roles": ["manager"]}
])
def test_admin_users(admin_user, config):
    '''
        Testing the admins configuration of the YAML fle
    '''
    admins = config["admins"]
    for admin in admins:
        if admin["username"] == admin_user["username"]:
            assert admin["email"] == admin_user["email"]
            assert admin["roles"] == admin_user["roles"]
            break
    else:
        pytest.fail(f"Admin user {admin_user['username']} not found in configuration")

def test_production_only_feature(config):
    '''
        Testing the configuration only if the environment is 'production' else
        the test is skipped using pytest.skip    
    '''
    if "production" not in config["app"]["environments"]:
        pytest.skip("Skipping test: production environment is not defined")

    assert config["server"]["production"]["ssl"] is True

def test_microserv_config(config):
    '''
        Testing the micro-service config of the YAML file
    '''
    microservices = config["microservices"]
    
    user_service = microservices["user_service"]
    assert user_service["url"] == "https://userservice.myapp.com", "User service URL mismatch"
    assert user_service["timeout_seconds"] == 10, "User service timeout should be 10 seconds"
    assert user_service["retries"] == 3, "User service retries should be 3"

    order_service = microservices["order_service"]
    assert order_service["url"] == "https://orderservice.myapp.com", "Order service URL mismatch"
    assert order_service["timeout_seconds"] == 15, "Order service timeout should be 15 seconds"
    assert order_service["retries"] == 5, "Order service retries should be 5"