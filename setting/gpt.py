import openai

openai.api_key = ""

def chatbot_v4():
    while True :
        user_input = input("입력: " )

        if user_input in  ['종료', 'exit', 'q'] :
            print("Chatbot: Goodbye!")
            break

        response = openai.ChatCompletion.create(
            model = "gpt-4o-mini",
            messages = [
                {"role":"system", "content":"You are helpful studymate with many knowledge"},
                {"role":"user", "content" : user_input}
            ],
            max_tokens = 150,
            temperature=0.7)

        exp = response.choices[0].message['content'].strip()
        print(f"답변:{exp}")
        
response = chatbot_v4()
print(f"Response from {response}")