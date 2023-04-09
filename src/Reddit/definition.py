import configparser
import os.path

import praw
import termcolor


class RedditReader:
    """
    Utilizes CLI arguments to fetch relevant posts from Reddit API.
    """

    def __init__(self, client_id, client_secret, user_agent):
        """
        Initialize the RedditReader class.
        """
        self.post = None
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
        )

    def fetch_post(self, subreddit_name, post_rank, post_time):
        """
        Fetches the post from the subreddit.
        """
        subreddit = self.reddit.subreddit(subreddit_name)
        if post_time not in ["hour", "day", "week", "month", "year", "all"]:
            post_time = "day"

        suitable_posts = []
        for batch_size in [post_rank, post_rank + 100]:
            submissions = list(subreddit.top(time_filter=post_time, limit=batch_size))
            suitable_posts.extend([submission for submission in submissions if
                                   not submission.url.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))])

            # Remove duplicates
            seen_ids = set()
            suitable_posts = [post for post in suitable_posts if not (post.id in seen_ids or seen_ids.add(post.id))]

            if suitable_posts and post_rank <= len(suitable_posts):
                self.post = suitable_posts[post_rank - 1]
                break
        else:
            print("No suitable post found without an image.")

    def parse_post(self):
        """
        Outputs a pretty version of a Reddit post with colors.
        """
        # Format the post title
        title = termcolor.colored(self.post.title, "white", attrs=["bold", "underline"])

        # Format the post author and subreddit
        author = termcolor.colored(f"Posted by u/{self.post.author.name}", "green")
        subreddit = termcolor.colored(f"in r/{self.post.subreddit.display_name}", "green")
        author_subreddit = f"{author} {subreddit}"

        # Format the post score, comment count, and time
        score = termcolor.colored(f"{self.post.score:,}", "cyan")
        comment_count = termcolor.colored(f"{self.post.num_comments:,}", "cyan")
        time = termcolor.colored(self.post.created_utc, "magenta")

        # Format the post URL and body
        url = termcolor.colored(self.post.url, "blue", attrs=["underline"])
        body = termcolor.colored(self.post.selftext, "yellow")

        # Combine all parts into a single string
        lines = [
            f"{title}\n",
            f"{author_subreddit} | {score} points | {comment_count} comments | {time}\n",
            f"{url}\n",
            f"{body}",
        ]
        return "\n".join(lines)
