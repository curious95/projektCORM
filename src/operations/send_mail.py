from mailjet_rest import Client
import os


def send_mail(data_dict):
	api_key = 'a250fe782d77b72c1d56e61dba45b90d'
	api_secret = '469d131a28910a535146932dbb9353f3'
	mailjet = Client(auth=(api_key, api_secret), version='v3.1')
	data = {
		'Messages': [
					{
							"From": {
									"Email": "kamal.flyhigh@gmail.com",
									"Name": "Zoneomics Metrics"
							},
							"To": [
									{
											"Email": "kamalpradhan95@outlook.com",
											"Name": "Kamal Pradhan"
									}
							],
							"Subject": "Zoneomics Daily Metrics",
							"TextPart": "Dear passenger 1, welcome to Mailjet! May the delivery force be with you!",
							"HTMLPart": "<h3>Dear passenger 1, welcome to <a href=\"https://www.mailjet.com/\">Mailjet</a>!</h3><br />May the delivery force be with you!"
					}
			]
	}
	result = mailjet.send.create(data=data)
	print(result.status_code)
	print(result.json())
