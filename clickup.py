# clickup.py — TEC ClickUp > WordPress Summarizer

import os
import openai
import requests
import clickup_module_correctly
from dotenv import load_dotenv

load_dotenv()

# Environment
openai.api_key = os.getenv("OPENAI_API_KEY")
clickup_api_token = os.getenv("CLICKUP_API_TOKEN")
clickup_list_id = os.getenv("CLICKUP_LIST_ID")
wp_url = os.getenv("WP_SITE_URL") + "/wp-json/wp/v2/posts"
wp_user = os.getenv("WP_USER")
wp_password = os.getenv("WP_APP_PASS")
