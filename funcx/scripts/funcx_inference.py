
from funcx import FuncXExecutor

def infer_p_values():
    import os

    # Get the current directory
    # os.chdir('/project/')
    current_dir = os.getcwd()
    print("Current working dir", current_dir)
    # List all files in the current directory
    # files = os.listdir(current_dir)
    # #
    # # # Print the list of files
    # retval = ''
    # for file in files:
    #     retval = retval + ' ' + file + ''
        # print(file)
    # from CLEAN.infer import infer_pvalue
    # train_data = "split100"
    # test_data = "new"
    # infer_pvalue(train_data, test_data, p_value=1e-5, nk_random=20,
    #              report_metrics=True, pretrained=True)

    return str(current_dir) + " Executed successfully"


def infer_maxsep():
    import os
    os.chdir('/project')
    from CLEAN.infer import infer_maxsep
    train_data = "split100"
    test_data = "price"
    infer_maxsep(train_data, test_data, report_metrics=False, pretrained=True)
    print("----- Executed Successfully ----")
    return 'Executed Successfully'

with FuncXExecutor(endpoint_id="b41a2cf6-ee51-4060-8317-27e2ac8e4891", container_id="ac70db7c-406d-4697-be1e-55cbf56b86f8") as ex:
    fut = ex.submit(infer_p_values)

    print(fut.result())


