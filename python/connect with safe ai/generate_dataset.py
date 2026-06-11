import pandas as pd
import random

normal = [
    "Hello friend", "Good morning", "How are you",
    "Thank you", "Nice work", "Happy birthday"
]

spam = [
    "Win money now", "Claim your reward",
    "Free gift card", "Earn money fast"
]

harassment = [
    "You are useless", "Nobody likes you",
    "Get lost idiot", "You are stupid"
]

sexual = [
    "Send private pics", "Hot girls chat now",
    "Adult content available", "Meet singles near you"
]

data = []

for _ in range(250):
    data.append([random.choice(normal), "normal"])

for _ in range(250):
    data.append([random.choice(spam), "spam"])

for _ in range(250):
    data.append([random.choice(harassment), "harassment"])

for _ in range(250):
    data.append([random.choice(sexual), "sexual"])

random.shuffle(data)

df = pd.DataFrame(data, columns=["message", "label"])

df.to_csv("dataset.csv", index=False)

print("Dataset Generated Successfully!")
print("Total Rows:", len(df))