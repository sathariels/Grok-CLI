import os
import sys
import json
import click
import pandas as pd
from dotenv import load_dotenv
from grok import Grok
import asyncio
import platform

# Load environment variables
load_dotenv()

# Initialize Grok client
try:
    api_key = os.getenv("XAI_API_KEY")
    if not api_key:
        raise ValueError("XAI_API_KEY not found in environment variables")
    grok_client = Grok(api_key=api_key)
except Exception as e:
    print(f"Error initializing Grok client: {e}")
    sys.exit(1)

# Ensure compatibility with Pyodide for browser execution
async def main_loop():
    while True:
        await asyncio.sleep(0.1)  # Control execution rate

if platform.system() == "Emscripten":
    asyncio.ensure_future(main_loop())
else:
    if __name__ == "__main__":
        asyncio.run(main_loop())

@click.group()
def cli():
    """Grok 4 CLI: A command-line interface for interacting with xAI's Grok 4 API."""
    pass

@cli.command()
@click.argument('prompt')
@click.option('--model', default='grok-4-0629', help='Grok model to use')
def chat(prompt, model):
    """Start an interactive chat session with Grok 4."""
    try:
        response = grok_client.chat(prompt, model=model)
        click.echo(f"Grok: {response}")
    except Exception as e:
        click.echo(f"Error in chat: {e}")

@cli.command()
@click.argument('filename')
@click.argument('prompt')
@click.option('--output', help='Output file for edited content')
def edit_file(filename, prompt, output):
    """Read a file, apply Grok 4 edits based on prompt, and save to output file."""
    try:
        if not os.path.exists(filename):
            click.echo(f"File {filename} does not exist")
            return
        
        with open(filename, 'r') as f:
            content = f.read()
        
        full_prompt = f"Edit the following code/content based on these instructions: {prompt}\n\nContent:\n{content}"
        response = grok_client.chat(full_prompt, model='grok-4-0629')
        
        output_file = output or filename
        with open(output_file, 'w') as f:
            f.write(response)
        
        click.echo(f"File edited and saved to {output_file}")
    except Exception as e:
        click.echo(f"Error editing file: {e}")

@cli.command()
@click.argument('filename')
@click.argument('content')
def create_file(filename, content):
    """Create a new file with specified content."""
    try:
        with open(filename, 'w') as f:
            f.write(content)
        click.echo(f"File {filename} created successfully")
    except Exception as e:
        click.echo(f"Error creating file: {e}")

@cli.command()
@click.argument('data_file')
@click.argument('prompt')
@click.option('--output', default='output.csv', help='Output file for analysis results')
def analyze_data(data_file, prompt, output):
    """Perform data analysis on a CSV file using Grok 4."""
    try:
        if not os.path.exists(data_file):
            click.echo(f"File {data_file} does not exist")
            return
        
        df = pd.read_csv(data_file)
        data_summary = df.to_string()
        
        full_prompt = f"Analyze the following data and provide insights based on this prompt: {prompt}\n\nData:\n{data_summary}"
        response = grok_client.chat(full_prompt, model='grok-4-0629')
        
        # Save analysis results
        with open(output, 'w') as f:
            f.write(response)
        
        click.echo(f"Analysis completed and saved to {output}")
    except Exception as e:
        click.echo(f"Error in data analysis: {e}")

@cli.command()
@click.argument('text')
@click.argument('task')
def nlp(text, task):
    """Perform NLP tasks (e.g., sentiment analysis, entity recognition) using Grok 4."""
    try:
        full_prompt = f"Perform the following NLP task: {task}\n\nText: {text}"
        response = grok_client.chat(full_prompt, model='grok-4-0629')
        click.echo(f"NLP Result: {response}")
    except Exception as e:
        click.echo(f"Error in NLP task: {e}")

@cli.command()
@click.argument('workflow_file')
def automate_workflow(workflow_file):
    """Execute an automated workflow defined in a JSON file using Grok 4."""
    try:
        if not os.path.exists(workflow_file):
            click.echo(f"Workflow file {workflow_file} does not exist")
            return
        
        with open(workflow_file, 'r') as f:
            workflow = json.load(f)
        
        for step in workflow.get('steps', []):
            prompt = step.get('prompt')
            action = step.get('action')
            output_file = step.get('output_file')
            
            if not prompt or not action:
                click.echo("Invalid workflow step: Missing prompt or action")
                continue
            
            response = grok_client.chat(prompt, model='grok-4-0629')
            
            if action == 'save':
                with open(output_file, 'w') as f:
                    f.write(response)
                click.echo(f"Workflow step completed: Saved to {output_file}")
            elif action == 'print':
                click.echo(f"Workflow step result: {response}")
            else:
                click.echo(f"Unsupported action: {action}")
                
    except Exception as e:
        click.echo(f"Error in workflow automation: {e}")

if __name__ == '__main__':
    cli()
