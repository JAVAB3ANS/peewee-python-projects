# Convert JSON to CSV

import json

if __name__ == "__main__":
    try:
        with open ("input.json", "r") as f:
            data = json.loads(f.read())

        output = ",".join(*data[0])
        for obj in data:
            output += f'\n{obj["SUBREDDIT NAME"]},{obj["USER NAME"]},{obj["POST TITLE"]},{obj["POST TEXT"]},{obj["POST ID"]},{obj["POST URL"]},{obj["POST UPVOTES"]},{obj["POST COMMENT AMOUNT"]},{obj["COMMENT ID"]},{obj["COMMENT CREATED"]},{obj["COMMENT TEXT"]},{obj["COMMENT UPVOTES"]},{obj["NEG COMMENT SCORE"]},{obj["NEU COMMENT SCORE"]},{obj["POS COMMENT SCORE"]},{obj["COMP COMMENT SCORE"]},{obj["WEIGHTED POS COMMENT SCORE"]}'

        with open("output.csv", "w") as f:
            f.write(output)

    except Exception as ex:
        print(f'Error: {str(ex)}')