from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Access environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
clickup_api_token = os.getenv("CLICKUP_API_TOKEN")
clickup_list_id = os.getenv("CLICKUP_LIST_ID")
wp_site_url = os.getenv("WP_SITE_URL")
wp_user = os.getenv("WP_USER")
wp_app_pass = os.getenv("WP_APP_PASS")

# Debugging: Print the ClickUp API token to verify it's loaded
print("ClickUp Token Loaded:", clickup_api_token)

# Debugging: Print the ClickUp List ID to verify it's loaded
print("ClickUp List ID Loaded:", clickup_list_id)

# Function to validate environment variables
def validate_env_vars():
    required_vars = {
        "OPENAI_API_KEY": openai_api_key,
        "CLICKUP_API_TOKEN": clickup_api_token,
        "CLICKUP_LIST_ID": clickup_list_id,
        "WP_SITE_URL": wp_site_url,
        "WP_USER": wp_user,
        "WP_APP_PASS": wp_app_pass,
    }
    for var_name, var_value in required_vars.items():
        if not var_value:
            print(f"Error: Missing environment variable {var_name}")
            return False
    return True

# Function to fetch ClickUp tasks
def fetch_clickup_tasks():
    if not validate_env_vars():
        print("Environment validation failed. Exiting.")
        return []

    headers = {
        "Authorization": clickup_api_token
    }
    url = f"https://api.clickup.com/api/v2/list/{clickup_list_id}/task"
    print("Fetching tasks from URL:", url)  # Debugging: Print the API URL
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("tasks", [])
    else:
        print("Failed to fetch tasks:", response.json())  # Improved error logging
        return []

# ...use these variables in your script...
