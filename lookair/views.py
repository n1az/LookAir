from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method == "POST" :
		zipcode = request.POST['zipcode']

		try:
			api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=150&API_KEY=C3F8A712-4226-454D-BB49-D92967FC2446")
			try:
				api = json.loads(api_request.content)
			except Exception as e:
				api = "Error.."

			if api[0]['Category']['Name'] == "Good" :
				category_description = "0 to 50 means Air quality is satisfactory, and air pollution poses little or no risk."
				category_color = "good"
			elif api[0]['Category']['Name'] == "Moderate" :
				category_description = "51 to 100 means Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
				category_color = "moderate"
			elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups" :
				category_description = "101 to 150 meansMembers of sensitive groups may experience health effects. The general public is less likely to be affected."
				category_color = "usg"
			elif api[0]['Category']['Name'] == "Unhealthy" :
				category_description = "151 to 200 means Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
				category_color = "unhealthy"
			elif api[0]['Category']['Name'] == "Very Unhealthy" :
				category_description = "201 to 300 means Health alert: The risk of health effects is increased for everyone."
				category_color = "veryunhealthy"
			elif api[0]['Category']['Name'] == "Hazardous" :
				category_description = "301 and higher means Health warning of emergency conditions: everyone is more likely to be affected."
				category_color = "hazardous"
			elif api[0]['Category']['Name'] == "Unavailable" :
				category_description = "Sorry no area found."
				category_color = "hazardous"
			elif api[0]['Category']['Name'] == NULL :
				category_description = "Sorry no area found."
				category_color = "hazardous"
			return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})


		except Exception as e:
			api = "Error.."

		##api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=150&API_KEY=C3F8A712-4226-454D-BB49-D92967FC2446")

		# try:
		# 	api = json.loads(api_request.content)
		# except Exception as e:
		# 	api = "Error.."

		# if api[0]['Category']['Name'] == "Good" :
		# 	category_description = "0 to 50 means Air quality is satisfactory, and air pollution poses little or no risk."
		# 	category_color = "good"
		# elif api[0]['Category']['Name'] == "Moderate" :
		# 	category_description = "51 to 100 means Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
		# 	category_color = "moderate"
		# elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups" :
		# 	category_description = "101 to 150 meansMembers of sensitive groups may experience health effects. The general public is less likely to be affected."
		# 	category_color = "usg"
		# elif api[0]['Category']['Name'] == "Unhealthy" :
		# 	category_description = "151 to 200 means Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
		# 	category_color = "unhealthy"
		# elif api[0]['Category']['Name'] == "Very Unhealthy" :
		# 	category_description = "201 to 300 means Health alert: The risk of health effects is increased for everyone."
		# 	category_color = "veryunhealthy"
		# elif api[0]['Category']['Name'] == "Hazardous" :
		# 	category_description = "301 and higher means Health warning of emergency conditions: everyone is more likely to be affected."
		# 	category_color = "hazardous"
		# elif api[0]['Category']['Name'] == "Unavailable" :
		# 	category_description = "Sorry no area found."
		# 	category_color = "hazardous"
		# elif api[0]['Category']['Name'] == NULL :
		# 	category_description = "Sorry no area found."
		# 	category_color = "hazardous"
		# return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})


	else:

		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=C3F8A712-4226-454D-BB49-D92967FC2446")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error.."

		if api[0]['Category']['Name'] == "Good" :
			category_description = "0 to 50 means Air quality is satisfactory, and air pollution poses little or no risk."
			category_color = "good"
		elif api[0]['Category']['Name'] == "Moderate" :
			category_description = "51 to 100 means Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
			category_color = "moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups" :
			category_description = "101 to 150 meansMembers of sensitive groups may experience health effects. The general public is less likely to be affected."
			category_color = "usg"
		elif api[0]['Category']['Name'] == "Unhealthy" :
			category_description = "151 to 200 means Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
			category_color = "unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy" :
			category_description = "201 to 300 means Health alert: The risk of health effects is increased for everyone."
			category_color = "veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous" :
			category_description = "301 and higher means Health warning of emergency conditions: everyone is more likely to be affected."
			category_color = "hazardous"
		return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})

def about(request):
	return render(request, 'about.html', {})