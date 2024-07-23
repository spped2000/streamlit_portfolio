import streamlit as st
import feedparser
from bs4 import BeautifulSoup

# Hide GitHub and fork badges
st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to parse the Medium RSS feed
def load_medium_articles(url):
    return feedparser.parse(url).entries

# Function to extract the first image from the article content
def extract_image_url(content):
    soup = BeautifulSoup(content, 'html.parser')
    img_tag = soup.find('img')
    if img_tag:
        return img_tag['src']
    return "https://via.placeholder.com/150"  # Default image if no image found

# Display articles in a horizontal scroll bar
def display_articles(articles):
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    cols = st.columns(len(articles))
    for col, article in zip(cols, articles):
        with col:
            image_url = extract_image_url(article.content[0].value)
            st.image(image_url, use_column_width=True)
            st.write(article.title)
            st.markdown(f"[Read more]({article.link})", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page", ["About Me", "My Medium Posts"])

if page == "About Me":
    st.title("About Me")
    st.image("my2.png", width=150)  # Replace with your local profile image file
    st.write("""
    ## Natdhanai Praneenatthavee
    Hi, I am Natdhanai Praneenatthavee, and this is my portfolio. I am a AI engineer. 
    Here you can find my Medium posts and learn more about my work.
    """)

if page == "My Medium Posts":
    st.title("My Medium Posts")
    # Enter your Medium feed URL
    feed_url = "https://medium.com/feed/@spped2000"
    articles = load_medium_articles(feed_url)
    display_articles(articles)
