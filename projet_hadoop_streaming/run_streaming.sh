#!/bin/bash
# run_dpt.sh

INPUT_HDFS=/user/maria_dev/dpt/dpt2022.csv
OUTPUT_HDFS=/user/maria_dev/dpt/output
STREAMING_JAR=/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar

# Copier et nettoyer
hdfs dfs -mkdir -p /user/maria_dev/dpt
hdfs dfs -put -f dpt2022.csv /user/maria_dev/dpt/
hdfs dfs -rm -r $OUTPUT_HDFS || true

# Exécuter en précisant python
hadoop jar $STREAMING_JAR \
  -files validation.py,mapper.py,reducer.py,post_traitement.py \
  -mapper "python validation.py | python mapper.py" \
  -reducer "python reducer.py | python post_traitement.py" \
  -input  $INPUT_HDFS \
  -output $OUTPUT_HDFS
