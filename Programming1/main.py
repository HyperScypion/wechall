import requests

text = requests.get(
    "https://www.wechall.net/challenge/training/programming1/index.php?action=request",
    cookies={"WC": "FIND IT IN YOUR BROWSER AS REQUEST COOCKIES"},
).text
print(
    requests.post(
        f"https://www.wechall.net/challenge/training/programming1/index.php?answer={text}",
        cookies={"WC": "FIND IT IN YOUR BROWSER AS REQUEST COOCKIES"},
    ).text
)
