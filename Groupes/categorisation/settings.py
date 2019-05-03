DOC_CLASS = {
    "immobilier": "imm",
    "travail": "trv",
    "personne et famille": "per",
    "finances, fiscalité et assurance": "fin",
    "rapports à la société": "soc",
    "monde de la justice": "jus",
    "entreprise": "ent",
    "internet, téléphonie et prop. intellectuelle": "int"
}

# FEAUTRE CONFIG
FEATURE_SIZE = 500
FEAT_HELP = """FEATURES:
    token(default),
    lemma,
    lemma+pos,
"""

# CLASSIFIER CONFIG
# SVM CONFIG SVC()
SVM_CONFIG = {
    # 'multi_class': 'ovr',
    # 'penalty': 'l2',
    'decision_function_shape': 'ovr',
    'kernel': 'linear'
}

# # SVM CONFIG LinearSVC()
# SVM_CONFIG = {
#     'multi_class': 'ovr',
#     'penalty': 'l2',
#     # 'decision_function_shape': 'ovr'
# }

# RANDOM FOREST CONFIG
RF_CONFIG = {
    "n_estimators": 130,
    "max_depth": 60,
    "min_samples_split": 10,
    "min_samples_leaf": 2,
    "random_state": 10,
}

# NAVIE BAYES CONFIG
NB_CONFIG = {
    "alpha": 1.0,
    "fit_prior": True,
    "class_prior": None,
    "norm": False
}

# regression logistique
LR_CONFIG = {
    "penalty": "l2",
    "class_weight": "balanced",
    "C": 0.1,
    "fit_intercept": True,
    "solver": "newton-cg",
    "multi_class": "multinomial",
}   # 0.76

# GBDT_CONGIF = {
#
#
# }
#
# MLP_CONFIG = {
#
# }

CLF_PARAM = {
    "rf": RF_CONFIG,
    "svm": SVM_CONFIG,
    # "nb": NB_CONFIG,
    "lr": LR_CONFIG,
    # "gbdt": GBDT_CONGIF,
    # "mlp": MLP_CONFIG,
    "dummy": dict(),
}
# CLF_HELP = """CLASSIFIERS:
#     lr = logistic regression,
#     rf = random forest,
#     svm = linearSVC, linear support vector classification,
#     nb = navie bayes,
#     dummy(default) =  baseline classifier
# """

CLF_HELP = """CLASSIFIERS:
    lr = logistic regression,
    rf = random forest,
    svm = SVC, support vector classification,
    dummy(default) =  baseline classifier
"""