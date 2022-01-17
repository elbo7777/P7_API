import pickle
import flask
import pandas as pd

# Load our model with pickle (adresses may be changed for serialisation)
model = pickle.load(open('banking_model.md', 'rb'))
# Load data test sample (index_col = 0 to keep id of loan)
# df_test_sample = pd.read_csv('app_test_1000.csv', sep=',', index_col=0, encoding='utf8')
df_test_sample = pd.read_csv('app_test_1000.csv', index_col = 0, encoding = 'utf8')

# Drop predict last column predict proba of our dataframe not used here
df_test_sample.drop(columns = 'TARGET', inplace = True)

# On définit le seuil de non solvabilité => si proba > seuil alors non solvable
seuil = 0.10
# defining flask pages
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# definig home page
@app.route('/', methods=['GET'])
def home():
    return "<h1>Deploiement API LBo</h1><p>project 7 OpenClassRooms formation DataScientist.</p>"
# defining page for the results of a prediction via index
@app.route('/scores', methods=['GET'])
def predict():
    # get the index from a request
    data_index = flask.request.args.get('index')
    # get inputs features from the data with index. Carreful you must pass data_index in int!! Last column must be drop when calling the model
    input = df_test_sample.loc[int(data_index), :]
    # predict probability score. Carreful you must reshape your input data since we have only one sample!!
    model_prediction = model.predict_proba(input.values.reshape(1,-1))
    # create a dictionnary to janosify. We get the probability to be positive and evaluate if the credit is accepted (1) or denied (0)!
    # careful bool object must be transformed in int for JSON format!
    # dict_result = {'ID Client':int(data_index), 'Credit_score': model_prediction[:,1][0], 'Réponse (1 : Non Solvable 0 Solvable)': int(model_prediction[:,1][0] < treshold)}
    dict_result = {'Credit_score': model_prediction[:,1][0], 'Reponse (1 : Solvable 0 Non Solvable)': int(model_prediction[:,1][0] < seuil),'ID Client':int(data_index), }
    return flask.jsonify(dict_result)

# define endpoint for Flask
app.add_url_rule('/scores', 'scores', predict)

# add command for running the application on cloud with Heroku
if __name__ == '__main__':
    ## Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
