from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_cicd_test02.config.ConfigStore import *
from pl_cicd_test02.functions import *

def ds_tgt_01(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("`default`.`emp_tbl`")
