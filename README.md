# DataScience Notebook

データサイエンスに関する内容をPythonをベースにまとめていきます。
もし間違いやTypoがあればIssue/PRお待ちしております。

## Contents

今後も変更する予定がありますが、とりあえず現在追加を考えているものも含めています。

#### データ加工(Data Wrangling)・可視化

- [JupyterNotebook / numpy / pandas / matplotlib 入門](./notebooks/getting-started.ipynb)
- Seabornを使った可視化
- 異常値・外れ値・欠損値
- 次元削減(主成分分析)

#### 統計(Statistics)と機械学習(Machine Learning)

- 機械学習を勉強していく前に
- 回帰分析
- [決定木](./notebooks/decision-tree.ipynb)
- クラスタリング
- トピックモデル
- パターン認識
- パラメータ推定
- アンサンブル学習
- 分類器

#### 応用例

- 日本語文書の感情分析(Sentiment Analysis)
- 日本語文書の分類(bag-of-word)
- レコメンド
- 画像のパターン認識


## SlideShow

notebookの「View」>「Cell Toolbar」>「SlideShow」からスライドショーにした時の表示方法を編集できます。
ここに追加しているnotebooksはスライドショーの表示にも対応しているため、下記のコマンドによってスライド形式で表示することが可能です。

```
$ ipython nbconvert --to slides notebooks/getting-started.ipynb --post serve
```


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

Dockerを使って簡単に環境を用意することができます。
jupyter notebookは[公式でdocker imageを公開](https://github.com/jupyter/docker-stacks/tree/master/datascience-notebook)してくれていますが、
ここにあるNotebooksでは一部その中に含まれていないパッケージ等を使用しているため、このRepositoryのDockerfileを使用してください。

```
$ docker build -t c-bata/datascience .
$ docker run -p 8888:8888 -v $PWD/notebooks:/home/jovyan/work c-bata/datascience
```

