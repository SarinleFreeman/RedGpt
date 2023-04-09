# RedGpt

RedGPT is a tool that allows you to fetch data from a subreddit and generate interesting replies using the GPT-3 language model. With RedGPT, you can quickly and easily find interesting posts and generate creative and engaging replies to them.

## Getting Started

### Prerequisites
To use RedGPT, you will need:

- Python 3.6 or higher
- An OpenAI API key for GPT-3
- A Reddit account with API credentials

### Installation

Clone the RedGPT repository:

```
git clone https://github.com/your-username/redgpt.git
```

Install the required Python packages:

```
pip install -r requirements.txt
```

Set up your OpenAI API key and Reddit API credentials. You can find instructions on how to do this in the "Configuration" section below.

## Configuration

To use RedGPT, you will need to set up your OpenAI API key and Reddit API credentials.

### OpenAI API key

To obtain an OpenAI API key, follow these steps:

- [Sign up for an OpenAI account](https://beta.openai.com/signup/)
- [Navigate to the API keys page](https://beta.openai.com/account/api-keys/)
- Create a new API key and note it down


### Reddit API credentials

To obtain Reddit API credentials, follow these steps:

- Create a Reddit account if you do not already have one
- Navigate to the Reddit apps preferences page at https://www.reddit.com/prefs/apps
- Click the "Create App" button
- Fill in the required fields and select the "Web app" option
- Set the redirect URI to http://localhost:8080
- Save the app and note down the client ID and client secret 

## Usage

To use RedGPT, follow these steps:

Open a terminal window and navigate to the RedGPT directory.

Run the redgpt.py script:

```
python redgpt.py --subreddit <subreddit-name> --prompt <prompt-text> --max-tokens <max-tokens> --temperature <temperature> --api-key <openai-api-key> --client-id <reddit-client-id> --client-secret <reddit-client-secret>
```

The arguments are as follows:

subreddit-name: the name of the subreddit to search for posts in

prompt-text: the text of the prompt to use for generating replies

max-tokens: the maximum number of tokens to generate in the GPT-3 response (default: 50)

temperature: the temperature to use for generating the GPT-3 response (default: 0.8)

openai-api-key: your OpenAI API key

reddit-client-id: your Reddit app client ID

reddit-client-secret: your Reddit app client secret

For example:
```
python redgpt.py --subreddit news --prompt "What do you think about this?" --max-tokens 100 --temperature 0.8 --api-key abcdefghijklmnopqrstuvwxyz012345 --client-id 123456 --client-secret abcdefghijklmnopqrstuvwxyz0123456789 --username myusername --password mypassword
```

RedGPT will search for the top posts in the specified subreddit and generate a reply to the most recent post that matches the prompt. RedGPT will only generate a reply if there is a post in the subreddit that matches the prompt. If no matching posts are found, RedGPT will exit without generating a reply.

### Example

Here's an example of how you can use RedGPT to generate a reply to a post in the news subreddit:

```
python redgpt.py --subreddit news --prompt "What do you think about this?" --max-tokens 50 --temperature 0.5 --api-key abcdefghijklmnopqrstuvwxyz012345 --client-id 123456 --client-secret abcdefghijklmnopqrstuvwxyz0123456789
```

This command searches for the top posts in the news subreddit, and generates a reply to the most recent post. The generated reply will have a maximum of 50 tokens and a temperature of 0.8. The information will be stored within RedGPT_summary_files which will contain both the post and the reply.

## Limitations

RedGPT has a few limitations that you should be aware of:

- RedGPT relies on the GPT-3 language model from OpenAI, which requires an API key and has limits on the number of requests you can make per month.
- RedGPT only generates replies to posts that contain the exact prompt text. It does not perform any natural language processing or topic modeling to identify related posts.
- RedGPT only generates one reply per run. If you want to generate multiple replies, you will need to run the script multiple times, with the prompt as the input.

## License
RedGPT is licensed under the MIT License. See the LICENSE file for more information.
