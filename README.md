# P7_API
documents utiles au déploiement de l'API de prédiction de proba de non solvabilité

## Pour une utilisation en local de l'API
```sh
$ git clone https://github.com/elbo7777/P7_API.git
$ git cd P7_API
$ python3 -m venv P7_API
$ pip install -r requirements.txt
```
dans un navigateur internet : 
- pour accéder à la homepage : http://localhost:5000
- pour tester sur un client (identifiant 100001 par exemple) : http://localhost:5000/scores?index=100001

## éxécution sur le web en production via heroku : 
- pour accéder à la homepage : https://p7lboapi.herokuapp.com
- pour tester sur un client (identifiant 100001 par exemple) : https://p7lboapi.herokuapp.com/scores?index=100001
