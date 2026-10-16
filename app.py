import streamlit as st

st.title("🍔 Ăn Vụng Trong Lớp Học - Thử Thách THCS")

# Khởi tạo điểm số trong session_state
if "score" not in st.session_state:
    st.session_state.score = 0

st.write("Hãy trả lời các câu hỏi Kết nối tri thức để ăn vặt mà không bị Thầy Vĩnh phát hiện!")

# Câu hỏi mẫu 1
st.subheader("Câu 1: Kết quả của phép tính (-2)^3 bằng bao nhiêu?")
answer = st.radio("Chọn đáp án:", ["-8", "8", "-6", "6"], key="q1")

if st.button("Nộp bài"):
    if answer == "-8":
        st.success("Chính xác! Món ăn đã vơi đi một phần.")
        st.session_state.score += 1
    else:
        st.error("Sai rồi! Bị Thầy Vĩnh phát hiện trừ 5 giây!")

st.write(f"Tiến độ hiện tại: {st.session_state.score} câu đúng")
