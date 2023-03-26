import cv2
import streamlit as st
from imutils.video import VideoStream


def generate_frames():
    vs = VideoStream(src=0).start()
    while True:
        frame = vs.read()
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        stframe.image(frame)


st.set_page_config(page_title="Webcam Live Streaming", page_icon=":movie_camera:")
st.title("Webcam Live Streaming")

stframe = st.empty()

if st.checkbox("Show Video"):
    video_feed = generate_frames()
