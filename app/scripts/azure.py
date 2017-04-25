import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'tBodyAcc-Mean-1': "0",
                            'tBodyAcc-Mean-2': "10000",
                            'tBodyAcc-Mean-3': "0",
                            'tBodyAcc-STD-1': "1",
                            'tBodyAcc-STD-2': "1",
                            'tBodyAcc-STD-3': "1",
                            'tBodyAcc-Mad-1': "1",
                            'tBodyAcc-Mad-2': "1",
                            'tBodyAcc-Mad-3': "1",
                            'tBodyAcc-Max-1': "1",
                            'tBodyAcc-Max-2': "1",
                            'tBodyAcc-Max-3': "1",
                            'tBodyAcc-Min-1': "1",
                            'tBodyAcc-Min-2': "1",
                            'tBodyAcc-Min-3': "1",
                            'tBodyAcc-SMA-1': "1",
                            'tBodyAcc-Energy-1': "1",
                            'tBodyAcc-Energy-2': "1",
                            'tBodyAcc-Energy-3': "1",
                            'tBodyAcc-IQR-1': "1",
                            'tBodyAcc-IQR-2': "1",
                            'tBodyAcc-IQR-3': "1",
                            'tBodyAcc-ropy-1': "1",
                            'tBodyAcc-ropy-2': "1",
                            'tBodyAcc-ropy-3': "1",
                            'tBodyAcc-ARCoeff-1': "1",
                            'tBodyAcc-ARCoeff-2': "1",
                            'tBodyAcc-ARCoeff-3': "1",
                            'tBodyAcc-ARCoeff-4': "1",
                            'tBodyAcc-ARCoeff-5': "1",
                            'tBodyAcc-ARCoeff-6': "1",
                            'tBodyAcc-ARCoeff-7': "1",
                            'tBodyAcc-ARCoeff-8': "1",
                            'tBodyAcc-ARCoeff-9': "1",
                            'tBodyAcc-ARCoeff-10': "1",
                            'tBodyAcc-ARCoeff-11': "1",
                            'tBodyAcc-ARCoeff-12': "1",
                            'tBodyAcc-Correlation-1': "1",
                            'tBodyAcc-Correlation-2': "1",
                            'tBodyAcc-Correlation-3': "1",
                            'tBodyAccMag-Mean-1': "1",
                            'tBodyAccMag-STD-1': "1",
                            'tBodyAccMag-Mad-1': "1",
                            'tBodyAccMag-Max-1': "1",
                            'tBodyAccMag-Min-1': "1",
                            'tBodyAccMag-SMA-1': "1",
                            'tBodyAccMag-Energy-1': "1",
                            'tBodyAccMag-IQR-1': "1",
                            'tBodyAccMag-ropy-1': "1",
                            'tBodyAccMag-ARCoeff-1': "1",
                            'tBodyAccMag-ARCoeff-2': "1",
                            'tBodyAccMag-ARCoeff-3': "1",
                            'tBodyAccMag-ARCoeff-4': "1",
                            'fBodyAcc-Mean-1': "1",
                            'fBodyAcc-Mean-2': "1",
                            'fBodyAcc-Mean-3': "1",
                            'fBodyAcc-STD-1': "1",
                            'fBodyAcc-STD-2': "1",
                            'fBodyAcc-STD-3': "1",
                            'fBodyAcc-Mad-1': "1",
                            'fBodyAcc-Mad-2': "1",
                            'fBodyAcc-Mad-3': "1",
                            'fBodyAcc-Max-1': "1",
                            'fBodyAcc-Max-2': "1",
                            'fBodyAcc-Max-3': "1",
                            'fBodyAcc-Min-1': "1",
                            'fBodyAcc-Min-2': "1",
                            'fBodyAcc-Min-3': "1",
                            'fBodyAcc-SMA-1': "1",
                            'fBodyAcc-Energy-1': "1",
                            'fBodyAcc-Energy-2': "1",
                            'fBodyAcc-Energy-3': "1",
                            'fBodyAcc-IQR-1': "1",
                            'fBodyAcc-IQR-2': "1",
                            'fBodyAcc-IQR-3': "1",
                            'fBodyAcc-ropy-1': "1",
                            'fBodyAcc-ropy-2': "1",
                            'fBodyAcc-ropy-3': "1",
                            'fBodyAcc-MaxInds-1': "1",
                            'fBodyAcc-MaxInds-2': "1",
                            'fBodyAcc-MaxInds-3': "1",
                            'fBodyAcc-MeanFreq-1': "1",
                            'fBodyAcc-MeanFreq-2': "1",
                            'fBodyAcc-MeanFreq-3': "1",
                            'fBodyAcc-Skewness-1': "1",
                            'fBodyAcc-Kurtosis-1': "1",
                            'fBodyAcc-Skewness-2': "1",
                            'fBodyAcc-Kurtosis-2': "1",
                            'fBodyAcc-Skewness-3': "1",
                            'fBodyAcc-Kurtosis-3': "1",
                            'fBodyAccMag-Mean-1': "1",
                            'fBodyAccMag-STD-1': "1",
                            'fBodyAccMag-Mad-1': "1",
                            'fBodyAccMag-Max-1': "1",
                            'fBodyAccMag-Min-1': "1",
                            'fBodyAccMag-SMA-1': "1",
                            'fBodyAccMag-Energy-1': "1",
                            'fBodyAccMag-IQR-1': "1",
                            'fBodyAccMag-ropy-1': "1",
                            'fBodyAccMag-MaxInds-1': "1",
                            'fBodyAccMag-MeanFreq-1': "1",
                            'fBodyAccMag-Skewness-1': "1",
                            'fBodyAccMag-Kurtosis-1': "1",
                            'CLASE': "1",
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/ca74073338724abfb41e897d53f7358b/services/9ae215b7a794489ea4815e24031f7d7f/execute?api-version=2.0&format=swagger'
api_key = 'liSWkYtq1dUfqdQTOKmxnNlmX++O77Vla6fsWE2YR61SK6xdrRvUyM9GeCfSg44cMt2xP46Pg/ispbVJyTNCyA==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
