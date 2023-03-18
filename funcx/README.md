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