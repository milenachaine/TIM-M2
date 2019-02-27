# Evaluation
## RANDOM FOREST
                precision    recall  f1-score   support

         ent       0.62      0.08      0.14       103
         fin       0.65      0.29      0.40       254
         imm       0.75      0.93      0.83       745
         int       0.75      0.05      0.10        56
         jus       0.61      0.40      0.49       208
         per       0.72      0.82      0.77       396
         soc       0.48      0.52      0.50       256
         trv       0.75      0.93      0.83       444

    micro avg       0.70      0.70      0.70      2462
    macro avg       0.67      0.50      0.51      2462
    weighted avg    0.69      0.70      0.67      2462

    Predicted  ent  fin  imm  int  jus  per  soc  trv  __all__
    Actual                                                    
    ent          8    8   26    1    6    8   20   26      103
    fin          3   74   61    0    7   40   32   37      254
    imm          0    7  690    0    5   30    5    8      745
    int          1    2    7    3    3    5   29    6       56
    jus          1    7   32    0   84   27   36   21      208
    per          0    4   33    0   11  326   11   11      396
    soc          0   10   54    0   20   13  134   25      256
    trv          0    2   11    0    1    3   15  412      444
    __all__     13  114  914    4  137  452  282  546     2462

### Parameters tuning



