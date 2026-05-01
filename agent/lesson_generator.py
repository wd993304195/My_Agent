
import os
from openai import OpenAI

class LessonGenerator:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url="https://api.deepseek.com"
        )

    def generate_lesson(self, knowledge:str)->str:
        prompt = f"""
请将以下内容转化为完整地理教案：
- 教学目标
- 教学重点难点
- 教学流程
- 课堂讨论
- 测验题

内容：
{knowledge}
"""
        resp = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role":"user","content":prompt}]
        )
        return resp.choices[0].message.content
