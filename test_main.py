from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/method")
    assert response.status_code == 200
    assert response.json() == {"method": "GET"}

def test_pk():
	pk=0
	response=client.post("/patient", json={"name": "NAME", "surename": "SURENAME"})
	response=client.get(f"/patient/{pk}")
	assert response.status_code==200
	assert response.json()=={"name": "NAME", "surename": "SURENAME"}
#@pytest.mark.parametrize("name", ['Zenek', 'Marek', 'Alojzy Niezdąży'])
#def test_hello_name(name):
    # name = 'elo'
    #response = client.get(f"/hello/{name}")
    #assert response.status_code == 200
    #assert response.json() == {'msg': f"Hello {name}"}
"""
Zadanie 4
Stwórz ścieżkę `/patient/{pk}`, która przyjmuje request w metodą GET.

pk, powinien być liczbą. Najlepiej intem.

W przypadku znalezienia takiego pacjenta, odpowiedź powinna wyglądać tak:
`{"name": "NAME", "surename": "SURENAME"}`

W przypadku nieznalezienia należy zwrócić odpowiedni kod http:
https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

PS 1 Podobnie jak w poprzednim zadaniu, znajdź miejsce w aplikacji, gdzie można zapisać pacjenta

PS 2 Zmodyfikuj endpoint POST `/patient`, tak aby zachował przesłane dane

PS 3 Pamiętaj, aby liczyć pacjentów od 0!
"""

#zad2
def test_delete_something():
	response=client.delete("/method")
	assert response.json()=={"method": "DELETE"}


def test_post_something():
	response=client.post("/method")
	assert response.json()=={"method": "POST"}

def test_put_something():
	response=client.put("/method")
	assert response.json()=={"method": "PUT"}	

#patient-zad3
#blad w slowie "surname" w warunkach zadania 

def test_create_patient():
	response=client.post("/patient", json={"name": "IMIE", "surename": "NAZWISKO"})
	#response=client.post("/patient", json={'surename': 'value'})
	response=client.post("/patient", json={"name": "IMIE", "surename": "NAZWISKO"})
	response=client.post("/patient", json={"name": "IMIE", "surename": "NAZWISKO"})
	assert response.json()=={"id": 3, "patient": {"name": "IMIE", "surename": "NAZWISKO"}}