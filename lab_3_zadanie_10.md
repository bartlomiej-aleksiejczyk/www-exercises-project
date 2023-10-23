>>> from ludzie.models import Osoba            
>>> Osoba.objects.all()             
<QuerySet [<Osoba: Jan Łoś>, <Osoba: Michał Tutego>, <Osoba: Karina Pracowita>, <Osoba: Jan Niezbędny>]>
>>> Osoba.objects.filter(id=3)                 
<QuerySet [<Osoba: Michał Tutego>]>
>>> Osoba.objects.filter(imie__startswith="k") 
<QuerySet [<Osoba: Karina Pracowita>]>
>>> Osoba.objects.order_by().values_list('stanowisko__nazwa', flat=True).distinct()
<QuerySet ['Śmieciarz', 'Klałn']>
>>> Osoba.objects.order_by('-stanowisko__nazwa').values_list('stanowisko__nazwa', flat=True)                                                                    
<QuerySet ['Śmieciarz', 'Śmieciarz', 'Śmieciarz', 'Klałn']>
>>> tomasz = Osoba(imie="Tomasz", nazwisko="Baranowski", plec=Osoba.Plcie.MEZCZYZNA, stanowisko_id=1)     
>>> tomasz.save() 
