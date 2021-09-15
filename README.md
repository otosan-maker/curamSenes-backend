This code is the repository for the project curamSenes, you can get more information about it here:
<a href="https://www.hackster.io/angelluiscabello/curam-senes-8252d3">Project Hacker.io</a>

They are started by AWS IoT, when a message arrives at an MQTT subject:<br>
 <b>csMQTT001</b> ---- the function that reads the json messages in the backend of the medicines taken by the patient, that updates the status in dbd (received, taken, forgotten)<br>
 <b>csMQTT002</b> ---- the function that reads the json messages in the backend of the medical tests, in this case the heart rate and oxygen saturation.<br>
 
 
 Triggered by an EventBridge event<br>
 A daily event<br>
 <b>csNotification002</b> ----- checks the medication data of the last day, if any medication has not been taken a text message is sent to the caregiver's phone informing him.<br>
 <b>csDispense002</b> ----- consult the tables to see if the patient has an appointment with the doctor. If so, send a JSON-MQTT message to the device to inform the patient.<br>
 
 
 One event every hour<br>
 <b>csDispense001</b> ----- check the tables to see if the patient needs to take any medicine or have a test in the next hour. If so, create a record in the test table and send a JSON-MQTT message to the device to inform the patient.<br>
