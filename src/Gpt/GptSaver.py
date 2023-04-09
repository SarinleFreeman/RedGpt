import os
import datetime
import json
import re

import termcolor
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


def save_to_json(post, summary, output_folder='RedGPT_summary_files/JSON', output_file=None):
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
    try:
        with open(output_path, "w") as f:
            json.dump(data, f, indent=2)
            print(termcolor.colored(f"Saved JSON based summary to {output_path}", "green"))
    except Exception as e:
        print(termcolor.colored(f"Error saving JSON based summary to {output_path}:", "red"))
        print(termcolor.colored(f"{e}", "red"))


def save_to_pdf(post, summary, output_folder="RedGPT_summary_files/PDF", output_file=None):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    unique_id = datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f")

    if output_file is None:
        output_file = f"summary-{unique_id}.pdf"

    output_path = os.path.join(output_folder, output_file)

    doc = SimpleDocTemplate(output_path, pagesize=letter)
    story = []

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="PostTitle", fontSize=14, textColor=colors.blue, spaceAfter=10))
    styles.add(ParagraphStyle(name="PostAuthor", fontSize=12, textColor=colors.green, spaceAfter=10))
    styles.add(ParagraphStyle(name="PostBody", fontSize=10, spaceAfter=10))
    styles.add(ParagraphStyle(name="SummaryTitle", fontSize=12, textColor=colors.red, spaceAfter=10))
    styles.add(ParagraphStyle(name="SummaryBody", fontSize=10, spaceAfter=10))

    post_content = post.selftext.replace('\n', ' ')
    post_content = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'\1: \2', post_content)

    story.append(Paragraph("Post Title:", styles["PostTitle"]))
    story.append(Paragraph(post.title, styles["PostBody"]))
    story.append(Paragraph(f"Posted by u/{post.author.name} in r/{post.subreddit.display_name}", styles["PostAuthor"]))
    story.append(Paragraph("Post Content:", styles["PostTitle"]))
    story.append(Paragraph(post_content, styles["PostBody"]))

    story.append(Spacer(1, 20))

    story.append(Paragraph("Summary:", styles["SummaryTitle"]))
    story.append(Paragraph(summary, styles["SummaryBody"]))

    try:
        doc.build(story)
        print(termcolor.colored(f"Saved PDF based summary to {output_path}", "green"))
    except Exception as e:
        print(termcolor.colored(f"Error saving PDF based summary to {output_path}:", "red"))
        print(termcolor.colored(f"{e}", "red"))

    return output_path
