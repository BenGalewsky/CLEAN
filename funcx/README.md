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
```shell
apptainer exec --mount type=bind,src=/scratch/bbmi/bengal1,dst=/projects /projects/bbmi/bengal1/CLEAN.sif python /CLEAN/infer.py
```
