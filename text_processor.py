import requests
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation

nltk.download('punkt_tab')

def get_text_from_url(url):
    """
    Fetches the HTML from a URL and extracts the text from all paragraph tags.
    """
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        article_text = ' '.join([p.get_text() for p in paragraphs])
        return article_text
    except requests.exceptions.RequestException as e:
        return f"Error: Could not retrieve the URL. {e}"

def calculate_word_frequencies(text):
    """
    Cleans the text and calculates the frequency of each non-stopword.
    """
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    freq_dist = {}
    
    for word in words:
        if word not in stop_words and word not in punctuation and word.isalpha():
            if word not in freq_dist:
                freq_dist[word] = 1
            else:
                freq_dist[word] += 1
                
    return freq_dist

from nltk.tokenize import sent_tokenize

def summarize_text(text, word_freqs, num_sentences=5):
    """
    Scores sentences based on word frequencies and returns a summary.
    
    Args:
        text (str): The original article text.
        word_freqs (dict): A dictionary of word frequencies.
        num_sentences (int): The desired number of sentences in the summary.
        
    Returns:
        str: The generated summary.
    """
    # 1. Tokenize the original text into sentences
    sentences = sent_tokenize(text)
    
    # 2. Find the maximum frequency to normalize scores
    if not word_freqs:
        return "" # Return empty string if no meaningful words found
    max_freq = max(word_freqs.values())
    
    # 3. Normalize frequencies (scale all values between 0 and 1)
    for word in word_freqs.keys():
        word_freqs[word] = (word_freqs[word] / max_freq)
        
    # 4. Score each sentence
    sentence_scores = {}
    for sent in sentences:
        # Tokenize the sentence into words
        sent_words = word_tokenize(sent.lower())
        score = 0
        for word in sent_words:
            if word in word_freqs:
                score += word_freqs[word]
        sentence_scores[sent] = score
        
    # 5. Get the top N sentences with the highest scores
    # We use heapq for efficiency, but sorting works fine too.
    import heapq
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    
    # 6. Join the sentences to form the final summary
    summary = ' '.join(summary_sentences)
    return summary