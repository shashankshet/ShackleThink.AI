from g4f.client import Client

client = Client()


def ask_method(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],

        )
        return response.choices[0].message.content
    except Exception as e:
        print(e)

