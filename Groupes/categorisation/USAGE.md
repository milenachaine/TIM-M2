# USAGE

    usage: classifier.py [-h] [-c {rf,svm,nb,dummy}] [-f {token,lemma,ngram}]
                        [-s FEATURE_SIZE] [-o OUTPUT]
                        corpus

    positional arguments:
    corpus

    optional arguments:
    -h, --help            show this help message and exit
    -c {rf,svm,nb,dummy}, --classifier {rf,svm,nb,dummy}
                            CLASSIFIERS:
                                rf = random forest,
                                svm = linearSVC, linear support vector classification,
                                nb = navie bayes,
                                dummy(default) =  baseline classifier
    -f {token,lemma,ngram}, --features {token,lemma,ngram}
                            FEATURES:
                                token(default),
                                lemma,
                                ngram
    -s FEATURE_SIZE, --feature_size FEATURE_SIZE
    -o OUTPUT, --output OUTPUT
