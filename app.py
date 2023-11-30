import streamlit as st
from huggingface_hub import login
from transformers import HfAgent



# HUGGINGFACE_TOKEN=os.getenv("HUGGINGFACE_API_TOKEN")
login("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")

def huggingface_agent(prompt):
    agent=HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoder")
    st.write("StarCoder is initialised")
    query =agent.run(prompt)
    image_name = 'output_img_huggingface.png'
    query.save(image_name)
    return image_name


st.title("AutoGPT")

text_prompt_huggingface=st.text_input("Enter your prompt:")

if text_prompt_huggingface is not None:
    if st.button("Run HuggingFace agent"):
        st.info("your input: "+ text_prompt_huggingface)
        output_image_huggingface = huggingface_agent(text_prompt_huggingface)
        st.image(output_image_huggingface)
        