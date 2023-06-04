import json


def fetch_high_score(username, score):
    """Fetch the HighScore,Username from high_score.json File. If Current Score
    Is higher, overwrites information."""
    # Read high scores from the file
    with open("high_score.json", 'r') as f:
        high_score_data = json.load(f)

    # Update the high score and username if the new score is higher
    if score > high_score_data["current_high_score"]:
        high_score_data["current_high_score"] = score
        high_score_data["username"] = username

        # Write the updated data back to the file
        with open("high_score.json", 'w') as f:
            json.dump(high_score_data, f)


if __name__ == '__main__':
    # Code to execute when running this script as the main entry point
    pass
