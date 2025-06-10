# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="sk-1c6bceaae4ef414bbe8ae21585bc9e73", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个插画设计师"},
        {"role": "user", "content": "生成学习stable Diffusion的技能路线图，包含训练模型等技术"},
    ],
    stream=False
)

print(response.choices[0].message.content)