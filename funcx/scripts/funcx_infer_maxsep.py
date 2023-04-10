from funcx import FuncXExecutor

def infer_maxsep():
    import os
    os.chdir('/project')
    from CLEAN.infer import infer_maxsep
    train_data = "split100"
    test_data = "price100"
    infer_maxsep(train_data, test_data, report_metrics=False, pretrained=True)
    print("----- Executed Successfully ----")
    return 'Executed Successfully'

with FuncXExecutor(endpoint_id="b41a2cf6-ee51-4060-8317-27e2ac8e4891", container_id="ac70db7c-406d-4697-be1e-55cbf56b86f8") as ex:
    fut = ex.submit(infer_maxsep)

    print(fut.result())
