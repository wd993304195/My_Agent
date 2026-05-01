
# GeoAI Agent Pro

AI驱动的地学知识库与教案辅助开发平台（LLM + RAG + Streamlit）

## 功能
- 上传 PDF / TXT / MD 地理资料
- 自动切块 + 向量化（FAISS）
- 检索增强生成（RAG）
- 自动生成：
  - 地学知识点
  - 教案
  - 课堂问题
  - 测验题

## 启动
```bash
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```
