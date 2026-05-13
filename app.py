import streamlit as st
import time
import json
import logging

st.title('**중간고사 대체 과제**')
st.header('숫자야구 + 마피아 / + 15 = 해방')
st.info('학번: 2024404088 / 이름: 이찬혁')

@st.cache_data
def load():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return [{"question": "오류", "dap": "X"}]


if 'login' not in st.session_state:
    st.session_state.login = False
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'score' not in st.session_state:
    st.session_state.score = 0

if not st.session_state.login:
    st.header('인증')
    col1, col2 = st.columns(2)
    with col1:
        id = st.text_input('아이디 (힌트: user)')
    with col2:
        pw = st.text_input('비밀번호 (힌트: 1111 + 333)')

    if st.button('로그인'):
        if id == 'user' and pw == '1444':
            st.session_state.login = True
            logging.info("!!! 로그인 성공 로그 !!!")
            st.rerun()
        else:
            st.error('인증 실패')
else:
    data = load()
    if st.session_state.step >= 7:
        st.header('끝')
        final = st.session_state.score
        st.metric(label="최종 점수", value=f"{final}점", delta="완료")
        
        if st.session_state.score == 7:
                    if st.button("우승"):
                        st.image('test4.jpg', caption='1945.8.15', width=300)

            
        
        if st.button("다시하기"):
            st.session_state.step = 0
            st.session_state.score = 0
            st.rerun()

    else:
        currentquiz = data[st.session_state.step]   
        
        st.write(f"질문: {currentquiz['question']}")
        userdap = st.radio('정답을 고르세요', ['O', 'X'], key=f"q{st.session_state.step}")
        
        if st.button('넘어가기'):
            if userdap == currentquiz['dap']:
                st.session_state.score += 1
            st.session_state.step += 1
            st.rerun()
   
