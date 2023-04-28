# NLTK Tree permutation API

API that provides variants of new tree with given NLTK tree

## How to run

```shell
git clone https://github.com/Nexxel05/nltk_tree_permutator.git
cd nltk_tree_permutator
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
Create .env file in root directory and store there your 
SECRET_KEY like shown in .env_sample

```
python manage.py migrate
python manage.py runserver
```

## URL example
localhost:<port>/paraphrase?tree=(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP
Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP
(JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ
trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS
restaurants) ) ) ) ) ) ) )

,where localhost is your localhost and port is your port