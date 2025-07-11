import streamlit as st
import random

st.set_page_config(page_title="고3을 위한 지루함 타파 게임", page_icon="🎮")
st.title("🎮 고3을 위한 지루함 타파 게임")

st.markdown("""
시험 끝난 고3 여러분 환영합니다! 아래 게임 중 하나를 선택해서 지루함을 날려보세요!
""")

menu = ["숫자 맞추기 게임", "가위바위보", "랜덤 퀴즈"]
choice = st.selectbox("게임을 선택하세요:", menu)

if choice == "숫자 맞추기 게임":
    st.subheader("🔢 숫자 맞추기 게임")
    if "number" not in st.session_state:
        st.session_state.number = random.randint(1, 100)
        st.session_state.tries = 0

    guess = st.number_input("1부터 100 사이의 숫자를 입력하세요:", min_value=1, max_value=100, step=1)
    if st.button("제출"):
        st.session_state.tries += 1
        if guess < st.session_state.number:
            st.warning("더 큰 숫자입니다!")
        elif guess > st.session_state.number:
            st.warning("더 작은 숫자입니다!")
        else:
            st.success(f"정답입니다! {st.session_state.tries}번 만에 맞추셨어요!")
            st.session_state.number = random.randint(1, 100)
            st.session_state.tries = 0

elif choice == "가위바위보":
    st.subheader("✊✌️🖐️ 가위바위보")
    user_choice = st.radio("당신의 선택은?", ["가위", "바위", "보"])
    if st.button("대결!"):
        options = ["가위", "바위", "보"]
        comp_choice = random.choice(options)
        st.write(f"컴퓨터의 선택: {comp_choice}")
        if user_choice == comp_choice:
            st.info("비겼습니다!")
        elif (user_choice == "가위" and comp_choice == "보") or \
             (user_choice == "바위" and comp_choice == "가위") or \
             (user_choice == "보" and comp_choice == "바위"):
            st.success("이겼습니다!")
        else:
            st.error("졌습니다ㅠㅠ")

elif choice == "랜덤 퀴즈":
    st.subheader("📚 랜덤 퀴즈")
    quizzes = [
        {"question": "태양은 어떤 종류의 천체인가요?", "answer": "항성"},
        {"question": "대한민국의 수도는?", "answer": "서울"},
        {"question": "3.14로 시작하는 원주율을 부르는 이름은?", "answer": "파이"},
    ]
    if "quiz" not in st.session_state:
        st.session_state.quiz = random.choice(quizzes)

    st.write(st.session_state.quiz["question"])
    user_answer = st.text_input("당신의 답은?")
    if st.button("정답 확인"):
        if user_answer.strip() == st.session_state.quiz["answer"]:
            st.success("정답입니다!")
        else:
            st.error(f"틀렸어요! 정답은 '{st.session_state.quiz['answer']}'입니다.")
        st.session_state.quiz = random.choice(quizzes)
