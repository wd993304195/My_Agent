
import os
from openai import OpenAI

class GeoLLMProcessor:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url="https://api.deepseek.com"
        )

    def extract_knowledge(self, text:str, context:str="")->str:
        prompt = f"""
你是地理教育专家。请基于输入和参考资料提取：
1. 核心地学主题
2. 关键概念
3. 成因机制
4. 教学价值

输入：
{text}

参考资料：
{context}
"""
        resp = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role":"user","content":prompt}]
        )
        return resp.choices[0].message.content
