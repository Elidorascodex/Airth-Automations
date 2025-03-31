# 🚀 AIRTH Automations

**Airth**—your fully automated TEC blogging assistant.

## 🔧 Features
- **Auto-Summarize:** AI-powered blog summaries.
- **ClickUp Integration:** Fetch tasks, auto-format & post.
- **WordPress Integration:** Automated publishing as drafts.
- **Flexible Prompt Templates:** Easily editable.

## 📂 Project Structure

- **airth.py**: Contains the main logic for Airth automation processes, including functions and classes for handling various tasks.
- **clickup.py**: Manages ClickUp integration, automating workflows and task management.
- **.env**: Stores environment variables such as API keys and configuration settings required for the application to run.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **prompts/**: Contains markdown files with templates for generating summaries.
  - **wp_blog_summary.md**: Guidelines for generating summaries of WordPress blog posts.
  - **clickup_summary.md**: Guidelines for generating summaries related to ClickUp tasks or projects.
- **n8n_workflows/**: Contains workflow configurations for n8n.
  - **tec_content_distribution.json**: Workflow configuration for automating content distribution processes.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Airth-Automations.git
   ```
2. Navigate to the project directory:
   ```
   cd Airth-Automations
   ```
3. Install the required dependencies (if applicable):
   ```
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add your environment variables:
   ```
   API_KEY=your_api_key
   OTHER_CONFIG=your_other_config
   ```

## Usage Guidelines

- To run the Airth automation processes, execute the `airth.py` script:
  ```
  python airth.py
  ```
- For ClickUp automation, use the `clickup.py` script:
  ```
  python clickup.py
  ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.