# from funcx import FuncXClient

from funcx import FuncXExecutor

def print_hw():
    import time
    import numpy as np
    ar = np.arange(100)
    return ar

# fx = FuncXClient()
# uuid = fx.register_container("/projects/bbmi/bengal1/CLEAN_ritwikd2.sif",
#                              container_type="singularity")
# print("Container ID for CLEAN is ", uuid)

# 30fb631f-0f1c-4733-aebb-f267bb2e52a6  Ben
# d40eaddf-6b6b-410a-983b-622e6e5af32d  Sindhu
# ac70db7c-406d-4697-be1e-55cbf56b86f8  Ritwik
with FuncXExecutor(endpoint_id="006f558d-df82-45c2-b2d5-94274ef41a69", container_id="ac70db7c-406d-4697-be1e-55cbf56b86f8") as ex:
    fut = ex.submit(print_hw)
    print(fut.result())


