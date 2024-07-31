   if response.status_code == 200:
       try:
           articles_data = response.json()
       except JSONDecodeError as e:
           print(f"Error decoding JSON: {e}")
   else:
       print(f"Request failed with status code: {response.status_code}")
   