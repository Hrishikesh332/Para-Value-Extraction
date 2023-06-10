import streamlit as st
import re
import json

def extract_nums(para):
    nums = re.findall(r'\d+(?:\.\d+)?', para)
    words = para.split()
    labels = []
    for num in nums:
        num_start = para.find(num)
        num_end = num_start + len(num)
        last_four = []
        for i, word in enumerate(words):
            if word.startswith(num) and num_start <= para.find(word) < num_end:
                last_four = words[max(0, i - 4):i]
                break
        labels.append('_'.join(last_four))
    return [(label, float(num)) for label, num in zip(labels, nums)]


st.title("Paragraph Extraction to Json Format")
para = st.text_area("Enter the para:")
values = extract_nums(para)

if st.button("Generate JSON"):
    data = {label: value for label, value in values}
    json_data = json.dumps(data, indent=4)
    st.text_area("JSON Output", json_data)
    

