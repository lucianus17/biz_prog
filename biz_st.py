import streamlit as st # stramlit 라이브러리 임포트

"""
#비즈니스 모델 분석
[네이버](https://www.naver.com)
[홍익대학교](https://www.hongik.ac.kr)

이것이 일반 본문**이것이 굵은 글씨**이것이 기울임 글씨*--이것이 취소선-*

:red[빨간색 글씨] :green[초록색 글씨] :blue[파란색 글씨]

``` c
import streamlit as st

print("코드블록")
```
"""

st.caption('캡션(작고 흐린 글씨로 표현됨) : st.caption()')

with st.echo():
    #이 블록의 코드와 결과를 출력
    name = 'Sunghyun Park' 
    st.write("Hello, Streamlit!", name)

st.latex('\int_a^b f(x)dx')
"$$\int_a^b f(x)dx$$"

'# 🎥: 이미지, 오디오, 동영상'

'#### :orange[이미지: st.image()]'
st.image("./data/pythonimage.jpeg", caption="파이썬 로고", width=800)

'#### :orange[오디오: st.audio()]'
st.audio("./data/bombinsound.mp3", format="audio/mpeg", loop=True)

'#### :orange[동영상: st.video()]'
# 'rb' : 바이너리 모드로 파일 열기
video_file = open("./data/korea.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)

st.divider()  # 👆 구분선
