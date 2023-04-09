import argparse


class CLI:
    """
    This class is used to define the CLI arguments.
    """

    def __init__(self):
        self.args = None
        self.parser = argparse.ArgumentParser(
            description="Welcome to RedGPT, RedGPT is a tool to analyse reddit posts with ChatGPT.")

    def set_parser(self):
        """
        This function is used to set the parser arguments.
        """
        self.parser.add_argument('-sred', '--subreddit ', type=str, help='Subreddit name', required=True)
        self.parser.add_argument('-p_rnk', '--post-rank', type=str,
                                 help='Which post to analyse, check by the rank of the post', default='1')
        self.parser.add_argument('-p_time', '--post-time', type=str, help='Maximum time range for the posts. Reddit '
                                                                          'offers 6 options hour, day, week, month, '
                                                                          'year, all', default='day')

        # Config file
        self.parser.add_argument('-cfg', '--config', type=str, help='Path to the config file', default='config.ini')

        # ChatGPT Options
        self.parser.add_argument('-prpt', '--custom_prompt', type=str, help='A custom prompt to ChatGPT', default='day')

        self.parser.add_argument('-temp', '--temperature', type=float, help='Temperature to use for generating the '
                                                                            'ChatGPT when using API', default=0.8)

        self.parser.add_argument('-m_tns', '--max_tokens', type=int, help='Maximum number of tokens ChatGPT uses for '
                                                                          'token', default=50)

        self.parser.add_argument('-scrp', '--use_web_scraper', type=bool, help='Use web scraper to get the post',
                                 default=False)

    def parse_parser(self):
        """
        This function is used to parse the parser arguments.
        """
        self.args = vars(self.parser.parse_args())

    def get_args(self):
        """
        This function is used to return the arguments.
        """
        return self.args
