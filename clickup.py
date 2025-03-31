# ClickUp Integration for Airth Automations

This file contains functions and classes related to the ClickUp integration, managing tasks, and automating workflows with ClickUp.

import os
import openai
import requests
from dotenv import load_dotenv

load_dotenv()

# Load API keys and endpoints
openai.api_key = os.getenv("OPENAI_API_KEY")
wp_user = os.getenv("WP_USER")
wp_password = os.getenv("WP_APP_PASS")
wp_url = os.getenv("WP_SITE_URL") + "/wp-json/wp/v2/posts"
clickup_api_token = os.getenv("CLICKUP_API_TOKEN")
clickup_list_id = os.getenv("CLICKUP_LIST_ID")

class ClickUp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.clickup.com/api/v2"

    def get_tasks(self, list_id):
        headers = {
            "Authorization": self.api_key
        }
        response = requests.get(f"{self.base_url}/list/{list_id}/task", headers=headers)
        return response.json()

    def create_task(self, list_id, task_name, task_description):
        headers = {
            "Authorization": self.api_key,
            "Content-Type": "application/json"
        }
        data = {
            "name": task_name,
            "description": task_description,
            "status": "to do"
        }
        response = requests.post(f"{self.base_url}/list/{list_id}/task", headers=headers, json=data)
        return response.json()

    def update_task(self, task_id, updates):
        headers = {
            "Authorization": self.api_key,
            "Content-Type": "application/json"
        }
        response = requests.put(f"{self.base_url}/task/{task_id}", headers=headers, json=updates)
        return response.json()

    def delete_task(self, task_id):
        headers = {
            "Authorization": self.api_key
        }
        response = requests.delete(f"{self.base_url}/task/{task_id}", headers=headers)
        return response.status_code

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

# Use GPT to summarize content
def generate_blog_summary(raw_text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Airth, TEC's blog assistant. Summarize and format this ClickUp task as a WordPress blog post."},
            {"role": "user", "content": raw_text}
        ]
    )
    return response.choices[0].message.content

# Send to WP draft
def post_to_wordpress(title, content):
    response = requests.post(
        wp_url,
        auth=(wp_user, wp_password),
        json={
            "title": title,
            "content": content,
            "status": "draft",
            "categories": [1]
        }
    )
    return response.json()

# Main automation
if __name__ == "__main__":
    tasks = fetch_clickup_tasks()
    for task in tasks:
        raw_input = task["description"]  # You can change this to task["name"] or task["text_content"]
        blog_content = generate_blog_summary(raw_input)
        title = blog_content.split("\n")[0][:70]
        post = post_to_wordpress(title, blog_content)
        print("✅ Posted:", post['link'])