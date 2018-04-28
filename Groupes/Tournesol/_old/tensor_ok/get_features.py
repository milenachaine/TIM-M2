features = {
            'selon': 'numeric',
            'impers': 'numeric',
            'ponctuation' : 'numeric',
           }

def getfeature(lemmes, feature_name):

    # arthur
    if feature_name == 'selon':
        nb_selon = 0
        nb_selon += lemmes.count('selon')
        return nb_selon

    # damien
    if feature_name == 'impers':
        nb_impers = 0
        nb_impers += lemmes.count("on")
        nb_impers += lemmes.count("nous")
        return nb_impers

    if feature_name == 'ponctuation':
        nb_ponct = 0
        for lemme in lemmes:
            if lemme in "'(),-:;[]–—…" or lemme == "...":
                nb_ponct += 1
        return nb_ponct

    return None
