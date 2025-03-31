# Airth Automation Script

import os
import openai
import requests
from dotenv import load_dotenv

def load_env_variables():
    """Load environment variables from .env file."""
    load_dotenv()

# Load API keys from .env file
load_env_variables()

openai.api_key = os.getenv("OPENAI_API_KEY")
wp_user = os.getenv("WP_USER")
wp_password = os.getenv("WP_APP_PASS")
wp_url = os.getenv("WP_SITE_URL") + "/wp-json/wp/v2/posts"
clickup_api_token = os.getenv("CLICKUP_API_TOKEN")
clickup_list_id = os.getenv("CLICKUP_LIST_ID")

# Get tasks from ClickUp
def fetch_clickup_tasks():
    headers = {
        "Authorization": clickup_api_token
    }
    response = requests.get(
        f"https://api.clickup.com/api/v2/list/{clickup_list_id}/task",
        headers=headers
    )
    if response.status_code == 200:
        return response.json()["tasks"]
    else:
        print("Failed to fetch tasks:", response.text)
        return []

# Function: Summarize using GPT-4
def generate_blog_summary(raw_text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Airth, TEC’s blogging assistant. Summarize, title, and format the following as a WordPress blog post."},
            {"role": "user", "content": raw_text}
        ]
    )
    return response.choices[0].message.content

# Function: Post to WordPress as a draft
def post_to_wordpress(title, content):
    response = requests.post(
        wp_url,
        auth=(wp_user, wp_password),
        json={
            "title": title,
            "content": content,
            "status": "draft",  # Change to 'publish' if ready
            "categories": [1]  # Optional: category ID
        }
    )
    return response.json()

def main():
    """Main function to execute Airth automation tasks."""
    load_env_variables()
    tasks = fetch_clickup_tasks()
    for task in tasks:
        raw_input = task["description"]  # You can change this to task["name"] or task["text_content"]
        blog_content = generate_blog_summary(raw_input)
        title = blog_content.split("\n")[0][:70]  # crude title grab
        post = post_to_wordpress(title, blog_content)
        print("✅ Posted:", post['link'])

if __name__ == "__main__":
    main()
````
__pycache__/
.env
*.log
.vscode/