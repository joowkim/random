#PBS -l walltime=100:00:00
#PBS -l mem=8gb
#PBS -N down_sra
#PBS -o logs/down_sra_workflow.o
#PBS -e logs/down_sra_workflow.e

cd ${PBS_O_WORKDIR}
# export Singularity 3.4.0-1 installed on node065 to $PATH.
# snakemake should now automatically call Singularity 3.4.0-1
#PATH=/usr/local/bin/:$PATH

module load bbc/snakemake/snakemake-6.1.0


# save DAG job file with time stamp
TIME=$(date "+%Y-%m-%d_%H.%M.%S")

# make logs dir if it does not exist already. Without this, logs/ is automatically generate only after the first run of the pipeline
logs_dir="logs/runs"
[[ -d $logs_dir ]] || mkdir -p $logs_dir


snakemake \
-p \
--use-envmodules \
--jobs 20 \
--cluster "qsub \
-q bbc \
-V \
-l nodes=1:ppn={threads} \
-l mem={resources.mem_gb}gb \
-l walltime=100:00:00 \
-o logs/runs/ \
-e logs/runs/"
