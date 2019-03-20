# EVAL

## LinearSVC + lemma+pos (500)
```bash
python3 classifier.py -c svm -f lemma+pos corpus
```

                precision    recall  f1-score   support

            ent       0.52      0.24      0.33        95
            fin       0.65      0.47      0.54       254
            imm       0.81      0.91      0.86       750
            int       0.50      0.25      0.33        53
            jus       0.58      0.45      0.51       201
            per       0.72      0.79      0.75       388
            soc       0.46      0.46      0.46       269
            trv       0.81      0.91      0.86       450

        micro avg       0.72      0.72      0.72      2460
        macro avg       0.63      0.56      0.58      2460
     weighted avg       0.70      0.72      0.70      2460

    Predicted  ent  fin  imm  int  jus  per  soc  trv  __all__
    Actual                                                    
    ent         23    6   15    3    4    9   16   19       95
    fin          9  119   41    1    8   34   24   18      254
    imm          3   12  685    0    7   22   11   10      750
    int          1    1    3   13    2    5   25    3       53
    jus          2    8   23    3   91   24   42    8      201
    per          0   14   32    3   17  306   12    4      388
    soc          5   20   42    2   17   24  124   35      269
    trv          1    4    7    1   10    3   13  411      450
    __all__     44  184  848   26  156  427  267  508     2460

## LinearSVC + lemma+pos (1000)
```bash
python3 classifier.py -c svm -f lemma+pos -s 1000 corpus
```
                precision    recall  f1-score   support

            ent       0.57      0.38      0.46        95
            fin       0.68      0.53      0.60       254
            imm       0.85      0.92      0.88       750
            int       0.70      0.30      0.42        53
            jus       0.62      0.49      0.55       201
            per       0.75      0.84      0.79       388
            soc       0.55      0.55      0.55       269
            trv       0.85      0.93      0.89       450

        micro avg       0.76      0.76      0.76      2460
        macro avg       0.69      0.62      0.64      2460
     weighted avg       0.75      0.76      0.75      2460

    Predicted  ent  fin  imm  int  jus  per  soc  trv  __all__
    Actual                                                    
    ent         36    5   14    3    4    9   11   13       95
    fin          9  135   37    0    8   30   21   14      254
    imm          3   12  692    0    7   17   11    8      750
    int          1    0    4   16    2    5   23    2       53
    jus          3    9   17    2   98   25   41    6      201
    per          2   16   17    1   16  325    7    4      388
    soc          5   18   30    0   19   22  149   26      269
    trv          4    4    6    1    4    2   10  419      450
    __all__     63  199  817   23  158  435  273  492     2460
    

## LinearSVC + lemma
```bash
python3 classifier.py -c svm -f lemma corpus
```
    
                precision    recall  f1-score   support

            ent       0.48      0.33      0.39        95
            fin       0.64      0.48      0.55       254
            imm       0.84      0.90      0.87       750
            int       0.43      0.38      0.40        53
            jus       0.54      0.47      0.50       201
            per       0.72      0.78      0.75       388
            soc       0.47      0.45      0.46       269
            trv       0.82      0.91      0.87       450

        micro avg       0.72      0.72      0.72      2460
        macro avg       0.62      0.59      0.60      2460
     weighted avg       0.71      0.72      0.71      2460

    Predicted  ent  fin  imm  int  jus  per  soc  trv  __all__
    Actual                                                    
    ent         31    7   11    5    6    9   14   12       95
    fin         11  121   36    2   12   31   25   16      254
    imm          5   13  677    2    8   21   13   11      750
    int          2    0    1   20    2    6   19    3       53
    jus          4    8   19    2   94   26   42    6      201
    per          0   14   25    9   21  304    9    6      388
    soc          9   22   34    5   21   24  120   34      269
    trv          3    3    5    1   10    3   14  411      450
    __all__     65  188  808   46  174  424  256  499     2460


## LinearSVC + token
```bash
python3 classifier.py -c svm corpus
```
                precision    recall  f1-score   support

            ent       0.47      0.35      0.40        95
            fin       0.63      0.49      0.55       254
            imm       0.82      0.89      0.85       750
            int       0.35      0.26      0.30        53
            jus       0.57      0.47      0.51       201
            per       0.73      0.79      0.75       388
            soc       0.49      0.45      0.47       269
            trv       0.78      0.89      0.83       450

        micro avg       0.71      0.71      0.71      2460
        macro avg       0.60      0.57      0.58      2460
     weighted avg       0.70      0.71      0.70      2460

    Predicted  ent  fin  imm  int  jus  per  soc  trv  __all__
    Actual                                                    
    ent         33    8   13    4    4    7   11   15       95
    fin         11  124   34    0   10   30   24   21      254
    imm          6   15  665    1    7   23   21   12      750
    int          4    1    4   14    2    6   15    7       53
    jus          5    8   20    2   94   25   34   13      201
    per          1   13   29    6   19  305    8    7      388
    soc          5   22   38   10   17   18  120   39      269
    trv          5    7    4    3   12    6   14  399      450
    __all__     70  198  807   40  165  420  247  513     2460


