from funcx import FuncXExecutor

def infer_maxsep():
    import os
    import pandas as pd
    os.chdir('/project')
    from CLEAN.infer import infer_maxsep
    train_data = "split100"
    test_data = "price"
    infer_maxsep(train_data, test_data, report_metrics=False, pretrained=True)
    df = pd.read_csv('./results/price_maxsep.csv', on_bad_lines='skip')
    print("----- Executed Successfully ----")
    return df

with FuncXExecutor(endpoint_id="006f558d-df82-45c2-b2d5-94274ef41a69", container_id="ac70db7c-406d-4697-be1e-55cbf56b86f8") as ex:
    fut = ex.submit(infer_maxsep)

    print(fut.result())
