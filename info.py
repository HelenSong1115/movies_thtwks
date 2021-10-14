import pandas as pd
from datetime import datetime


genome_scores_path = "./data/genome-scores.csv"
genome_tags_path = "./data/genome-tags_path.csv"
links_path = "./data/links.csv"
movies_path = "./data/movies.csv"
ratings_path = "./data/ratings.csv"
tags_path = "./data/tags.csv"



#todo 抽取所有不同用户
def get_user_count(tags_path=tags_path, ratings_path=ratings_path):
    ratings = pd.read_csv(ratings_path)
    user = ratings["userId"]
    
    tags = pd.read_csv(tags_path)
    user_t = tags["userId"]
    user.append(user_t)
    return user.unique().size


#todo 抽取不同电影的个数
def get_movie_count(movies_path=movies_path):
    movies = pd.read_csv(movies_path)
    movies_id = movies["movieId"]
    return movies_id.unique().size


#todo 抽取不同的电影种类
def get_genre_count(movies_path=movies_path):
    movies = pd.read_csv(movies_path)
    genres_s = movies["genres"]
    genress = genres_s.str.split(pat="|")       # 将给定体裁表按照|划分
    genres = pd.Series([genre for _, genre_list in genress.items() for genre in genre_list], name="genres")   # 所有体裁组成一个list（包含重复）
    genres = genres.unique().tolist()
    genres.remove('(no genres listed)')     #! 认为没有题材不算一个题材，如果认为算，删掉此行即可
    return len(genres)
    

#todo 抽取没有外部链接电影个数
def get_nolink_count(links_path=links_path):
    links = pd.read_csv(links_path)
    movies_count = links["movieId"].unique().size
    imdbId = links["imdbId"].unique().size
    tmdbId = links["tmdbId"].unique().size
    link_count = movies_count - tmdbId
    return link_count


#todo 抽取2018年进行过电影评分的用户数
def get_score_count(ratings_path=ratings_path):
    ratings = pd.read_csv(ratings_path)
    start_time = datetime(2018, 1, 1, 0, 0).timestamp()
    end_time = datetime(2019, 1, 1, 0, 0).timestamp()-1
    item = ratings.loc[(ratings["timestamp"] >= start_time)&(ratings["timestamp"] <= end_time)]
    userid = item['userId']
    return userid.unique().size


if __name__ == "__main__":
    user_count = get_user_count()
    print("所有用户个数：" + str(user_count))
    movie_count = get_movie_count()
    print("所有电影个数：" + str(movie_count))
    genres_count = get_genre_count()
    print("所有题材个数：", str(genres_count))
    nolink_count = get_nolink_count()
    print("没有外部链接的电影个数：" + str(nolink_count))
    userstar_count = get_score_count()
    print("2018年进行过评分的用户数：" + str(userstar_count))
    
    