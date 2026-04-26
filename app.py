

import streamlit as st
import time
import json

st.title('중간고사 대체 과제 / + 1 = 해방')
st.info('학번: 2024404088 / 이름: 이찬혁')

@st.cache_data
def load():
    time.sleep(2) 
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return [{"question": "데이터 파일 오류", "dap": "X"}]

if 'login' not in st.session_state:
    st.session_state.login = False
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'score' not in st.session_state:
    st.session_state.score = 0



if not st.session_state.login:
    st.header('로그인 인증')
    col1, col2 = st.columns(2)
    with col1:
        id = st.text_input('아이디 (힌트: user)', value='user')
    with col2:
        pw = st.text_input('비밀번호  (힌트: 1111 + 333)', type='password', value='1444')

    if st.button('로그인 하기'):
        if id == 'user' and pw == '1234':
            st.session_state.login = True
            st.rerun()
        else:
            st.error('인증 실패')

else:
    st.sidebar.header('메뉴')
    if st.sidebar.button('로그아웃'):
        st.session_state.login = False
        st.session_state.step = 0
        st.session_state.score = 0
        st.rerun()

    data = load()
    
    try:
        currentquiz = data[st.session_state.step]
        
        st.subheader(f'문제 진행 중...')
        st.write(f"질문: {currentquiz['question']}")
        
        userdap = st.radio('정답을 고르세요', ['O', 'X'], key=f'dap_{st.session_state.step}')
        
        if st.button('다음으로 넘어가기'):
            if userdap == currentquiz['dap']:
                st.session_state.score += 1
            st.session_state.step += 1
            st.rerun()

    except IndexError:
        st.header('퀴즈가 모두 끝났습니다!')
        final = st.session_state.score
        st.metric(label="최종 점수", value=f"{final}점", delta="테스트 완료")
        
        if st.button('처음부터 다시 풀기'):
            st.session_state.step = 0
            st.session_state.score = 0
            st.rerun()
