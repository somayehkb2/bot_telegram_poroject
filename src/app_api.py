import requests

def get_movie_info_by_id(movie_id):
    url = f'https://moviesapi.ir/api/v1/movies/{movie_id}'
    response = requests.get(url)
    if response.status_code != 200:
        return 'ERROR'
    else:
        response = response.json()
        title = response['title']
        country = response['country']
        director = response['director']
        year = response['year']
        imdb_rate = response['imdb_rating']

        return (title, country , director, year, imdb_rate)


def get_movie_info_by_name(movie_name):
    url = f'https://moviesapi.ir/api/v1/movies'
    params_dict = {
        'q': movie_name
    }
    response = requests.get(url, params=params_dict)
    if response.status_code != 200:
        return 'ERROR'
    else:
        response = response.json()
        result = response['data'][0]
        title = result['title']
        year = result['year']
        country =  result['country']
        imdb_rate = result['imdb_rating']
        return (title, country , year, imdb_rate)




if __name__ == '__main__':
    # id =  input('Enter Your movie id: ')
    # result = get_movie_info_by_id(id)
    # print(f'result is: {result}')
    movie_name = input('enter movie name: ')
    result = get_movie_info_by_name(movie_name)
    print(f'result: {result}')