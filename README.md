# News Article Summarizer

A web-based application built with Python and Flask that uses text mining techniques to generate a concise summary of any news article from a URL or pasted text. This project demonstrates an extractive summarization approach based on word frequency analysis.

# Table of Content

- [Features](#features)
- [Snapshots](#snapshots)
- [Technology Stack](#technology-stack)
- [How It Works](#how-it-works-)
- [Setup and Installation](#setup-and-installation)

# Features

**Summarize from URL** : Provide a link to a news article to automatically scrape and summarize it.

**Summarize from Text** : Paste the full text of an article directly into the application.

**Clean & Responsive UI** : A modern and easy-to-use interface built with Tailwind CSS.

**Extractive Summarization** : Implements a classic TF (Term Frequency) algorithm to identify and rank the most important sentences.

# Snapshots

Landing Page: 

![Landing Page](https://github.com/YashovardhanGupta/Article-Summarizer/blob/main/snapshots/Landing_page.png?raw=true)

Summary:

![Summary](https://github.com/YashovardhanGupta/Article-Summarizer/blob/main/snapshots/Summary.png?raw=true)

# Technology Stack

#### Backend:

- **Python 3**: Core programming language.

- **Flask** : A lightweight web framework for serving the application.

- **NLTK (Natural Language Toolkit)** : Used for text processing tasks like tokenization and stop-word removal.

- **Requests** : For making HTTP requests to fetch article URLs.

- **BeautifulSoup4** : For parsing HTML and extracting article text.

#### Frontend:

- **HTML5** : Standard markup for the web page structure.

- **Tailwind CSS** : A utility-first CSS framework for rapid UI development (included via CDN).

# How It Works 🧠

The summarization logic follows a classic extractive text mining pipeline:

1. **Content Extraction** : For a given URL, the application uses `requests` to fetch the page's HTML and `BeautifulSoup` to parse it, extracting all text from paragraph (`<p>`) tags.

2. **Text Preprocessing** : The raw text is cleaned using NLTK:

    - It's converted to lowercase.

    - The text is tokenized into individual words.

    - Common "stop words" (like "the", "a", "in") and punctuation are removed, as they don't carry significant meaning.

3. **Word Frequency Calculation** : The application builds a frequency distribution of the remaining meaningful words. This acts as a measure of a word's importance in the text.

4. **Sentence Scoring** : The original text is tokenized into sentences. Each sentence is then assigned a score based on the sum of the frequency scores of the words it contains.

5. **Summary Generation** : The sentences with the highest scores are selected and joined together to form the final, concise summary.

# Setup and Installation

Follow these steps to run the project on your local machine.
1. **Clone the Repository**

        git clone 
        cd News-Summarizer

2. **Create a Virtual Environment**

    It's highly recommended to use a virtual environment to manage project dependencies.

    - **Windows** :

            python -m venv venv
            .\venv\Scripts\activate

    - **macOS / Linux** :

            python3 -m venv venv
            source venv/bin/activate

3. **Install Dependencies**

    Install all the required Python libraries from the requirements.txt file.

        pip install -r requirements.txt

4. **Download NLTK Data**

    The application requires specific data packages from NLTK. Run the following command in your terminal to download them:

        python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

5. **Run the Application**

    Start the Flask development server.

        python app.py

    You should see output indicating the server is running, like this:

    `Running on http://127.0.0.1:5000`
6. **Access the App**

    Open your web browser and navigate to http://127.0.0.1:5000. You can now use the News Article Summarizer!
