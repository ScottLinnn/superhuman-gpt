import os
from openai import OpenAI
from words_gen import WordPairGenerator  

def inference(generator, gpt_model: OpenAI):
    word_a, word_b = generator.generate_pair()
    print(f"------------------------------------")
    print(f"Current words are: {word_a}, {word_b}")
    print("")

    token_limit = 80
    system_prompt = f"""You will be given two words, <word_a> and <word_b>. Your task is 
    to find nd anything that can be inspiring for human to derive new ideas from these two words, 
    be creative.  You can try to think in terms of association between these two words. Limit your 
    output within {token_limit} words. Your output should be formatted in this way:  \n
The idea can be used in <the field/domain that the idea can apply>\n
Briefly describe the idea in 2 sentences."""
    prompt = f"word_a is {word_a}, word_b is {word_b}"
    chat_completion = gpt_model.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
        max_tokens = 100,
    )
    print(chat_completion.choices[0].message.content)

def main():
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    if not openai_api_key:
        raise ValueError("OpenAI API key is not set in the environment variables.")

    gpt = OpenAI(
        # This is the default and can be omitted
        api_key=openai_api_key,
    )

    generator = WordPairGenerator()
    generator.init(4000)

    loop_count = 3
    for _ in range(loop_count):
        inference(generator, gpt)

if __name__ == "__main__":
    main()
