from django.shortcuts import render
import requests
# import folium

def data(request):
    link = requests.get('https://covid19.mathdro.id/api')
    data = link.json()
    world_kon = data['confirmed']
    world_re = data['recovered']
    world_de = data['deaths']
    negara = {}
    if 'country' in request.GET:
        negara = request.GET['country']
        negara = negara.title()
        print(negara)
        url = requests.get('https://covid19.mathdro.id/api/countries')
        res = url.json()
        country = res['countries']
        for i in country:
            try:
                
                if (negara.title() == i['name']) or (negara.upper() != i['iso2']) or (negara.upper() != i['iso3']):
                    url2 = 'https://covid19.mathdro.id/api/countries/%s' % negara
                    response2 = requests.get(url2)
                    data2 = response2.json()
                    confirmed = data2['confirmed']
                    recovered = data2['recovered']
                    deaths = data2['deaths']
                  
                    


                    return render(request, 'covid/dashboard.html',
                    {
                        'country':negara,
                        'data':data2,
                        'konfirmasi':confirmed['value'],
                        'recovered':recovered['value'],
                        'lastupdate':data2['lastUpdate'],
                        'meninggal':deaths['value'],
                        'terkonfirmasi' : world_kon['value'],
                        'terrecovered' : world_re['value'],
                        'termeninggal' : world_de['value'],
                        
                    })
                    
               
            except:
                return render(request, 'covid/dashboard.html',{
                    'terkonfirmasi' : world_kon['value'],
                    'terrecovered' : world_re['value'],
                    'termeninggal' : world_de['value'],
                })
              
                

                    

    return render(request, 'covid/dashboard.html',{

        'terkonfirmasi' : world_kon['value'],
        'terrecovered' : world_re['value'],
        'termeninggal' : world_de['value'],
        'update' :data['lastUpdate'],
      
        

    })                
    

def nasio(request):
    urlidn = requests.get('https://apicovid19indonesia-v2.vercel.app/api/indonesia')
    res = urlidn.json()
    pos = res['positif']
    ra = res['dirawat']
    semb = res['sembuh']
    meninggal = res['meninggal']
    urlidn2 = requests.get('https://apicovid19indonesia-v2.vercel.app/api/indonesia/provinsi')
    res2 = urlidn2.json()
    prov = []
    for i in res2:
         attributes = {}
         attributes['provin'] = i['provinsi']
         attributes['kasus'] = i['kasus']
         attributes['dirawat'] = i['dirawat']
         attributes['sembuh'] = i['sembuh']
         attributes['meninggal'] = i['meninggal']
         prov.append(attributes)
    
    
    url3 = requests.get('https://vaksincovid19-api.vercel.app/api/vaksin')
    vak = url3.json()
    tot = vak['totalsasaran'] 
    sdmk = vak['sasaranvaksinsdmk']
    lansia = vak['sasaranvaksinlansia']
    publik = vak['sasaranvaksinpetugaspublik']
    vak1 = vak['vaksinasi1']    
    vak2 = vak['vaksinasi2']
         
    
    return render (request, 'covid/nasio.html', {
        'data':prov,
        'positif' :pos,
        'rawat' : ra,
        'sembuh' : semb,
        'deaths' : meninggal,
        'total' : tot,
        'sdmk' : sdmk,
        'lansia' : lansia,
        'publik' : publik,
        'vak1' :vak1,
        'vak2' : vak2,
        'update':vak['lastUpdate']
        
    })
   
       
   

def chart(request):
    url = requests.get('https://covid19.mathdro.id/api')
    reschart = url.json()
    konfirmasi = reschart['confirmed']
    recovered = reschart['recovered']
    meninggal = reschart['deaths']
    return render(request, 'covid/chart.html',{
        'confirmed' : konfirmasi['value'],
        'recovered' : recovered['value'],
        'meninggal' : meninggal['value'],
        'update' : reschart['lastUpdate']
    })


