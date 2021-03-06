#!/usr/bin/env python
import click

@click.command()
@click.option("--words")
def hello(words): 

    from google.cloud import language_v1

    # Instantiates a client
    client = language_v1.LanguageServiceClient()

    # The text to analyze
    text = words
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

    print("Text: {}".format(text))
    print("Sentiment: {}".format(sentiment.score)) 
    #click.echo(f'Hello {name}!')

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    hello()