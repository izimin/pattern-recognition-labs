# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy
from scipy import interp
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import StratifiedKFold

def cross_validation(dataset, k = 10):
    scores = []
    predicts = []
    data = numpy.array_split(dataset.data, k)
    targets = numpy.array_split(dataset.target, k)
    for i in range(k):
        training_data = data.pop(i)
        training_targets = targets.pop(i)
        #Learning
        classifier = svm.SVC(kernel='linear', C=1).fit(numpy.concatenate(data,0), numpy.concatenate(targets,0))
        #Training
        scores.append(classifier.score(training_data, training_targets))
        predicts.append(classifier.predict(training_data))
        data.insert(i, training_data)
        targets.insert(i, training_targets)
    print('Scores: ', scores)
    print('Average score: ', sum(scores)/len(scores))

def cvROC(dataset):
    X = dataset.data
    y = dataset.target
    X, y = X[y != 2], y[y != 2]
    n_samples, n_features = X.shape
    
    # Add noisy features
    random_state = numpy.random.RandomState(0)
    X = numpy.c_[X, random_state.randn(n_samples, 200 * n_features)]
    cv = StratifiedKFold(n_splits=10)
    classifier = svm.SVC(kernel='linear', probability=True,
                         random_state=random_state)
    
    tprs = []
    aucs = []
    mean_fpr = numpy.linspace(0, 1, 100)
    
    i = 0
    for train, test in cv.split(X, y):
        probas_ = classifier.fit(X[train], y[train]).predict_proba(X[test])
        fpr, tpr, thresholds = roc_curve(y[test], probas_[:, 1])
        tprs.append(interp(mean_fpr, fpr, tpr))
        tprs[-1][0] = 0.0
        roc_auc = auc(fpr, tpr)
        aucs.append(roc_auc)
        plt.plot(fpr, tpr, lw=1, alpha=0.3,
                 label='ROC fold %d (AUC = %0.2f)' % (i, roc_auc))
    
        i += 1
    plt.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r',
             label='Chance', alpha=.8)
    
    mean_tpr = numpy.mean(tprs, axis=0)
    mean_tpr[-1] = 1.0
    mean_auc = auc(mean_fpr, mean_tpr)
    std_auc = numpy.std(aucs)
    plt.plot(mean_fpr, mean_tpr, color='b',
             label=r'Mean ROC (AUC = %0.2f $\pm$ %0.2f)' % (mean_auc, std_auc),
             lw=2, alpha=.8)
    
    std_tpr = numpy.std(tprs, axis=0)
    tprs_upper = numpy.minimum(mean_tpr + std_tpr, 1)
    tprs_lower = numpy.maximum(mean_tpr - std_tpr, 0)
    plt.fill_between(mean_fpr, tprs_lower, tprs_upper, color='grey', alpha=.2,
                     label=r'$\pm$ 1 std. dev.')
    
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    plt.show()