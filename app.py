import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from transformers import pipeline

# Title
st.title("💬 Customer Sentiment Analyzer")
st.write("Upload a CSV file with a column named **Response** to analyze customer feedback.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    if "Response" not in df.columns:
        st.error("CSV must contain a column named 'Response'")
    else:
        # Load transformer model
        st.info("Running sentiment analysis... please wait ⏳")
        sentiment_model = pipeline("sentiment-analysis")
        df['Sentiment'] = df['Response'].apply(lambda x: sentiment_model(str(x))[0]['label'])
        
        st.success("✅ Sentiment analysis completed!")
        st.write(df.head())
        
        # Visualization
        st.subheader("📊 Sentiment Distribution")
        fig, ax = plt.subplots()
        sns.countplot(x='Sentiment', data=df, ax=ax)
        st.pyplot(fig)
        
        # Word Cloud
        st.subheader("☁️ Word Cloud of Responses")
        text = ' '.join(df['Response'].astype(str))
        wc = WordCloud(width=800, height=400, background_color='white').generate(text)
        fig_wc, ax_wc = plt.subplots()
        ax_wc.imshow(wc, interpolation='bilinear')
        ax_wc.axis('off')
        st.pyplot(fig_wc)
        
        # Download results
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("⬇️ Download Results CSV", csv, "sentiment_results.csv", "text/csv")
