They are started by AWS IoT, when a message arrives at an MQTT subject:
 csMQTT001 ---- the function that reads the json messages in the backend of the medicines taken by the patient, that updates the status in dbd (received, taken, forgotten)
 csMQTT002 ---- the function that reads the json messages in the backend of the medical tests, in this case the heart rate and oxygen saturation.
 
 
 Triggered by an EventBridge event
 A daily event
 csNotification002 ----- checks the medication data of the last day, if any medication has not been taken a text message is sent to the caregiver's phone informing him.
 csDispense002 ----- consult the tables to see if the patient has an appointment with the doctor. If so, send a JSON-MQTT message to the device to inform the patient.
 
 
 One event every hour
 csDispense001 ----- check the tables to see if the patient needs to take any medicine or have a test in the next hour. If so, create a record in the test table and send a JSON-MQTT message to the device to inform the patient.