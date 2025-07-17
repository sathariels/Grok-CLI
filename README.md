# Grok 4 CLI

A command-line interface for interacting with xAI's Grok 4 API, designed for file access, code editing, data analysis, NLP, and workflow automation.

## Features

- **Chat**: Interactive chat sessions with Grok 4
- **File Editing**: Read, edit, and save files using Grok 4's editing capabilities
- **File Creation**: Create new files with specified content
- **Data Analysis**: Analyze CSV datasets and generate insights using Grok 4
- **NLP**: Perform natural language processing tasks like sentiment analysis and entity recognition
- **Workflow Automation**: Execute automated workflows defined in JSON files

## Prerequisites

- Python 3.8+
- xAI API key (obtain from https://x.ai/api)
- Internet connection (no local file I/O restrictions, but API calls require connectivity)

## Installation

### 1. Clone the Repository (if applicable)

```bash
git clone <repository-url>
cd grok4-cli
```

### 2. Install Dependencies

```bash
pip install click python-dotenv pandas grok
```

### 3. Set Up Environment

Create a `.env` file in the project root with your xAI API key:

```bash
echo "XAI_API_KEY=your_api_key_here" > .env
```

Replace `your_api_key_here` with your actual API key.

## Usage

Run the CLI using the `python grok4_cli.py` command followed by the desired subcommand.

## Commands

### 1. Chat
Start an interactive chat session with Grok 4.

```bash
python grok4_cli.py chat "Tell me about AI advancements" --model grok-4-0629
```

### 2. Edit File
Edit a file based on a prompt and save the result.

```bash
python grok4_cli.py edit-file script.py "Add error handling to this code" --output edited_script.py
```

### 3. Create File
Create a new file with specified content.

```bash
python grok4_cli.py create-file new_script.py "print('Hello, World!')"
```

### 4. Analyze Data
Analyze a CSV file and save insights to an output file.

```bash
python grok4_cli.py analyze-data data.csv "Find trends in sales data" --output analysis.txt
```

### 5. NLP
Perform an NLP task on provided text.

```bash
python grok4_cli.py nlp "I love this product!" "sentiment analysis"
```

### 6. Automate Workflow
Execute a workflow defined in a JSON file.

```bash
python grok4_cli.py automate-workflow workflow.json
```

#### Example workflow.json:

```json
{
    "steps": [
        {
            "prompt": "Generate a report summary",
            "action": "save",
            "output_file": "report.txt"
        },
        {
            "prompt": "Analyze dataset trends",
            "action": "print"
        }
    ]
}
```

## Notes

- Ensure your API key is stored securely in the `.env` file or passed directly (less secure)
- The CLI uses the `grok-4-0629` model by default. Check xAI documentation for available models
- For data analysis, input files must be in CSV format
- Workflow automation requires a JSON file with a `steps` array, each containing `prompt`, `action`, and optional `output_file`
- The CLI is designed to run in a browser via Pyodide, avoiding local file I/O restrictions where applicable

## Troubleshooting

- **API Errors**: Check your API key and rate limits (60 requests/minute, 16,000 tokens/minute)
- **File Not Found**: Ensure file paths are correct and accessible
- **Module Not Found**: Verify all dependencies are installed (`pip install -r requirements.txt`)

## Contributing

Contributions are welcome! Please submit a pull request or open an issue on the project repository.

## License

MIT License
