
# **YT Summarizer: YouTube Video Summarizer & Transcriber using Google Gemini Pro**

**YT Summarizer** is a web application that converts YouTube video transcripts into detailed, point-based summaries using Google Gemini Pro's LLM. It provides an efficient way to understand long videos by extracting key points and presenting them concisely within 250 words.



---

## **Demo Video :**


https://github.com/user-attachments/assets/782594ea-7c6f-43d0-8098-c2f4dd43a61d

---------------
## **Features**

### **YouTube Video Transcription:**
- **Automatic Transcript Extraction**: Extracts the full transcript from any YouTube video.
- **Language Support**: Automatically handles transcript extraction in supported languages.

### **Summarization**:
- **Point-based Summaries**: Summarizes video transcripts in bullet points, highlighting key information.
- **Concise Summary**: Generates a summary within 250 words for efficient consumption.

### **User-friendly Interface**:
- **YouTube Video Preview**: Displays a thumbnail of the video before processing the transcript.
- **Text Input**: Simply paste the YouTube video link to start the process.

### **Download Summary**:
- Users will be able to download the summary in PDF format.
---

## **Tech Stack**

- **Streamlit**: Used for creating a simple, interactive UI for entering the YouTube video link and displaying results.
- **Google Gemini Pro**: The LLM model for generating video summaries from transcript data.
- **YouTube Transcript API**: For extracting video transcript data.
- **Python**: Backend logic for API integration and data processing.
- **dotenv**: Used to manage environment variables securely.

---

## **Setup and Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/yt-summarizer.git
   cd yt-summarizer
   ```

2. **Install Dependencies**:
   Ensure that you have `pip` installed, and then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys**:
   - Get the Google Gemini Pro API key.
   - Create a `.env` file in the root directory and add the following:
     ```bash
     GOOGLE_API_KEY=your-google-api-key
     ```

4. **Run the Application**:
   Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. **Access the Application**:
   Open your browser and navigate to `http://localhost:8501`.

---

## **How to Use**

1. **Enter YouTube Video Link**: Paste the link of the YouTube video you want to summarize.
2. **click on generate summary**: click on the generate summary button then app extracts text from video and gnerates summary of the video within 5-10 seconds.
3. **click on download summary**: The entire summary will be downloaded as PDF.

---

## **Future Enhancements**

- **Multimedia Support**: Extend support for other types of media like audio and podcasts.
- **Multi language summarization**: Currently, this app only works for English videos, but in the future, we plan to expand support for all languages.
- **Multimedia Support**: Extend support for other types of media like audio and podcasts.
- **Search Functionality**: Allow users to search for specific keywords in the transcript.

---

## **contact**

For any inquiries or questions, please contact us at sana000dasaradha@gmail.com

