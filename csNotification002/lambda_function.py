import sys
import logging
import pymysql
import boto3
import json
from botocore.exceptions import ClientError


#rds settings
rds_host  = "db001.xxxxxxxxxxx.eu-west-1.rds.amazonaws.com"
name = "admin"
password = "xxxxxxxxxxxxxx" 
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
try:
    client = boto3.client('iot-data', region_name='eu-west-1')
except ClientError as e:
    print("Client error: %s" % e)


# Initialize SNS client for Ireland region
session = boto3.Session(
    region_name="eu-west-1"
)
sns_client = session.client('sns')



def lambda_handler(event, context):
    item_count = 0
    with conn.cursor() as cur:
        cur.execute("select p_name PatienName,nurse_tlfno NurseTlfno,m_name Medicine from dispense_medication_sent dms,patient p where dms.id_patient=p.id_patient and status=2 and (now() -  c_time ) < 24*3600;")
        for row in cur:
            logger.info(row)
            PatientName    = str(row[0])
            NurseTlfno     = str(row[1])
            Medicine       = str(row[2])
            
            response = sns_client.publish(
                PhoneNumber=NurseTlfno,
                Message=PatientName+' has stopped taking these medicines:'+Medicine,
                MessageAttributes={
                    'AWS.SNS.SMS.SenderID': {
                        'DataType': 'String',
                        'StringValue': 'CURAMSENES'
                        },
                    'AWS.SNS.SMS.SMSType': {
                    'DataType': 'String',
                    'StringValue': 'Promotional'
                    }
                }   
            )
            logger.info(response)
            
            
    conn.commit()

    return "OK"