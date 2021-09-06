import sys
import logging
import pymysql
import boto3
import json
from botocore.exceptions import ClientError


#rds settings
rds_host  = "db001.xxxxxxxxxx.eu-west-1.rds.amazonaws.com"
name = "admin"
password = "xxxxxxxxxx" 
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

def lambda_handler(event, context):
    # looking for medicines
    with conn.cursor() as cur:
        cur.execute("select da.m_doctor name,pat.id_device iddevice,pat.id_patient idpatient from doctor_appointment da,patient pat where  pat.id_patient = da.id_patient and dayofyear(appointment)=dayofyear(now()) and year(appointment)=year(now());")
        for row in cur:
            logger.info(row)
            strIDPatient = str(row[2])
            strMName     = str(row[0])
            strIDClient  = str(row[1])
            
            
            
            strTopic = strIDClient + '/med_appointment'
            strPayLoad = '{"m_doctor":"'+ str(strMName) +'"}'
            response = client.publish(topic=strTopic,qos=1,payload= strPayLoad  )
    conn.commit()

  

    
    return "200 OK" 