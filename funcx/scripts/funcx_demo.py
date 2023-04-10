from funcx import FuncXExecutor

def print_hw():
    import numpy as np
    ar = np.arange(100)
    return ar


with FuncXExecutor(endpoint_id="006f558d-df82-45c2-b2d5-94274ef41a69", container_id="ac70db7c-406d-4697-be1e-55cbf56b86f8") as ex:
    fut = ex.submit(print_hw)
    print(fut.result())


