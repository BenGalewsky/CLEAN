# Running Inference Using FuncX

## Apptainer
We are using an Apptainer to manage dependencies on Delta. 
[CLEAN.def](CLEAN.def) builds the container.

```shell
apptainer build /projects/bbmi/bengal1/CLEAN.sif CLEAN.def
```

This builds the container and puts in our `projects` directory.

## Running the Container
We need to mount the data directory in the running image:

This doesn't work very well since it runs on the login node and not on a GPU node
like the base image of the container expects.
```shell
apptainer run --mount type=bind,src=/scratch/bbmi/bengal1,dst=/project /projects/bbmi/bengal1/CLEAN.sif
```

Run this on a GPU node. The `-interactive` paritions have short max wall times,
so perfect for getting a short job executed.
```shell
srun --gpus=1 --account=bbmi-delta-gpu --partition=gpuA100x4-interactive --mem 32g infer.sh
```

## Running on FuncX
Login to Delta cluster
```shell
srun --gpus=1 --account=bbmi-delta-gpu --partition=gpuA100x4-interactive --mem 32g infer.sh
```

Install funcx-endpoint on the node
```shell
pip install funcx-endpoint==1.0.11
```

Create funcx-endpoint
```shell
funcx-endpoint configure clean
```

Update ~/.funcx/clean/config.py to CLEAN/funcx/config/delta_container_config.py

Start clean endpoint
```shell
funcx-endpoint start clean
```

### Run on the local system, where you are publishing the results

Install funcx SDK
```shell
pip install funcx==1.0.11
```

To run the demo file initially to test funcx-execution, run the CLEAN/funcx/scripts/funcx_demo.py file
```shell
python funcx_demo.py
```
You should see an array of 0-99 integers.

Then run infer_maxsep, CLEAN/funcx/scripts/funcx_infer_maxsep.py
```shell
python funcx_infer_maxsep.py
```