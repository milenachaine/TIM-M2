# Evaluation
## RANDOM FOREST
              precision    recall  f1-score   support

         int       1.00      0.96      0.98       100
         fin       1.00      0.96      0.98       251
         ent       0.93      1.00      0.96       808
         jus       1.00      1.00      1.00        60
         trv       1.00      0.96      0.98       206
         imm       0.97      0.96      0.96       442
         per       0.97      0.95      0.96       292
         soc       1.00      0.96      0.98       636

        micro avg       0.97      0.97      0.97      2795
        macro avg       0.98      0.97      0.98      2795
        weighted avg       0.97      0.97      0.97      2795

### Parameters tuning
- BEST SCORE:  0.9866190900981266
- BEST PARAMETERS:  {'rf__oob_score': True, 'rf__n_estimators': 60, 'rf__random_state': 10}

                precision    recall  f1-score   support

         per       1.00      0.78      0.88         9
         ent       1.00      0.96      0.98        25
         imm       1.00      1.00      1.00        82
         fin       1.00      1.00      1.00         7
         soc       1.00      1.00      1.00        17
         int       0.98      1.00      0.99        49
         trv       1.00      1.00      1.00        23
         jus       0.97      1.00      0.99        69

        micro avg       0.99      0.99      0.99       281
        macro avg       0.99      0.97      0.98       281
        weighted avg    0.99      0.99      0.99       281


