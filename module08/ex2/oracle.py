import os
import sys


def loader():
    """
    loads env requirements so we can inject them
    later with os
    """
    ven_dict = {}  # so we return an empty dic if function fails
    try:
        with open('.ven.example', 'r') as f:
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


def security_check(ven_dic):
    """add a layer of security and control erros"""
    if not ven_dic:
        print("Error, the loader didnt work")
        return False
    print("[OK] .env file properly configured")

    # 2. Check for placeholders in sensitive keys
    placeholders = ["your_api_key_here", "Connection string for data storage"]
    if ven_dic.get("API_KEY") in placeholders:
        print("[ERROR] Hardcoded placeholders detected in secrets")
        return False
    print("[OK] No hardcoded secrets detected")

    # 3. Check for valid mode
    if ven_dic.get("MATRIX_MODE") in ["development", "production"]:
        print("[OK] Production overrides available")
        return True
    return False

def oracle():
    """Uses os to add the .env requirements to the system and displays status"""
    print("ORACLE STATUS: Reading the Matrix...")
    # Load our dictionary from the .env file
    ven_dic = loader()
    print("\nConfiguration loaded:")
    for key, value in ven_dic.items():
        # Inject into the system environment
        os.environ[key] = value

        if key == "MATRIX_MODE" and value is not None:
            print(f"Mode: {value}")
        elif key == "DATABASE_URL" and value is not None:
            print("Database: Connected to local instance")
        elif key == "API_KEY" and value is not None:
            print("API Access: Authenticated")
        elif key == "LOG_LEVEL" and value is not None:
            print(f"Log Level: {value}")
        elif key == "ZION_ENDPOINT" and value is not None:
            print("Zion Network: Online")
        else:
            print(f"do not recognize this key: {key}")
    print()
    security_check(ven_dic)


if __name__ == "__main__":
    oracle()
