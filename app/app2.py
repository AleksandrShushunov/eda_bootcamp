from explainerdashboard import ClassifierExplainer, ExplainerDashboard
import dill


db = ClassifierExplainer.from_file('explainer.dill')
ExplainerDashboard(db).run(host='0.0.0.0', port=9055)
