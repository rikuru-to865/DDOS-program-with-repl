import json
import boto3
import subprocess
import time
import schedule


bucket_name = "resultfolderofrikuruto"
s3 = boto3.resource('s3')
def main():
    subprocess.run("masscan -p22 0.0.0.0/0 --rate 1200000 -oJ result.json ‐‐excludefile exclude.txt")
    dt_now = datetime.datetime.now()
    s3.Bucket(bucket_name).upload_file('/root/result.json', 'result-'+dt_now.year+"-"+dt_now.month+"-"+dt_now.day+".json")

schedule.every().monday.do(main)
while True:
    schedule.run_pending()
    time.sleep(1)
    l+GEkByJD2bQuGrTUKpHqgxeVj+T/l8qRSej6Rgq