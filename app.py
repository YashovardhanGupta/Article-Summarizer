from flask import Flask, render_template, request
from text_processor import get_text_from_url, calculate_word_frequencies, summarize_text

# Initialize the Flask application
app = Flask(__name__)

# Define the main route for the home page
@app.route('/')
def home():
    # Just render the HTML page
    return render_template('index.html')

# Define the route that handles the form submission
@app.route('/summarize', methods=['POST'])
def summarize():
    # Get the data from the form inputs
    url = request.form.get('url_input')
    pasted_text = request.form.get('text_input')
    
    article_text = ""
    input_used = ""

    # Logic to decide which input to use
    if url:
        article_text = get_text_from_url(url)
        input_used = url
    elif pasted_text:
        article_text = pasted_text
        input_used = "Pasted Text"
    else:
        # If no input, return an error
        return render_template('index.html', error="Please enter a URL or paste some text to summarize.")

    # Check if scraping or processing failed
    if "Error:" in article_text:
        return render_template('index.html', error=article_text)
    if not article_text.strip():
        return render_template('index.html', error="Could not find any text to summarize.")

    # Run the summarization process
    word_freqs = calculate_word_frequencies(article_text)
    summary = summarize_text(article_text, word_freqs, num_sentences=5)

    # Render the same page, but now with the results
    return render_template('index.html', summary=summary, original_input=input_used)

# This allows you to run the app directly
if __name__ == '__main__':
    app.run(debug=True) # debug=True allows for auto-reloading during development