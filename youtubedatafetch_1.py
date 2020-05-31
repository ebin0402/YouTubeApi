from googleapiclient.discovery import build

api_key="AIzaSyBOoxYiyzrp8xwSz-CW8ty6n-Bl4o90r0w"

youtube  = build('youtube','v3',developerKey=api_key)

# request = youtube.channels().list(
#     part='statistics',
#     id='UCNU_lfiiWBdtULKOw6X0Dig'
# )

# response = request.execute()
# print(response)

# reportAbuse(body={
#     "comments":"Inappropriate content"
#     "language":"English"
#     "videoId":"5IveoJ3Fwd0"
# })
req = youtube.reportAbuse(body={
    "comments":"Inappropriate content"
    "videoId":"5IveoJ3Fwd0"
})
resp = req.execute()
print(resp)
