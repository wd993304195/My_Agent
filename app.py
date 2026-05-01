
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from agent.processor import GeoLLMProcessor
from agent.lesson_generator import LessonGenerator
from rag.vector_store import build_vectorstore, query_vectorstore

st.set_page_config(page_title="你的地理老师")
st.title("🌍 你的地理老师")

uploaded = st.file_uploader("上传地理资料（PDF/TXT/MD）", type=["pdf","txt","md"])

if uploaded:
    with open(f"data/{uploaded.name}", "wb") as f:
        f.write(uploaded.read())
    build_vectorstore(f"data/{uploaded.name}")
    st.success("知识库已更新")

query = st.text_area("输入新闻 / 论文 / 问题")
if st.button("生成教学素材") and query:
    context = query_vectorstore(query)
    processor = GeoLLMProcessor()
    lesson_gen = LessonGenerator()

    knowledge = processor.extract_knowledge(query, context)
    lesson = lesson_gen.generate_lesson(knowledge)

    st.subheader("知识点")
    st.write(knowledge)

    st.subheader("教案")
    st.write(lesson)
