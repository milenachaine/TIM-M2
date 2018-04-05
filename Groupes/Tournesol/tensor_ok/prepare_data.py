#!/bin/python3
#coding : utf8

"""
Pour la préparation du corpus, implémente des méthodes tirées de
https://www.tensorflow.org/get_started/get_started_for_beginners
"""

from lxml import etree
import pandas as pd
import tensorflow as tf

from get_features import getfeature, features


FEATURE_KEYS = sorted(list(features.keys()))
COLUMN_NAMES = FEATURE_KEYS + ["label"]
LABELS = ["fake", "trusted", "parodic"]


def load_data(fichier):
    """Préparation des données"""
    with open(fichier, encoding="utf-8") as f:
        tree = etree.parse(f)

        document_label = [LABELS.index(doc.get("class")) for doc in tree.xpath("//doc")]

        data = list()
        for i, doc in enumerate(tree.xpath("//treetagger")):
            lemmes = list()
            for token in (doc.text).split(' '):
                token_split = token.split('/')
                lemme = token_split[2]
                if token_split[2] == "<unknown>":
                    lemme = token_split[0].lower()
                lemmes.append(lemme)

            data.append([getfeature(lemmes, feature) for feature in FEATURE_KEYS]
                        + [document_label[i]])

    donnees = pd.DataFrame(data,columns=COLUMN_NAMES)
    donnees_x, donnees_y = donnees, donnees.pop("label")

    return (donnees_x, donnees_y)


def train_input_fn(features, labels, batch_size):
    """An input function for training"""
    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    # Shuffle, repeat, and batch the examples.
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)

    # Return the dataset.
    return dataset


def eval_input_fn(features, labels, batch_size):
    """An input function for evaluation or prediction"""
    features=dict(features)
    if labels is None:
        # No labels, use only features.
        inputs = features
    else:
        inputs = (features, labels)

    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices(inputs)

    # Batch the examples
    assert batch_size is not None, "batch_size must not be None"
    dataset = dataset.batch(batch_size)

    # Return the dataset.
    return dataset
