import requests

def weather_forecast(city):

    api_key='2ad207f1576cc623c5396f3df877c5d7'
    response=requests.get('https://api.openweathermap.org/data/2.5/weather',params={'q':city,'units':'metric','APPID':api_key})


    if response.status_code ==200:
        data=response.json()
        try:
            print('City',data['name'])
            for i in data['main']:
                print('  ',i,'-->',data['main'][i])
        except Exception as error_name:
            print(error_name)


    else:
        print('status_code--',response.status_code)


def main():
    city_name="GYUMRI"
    weather_forecast(city_name)

if __name__=='__main__':
    main()

