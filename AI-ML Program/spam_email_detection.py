import pandas
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pandas.read_csv(url, sep="\t", header=None, names=["label","message"])

df["label"] = df["label"].map({'ham':0, 'spam':1 })

msg = df["message"]
label = df["label"]

vectorizer = CountVectorizer()
msg_vec = vectorizer.fit_transform(msg)

model = MultinomialNB()
model.fit(msg_vec, label)


def check_email_spam(email_text):
    email_vec = vectorizer.transform([email_text])
    prediction = model.predict(email_vec)[0]
    result = "Spam" if prediction == 1 else "Not Spam"
    print(f"\nEmail: {email_text}\nPrediction: {result}")

if __name__ == "__main__":
    while True:
        print("===============================================================")
        email_input = input("\n> Enter email text to check (or type 'exit' to quit):\n> ")
        if email_input.lower() == "exit":
            break
        check_email_spam(email_input)


