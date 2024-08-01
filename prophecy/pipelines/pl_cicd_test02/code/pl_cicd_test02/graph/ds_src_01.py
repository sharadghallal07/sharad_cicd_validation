from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_cicd_test02.config.ConfigStore import *
from pl_cicd_test02.functions import *

def ds_src_01(spark: SparkSession) -> DataFrame:
    return spark.read.table("`default`.`employee_tbl`")
