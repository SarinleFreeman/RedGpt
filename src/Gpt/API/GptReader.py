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


