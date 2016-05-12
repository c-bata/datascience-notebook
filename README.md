# Data Science

データサイエンスに関する内容をPythonをベースにまとめていきます。

## Setup

#### Requirements

下記の環境を用意してください。

- Python3.5
- GraphViz
- Jupyter Notebook
- Numpy / Scipy / Pandas
- seaborn / matplotlib
- Scikit-learn

```
$ pip install -r requirements.txt -c constraints.txt
```

#### Setup with Docker (Recommended)

Dockerが使える場合は、簡単に環境を用意することができます。
jupyter notebookは[公式でdocker imageを公開](https://github.com/jupyter/docker-stacks/tree/master/datascience-notebook)してくれていますが、
ここにあるNotebooksではいくつかその中に含まれていないパッケージ等を使用しているため、このRepositoryのDockerfileを使用してください。

```
$ docker build -t c-bata/datascience .
$ docker run -p 8888:8888 -v $PWD/notebooks:/home/jovyan/work c-bata/datascience
```


## Contents

追加予定のコンテンツ一覧です。

#### データ加工(Data Wrangling)・可視化

- Pandasの基礎
- Scikit-learnの基礎
- 異常値・外れ値・欠損値
- 可視化(matplotlib, seaborn)

#### 統計(Statistics)と機械学習(Machine Learning)

- 機械学習を勉強していく前に
- 回帰分析
- [決定木](./notebooks/decision-tree.ipynb)
- クラスタリング
- パターン認識
- パラメータ推定
- アンサンブル学習
- 分類器