## Random Forest + token
```bash
python3 classifier.py -c rf corpus
```

                precision    recall  f1-score   support

            ent       0.70      0.07      0.13        95
            fin       0.62      0.29      0.39       254
            imm       0.74      0.93      0.82       750
            int       0.80      0.08      0.14        53
            jus       0.65      0.41      0.50       201
            per       0.68      0.79      0.73       388
            soc       0.49      0.43      0.46       269
            trv       0.71      0.91      0.80       450

        micro avg       0.69      0.69      0.69      2460
        macro avg       0.67      0.49      0.50      2460
     weighted avg       0.68      0.69      0.65      2460

    Predicted  ent  fin  imm  int  jus  per  soc  trv  __all__
    Actual                                                    
    ent          7    5   21    1    4   12   12   33       95
    fin          2   73   68    0    8   42   26   35      254
    imm          0    8  695    0    5   22    9   11      750
    int          0    2    5    4    2    7   21   12       53
    jus          1    5   35    0   83   26   31   20      201
    per          0    5   49    0    5  308    8   13      388
    soc          0   16   53    0   16   29  116   39      269
    trv          0    4    9    0    5    8   16  408      450
    __all__     10  118  935    5  128  454  239  571     2460

## Random Forest + lemma
```bash
python3 classifier.py -c rf -f lemma corpus
```
                precision    recall  f1-score   support

            ent       0.56      0.05      0.10        95
            fin       0.65      0.33      0.44       254
            imm       0.76      0.94      0.84       750
            int       0.25      0.02      0.04        53
            jus       0.60      0.39      0.47       201
            per       0.69      0.79      0.74       388
            soc       0.47      0.45      0.46       269
            trv       0.75      0.92      0.83       450

        micro avg       0.70      0.70      0.70      2460
        macro avg       0.59      0.49      0.49      2460
     weighted avg       0.67      0.70      0.66      2460

    Predicted  ent  fin  imm  int  jus  per  soc  trv  __all__
    Actual                                                    
    ent          5    8   12    1    4   10   16   39       95
    fin          0   84   67    1    8   39   24   31      254
    imm          1    6  705    0    4   18    7    9      750
    int          0    2    5    1    1    6   32    6       53
    jus          2    9   36    1   78   26   32   17      201
    per          0    3   45    0   12  307   12    9      388
    soc          1   14   54    0   21   28  121   30      269
    trv          0    4    7    0    3    8   13  415      450
    __all__      9  130  931    4  131  442  257  556     2460

## Random Forest + lemma
```bash
python3 classifier.py -c rf -f lemma+pos corpus
```
                precision    recall  f1-score   support

            ent       0.80      0.04      0.08        95
            fin       0.64      0.34      0.44       254
            imm       0.75      0.94      0.83       750
            int       0.33      0.04      0.07        53
            jus       0.64      0.38      0.48       201
            per       0.70      0.78      0.74       388
            soc       0.47      0.45      0.46       269
            trv       0.72      0.92      0.81       450

        micro avg       0.69      0.69      0.69      2460
        macro avg       0.63      0.49      0.49      2460
     weighted avg       0.68      0.69      0.66      2460

    Predicted  ent  fin  imm  int  jus  per  soc  trv  __all__
    Actual                                                    
    ent          4    3   19    1    4   12   13   39       95
    fin          0   86   65    1    6   37   24   35      254
    imm          0    8  703    0    3   14    9   13      750
    int          0    2    7    2    2    6   27    7       53
    jus          0   10   34    1   77   28   34   17      201
    per          0    7   46    0    9  303   12   11      388
    soc          0   15   53    1   16   27  121   36      269
    trv          1    4    7    0    4    7   15  412      450
    __all__      5  135  934    6  121  434  255  570     2460

## NB + lemma+pos
```bash
python3 classifier.py -c nb -f lemma+pos corpus
```
                precision    recall  f1-score   support

            ent       0.60      0.16      0.25        95
            fin       0.66      0.40      0.50       254
            imm       0.82      0.89      0.86       750
            int       0.64      0.13      0.22        53
            jus       0.62      0.48      0.54       201
            per       0.69      0.84      0.76       388
            soc       0.47      0.38      0.42       269
            trv       0.70      0.94      0.80       450

        micro avg       0.71      0.71      0.71      2460
        macro avg       0.65      0.53      0.54      2460
     weighted avg       0.69      0.71      0.68      2460

    Predicted  ent  fin  imm  int  jus  per  soc  trv  __all__
    Actual                                                    
    ent         15    7   15    1    5   12    7   33       95
    fin          3  101   41    0    8   43   20   38      254
    imm          1   11  670    0    7   31   10   20      750
    int          2    0    2    7    2    4   29    7       53
    jus          1    9   17    1   97   25   31   20      201
    per          0    6   21    1   14  327    8   11      388
    soc          2   17   43    1   20   30  103   53      269
    trv          1    2    5    0    4    5    9  424      450
    __all__     25  153  814   11  157  477  217  606     2460

## NB + token
```bash
python3 classifier.py -c nb corpus
```

                precision    recall  f1-score   support

            ent       0.55      0.13      0.21        95
            fin       0.68      0.34      0.45       254
            imm       0.82      0.90      0.86       750
            int       0.42      0.09      0.15        53
            jus       0.57      0.47      0.51       201
            per       0.65      0.85      0.74       388
            soc       0.52      0.35      0.42       269
            trv       0.68      0.94      0.79       450

        micro avg       0.70      0.70      0.70      2460
        macro avg       0.61      0.51      0.52      2460
     weighted avg       0.68      0.70      0.67      2460

    Predicted  ent  fin  imm  int  jus  per  soc  trv  __all__
    Actual                                                    
    ent         12    4   17    0    6   14    9   33       95
    fin          2   86   40    0    9   52   22   43      254
    imm          1    8  675    0    9   32    6   19      750
    int          2    0    3    5    4    7   17   15       53
    jus          2    7   17    1   94   29   23   28      201
    per          0    5   22    3   16  329    6    7      388
    soc          1   15   48    2   23   30   93   57      269
    trv          2    1    6    1    4   11    2  423      450
    __all__     22  126  828   12  165  504  178  625     2460
