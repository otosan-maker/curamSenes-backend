import sys
import logging
import pymysql
#rds settings
rds_host  = "db001.xxxxxxxxxxx.eu-west-1.rds.amazonaws.com"
name = "admin"
password = "xxxxxxxxxxxx" 
db_name = "health001"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

def lambda_handler(event, context):
    logger.info(event["id_ths"])
    with conn.cursor() as cur:
        strSQL='update test_heart_sent  set bpm='+ str(event["bpm"]) +',spo2='+ str(event["spo2"]) +' where id_ths = '+ str(event["id_ths"])
        logger.info(strSQL)
        cur.execute( strSQL )
        conn.commit()

    conn.commit()

