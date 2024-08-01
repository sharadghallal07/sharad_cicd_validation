from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_cicd_test01.config.ConfigStore import *
from pl_cicd_test01.functions import *
from prophecy.utils import *
from pl_cicd_test01.graph import *

def pipeline(spark: SparkSession) -> None:
    script(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_cicd_test01")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_cicd_test01")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_cicd_test01", config = Config)(pipeline)

if __name__ == "__main__":
    main()
