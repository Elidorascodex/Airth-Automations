from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
clickup_api_token = os.getenv("CLICKUP_API_TOKEN")
clickup_list_id = os.getenv("CLICKUP_LIST_ID")
wp_site_url = os.getenv("WP_SITE_URL")
wp_user = os.getenv("WP_USER")
wp_app_pass = os.getenv("WP_APP_PASS")

# ...use these variables in your script...
