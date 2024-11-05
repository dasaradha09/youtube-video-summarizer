import streamlit as st
import os
import tempfile
from dotenv import load_dotenv
import re
import google.generativeai as genai
from  youtube_transcript_api import YouTubeTranscriptApi
from fpdf import FPDF
import io

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-pro")


def transcriptGenerator(video_url):
    # Extract the video ID from the URL
    video_id = re.search(r'(?<=v=)[^&]+', video_url)
    if not video_id:
        video_id = re.search(r'(?<=be/)[^&]+', video_url)

    if video_id:
        video_id = video_id.group(0)
    else:
        raise ValueError("Invalid YouTube URL")

    try:
        # Get the transcript for the video
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Combine the transcript parts into a single string
        transcription_text = ' '.join([entry['text'] for entry in transcript])
        return transcription_text
    except Exception as e:
        return f"An error occurred: {e}"
def extract_video_id(url):
    # Regular expression to match YouTube video URLs
    regex = r'(?:https?://)?(?:www\.)?(?:youtube\.com/(?:[^/]+/.*/|(?:v|e(?:mbed)?)|.*[?&]v=)|youtu\.be/)([a-zA-Z0-9_-]{11})'
    match = re.search(regex, url)
    return match.group(1) if match else None

def summarize(transcript,prompt):
    response=model.generate_content(prompt+transcript)
    return response.text


def create_pdf(transcript):
    # Create a PDF object
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Add the transcript text to the PDF
    pdf.multi_cell(0, 10, transcript)
    
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        pdf.output(tmp_file.name, 'F')  # Save the PDF to a temporary file
        
        # Read the temporary file into BytesIO
        pdf_output = io.BytesIO()
        with open(tmp_file.name, 'rb') as f:
            pdf_output.write(f.read())
        
    # Clean up: Delete the temporary file
    os.remove(tmp_file.name)
    
    pdf_output.seek(0)  # Move to the beginning of the BytesIO buffer
    return pdf_output

prompt="""you need to provide summarize the
youtube video transcript and return important poins as bullet points.here is my transcript:"""

st.title("YOUTUBE VIDEO SUMMARIZER")
youtube_link=st.text_input("enter the video link")
summary=""
if st.button("Generate summary"):
    video_id = extract_video_id(youtube_link)
    if video_id:
        # Construct thumbnail URL
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

        # Display the thumbnail
        st.image(thumbnail_url, caption="Video Thumbnail", use_column_width=True)
    else:
        st.error("Invalid YouTube URL. Please try again.")
    transcript=transcriptGenerator(youtube_link)
    st.markdown("##detailednote")
    summary=summarize(transcript,prompt)
    st.write(summary)
    pdf_file = create_pdf(summary)
    
    # Provide a download button
    st.download_button(
        label="Download PDF",
        data=pdf_file,
        file_name="transcript.pdf",
        mime="application/pdf"
    )


    
    
    

    