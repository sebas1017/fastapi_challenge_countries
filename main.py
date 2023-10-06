from fastapi import FastAPI, HTTPException
from core.config import settings
import json
import requests
import pandas as pd
import time
import random
import hashlib
import os
import uvicorn
import asyncio
import aiohttp
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)






app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)



def json_read():
		script_dir = os.path.dirname(__file__) # <-- absolute dir the script 
		rel_path = "data.json"
		abs_file_path = os.path.join(script_dir, rel_path)
		# open json file and give it to data variable as a dictionary
		with open(abs_file_path) as data_file:
			data_information = json.load(data_file)
		return data_information

async def fetch(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            data_response = response.json()
            return await data_response
    return {}


@app.get("/", status_code=200)
async def index():
		try:
			url = "https://restcountries.com/v3.1/all"
			url_countries_by_region = "https://restcountries.com/v3.1/region/{region}"

			headers = {
				'x-rapidapi-key': "921cfc17abmsh42834139575656fp12725cjsn8ce3ad10333d",
				'x-rapidapi-host': "restcountries-v1.p.rapidapi.com"
				}
			regions_data = []
			hash_languages =[]
			countries = []
			times=[]
			data  = requests.get(url, headers=headers)
			if data.status_code == 200:
				try: 
					for information in data.json():
						if information["region"]  and not information["region"]  in regions_data:
							regions_data.append(information["region"])
							# only the different existing regions

					async with aiohttp.ClientSession() as session:
						for region in regions_data:
							start_time = time.time()
							data_task = asyncio.create_task( fetch(session, url_countries_by_region.format(region=region) ))
							response_by_region = await asyncio.gather(data_task)

							response_by_region = response_by_region[0]
       
							
							# we consult the data requested by region
							valid = False
							while valid is False:
								country_option = random.randint(0,len(response_by_region)-1)
								if "languages" in list( response_by_region[country_option].keys()):
									valid = True
								else:
									response_by_region.pop(country_option)

							countries.append(response_by_region[country_option]['name']['common'])
							key_language =  list(response_by_region[country_option]['languages'].keys())[0]
							hash_languages.append(hashlib.sha1(response_by_region[country_option]['languages'][str(key_language)].encode()).hexdigest())
							end_time = time.time()
							times.append(round((end_time-start_time)*1000,2))
				except KeyError:
					data = {"message":"Error en API externa de paises recargar nuevamente"}
					raise HTTPException(status_code=500,detail=data)
				
				df = pd.DataFrame({
					"Region": regions_data,
					"Country": countries,
					"Language SHA1": hash_languages,
					"Time [ms]": times
				})
				#  we build a dataframe and a data.json file with the results of the algorithm
				df.to_json(path_or_buf='data.json')
				# here we can return the answer in html format but I decided to leave the answer in json format
				data_information = json_read()
				return data_information
			else:
				data = {"message":"error en api externa de paises"}
				raise HTTPException(status_code=500,detail=data)
		except Exception as error:
			logger.error(f"Error in funcion index endpoint -> {error}")
if __name__=="__main__":
	print("Started app")