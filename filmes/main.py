import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

api_key = '133beb428fb46ca3f2317c6b19bf49ef'
analyzer = SentimentIntensityAnalyzer()

def suggest_movies(i):
    phrase = i
    emotion = analyzer.polarity_scores(phrase)['compound']

    if emotion <= -0.5:
        genre = "18" #Drama
    elif emotion < 0:
        genre = "35" #Comedia
    elif emotion < 0.5:
        genre = "10749" #Romance
    else:
        genre = "27" #Horror

    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&sort_by=popularity.desc&with_genres={genre}&vote_count.gte=4"
    response = requests.get(url).json()

    print(response)

    if response['results']:
        # Pegando os titulos dos filmes
        titles = [result['title'] for result in response['results'][:3]]
        # Pegando as datas dos filmes
        release_date = [result['release_date'] for result in response['results'][:3]]
        # Pegando os votos dos filmes
        vote_average = [result['vote_average'] for result in response['results'][:3]]
        # Pegando os posters dos filmes
        # Definindo a string do prefixo
        prefix = "https://www.themoviedb.org/t/p/w220_and_h330_face/"

        #Concatenar o prefixo com o caminho da imagem do link
        poster_path = [prefix + result['poster_path'].lstrip('/') for result in response['results'][:3]]

        # Retornando os resultados como uma lista
        return [titles, poster_path, release_date, vote_average]






