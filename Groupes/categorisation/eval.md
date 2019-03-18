# EVAL

## Baseline + token
```
python3 classifier.py corpusIrisVersion4.xml
```

                precision    recall  f1-score   support

            ent       0.03      0.03      0.03       103
            fin       0.11      0.10      0.11       254
            imm       0.31      0.30      0.30       745
            int       0.01      0.02      0.02        56
            jus       0.05      0.05      0.05       208
            per       0.15      0.13      0.14       396
            soc       0.09      0.11      0.10       256
            trv       0.18      0.20      0.19       444

        micro avg       0.17      0.17      0.17      2462
        macro avg       0.12      0.12      0.12      2462
     weighted avg       0.18      0.17      0.18      2462

    Predicted  ent  fin  imm  int  jus  per  soc  trv  __all__
    Actual                                                    
    ent          3    9   27    2   12   18   10   22      103
    fin         16   26   74    3   27   32   35   41      254
    imm         33   71  222   18   68  104   91  138      745
    int          2    6   18    1    4    8    4   13       56
    jus          6   15   60    8   10   39   24   46      208
    per         13   43  111   13   31   53   47   85      396
    soc          6   19   63   16   28   38   27   59      256
    trv         17   39  148    9   32   59   52   88      444
    __all__     96  228  723   70  212  351  290  492     2462


## Random Forest + token
```bash
python3 classifier.py -c rf corpusIrisVersion4.xml
```

                precision    recall  f1-score   support

            ent       0.71      0.05      0.09       103
            fin       0.67      0.28      0.39       254
            imm       0.73      0.91      0.81       745
            int       0.67      0.04      0.07        56
            jus       0.56      0.38      0.45       208
            per       0.71      0.79      0.75       396
            soc       0.44      0.48      0.46       256
            trv       0.72      0.90      0.80       444

        micro avg       0.68      0.68      0.68      2462
        macro avg       0.65      0.48      0.48      2462
     weighted avg       0.67      0.68      0.64      2462

    Predicted  ent  fin  imm  int  jus  per  soc  trv  __all__
    Actual                                                    
    ent          5    4   24    0    7   10   19   34      103
    fin          0   70   64    0   10   36   30   44      254
    imm          0    6  678    0    7   33    9   12      745                                                                                                                                                                                     
    int          0    3    8    2    5    6   26    6       56                                                                                                                                                                                     
    jus          1    5   35    0   80   22   42   23      208                                                                                                                                                                                     
    per          0    7   39    0   13  314    9   14      396                                                                                                                                                                                     
    soc          1    8   64    0   19   15  124   25      256                                                                                                                                                                                     
    trv          0    1   11    1    3    7   23  398      444                                                                                                                                                                                     
    __all__      7  104  923    3  144  443  282  556     2462


## Naive Bayes + token
```bash
python3 classifier.py -c nb corpusIrisVersion4.xml
```

                precision    recall  f1-score   support

            ent       0.52      0.13      0.20       103
            fin       0.68      0.36      0.47       254
            imm       0.80      0.87      0.83       745
            int       0.54      0.12      0.20        56
            jus       0.56      0.45      0.50       208
            per       0.66      0.83      0.74       396
            soc       0.48      0.37      0.42       256
            trv       0.66      0.92      0.77       444

        micro avg       0.68      0.68      0.68      2462
        macro avg       0.61      0.51      0.52      2462
     weighted avg       0.67      0.68      0.66      2462

    Predicted  ent  fin  imm  int  jus  per  soc  trv  __all__
    Actual                                                    
    ent         13    7   20    1    7   12    8   35      103
    fin          0   92   32    0   13   45   28   44      254
    imm          1   11  649    0    7   49    6   22      745
    int          1    1    3    7    6    6   20   12       56
    jus          2    6   22    2   93   28   25   30      208
    per          1    7   24    1   15  329    7   12      396
    soc          6   10   55    0   23   16   95   51      256
    trv          1    2    8    2    3   11    9  408      444
    __all__     25  136  813   13  167  496  198  614     2462
        

