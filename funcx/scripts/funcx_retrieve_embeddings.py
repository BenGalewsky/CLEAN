# Before inference, AA sequences to be inferred are stored in a CSV file, with the same format as the split100.csv. The field EC number in the csv file can be any EC number if unknow, but please ignore the printed evaluation metrics in this case. The esm-1b embeddings of the infered sequences need to be pre-computed using the following commands (using new.csv as an example):
from funcx import FuncXExecutor


def retrieve_embeddings():
    from CLEAN.utils import csv_to_fasta, retrive_esm1b_embedding
    csv_to_fasta("data/new.csv", "data/new.fasta")
    retrive_esm1b_embedding("new")
    return "Executed Successfully"

with FuncXExecutor(endpoint_id="b41a2cf6-ee51-4060-8317-27e2ac8e4891", container_id="ac70db7c-406d-4697-be1e-55cbf56b86f8") as ex:
    fut = ex.submit(retrieve_embeddings)

    print(fut.result())