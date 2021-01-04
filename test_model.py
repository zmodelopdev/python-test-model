#fastscore.schema.0: input_schema.avsc
#fastscore.schema.1: output_schema.avsc

import time
import json
import math

# This is a test comment

# This is a second test comment

print("Starting program", flush=True)

#modelop.init
def begin():
    global coefs
    coefs = json.load(open('external_file_asset.json', 'r'))
    print("pass", flush=True)
    for x in range(10):
        print(x, flush=True)
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        print(result, end="", flush=True)
        print("\r", end="", flush=True)
        time.sleep(5)
    pass

#modelop.score
def action(datum):
    prediction = compute_prediction(datum)
    print("Can you hear me now?", flush=True)
    yield prediction

def compute_prediction(datum):
    x_score = coefs['x']*datum['x'] 
    y_score = coefs['y']*datum['y'] 
    prediction = x_score + y_score + coefs['intercept']
    return prediction

#modelop.metrics
def metrics(data):
    actuals = data.z.tolist()
    data = data.to_dict(orient='records')
    predictions = list(map(compute_prediction, data))
    diffs = [x[0] - x[1] for x in zip(actuals, predictions)]
    rmse = math.sqrt(sum(list(map(lambda x: x**2, diffs)))/len(diffs))
    mae = sum(list(map(abs, diffs)))/len(diffs)
    yield dict(MAE=mae, RMSE=rmse)
