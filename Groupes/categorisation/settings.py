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
    ngram
"""

# CLASSIFIER CONFIG
# SVM CONFIG
SVM_CONFIG = {
    # 'multi_class': 'ovr',
    # 'penalty': 'l2',
    'decision_function_shape': 'ovr'
}

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

LR_CONFIG = {


}

GBDT_CONGIF = {


}

MLP_CONFIG = {

}

CLF_PARAM = {
    "rf": RF_CONFIG,
    "svm": SVM_CONFIG,
    "nb": NB_CONFIG,
    "lr": LR_CONFIG,
    "gbdt": GBDT_CONGIF,
    "mlp": MLP_CONFIG,
    "dummy": dict(),
}
CLF_HELP = """CLASSIFIERS:
    rf = random forest,
    svm = linearSVC, linear support vector classification,
    nb = navie bayes,
    dummy(default) =  baseline classifier
"""