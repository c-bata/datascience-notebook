import numpy as np
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt


def plot_result(clf, clf_name, df):    
    X = df[['x','y']]
    Y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=.4, random_state=40)
    n_classes = len(Y.unique())
    cm = plt.cm.RdBu
    plot_colors = "rbym"
    plot_markers = "o^v*"
    plot_step = 0.02
    
    x_min, x_max = X.ix[:, 0].min() - .5, X.ix[:, 0].max() + .5
    y_min, y_max = X.ix[:, 1].min() - .5, X.ix[:, 1].max() + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                             np.arange(y_min, y_max, plot_step))
    
    clf.fit(X_train,y_train)    
    score = clf.score(X_test, y_test)

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    cs = plt.contourf(xx, yy, Z, cmap=cm,  alpha=.5)

    # 学習用の点をプロット
    for i, color, m in zip(range(n_classes), plot_colors, plot_markers):
        plt.scatter(X[Y==i].x, X[Y==i].y, c=color, label=i, cmap=cm, marker=m, s=80)

    plt.text(xx.max() - .3, yy.min() + .3, ('%.2f' % score).lstrip('0'),
                    size=15, horizontalalignment='right')        
    plt.title(clf_name)

