

from src.DiamondPricePrediction.pipelines.prediction_pipeline import CustomData

custdataobj =CustomData(1.52,"Premium","F","VS2",62.2,58.0,7.27,7.33,4.55)

data = custdataobj.get_data_as_dataframe()

print(data)