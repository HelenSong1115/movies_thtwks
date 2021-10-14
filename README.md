# 代码说明

info.py脚本中的每一个函数分别完成了所要求的5个题目

## 环境依赖

pandas1.2.5   ---->> pip install pandas=1.2.5



## 相关题目说明

### 第三题读取电影题材

从文档中读取的19中电影题材如下。

> ['Adventure' 'Animation' 'Children' 'Comedy' 'Fantasy' 'Romance' 'Drama' 'Action' 'Crime' 'Thriller' 'Horror' 'Mystery' 'Sci-Fi' 'IMAX' 'Documentary' 'War' 'Musical' 'Western' 'Film-Noir' '(no genres listed)']

但是根据官方文档里面显示的题材种类如下，从movies.csv读取的电影题材和官方文档不一致

> ```
> Genres are a pipe-separated list, and are selected from the following:
> 
> * Action
> * Adventure
> * Animation
> * Children's
> * Comedy
> * Crime
> * Documentary
> * Drama
> * Fantasy
> * Film-Noir
> * Horror
> * Musical
> * Mystery
> * Romance
> * Sci-Fi
> * Thriller
> * War
> * Western
> * (no genres listed)
> ```
