from funcx import FuncXExecutor


def write_list_to_csv():
    import os
    import csv
    import numpy as np
    os.chdir('/project/results')
    my_array = [
        [1, 'John', 'Doe'],
        [2, 'Jane', 'Doe'],
        [3, 'Bob', 'Smith']
    ]

    output_file = 'my_output_file.csv'

    # Open the output file for writing
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for row in my_array:
            writer.writerow(row)

    return np.array(my_array)


with FuncXExecutor(endpoint_id="b41a2cf6-ee51-4060-8317-27e2ac8e4891", container_id="ac70db7c-406d-4697-be1e-55cbf56b86f8") as ex:
    fut = ex.submit(write_list_to_csv)

    print(fut.result())