## LinearSVC + token (corpusIrisVersion4)
```bash
python3 classifier.py -c svm corpusIrisVersion4.xml
```


                precision    recall  f1-score   support

            ent       0.48      0.28      0.36       103
            fin       0.60      0.46      0.52       254
            imm       0.82      0.86      0.84       745
            int       0.44      0.34      0.38        56
            jus       0.53      0.48      0.51       208
            per       0.69      0.76      0.72       396
            soc       0.46      0.48      0.47       256
            trv       0.80      0.89      0.84       444

        micro avg       0.70      0.70      0.70      2462
        macro avg       0.60      0.57      0.58      2462
     weighted avg       0.69      0.70      0.69      2462

    Predicted  ent  fin  imm  int  jus  per  soc  trv  __all__
    Actual                                                    
    ent         29   11   13    3    4    6   16   21      103
    fin          9  118   30    2   13   30   33   19      254
    imm          3   19  641    2   11   44   15   10      745
    int          1    1    4   19    5    7   18    1       56
    jus          3    8   14    2  100   27   39   15      208
    per          2   13   32    5   19  302   10   13      396
    soc         11   14   41    6   30   14  122   18      256
    trv          2   12    5    4    5    9   13  394      444
    __all__     60  196  780   43  187  439  266  491     2462


## LinearSVC + token (sample.xml)
```bash
python3 classifier.py -c svm -f lemma sample.xml

```

                    precision    recall  f1-score   support

                ent       0.27      0.21      0.24        14
                fin       0.41      0.37      0.39        19
                imm       0.80      0.86      0.82        77
                int       0.67      0.29      0.40         7
                jus       0.33      0.29      0.31        17
                per       0.66      0.71      0.68        35
                soc       0.26      0.21      0.23        29
                trv       0.74      0.86      0.79        49

        micro avg       0.63      0.63      0.63       247
        macro avg       0.52      0.47      0.48       247
     weighted avg       0.61      0.63      0.61       247

    Predicted  ent  fin  imm  int  jus  per  soc  trv  __all__
    Actual                                                    
    ent          3    1    5    0    0    0    2    3       14
    fin          2    7    3    0    1    1    3    2       19
    imm          1    0   66    0    2    5    3    0       77
    int          0    0    0    2    0    0    2    3        7
    jus          0    2    2    0    5    3    4    1       17
    per          0    4    0    1    3   25    2    0       35
    soc          4    2    6    0    2    3    6    6       29
    trv          1    1    1    0    2    1    1   42       49
    __all__     11   17   83    3   15   38   23   57      247



## LinearSVC + lemma (sample.xml)
```bash
python3 classifier.py -c svm -f lemma sample.xml

```
                precision    recall  f1-score   support

            ent       0.40      0.14      0.21        14
            fin       0.35      0.32      0.33        19
            imm       0.77      0.90      0.83        77
            int       1.00      0.14      0.25         7
            jus       0.33      0.29      0.31        17
            per       0.73      0.77      0.75        35
            soc       0.29      0.17      0.22        29
            trv       0.65      0.86      0.74        49

        micro avg       0.64      0.64      0.64       247
        macro avg       0.57      0.45      0.45       247
     weighted avg       0.61      0.64      0.60       247

    Predicted  ent  fin  imm  int  jus  per  soc  trv  __all__
    Actual                                                    
    ent          2    4    2    0    1    0    0    5       14
    fin          1    6    6    0    1    0    4    1       19
    imm          0    0   69    0    0    4    2    2       77
    int          0    0    1    1    1    0    2    2        7
    jus          0    1    4    0    5    2    2    3       17
    per          0    2    1    0    3   27    1    1       35
    soc          1    3    6    0    2    3    5    9       29
    trv          1    1    1    0    2    1    1   42       49
    __all__      5   17   90    1   15   37   17   65      247
