import sys
import logging
import pymysql
#rds settings
rds_host  = "db001.xxxxxxxxxxx.eu-west-1.rds.amazonaws.com"
name = "admin"
password = "xxxxxxxxxxxxx" 
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
    logger.info(event["id_dsm"])
    strIDDSM ='('
    for i in event["id_dsm"]:
        strIDDSM += str(i)+','
    strIDDSM = strIDDSM[:-1]
    strIDDSM +=')' 
    logger.info(strIDDSM)
    with conn.cursor() as cur:
        strSQL='update dispense_medication_sent set status='+ str(event["status"]) +' where id_dms in '+ strIDDSM
        logger.info(strSQL)
        cur.execute( strSQL )
        conn.commit()

    conn.commit()

