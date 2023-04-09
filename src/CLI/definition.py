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
        self.parser.add_argument('-sred', '--sub_reddit', type=str, help='Subreddit name',required=True)
        self.parser.add_argument('-p_rnk', '--post_rank', type=str,
                            help='Which post to analyse, check by the rank of the post',default='1')
        self.parser.add_argument('-p_time', '--post_time', type=str, help='Maximum time range for the posts. Reddit '
                                                                          'offers 6 options hour, day, week, month, '
                                                                          'year, all',default='day')
        self.parser.add_argument('-prpt', '--custom_prompt', type=str, help='A custom prompt to ChatGPT', default='day')

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
