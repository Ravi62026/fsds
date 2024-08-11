import os
import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
from src.DiamondPricePrediction.utils.utils import load_object
import dagshub

os.environ['MLFLOW_TRACKING_URI'] = 'https://dagshub.com/rs1806105/fsds.mlflow'
os.environ['MLFLOW_TRACKING_USERNAME'] = 'rs1806105'
os.environ['MLFLOW_TRACKING_PASSWORD'] = '46c8605b7155b7140215c1c01d0a1523bf3aba24'

class ModelEvaluation:
    def __init__(self):
        pass

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def initiate_model_evaluation(self, test_array):
        try:
            X_test, y_test = test_array[:, :-1], test_array[:, -1]

            model_path = os.path.join("artifacts", "model.pkl")
            model = load_object(model_path)

            # dagshub.init(repo_owner='rs1806105', repo_name='fsds', mlflow=True)

            # mlflow.set_tracking_uri("https://dagshub.com/rs1806105/fsds.mlflow")
            # tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

            # print(f"Tracking URL Type: {tracking_url_type_store}")

            # with mlflow.start_run():
            #     predicted_qualities = model.predict(X_test)

            #     rmse, mae, r2 = self.eval_metrics(y_test, predicted_qualities)

            #     mlflow.log_metric("rmse", rmse)
            #     mlflow.log_metric("r2", r2)
            #     mlflow.log_metric("mae", mae)

                # signature = mlflow.models.infer_signature(X_test, predicted_qualities)

                # if tracking_url_type_store != "file":

                #     # Register the model
                #     # There are other ways to use the Model Registry, which depends on the use case,
                #     # please refer to the doc for more information:
                #     # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                #     mlflow.sklearn.log_model(model, "model", registered_model_name="my_model", signature=signature)
                # # it is for the local 
                # else:
                #     mlflow.sklearn.log_model(model, "model", signature=signature)
                

        except Exception as e:
            print(f"Error occurred: {e}")
            raise e
