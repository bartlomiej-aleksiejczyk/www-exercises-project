>>> from ludzie.models import Osoba
>>> from ludzie.models import Stanowisko
>>> from ludzie.serializers import StanowiskoSerializer
>>> from ludzie.serializers import OsobaSerializer      
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser    
>>> stanowisko = Stanowisko(nazwa="kuglarz", opis="zabawa z ludzmi") 
>>> stanowisko.save()
>>> serializer = StanowiskoSerializer(stanowisko) 
>>> serializer.data
{'nazwa': 'kuglarz', 'opis': 'zabawa z ludzmi'}
>>> content = JSONRenderer().render(serializer.data)
>>> content
b'{"nazwa":"kuglarz","opis":"zabawa z ludzmi"}'
>>> import io
>>> stream = io.BytesIO(content) 
>>> data = JSONParser().parse(stream) 
>>> deserializer = StanowiskoSerializer(data=data) 
>>> deserializer.is_valid()
True
>>> deserializer.errors
{}
>>> deserializer.fields
{'nazwa': CharField(allow_blank=False, allow_null=False, max_length=60), 'opis': CharFie
ld(allow_blank=True, allow_null=True, max_length=255)}
>>> deserializer.save()
>>> modyfikacja = Stanowisko.objects.get(pk=3) 
>>> new_data = {'nazwa': 'muzykant'} 
>>> update_serializer = StanowiskoSerializer(modyfikacja, data=data, partial=True)
>>> update_serializer.is_valid()
True
>>> update_serializer.save()
<Stanowisko: Stanowisko object (3)>
>>> modyfikacja.nazwa                                                              
'kuglarz'
>>> modyfikacja.opis
'zabawa z ludzmi'
>>> update_serializer.save()
<Stanowisko: Stanowisko object (3)>
>>> modyfikacja = Stanowisko.objects.get(pk=3)                                     
>>> modyfikacja.nazwa                                                
'kuglarz'
>>> modyfikacja.opis 
'zabawa z ludzmi'
>>> update_serializer = StanowiskoSerializer(modyfikacja, data=new_data, partial=True) 
>>> update_serializer.is_valid()               
True
>>> update_serializer.save()                                                       
<Stanowisko: Stanowisko object (3)>
>>> modyfikacja.opis
'NIE PODANO'
>>> modyfikacja.nazwa
'muzykant'
>>> osoba = Osoba.objects.get(pk=3)            
>>> osoba.imie
'Michał'
>>> serializer_osoba = OsobaSerializer(osoba) 
>>> serializer_osoba.data
{'id': 3, 'imie': 'Michał', 'nazwisko': 'Tutego', 'plec': 2, 'data_dodania': '2023-10-23
', 'stanowisko': 2}
>>> content_osoba = JSONRenderer().render(serializer.data)
>>> content_osoba
b'{"nazwa":"kuglarz","opis":"zabawa z ludzmi"}'
>>> serializer_osoba = OsobaSerializer(osoba)
>>> serializer.data
{'nazwa': 'kuglarz', 'opis': 'zabawa z ludzmi'}
>>> deserializer.is_valid()
True
>>> deserializer.save()
<Osoba: Michał Tutego>












