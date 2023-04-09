import datetime
import os

import openai
import json


class GPTReader:
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model
        openai.api_key = self.api_key

    def generate_text(self, prompt, max_tokens=100, temperature=0.8):
        response = openai.ChatCompletion.create(
            model=self.model, messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ], max_tokens=max_tokens, n=1, stop=None, temperature=temperature)

        return response.choices[0].message['content'].strip()

    def create_summary(self, post, prompt="summarize the post"):
        text = post.title + "\n" + post.selftext
        text = text[:4096]  # Truncate the text if it's too long
        response = self.generate_text(f"{prompt}: {text}")
        return response

    @staticmethod
    def save_to_json(post, summary, output_folder="RedGPT_summary_files/json", output_file=None):
        # Create output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Generate a unique ID based on the current date and time
        unique_id = datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f")

        # Set the output file name if not provided
        if output_file is None:
            output_file = f"summary-{unique_id}.json"

        # Combine output folder and file name
        output_path = os.path.join(output_folder, output_file)

        data = {
            "post": {
                "title": post.title,
                "author": str(post.author),
                "score": post.score,
                "url": post.url,
                "body": post.selftext,
            },
            "summary": summary,
        }
        with open(output_path, "w") as f:
            json.dump(data, f, indent=2)

