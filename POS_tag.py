#!/usr/bin/env python
# coding: utf8
"""A simple example of extracting relations between phrases and entities using
spaCy's named entity recognizer and the dependency parse. Here, we extract
money and currency values (entities labelled as MONEY) and then check the
dependency tree to find the noun phrase they are referring to – for example:
$9.4 million --> Net income.
Compatible with: spaCy v2.0.0+
"""
from __future__ import unicode_literals, print_function

import plac
import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()

TEXTS = [
    '$23.4 million was the net income compared to the prior year of $2.7 million.',
    'Revenue exceeded twelve billion dollars, with a loss of $1b.',
]

#
# @plac.annotations(
#     model=("Model to load (needs parser and NER)", "positional", None, str))

def main(model='en_core_web_sm'):
    # nlp = spacy.load(model)
    print("Loaded model '%s'" % model)
    print("Processing %d texts" % len(TEXTS))

    for text in TEXTS:
        doc = nlp(text)
        relations = extract_currency_relations(doc)
        for r1, r2 in relations:
            print('{:<10}\t{}\t{}'.format(r1.text, r2.ent_type_, r2.text))


def extract_currency_relations(doc):
    # merge entities and noun chunks into one token
    spans = list(doc.ents) + list(doc.noun_chunks)
    for span in spans:
        span.merge()

    relations = []
    for money in filter(lambda w: w.ent_type_ == 'MONEY', doc):
        if money.dep_ in ('attr', 'dobj'):
            subject = [w for w in money.head.lefts if w.dep_ == 'nsubj']
            if subject:
                subject = subject[0]
                relations.append((subject, money))
        elif money.dep_ == 'pobj' and money.head.dep_ == 'prep':
            relations.append((money.head.head, money))
    return relations


if __name__ == '__main__':
    plac.call(main)
    print("\n\n\n")
    doc = nlp(u'Lately i feel I am short of breath')

    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)
        if(token.dep_ == 'dobj'):
            medicine = token


    print("Prescribing: " + str(token))

    # Expected output:
    # Net income      MONEY   $9.4 million
    # the prior year  MONEY   $2.7 million
    # Revenue         MONEY   twelve billion dollars
    # a loss          MONEY   1b