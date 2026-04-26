import streamlit as st
import time
import json

st.title('**중간고사 대체 과제**')
st.header('숫자야구 + 마피아 / + 1 = 해방')
st.info('학번: 2024404088 / 이름: 이찬혁')

@st.cache_data
def load():
    time.sleep(2) 
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
        user_id = st.text_input('아이디 (힌트: user)', value='user')
    with col2:
        user_pw = st.text_input('비밀번호 (힌트: 1111 + 333)')

    if st.button('로그인 하기'):
        if user_id == 'user' and user_pw == '1444':
            st.session_state.login = True
        else:
            st.error('인증 실패')
else:
    data = load()
    if st.session_state.step >= 7:
        st.header('끝')
        final = st.session_state.score
        st.metric(label="최종 점수", value=f"{final}점", delta="테스트 완료")
        
        if st.button("다시 시작하기"):
            st.session_state.step = 0
            st.session_state.score = 0

    else:
        currentquiz = data[st.session_state.step]   
        
        st.write(f"질문: {currentquiz['question']}")
        userdap = st.radio('정답을 고르세요', ['O', 'X'], key=f"q{st.session_state.step}")
        
        if st.button('넘어가기'):
            if userdap == currentquiz['dap']:
                st.session_state.score += 1
            st.session_state.step += 1
   
