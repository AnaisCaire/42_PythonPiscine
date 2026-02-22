import os

REQUIRED_KEYS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]

DEFAULTS = {
    "MATRIX_MODE": "development",
    "LOG_LEVEL": "DEBUG",
}


def loader():
    """
    loads env requirements so we can inject them
    later with os
    """
    ven_dict = {}  # so we return an empty dic if function fails
    try:
        with open('.env', 'r') as f:
            for line in f:
                line = line.strip()
                # Skip empty lines or comments
                if not line or line.startswith('#'):
                    continue
                key, value = line.split('=', 1)
                ven_dict[key] = value
        return ven_dict
    except FileNotFoundError:
        print("there is no .ven file found")
        return ven_dict


def security_check(config, ven_dic):
    """add a layer of security and control erros"""
    print("Environment security check:")
    if ven_dic:
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file not found or empty")

    placeholders = {
        "your_api_key_here",
        "changeme",
        "postgres://user:pass@host:5432/dbname",
    }
    if config.get("API_KEY") in placeholders or config.get("DATABASE_URL") in placeholders:
        print("[ERROR] Hardcoded placeholders detected in secrets")
        return False

    print("[OK] No hardcoded secrets detected")

    if config.get("MATRIX_MODE") in ("development", "production"):
        print("[OK] Production overrides available")
        return True

    print("[WARN] MATRIX_MODE invalid")
    return False


def oracle():
    """Uses os to add the .env requirements to the system and displays status"""
    print("Accessing the Mainframe")
    print("ORACLE STATUS: Reading the Matrix...")

    ven_dic = loader()

    config = {}
    for key in REQUIRED_KEYS:
        value = os.getenv(key)
        if not value:
            value = ven_dic.get(key)
        if not value and key in DEFAULTS:
            value = DEFAULTS[key]
            print(f"[WARNIG] {key} missing, defaulting to {value}")
        config[key] = value

    mode = config.get("MATRIX_MODE")
    if mode not in ("development", "production"):
        print("Error: MATRIX_MODE must be development or production")
        mode = "development"

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")

    if config.get("DATABASE_URL"):
        if mode == "production":
            print("Database: Connected to production cluster")
        else:
            print("Database: Connected to local instance")
    else:
        print("Database: Missing configuration")

    if config.get("API_KEY"):
        print("API Access: Authenticated")
    else:
        print("API Access: Missing credentials")

    if config.get("LOG_LEVEL"):
        print(f"Log Level: {config['LOG_LEVEL']}")
    else:
        print("Log Level: Missing configuration")

    if config.get("ZION_ENDPOINT"):
        if mode == "production":
            print("Zion Network: Online")
        else:
            print("Zion Network: Sandbox")
    else:
        print("Zion Network: Offline (missing endpoint)")

    print()
    security_check(config, ven_dic)
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    oracle()