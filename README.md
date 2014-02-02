sms-proxy
=========
A cURL-able SMS service that hides the complexity of various SMS web services

to start run the following command:

    python SMSProxy.py [port]

to test run this command:

    curl --data "To=[Phone Number]&Body=It works\!" http://127.0.0.1:[port]/sms/send