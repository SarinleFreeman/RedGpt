import configparser
import termcolor

from src.CLI.definition import CLI
from src.Gpt.API.GptReader import GPTReader
from src.Gpt.API.GptSaver import save_to_json, save_to_pdf
from src.Reddit.definition import RedditReader

if __name__ == "__main__":
    # Initialize CLI and fetch arguments
    cli = CLI()
    cli.set_parser()
    cli.parse_parser()
    args = cli.get_args()


    # Read base configs
    config = configparser.ConfigParser()
    config.read(args["config"])
    client_id = config["Reddit"]["client_id"]
    client_secret = config["Reddit"]["client_secret"]
    user_agent = config["Reddit"]["user_agent"]

    # Read reddit post
    reddit_reader = RedditReader(client_id, client_secret, user_agent)
    reddit_reader.fetch_post(args["sub_reddit"], int(args["post_rank"]), args["post_time"])

    # Check if post was found
    if reddit_reader.post:
        # Read post and save to JSON
        # Choose path
        web_scraper = args["use_web_scraper"]

        if web_scraper:


        else:
            # Take webscraper path
            openai_api_key = config["OpenAI"]["api_key"]
            gpt_reader = GPTReader(openai_api_key)
            summary = gpt_reader.create_summary(reddit_reader.post, prompt=args["custom_prompt"])

            # Format and print the post and summary
            print("Original Post:")
            print(reddit_reader.parse_post()[:4096])
            print("\nGenerated Summary:")
            print(termcolor.colored(summary, "cyan")[:4096])

            # Save the post and summary to JSON&PDF
            save_to_json(reddit_reader.post, summary)
            save_to_pdf(reddit_reader.post, summary)

    else:
        print(termcolor.colored("No post found with the given criteria.", "red"))



