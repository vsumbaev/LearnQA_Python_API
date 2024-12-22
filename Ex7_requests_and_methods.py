import requests

URL="https://playground.learnqa.ru/ajax/api/compare_query_type"

type = ["get", "put", "post", "delete"]

method = ["GET", "PUT", "POST", "DELETE"]

#1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.

print("#1 get - " + requests.get(URL).text)
print(requests.get(URL))
print("#1 put - " + requests.put(URL).text)
print(requests.put(URL))
print("#1 post - " + requests.post(URL).text)
print(requests.post(URL))
print("#1 delete - " + requests.delete(URL).text)
print(requests.delete(URL))

#2 Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.

print("#2 get - " + requests.get(URL, params={"method":"HEAD"}).text)
print(requests.get(URL, params={"method":"HEAD"}))
print("#2 put - " + requests.put(URL, data={"method":"HEAD"}).text)
print(requests.put(URL, data={"method":"HEAD"}))
print("#2 post - " + requests.post(URL, data={"method":"HEAD"}).text)
print(requests.post(URL, data={"method":"HEAD"}))
print("#2 delete - " + requests.delete(URL, data={"method":"HEAD"}).text)
print(requests.delete(URL, data={"method":"HEAD"}))



#3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.

print("#3 " + requests.get(URL, params={"method": "GET"}).text)
print(requests.get(URL, params={"method": "GET"}))
print("#3 " + requests.put(URL, data={"method": "PUT"}).text)
print(requests.put(URL, data={"method": "PUT"}))
print("#3 " + requests.post(URL, data={"method": "POST"}).text)
print(requests.post(URL, data={"method": "POST"}))
print("#3 " + requests.delete(URL, data={"method": "DELETE"}).text)
print(requests.delete(URL, data={"method": "DELETE"}))

#4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
# Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ 
# и так далее. И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает
# со значением параметра, но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают,
# но сервер считает, что это не так.

for i in method:
    print(i)
    print("#4 method=" + i + " and type=GET " + requests.get(URL, params={"method": i}).text)
    print(requests.get(URL, params={"method": i}))
    print("#4 method=" + i + " and type=PUT " + requests.put(URL, data={"method": i}).text)
    print(requests.put(URL, data={"method": i}))
    print("#4 method=" + i + " and type=POST " + requests.post(URL, data={"method": i}).text)
    print(requests.post(URL, data={"method": i}))
    print("#4 method=" + i + " and type=DELETE " + requests.delete(URL, data={"method": i}).text)
    print(requests.delete(URL, data={"method": i}))


