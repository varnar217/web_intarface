from flask import Flask,render_template,url_for,request,redirect, make_response,Response,session, jsonify
import random
import json
from time import time
from ochistit import func_ochist
import requests as req
from random import random
import random
from datetime import datetime
import re
from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import time
#import time
from flask import Flask, render_template, make_response
json_data=[]
spisok_scenariev=[]
epdb=0
regim_rabota_mode=0
#from flask_socketio import SocketIO, send, emit
global_number_eps=100
global_spis=''
global_pcath_size=0
global_velocity=0
pcap_cortg=[]
network_list=[]
eps_br=[]
lang_switch=0
GTP_FLAG=True
ipsrc=''
ipdst=''
minteid=''
maxteid=''
time_otvet=0
start_flag1=0
eb_pies_for_one=0
ind_sce_0_iter =0
ind_sce_0 =-1
net_sce_0 =-1
indef_scen =-1
indef_netw =-1
app = Flask(__name__)
random.seed()  # Initialize the random number generator
number_EPS=0
conect=True
number_idd=0
udras= ''
data_grafik1=  [0 ]
data_grafik2=  [0 ]
bufer_network2=[{'name':'Bitrate','der':0},{'name':'Video-ratio','der':1}]

data2_global=0
labels = [
    'Video', 'Not Video'
]

rabota_status=[{'key':0,'name':'в реальном времени с отправкиой в сеть'},{'key':1,'name':'не в реальном с записью файла'}]


iterater_schetchik=0
secret_key=[str('test'),str('test2')]
user_key=[str('User'),str('User_2')]
flag_regst=False
port_adres={'addr':'192.168.0.143','port':'5000'}



@app.route('/', methods = ['POST','GET','PUT'])
def nachal():

    if request.method == 'POST':
        global udras ,  secret_key , user_key ,  time_otvet
        global global_spis,global_pcath_size,global_velocity,GTP_FLAG,ipsrc,ipdst,minteid,maxteid,global_number_eps,network_list,spisok_scenariev,regim_rabota_mode

        udras=str(request.form.get('uds'))
        udras=udras+':'+str(request.form.get('port'))
        login=str(request.form.get('login'))
        password=str(request.form.get('password'))
        try:
            global port_adres
            #data={'addr':'192.168.0.163','port':'5000'}
            #start=time.clock()
            start = time()
            rr=req.get(f'http://{udras}/init',params=(port_adres))
            stop=time() -start
            #print('seconds=',rr.elapsed.total_seconds())
            #print('stop=',stop)
            time_otvet= stop*1000 #rr.elapsed.total_seconds()


            buferr=rr.text
            print('bb=',buferr)
            #buferr=rr.text
            js = json.loads(buferr)
            global pcap_cortg

            if js['response']['code'] == 0 :
                #print('js=',js)
                spisok_scenariev=[]
                network_list=[]
                pcapp=js['params']['pcap']
                #print('\njs333=',js['params']['pcap'])
                for it in pcapp:
                    bufer=[]
                    bufer.append(it['video'])
                    bufer.append(it['br'])
                    bufer.append(it['path'])
                    pcap_cortg.append(bufer)
                print('\npcap=',pcap_cortg)



                #for it in js['params']:
                #print('js=',js['params'])
                #print('keys=',js.keys())

                jss2=js['params']
                global_spis=jss2['file']['path']
                #print('jss2=',jss2)
                global_pcath_size=jss2['file']['size']
                global_velocity=jss2['br']
                regim_rabota_mode=jss2['mode']
                GTP_FLAG=jss2['gtp']['use']
                ipsrc=jss2['gtp']['ipsrc']
                ipdst=jss2['gtp']['ipdst']
                minteid=jss2['gtp']['minteid']
                maxteid=jss2['gtp']['maxteid']

                global_number_eps=len(jss2['eb']) #возможно ошибка
                #print('scenr=',jss2['user_scenario'])
                ###############################custom
                bufer=[]
                bufer.append(0)
                bufer.append('Custom')

                ###############################
                bufe_pcap=[]

                print('\n !!!!jss2[user_scenario]=',jss2['user_scenario'])
                for i in jss2['user_scenario'][0]['pcap_id']:
                    bufe_pcap.append(i)
                bufer.append(bufe_pcap)
                spisok_scenariev.append(bufer)
                print('\nperv=',spisok_scenariev)
                for it in jss2['user_scenario']:


                    bufer=[]
                    #bufer2=[]
                    bufer.append(it['id'])
                    bufer.append(it['name'])
                    #bufer.append(it['br'])
                    #spisok_outt.append(bufer2)

                    #bufer.append(it['id'])
                    #bufer.append(it['name'])
                    #spisok_outt.append(bufer)
                    bufe_pcap=[]
                    for i in it['pcap_id']:
                        bufe_pcap.append(i)
                    bufer.append(bufe_pcap)
                    #print(bufer)

                    #print(dir())
                    #bufer.append(list(it['pcap_id'].value()))
                    #print(it['pcap_id'])
                    #bufer.append(it['pcap_id'])

                    spisok_scenariev.append(bufer)
                print('\nspisok_scenariev=',spisok_scenariev)
                print('\n jss2[network_scenario]=',jss2['network_scenario'])
                bufe_pcap=[] # не удалять


                bufe_pcap.append('Custom')


                bufe_pcap.append(jss2['network_scenario'][0]['jitter'])
                #bufe_pcap.append(jss2['network_scenario'][0]['jitter'])
                bufe_pcap.append(jss2['network_scenario'][0]['burst'])
                bufe_pcap.append(0)
                network_list.append(bufe_pcap)
                print('\n !!!!!network_list =',network_list)
                print('\n @@@@@@network_list =',jss2['network_scenario'][0])
                #spisok_scenariev
                #print('j=',jss2['network_scenario'])
                for it in jss2['network_scenario'] :
                    bufer=[]
                    bufer.append(it['name'])
                    bufer.append(it['jitter'])
                    bufer.append(it['burst'])
                    bufer.append(it['id'])
                    #print(it)
                    network_list.append(bufer) #name jitter , burst
                print('\ndo network_list=',network_list)




                global start_flag1
                #print('\n js =',['state']['run'])
                if js['state']['run'] == True :
                    start_flag1=start_flag1+1
                    #sesion_1=req.put(f'http://{udras}/state/graph')
                start_flag=True
                if start_flag1%2 == 0:
                    start_flag=True
                else:
                    start_flag=False


                global   secret_key , user_key
                flag_1=False
                for it in secret_key:
                    if login == it:
                        flag_1=True
                flag_2=False
                for it in user_key:
                    if password == it:
                        flag_2=True

                if flag_1 and flag_2:

                    return  redirect(url_for("gra"))
                else:
                    return  render_template('first.html')


        except Exception as ex:
            #conect = False
            return  render_template('first.html')


    return  render_template('first.html')

@app.route('/lengrth_table_scer', methods=[ 'POST'])
def lengrth_table_scer():
    if request.method == 'POST':
        global lang_switch
        lang_switch=lang_switch+1

        return redirect(url_for("scenar_spis"))
@app.route('/lengrth_table_network', methods=[ 'POST'])
def lengrth_table_network():
    if request.method == 'POST':
        global lang_switch
        lang_switch=lang_switch+1

        return redirect(url_for("network_spis"))

@app.route('/lengrth_form_nastroika', methods=[ 'POST'])
def lengrth_form_nastroika():
    if request.method == 'POST':
        global lang_switch ,number_idd
        lang_switch=lang_switch+1

        return redirect(url_for("eps_scenar",number=number_idd))
@app.route('/lengrth_epsbiar_network', methods=[ 'POST'])
def lengrth_epsbiar_network():
    if request.method == 'POST':
        global lang_switch ,number_idd
        lang_switch=lang_switch+1

        return redirect(url_for("eps_network",number=number_idd))
@app.route('/lengrth_epb_table', methods=[ 'POST'])
def lengrth_epb_table():
    if request.method == 'POST':
        global lang_switch
        lang_switch=lang_switch+1

        return redirect(url_for("LIST_EPS"))

@app.route('/lengrth_epsbiar_scene', methods=[ 'POST'])
def lengrth_epsbiar_scene():
    if request.method == 'POST':
        global lang_switch ,number_idd
        lang_switch=lang_switch+1

        return redirect(url_for("eps_scenar",number=number_idd))
#
@app.route('/lengrth_2_gra', methods=[ 'POST'])
def lengrth_2_gra():
    if request.method == 'POST':
        global lang_switch
        lang_switch=lang_switch+1

        return redirect(url_for("gra"))
@app.route('/lengrth_form', methods=[ 'POST'])
def lengrth_form():
    if request.method == 'POST':
        global lang_switch
        lang_switch=lang_switch+1

        return redirect(url_for("Menu"))

@app.route('/back', methods=[ 'POST'])
def back_menu():
    if request.method == 'POST':
        return redirect(url_for("gra"))
@app.route('/back_1', methods=[ 'POST'])
def back_menu_1():
    if request.method == 'POST':
        return redirect(url_for("gra"))
@app.route('/back_2', methods=[ 'POST'])
def back_list_1():
    if request.method == 'POST':
        return redirect("/scenar")
@app.route('/back_3', methods=[ 'POST'])
def back_list_2():
    if request.method == 'POST':
        return redirect("/scenar_network")
@app.route('/back_4', methods=[ 'POST'])
def back_list_4():
    if request.method == 'POST':
        return redirect(url_for('LIST_EPS'))
@app.route('/izmen1', methods=[ 'POST'])
def izmen1():
    if request.method == 'POST':
        print('rabotaetss\n')
        regim=request.form['user_regim']
        #pass
        velocity=request.form['velocity']
        adres_ist=request.form['adres_ist']
        adres_naz=request.form['adres_naz']
        size=request.form['razm_mb']
        TEID=request.form['TEID']
        TEID2=request.form['TEID2']
        #GTP2=request.form['GTP2']
        GTP2= request.form.getlist('GTP2')
        pcap_adr= request.form['pcap_adr']
        #GTP=request.form['GTP']
        out_gtp=True
        if len(GTP2) == 0:
            out_gtp=False
        #print(regim,velocity,adres_ist,out_gtp,adres_naz,TEID,pcap_adr,TEID2)
        stringer=''
        for it in pcap_adr:
            stringer=str(it)


        json_out={

        "params":{
        "mode":int(regim),
        "br":int(velocity),
        "file":{
        "path": pcap_adr,
        "size": int(size)},
        "gtp":{
        "use": out_gtp,
        "ipsrc": str(adres_ist),
        "ipdst": str(adres_naz),
        "minteid": int(TEID),
        "maxteid": int(TEID2)}
        }
        }
        #print(json_out)
        json_out2=json.dumps(json_out)
        print('json_2=',json_out2)
        #req.put
        rr=req.put(f'http://{udras}/params/common',json=(json_out2))
        print('rr=',rr.text)



        # вставить изменения из общего конфигурации form
        return redirect(url_for("gra"))

@app.route('/izmen_scenari/new', methods=[ 'POST','GET'])
def izmen_scenari():
    if request.method == 'POST' or request.method == 'GET':
        print('\n zachel_rabotaet')
        print('\n zachel_rabotaet')
        scen=int(request.form['scenar_number234'])
        #regim=request.form['user_regim']
        scenar_pcap =request.form.getlist('scenar')
        print('\n scenar_pcap=',scenar_pcap)
        print('\n scen=',scen)
        vr_summ=0
        scenar_izmen=[]
        for i in scenar_pcap:
            scenar_izmen.append(int(i))
        vr_summ=0
        for i in scenar_izmen:
            print(pcap_cortg[i-1])
            vr_summ=vr_summ+pcap_cortg[i-1][1]


        bufer=0
        g=0

        for it in spisok_scenariev :
            if scen == int(it[0]):
                bufer=g
            g=g+1

        print('\nspisok_sceanarieb=',spisok_scenariev[bufer][1])
        name=spisok_scenariev[bufer][1]
        if scen == 0:
            spisok_scenariev[bufer][2]=scenar_izmen


        if scen != 0:

            json_out={
            "params":{
            "user_scenario":[{
            "id": scen,
            "name":name,
            "br": int(vr_summ),
            "pcap_id":scenar_izmen
            }]
            }
            }
            print('do json=',json_out)
            try :
                print('do do put scenario out=',json)
                rr=req.put(f'http://{udras}/params/user_scenario',json=(json_out))
                js = json.loads(rr.text)
                print('\nout_put_scenar=',js)

                if js['response']['code'] == 0 :
                    return redirect(url_for('scenar_spis'))
                else:
                    return redirect(url_for('scenar_spis'))
            except Exception as ex:
                return  render_template('first.html')
        else:
            return redirect(url_for('scenar_spis'))

        #pass




@app.route('/izmen2', methods=[ 'POST']) # добавить условие при  нуле custom
def izmen2():
    if request.method == 'POST':
        print('rabotaetss\n')
        #eb=request.form.getlist('scenar')
        #print('\n eb=',eb)

        eb=int(request.form['eps_number'])
        num_scen=int(request.form['eps_scen'])
        eps_netw=int(request.form['eps_netw'])
        print('\neb=',eb)
        print(dir(request.form))
        print('\npcap_cortg=',pcap_cortg)
        scenar=request.form.getlist('scenar')
        scenar_izmen=[]
        vr_summ=0
        id=0
        id_netw=0
        #spisok_scenariev
        for i in scenar:
            scenar_izmen.append(int(i))
        print('\n !!!!!!!!!!!!!!!!! scenar=',scenar_izmen)
        print('\nnum_scen=',num_scen)
        print('\neps_netw=',eps_netw)
        print('\nspis_scenar=',spisok_scenariev[num_scen])
        print('\nallspis_scenar=',spisok_scenariev)

        print('\nspis_netw=',network_list[eps_netw])
        print('\nallspis_netw=',network_list)

        ############################newtork###################################################################
        jitter_timeup=int(request.form['jitter_timeup'])

        jitter_timedown=int(request.form['jitter_timedown'])
        jitter_value=int(request.form['jitter_value'])
        burst_timeup=int(request.form['burst_timeup'])
        burst_timedown=int(request.form['burst_timedown'])

        ###############################################################################################

        flag_scenar=False
        name_scenar=''
        print('\n \n !!!!!!!!!!!!!!!!!!! len len len spisok_scenariev[num_scen][2]=',len(spisok_scenariev[num_scen][2]))
        print('\n \n !!!!!!!!!!!!!!!!!!! len len len scenar_izmen=',len(scenar_izmen))
        if spisok_scenariev[num_scen][2] == scenar_izmen and len(spisok_scenariev[num_scen][2])== len(scenar_izmen):
            print('sovpadate')
            flag_scenar=True
            id = num_scen
            name_scenar=spisok_scenariev[num_scen][1]

        else:
            print('nesovpadate')
            flag_scenar=False
            id = 0
            name_scenar='Custom'
        flag_netw=False
        print(network_list[eps_netw])
        if jitter_timeup == int(network_list[eps_netw][1]['timeup']) and  jitter_timedown == int(network_list[eps_netw][1]['timedown']) and jitter_value == int(network_list[eps_netw][1]['value']) and  burst_timeup == int( network_list[eps_netw][2]['timeup']) and burst_timedown ==  int(network_list[eps_netw][2]['timedown']):
            print('sovpadate')
            flag_netw=True
            id_netw = eps_netw
            print(network_list[eps_netw])
            name_netw=network_list[eps_netw][0]

        else:
            print('nesovpadate')
            flag_netw=False
            id_netw = 0
            name_netw='Custom'

        if spisok_scenariev[num_scen][0] == 0:
            print('nesovpadate')
            flag_scenar=False
            id = 0
            name_scenar='Custom'

        if network_list[eps_netw][3] == 0:
            print('nesovpadate')
            flag_netw=False
            id_netw = 0
            name_netw='Custom'

        print('scenar=',flag_scenar,'netw=',flag_netw)

        jsno_out={}
        #if  flag_netw and flag_netw :
        vr_summ=0
        for i in scenar_izmen:
            print(pcap_cortg[i-1])
            vr_summ=vr_summ+pcap_cortg[i-1][1]
        vr_summ=int(request.form['znachenie'])
        print('vr_summ=',vr_summ)
        json_out={}
        json_out2=0

        #for iitre in scenar_izmen:
        if  flag_scenar == False and  flag_netw == False  :
            json_out={
            "params":{
            "eb": [{
            "id":int(eb),
            "br":int(vr_summ),
            "user_scenario":{
            "id": 0,
            "name": name_scenar,
            "br": int(vr_summ),
            "pcap_id":scenar_izmen
            }, "network_scenario":{
            "id": 0,
            "name": "Custom",
            "jitter" :{
            "timeup":jitter_timeup,
            "timedown":jitter_timedown,
            "value":jitter_value
            },
            "burst": {
            "timeup":burst_timeup,
            "timedown":burst_timedown
            }
            }
            }]
            }
            }
            json_out2=json.dumps(json_out)
            print('json_2=',json_out)
            try:
                rr=req.put(f'http://{udras}/params/eb',json=(json_out))

                js = json.loads(rr.text)
                print('\nFalse False=',js)

                if js['response']['code'] == 0 :
                    return redirect(url_for('LIST_EPS'))
                else:
                    return redirect(url_for('LIST_EPS'))
            except Exception as ex:
                return  render_template('first.html')

        if  flag_scenar == True and  flag_netw == True  :
            json_out={
            "params":{
            "eb": [{
            "id":int(eb),
            "br":int(vr_summ),
            "user_scenario":{
            "id": int(id)

            }, "network_scenario":{
            "id": int(id_netw)
            }
            }]
            }
            }
            json_out2=json.dumps(json_out)
            print('json_2=',json_out)
            try:
                rr=req.put(f'http://{udras}/params/eb',json=(json_out))

                js = json.loads(rr.text)
                print('\nTrue True=',js)

                if js['response']['code'] == 0 :
                    return redirect(url_for('LIST_EPS'))
                else:
                    return redirect(url_for('LIST_EPS'))
            except Exception as ex:
                return  izmen2render_template('first.html')
        if  flag_scenar == True and  flag_netw == False  :
            json_out={
            "params":{
            "eb": [{
            "id":int(eb),
            "br":int(vr_summ),
            "user_scenario":{
            "id": int(id)
            }, "network_scenario":{
            "id": 0,
            "name": "Custom",
            "jitter" :{
            "timeup":jitter_timeup,
            "timedown":jitter_timedown,
            "value":jitter_value
            },
            "burst": {
            "timeup":burst_timeup,
            "timedown":burst_timedown
            }
            }
            }]
            }
            }
            json_out2=json.dumps(json_out)
            print('json_2=',json_out)
            try:
                rr=req.put(f'http://{udras}/params/eb',json=(json_out))

                js = json.loads(rr.text)
                print('\nTrue False=',js)

                if js['response']['code'] == 0 :
                    return redirect(url_for('LIST_EPS'))
                else:
                    return redirect(url_for('LIST_EPS'))
            except Exception as ex:
                return  render_template('first.html')
        if  flag_scenar == False and  flag_netw == True  :
            json_out={
            "params":{
            "eb": [{
            "id":int(eb),
            "br":int(vr_summ),
            "user_scenario":{
            "id": 0,
            "name": name_scenar,
            "br": int(vr_summ),
            "pcap_id":scenar_izmen
            }, "network_scenario":{
            "id": int(id_netw)
            }
            }]
            }
            }
            json_out2=json.dumps(json_out)
            print('json_2=',json_out)
            try:
                rr=req.put(f'http://{udras}/params/eb',json=(json_out))

                js = json.loads(rr.text)
                print('\nFalse True=',js)

                if js['response']['code'] == 0 :
                    return redirect(url_for('LIST_EPS'))
                else:
                    return redirect(url_for('LIST_EPS'))
            except Exception as ex:
                return  render_template('first.html')

        #network=request.form['network']
        #print('\neb=',eb)
        #print('\nnetwork=',network)



        # вставить изменения из общего конфигурации form
        return redirect(url_for("LIST_EPS"))


@app.route('/eb_ALL/add', methods=[ 'POST'])
def eb_all_add():
    global  eps_br , spisok_scenariev , network_list

    if request.method == 'POST' :
        col=int(request.form['colich'])
        print('\n 222 spisok_scenariev =',spisok_scenariev)
        print('\n 2222 network_list =',network_list)
        scenar=request.form.getlist('scenar')
        print('\n \n \n \n scenar=',scenar)
        scenar_numb=0
        for it  in scenar:
            scenar_numb= int(it)

        network=request.form.getlist('network')
        print('\n \n \n \n network=',network)
        pass

        network_numb=0
        for it  in network:
            network_numb= int(it)

        print('\n scenar=',scenar)
        print('\n network=',network)
        print('\n eps_br=',eps_br)
        #out=len(eps_br)-1
        #print('\n out=',eps_br[out])
        print('\n eps_br=',eps_br)
        spisok_eps=[]
        for i in eps_br:
            spisok_eps.append(int(i[3]))
        j=0
        js=[]

        for ii in range(1,201) :

            if ii not in spisok_eps :
                print('\n zachodit i=',ii)
                j=j+1
                if network_numb == 0 and scenar_numb == 0:
                    print('\n scenar_numb = ', spisok_scenariev[scenar_numb])
                    print('\n scenar_numb = ', scenar_numb)
                    print('\n network_numb = ', network_list[network_numb])
                    print('\n network_numb = ', network_numb)
                    #new_id=int(eps_br[out][3])+i
                    #vr_summ1=spisok_scenariev[scenar_numb][0]
                    scenar_izmen=[]

                    #vr_summ=0 #pcap_cortg[i-1][1]
                    scenar_izmen=[]
                    for it in spisok_scenariev[scenar_numb][2] :
                        scenar_izmen.append(int(it))

                    vr_summ=0
                    for i in scenar_izmen:
                        #print(pcap_cortg[i-1])
                        vr_summ=vr_summ+pcap_cortg[i-1][1]

                    json_out={
                    "params":{
                    "eb": [{
                    "id":ii,
                    "br":int(vr_summ),
                    "user_scenario":{
                    "id": 0,
                    "name": "Custom",
                    "br": int(vr_summ),
                    "pcap_id":spisok_scenariev[scenar_numb][2]
                    }, "network_scenario":{
                    "id": 0,
                    "name": "Custom",
                    "jitter" :{
                    "timeup":network_list[network_numb][1]['timeup'],
                    "timedown":network_list[network_numb][1]['timedown'],
                    "value":network_list[network_numb][1]['value']
                    },
                    "burst": {
                    "timeup":network_list[network_numb][2]['timeup'],
                    "timedown":network_list[network_numb][2]['timedown']
                    }
                    }
                    }]
                    }
                    }
                    try :
                        print('do do put scenario out=',json_out)
                        rr=req.post(f'http://{udras}/params/eb',json=(json_out))
                        js = json.loads(rr.text)
                        print('\nout_put_scenar=',js)


                    except Exception as ex:
                        return  render_template('first.html')
                        print('do do =',json_out)

                if network_numb == 0 and scenar_numb != 0:
                    print('\n scenar_numb = ', spisok_scenariev[scenar_numb])
                    print('\n scenar_numb = ', scenar_numb)
                    print('\n network_numb = ', network_list[network_numb])
                    print('\n network_numb = ', network_numb)
                    print('\n \n \n  !!!!!!!!!!!!!!!!! = ', spisok_scenariev[scenar_numb][0])
                    #new_id=int(eps_br[out][3])+i
                    vr_summ1=spisok_scenariev[scenar_numb][0]
                    scenar_izmen=[]


                    #vr_summ=0 #pcap_cortg[i-1][1]
                    scenar_izmen=[]
                    for it in spisok_scenariev[scenar_numb][2] :
                        scenar_izmen.append(int(it))

                    vr_summ=0
                    for i in scenar_izmen:
                        #print(pcap_cortg[i-1])
                        vr_summ=vr_summ+pcap_cortg[i-1][1]

                    json_out={
                    "params":{
                    "eb": [{
                    "id":ii,
                    "br":int(vr_summ),
                    "user_scenario":{
                    "id": spisok_scenariev[scenar_numb][0]

                    }, "network_scenario":{
                    "id": 0,
                    "name": "Custom",
                    "jitter" :{
                    "timeup":network_list[network_numb][1]['timeup'],
                    "timedown":network_list[network_numb][1]['timedown'],
                    "value":network_list[network_numb][1]['value']
                    },
                    "burst": {
                    "timeup":network_list[network_numb][2]['timeup'],
                    "timedown":network_list[network_numb][2]['timedown']
                    }
                    }
                    }]
                    }
                    }

                    try :
                        print('do do put scenario out=',json_out)
                        rr=req.post(f'http://{udras}/params/eb',json=(json_out))
                        js = json.loads(rr.text)
                        print('\nout_put_scenar=',js)


                    except Exception as ex:
                        return  render_template('first.html')
                        print('do do =',json_out)

                if network_numb != 0 and scenar_numb != 0:
                    print('\n scenar_numb = ', spisok_scenariev[scenar_numb])
                    print('\n scenar_numb = ', scenar_numb)
                    print('\n network_numb = ', network_list[network_numb])
                    print('\n network_numb = ', network_numb)
                    #new_id=int(eps_br[out][3])+i
                    vr_summ1=spisok_scenariev[scenar_numb][0]
                    scenar_izmen=[]


                    #vr_summ=0 #pcap_cortg[i-1][1]
                    scenar_izmen=[]
                    for it in spisok_scenariev[scenar_numb][2] :
                        scenar_izmen.append(int(it))

                    vr_summ=0
                    for i in scenar_izmen:
                        #print(pcap_cortg[i-1])
                        vr_summ=vr_summ+pcap_cortg[i-1][1]
                    json_out={
                    "params":{
                    "eb": [{
                    "id":ii,
                    "br":int(vr_summ),
                    "user_scenario":{
                    "id": spisok_scenariev[scenar_numb][0]

                    }, "network_scenario":{
                    "id": network_list[network_numb][3]
                    }

                    }]
                    }
                    }
                    try :
                        print('do do put scenario out=',json_out)
                        rr=req.post(f'http://{udras}/params/eb',json=(json_out))
                        js = json.loads(rr.text)
                        print('\nout_put_scenar=',js)


                    except Exception as ex:
                        return  render_template('first.html')
                        print('do do =',json_out)

                if network_numb != 0 and scenar_numb == 0:
                    print('\n scenar_numb = ', spisok_scenariev[scenar_numb])
                    print('\n scenar_numb = ', scenar_numb)
                    print('\n network_numb = ', network_list[network_numb])
                    print('\n network_numb = ', network_numb)
                    #new_id=int(eps_br[out][3])+i
                    vr_summ1=spisok_scenariev[scenar_numb][0]
                    scenar_izmen=[]


                    #vr_summ=0 #pcap_cortg[i-1][1]
                    scenar_izmen=[]
                    for it in spisok_scenariev[scenar_numb][2] :
                        scenar_izmen.append(int(it))

                    vr_summ=0
                    for i in scenar_izmen:
                        #print(pcap_cortg[i-1])
                        vr_summ=vr_summ+pcap_cortg[i-1][1]
                    json_out={
                    "params":{
                    "eb": [{
                    "id":ii,
                    "br":int(vr_summ),
                    "user_scenario":{
                    "id": 0,
                    "name": "Custom",
                    "br": int(vr_summ),
                    "pcap_id":spisok_scenariev[scenar_numb][2]
                    }, "network_scenario":{
                    "id": network_list[network_numb][3]
                    }

                    }]
                    }
                    }

                    try :
                        print('do do put scenario out=',json_out)
                        rr=req.post(f'http://{udras}/params/eb',json=(json_out))
                        js = json.loads(rr.text)
                        print('\nout_put_scenar=',js)


                    except Exception as ex:
                        return  render_template('first.html')
                        print('do do =',json_out)
            if j == col :
                break

        if js['response']['code'] == 0 :

            return redirect(url_for('LIST_EPS'))
        else:
            return redirect(url_for('LIST_EPS'))


@app.route('/eb/add', methods=[ 'POST'])
def eb_add():
    """ Добавление нового EPS_BIAR"""
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    if request.method == 'POST' :
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        global  eps_br
        print('\n!!!!!!!!!!!!!!eps_br=',eps_br)
        new_id=len(eps_br)+1
        #if new_id == 0:
            #new_id=new_id+1
        print('new_id=',new_id)

        scenar_izmen=[]
        vr_summ=0

        if new_id <=200 :

            try:
                for i in scenar_izmen:
                    #print(pcap_cortg[i-1])
                    vr_summ=vr_summ+pcap_cortg[i-1][1]

                json_out={
                "params":{
                "eb": [{
                "id":new_id,
                "br":int(vr_summ),
                "user_scenario":{
                "id": 0,
                "name": "Custom",
                "br": int(vr_summ),
                "pcap_id":scenar_izmen
                }, "network_scenario":{
                "id": 0,
                "name": "Custom",
                "jitter" :{
                "timeup":0,
                "timedown":0,
                "value":0
                },
                "burst": {
                "timeup":0,
                "timedown":0
                }
                }
                }]
                }
                }
                print('do do =',json_out)
                rr=req.post(f'http://{udras}/params/eb',json=(json_out))

                js = json.loads(rr.text)
                print('\nadd new EPSBEAR=',js)

                if js['response']['code'] == 0 :
                    return redirect(url_for('LIST_EPS'))
                else:
                    return redirect(url_for('LIST_EPS'))
            except Exception as ex:
                return  render_template('first.html')

        #pass
@app.route('/eps_epb/add', methods=[ 'POST','GET'])
def eps_epb_add():
    global   eps_br
    if request.method == 'POST' or request.method == 'GET':
        number_eps= int(request.form['scenar_number'])
        eps_tek_uscher=[]
        g=0
        for itt in eps_br :
            if number_eps == int(itt[3]):
                eps_tek_uscher=itt
                break
            g=g+1
        #print('\n x x =',len(eps_br[g][4]))
        ber=[]

        if len(eps_br[g][4]) == 3:
            ber=eps_br[g][4][2]
            new=[]
            for it in ber:
                new.append(it)
            new.append(1)
            eps_br[g][4][2]=new
        else:
            ber=eps_br[g][4]['pcap_id']
            new=[]
            for it in ber:
                new.append(it)
            new.append(1)
            eps_br[g][4]['pcap_id']=new
        print('\n wert epss=',eps_br[g])
        print('\n \n wert epss=',spisok_scenariev)

        return  redirect(url_for("eb_nastroit",number = number_eps))


@app.route('/eps_epb/delete/<int:num>', methods=[ 'POST','GET'])
def eps_epb_delete(num):
    global   eps_br
    if request.method == 'POST' or request.method == 'GET':
        number_eps= int(request.form['scenar_number'])
        eps_tek_uscher=[]

        g=0
        for itt in eps_br :
            if number_eps == int(itt[3]):
                eps_tek_uscher=itt
                break
            g=g+1
        #print('\n x x =',len(eps_br[g][4]))
        ber=[]
        print('\n \n num=',num)



        if len(eps_br[g][4]) == 3:
            ber=eps_br[g][4][2]
            new=[]
            for it in ber:
                if num != int(it):
                    new.append(it)
            #new.append(1)
            eps_br[g][4][2]=new
        else:
            ber=eps_br[g][4]['pcap_id']
            new=[]
            for it in ber:
                if num != int(it):
                    new.append(it)
            eps_br[g][4]['pcap_id']=new
        #print('\n epss=',eps_br[g])

        return  redirect(url_for("eb_nastroit",number = number_eps))


@app.route('/eb/nastroit/<int:number>', methods=[ 'POST','GET'])
def eb_nastroit(number):
    #print("!!!!!!!!!!!!!!!!!!! rabotaer")
    global  time_otvet , lang_switch , conect ,number_idd , eps_br
    global  spisok_scenariev ,  network_list ,eb_pies_for_one,time_otvet

    number_idd=number
    buferr_scena=0
    buferr_network=0

    punkt_menu_nach=[['Back','Change' ,'EPS number','number user scenario','number network scenario'],['Назад','Изменить' ,'Номер EPS','Номер 	пользовательского сценария','Номер Сетевого сценария']]
    lang_bool=False
    punkt_menu=[]
    if lang_switch%2== 0:
        punkt_menu=punkt_menu_nach[0]
        lang_bool=True
    else:
        punkt_menu=punkt_menu_nach[1]
        lang_bool=False

    if request.method == 'POST' or request.method == 'GET':
        global conect  , ind_sce_0_iter , ind_sce_0,  net_sce_0 , indef_scen ,indef_netw
        eps_tek_uscher=[]

        if ind_sce_0_iter==0 :
            ind_sce_0=int(request.form['scenar'])
            net_sce_0= int(request.form['network'])
            g=0
            print('\n \n rabota\n')
            print('\n spisok_scenariev=',spisok_scenariev)
            print('\n network_list=',network_list)
            print('\n ind_sce_0=',ind_sce_0)
            print('\n net_sce_0=',net_sce_0)

            for itt in eps_br :
                if number == int(itt[3]):
                    eps_tek_uscher=itt
                    break
                g=g+1
            print('\n eps_br=',eps_br[g])
            lerg2=[]
            #for lit in spisok_scenariev:
                #print('\n lit=',lit)
                #if lit[0] == ind_sce_0:
            lerg2=spisok_scenariev[ind_sce_0]
            print('\n xer eps_br=',eps_br[g][1])
            print('\n xer lerg=',lerg2)
            eps_br[g][1]['id']=lerg2[0]
            eps_br[g][4]=lerg2


            print('\n spisok_scenariev=',spisok_scenariev)
            print('\n lerg=',lerg2)
            lerg=[]
            lerg=network_list[net_sce_0]
            #for lit in network_list:
                #if lit[3] == net_sce_0:
                    #lerg1=lit
            eps_br[g][2]['id']=lerg[3]
            eps_br[g][5]=lerg
            print('\n \n 11111eps_br=',eps_br)


            #pass
        #ind_sce_0=  #int(request.form['scenar'])
        #net_sce_0= #int(request.form['network'])
        #indef_scen= #int(request.form['scenar'])-1
        #indef_netw= #int(request.form['network'])-1
        ind_sce_0_iter=ind_sce_0_iter+1
        print('\nindef_scen=',indef_scen)
        print('\nindef_netw=',indef_netw)
        print('\nindef_netw=',indef_netw)



        #for itt in eps_br :
        eps_tek_uscher=[]
        for itt in eps_br :
            if number == int(itt[3]):
                eps_tek_uscher=itt
        print('\n x x =',eps_tek_uscher)
        if ind_sce_0 >0 :
            ind_sce_0=eps_tek_uscher[1]['id']  #int(request.form['scenar'])
            net_sce_0= eps_tek_uscher[2]['id']#int(request.form['network'])
            indef_scen= eps_tek_uscher[1]['id']-1
            indef_netw= eps_tek_uscher[2]['id']-1

        zagolovok =[]
        #zagolovok =[]

        eb_pies_for_one=eb_pies_for_one+1
        outp=[]
        for it in range(eb_pies_for_one) :
            outp.append('')

        print('spisok_scenariev=',spisok_scenariev)
        scenar_podchodit=[]
        scenar_netw=[]

        g=0
        out_pcap_spis=[]
        string_pcap=[]
        out_pcap_id=[]
        size_min=0
        spisok_pcapof=[]
        for it in pcap_cortg:
            bufer_str=''
            g=g+1
            out_pcap_spis.append({'key':g,'video':it[0],'br_v':it[1],'path':it[2]})
            bufer_str=str(it[0])+', '+str(it[1])+', '+str(it[2])
            string_pcap.append({'key':g,'string':bufer_str})

        print('\nstr_pcap=',string_pcap)


        if indef_scen <0 :

            print('eps_tek_uscher=',eps_tek_uscher[4])

            spisok_pcapof=eps_tek_uscher[4]['pcap_id']
            size_min=eps_tek_uscher[4]['br']

        else:
            spisok_pcapof=eps_tek_uscher[4][2]
            size_min=0
            for iter in spisok_pcapof:
                for iler in out_pcap_spis:
                    if iter == iler['key']:
                        size_min=size_min+iler['br_v']



        out_pcap_id=[]
        for iter in spisok_pcapof:
            out_pcap_id.append({'znach':int(iter)})

        if indef_netw <0 :
            zagolovok.append(int(eps_tek_uscher[5]['jitter']['timeup']))
            zagolovok.append(int(eps_tek_uscher[5]['jitter']['timedown']))
            zagolovok.append(int(eps_tek_uscher[5]['jitter']['value']))
            zagolovok.append(int(eps_tek_uscher[5]['burst']['timeup']))
            zagolovok.append(int(eps_tek_uscher[5]['burst']['timedown']))
            #ebs_id=eps_br[number-1][2]
            #print('ebs_id=',ebs_id)

            #if eps_br[number-1][2]['id'] == 0:
                #ert=eps_br[number-1][2]
                #print('ert=',ert)
                #poluch=ert['jitter']
                #zagolovok.append(int(poluch['timeup']))
                #zagolovok.append(int(poluch['timedown']))
                #zagolovok.append(int(poluch['value']))
                #poluch=ert['burst']
                #zagolovok.append(int(poluch['timeup']))
                #zagolovok.append(int(poluch['timedown']))

            #else:
                #znach=network_list[0]
                #buferr=[]
                #video=[]
                #pcap_velocity=[]
                #js_jitter=znach[1]
                #zagolovok.append(int(js_jitter['timeup']))
                #zagolovok.append(int(js_jitter['timedown']))
                #zagolovok.append(int(js_jitter['value']))
                #js_jitter=znach[2]
                ##zagolovok =[]
                #zagolovok.append(int(js_jitter['timeup']))
                #zagolovok.append(int(js_jitter['timedown']))
                #scenar_netw=network_list[indef_netw]

        else:
            print('eps_tek_uscher[5][1]=',eps_tek_uscher[5][1])
            zagolovok.append(int(eps_tek_uscher[5][1]['timeup']))
            zagolovok.append(int(eps_tek_uscher[5][1]['timedown']))
            zagolovok.append(int(eps_tek_uscher[5][1]['value']))
            zagolovok.append(int(eps_tek_uscher[5][2]['timeup']))
            zagolovok.append(int(eps_tek_uscher[5][2]['timedown']))
            ############################################################
            #buferr_network=0
            #for it in network_list:
                #if net_sce_0 == it[0]:
                    #break
            #buferr_network=buferr_network+2

            #znach=network_list[buferr_network]
            #print('xerty znach=',znach)
            #buferr=[]
            #video=[]
            #pcap_velocity=[]
            #js_jitter=znach[1]

            #zagolovok.append(int(js_jitter['timeup']))
            #zagolovok.append(int(js_jitter['timedown']))
            #zagolovok.append(int(js_jitter['value']))
            #js_jitter=znach[2]
            #zagolovok =[]
            #zagolovok.append(int(js_jitter['timeup']))
            #zagolovok.append(int(js_jitter['timedown']))
            #print(zagolovok)
            #scenar_netw=network_list[indef_netw]

            #out_pcap_id=[]
            #print('scenar_podchodit=',scenar_podchodit)
            #size_min=0
            #out_pcap_spis.append({'key':g,'video':it[0],'br_v':it[1],'path':it[2]})
            #for i in scenar_podchodit:
                #size_min=size_min+int(out_pcap_spis[i-1]['br_v'])
                #out_pcap_id.append({'znach':i})
        print('size_min=',size_min)

        print('werwds=',out_pcap_id)
        print('zagolovok=',zagolovok)
        print('number=',number)
        print('network_list=',network_list)
        return render_template('form_nastroika.html',eps_number=number,size_min=size_min,punkt_menu=punkt_menu,conect=conect,lang_bool=lang_bool,

        int_scenar=ind_sce_0,int_netw=net_sce_0,pcap_spis=out_pcap_spis,pcap_id=out_pcap_id,string_pcap=string_pcap,zagolovok=zagolovok,eb_pies_for_one=outp,number=number,time_otvet=time_otvet)

@app.route('/eps_scenar/add', methods=[ 'POST'])
def add_pcap_scen():
    global  time_otvet , lang_switch , conect

    punkt_menu_nach=[['Back','Change' ,'EPS number','number user scenario','number network scenario'],['Назад','Изменить' ,'Номер EPS','Номер 	пользовательского сценария','Номер Сетевого сценария']]
    lang_bool=False
    punkt_menu=[]
    if lang_switch%2== 0:
        punkt_menu=punkt_menu_nach[0]
        lang_bool=True
    else:
        punkt_menu=punkt_menu_nach[1]
        lang_bool=False
    if request.method == 'POST':

            scen=int(request.form['scenar_number'])
            print('\nrabotaet=',1)

            global spisok_scenariev

            bufer=0
            g=0

            for it in spisok_scenariev :
                if scen == int(it[0]):
                    bufer=g
                g=g+1
            znach=spisok_scenariev[bufer]
            print('znach=',znach)
            buferr=[]
            video=[]
            pcap_velocity=[]
            #print('2=',znach)
            values=[]

            for it in znach[2]:
                puth=[]
                puth.append(pcap_cortg[it-1][0])
                puth.append(pcap_cortg[it-1][1])
                puth.append(pcap_cortg[it-1][2])
                buferr.append(puth)
            size=0
            ###############################################################################
            g=0
            out_pcap_spis=[]
            string_pcap=[]
            out_pcap_id=[]
            for it in pcap_cortg:
                bufer_str=''
                g=g+1
                out_pcap_spis.append({'key':g,'video':it[0],'br_v':it[1],'path':it[2]})
                bufer_str=str(it[0])+', '+str(it[1])+', '+str(it[2])
                string_pcap.append({'key':g,'string':bufer_str})
            ###############################################################################

            video=0
            dontvideo=0
            #print('spisok=',spisok_scenariev[number-1])
            promeg=spisok_scenariev[bufer][2]
            pr=[]

            print('do do !!!!!!!!!!!!!!!out_pcap_id=',spisok_scenariev[bufer][2])

            spisok_scenariev[bufer][2].append(1)

            scenar_podchodit=spisok_scenariev[bufer][2]
            out_pcap_id=[]
            for i in scenar_podchodit:
                out_pcap_id.append({'znach':i})
            print('!!!!!!!!!!!!!!!out_pcap_id=',spisok_scenariev[bufer][2])

            for i in     out_pcap_id :
                #print('i=',i)
                for j in out_pcap_spis:
                    #print('j=',j)
                    if i['znach'] == j['key']:
                        size=size+j['br_v']
                        if j['video'] :
                            video=video+j['br_v']
                        else:
                            dontvideo=dontvideo+j['br_v']




            values.append(video/size*100)
            values.append(dontvideo/size*100)

            start_flag=True
            print('!!!!!!!!!!!!!rabotaet=',scenar_podchodit)



            return render_template('epsbiar_scene.html',punkt_menu=punkt_menu,conect=conect, scen_number =scen, set=zip(values,labels),berr=buferr ,size=size,string_pcap=string_pcap,pcap_id=out_pcap_id,time_otvet=time_otvet,start_flag1=start_flag)




@app.route('/eps_scenar/delete/<int:number>', methods=[ 'POST'])
def delete_pcap_scen(number):
    global  time_otvet , lang_switch , conect ,number_idd , spisok_scenariev

    number_idd=number

    punkt_menu_nach=[['Back','Change' ,'EPS number','number user scenario','number network scenario'],['Назад','Изменить' ,'Номер EPS','Номер 	пользовательского сценария','Номер Сетевого сценария']]
    lang_bool=False
    punkt_menu=[]
    if lang_switch%2== 0:
        punkt_menu=punkt_menu_nach[0]
        lang_bool=True
    else:
        punkt_menu=punkt_menu_nach[1]
        lang_bool=False
    if request.method == 'POST':
        scen=int(request.form['scenar_number'])
        bufer=0
        g=0

        for it in spisok_scenariev :
            if scen == int(it[0]):
                bufer=g
            g=g+1
        print('\nrabotaet=',scen)
        if len(spisok_scenariev[bufer][2]) >1 :
            scen=int(request.form['scenar_number'])
            print('\nrabotaet=',scen)

            pcap_id=int(number)


            znach=spisok_scenariev[bufer]
            buferr=[]
            video=[]
            pcap_velocity=[]
            #print('2=',znach)
            values=[]

            for it in znach[2]:
                puth=[]
                puth.append(pcap_cortg[it-1][0])
                puth.append(pcap_cortg[it-1][1])
                puth.append(pcap_cortg[it-1][2])
                buferr.append(puth)
            size=0
            ###############################################################################
            g=0
            out_pcap_spis=[]
            string_pcap=[]
            out_pcap_id=[]
            for it in pcap_cortg:
                bufer_str=''
                g=g+1
                out_pcap_spis.append({'key':g,'video':it[0],'br_v':it[1],'path':it[2]})
                bufer_str=str(it[0])+', '+str(it[1])+', '+str(it[2])
                string_pcap.append({'key':g,'string':bufer_str})
            ###############################################################################

            video=0
            dontvideo=0
            #print('spisok=',spisok_scenariev[number-1])
            promeg=spisok_scenariev[bufer][2]
            pr=[]
            g=0
            for it in promeg:
                if it == pcap_id:

                    break
                g=g+1

            spisok_scenariev[bufer][2].pop(g)

            scenar_podchodit=spisok_scenariev[bufer][2]
            out_pcap_id=[]
            for i in scenar_podchodit:
                out_pcap_id.append({'znach':i})
            print('!!!!!!!!!!!!!!!out_pcap_id=',)

            for i in     out_pcap_id :
                #print('i=',i)
                for j in out_pcap_spis:
                    #print('j=',j)
                    if i['znach'] == j['key']:
                        size=size+j['br_v']
                        if j['video'] :
                            video=video+j['br_v']
                        else:
                            dontvideo=dontvideo+j['br_v']
            print('size=',size)

            #if size >0 :
            values.append(video/size*100)
            values.append(dontvideo/size*100)

            start_flag=True
            print('!!!!!!!!!!!!!rabotaet=',scenar_podchodit)
            #if scenar_podchodit
            #scenar_podchodit=tuple(scenar_podchodit)


            return render_template('epsbiar_scene.html',punkt_menu=punkt_menu,conect=conect,
             scen_number =scen, set=zip(values,labels)
             ,berr=buferr ,size=size,string_pcap=string_pcap
             ,pcap_id=out_pcap_id,time_otvet=time_otvet,start_flag1=start_flag)
        else:
            return redirect(url_for('eps_scenar',number=scen))


            # pass
@app.route('/eps/scenar/delete/<int:number>', methods=[ 'POST'])
def delete_scenar(number):
    if request.method == 'POST':
        if number !=0  and number>1:
            try:
                json_out={
                "params":{
                "user_scenario":[{
                "id":int(number)
                }]
                }
                }
                json_out2=json.dumps(json_out)
                print('do do rr=',json_out2)

                rr=req.delete(f'http://{udras}/params/user_scenario',json=(json_out))

                js = json.loads(rr.text)
                print('delete outrr=',js)
                #print('js=',js)
                if js['response']['code'] == 0 :
                    return redirect(url_for('scenar_spis'))
                else:
                    return redirect(url_for('scenar_spis'))

            except Exception as ex:
                return  render_template('first.html')
        else:
            return redirect(url_for('scenar_spis'))



@app.route('/eps/network/delete/<int:number>', methods=[ 'POST'])
def delete_network(number):
    if request.method == 'POST':
        if number !=0 and  number>0 :
            try:

                json_out={
                "params":{
                "network_scenario":[{
                "id":int(number)
                }]
                }
                }
                json_out2=json.dumps(json_out)
                print('do do rr=',json_out2)

                rr=req.delete(f'http://{udras}/params/network_scenario',json=(json_out))

                js = json.loads(rr.text)
                print('delete outrr=',js)
                #print('js=',js)
                if js['response']['code'] == 0 :
                    return redirect(url_for('network_spis'))
                else:
                    return redirect(url_for('network_spis'))

            except Exception as ex:
                return  render_template('first.html')
            else:
                pass



@app.route('/eb/delete/<int:number>', methods=[ 'POST'])
def delete_eb(number):
    if request.method == 'POST':
        if len(eps_br)>1 :
            try:
                json_out={
                "params":{
                "eb":[{
                "id":int(number)
                }]
                }
                }
                json_out2=json.dumps(json_out)
                #print('do do rr=',json_out2)

                rr=req.delete(f'http://{udras}/params/eb',json=(json_out))

                js = json.loads(rr.text)
                #print('delete outrr=',js)
                #print('js=',js)
                if js['response']['code'] == 0 :
                    return redirect(url_for('LIST_EPS'))
                else:
                    return redirect(url_for('LIST_EPS'))

            except Exception as ex:
                return  render_template('first.html')
        else:
            return redirect(url_for('LIST_EPS'))

                #pass

        #rr=req.get(f'http://{udras}/params/eb')


    #pass
@app.route('/eps/scenar/<int:number>', methods=[ 'POST','GET'])
def eps_scenar(number):
    """  настройка индивидуального сценария """
    global lang_switch , conect , number_idd
    number_idd=number

    punkt_menu=[]
    punkt_menu_nach=[['back','Change' ,'Video','Bitrate','file'],['назад','Изменить' ,'Видео','Битрейт','файл']]

    lang_bool=False
    punkt_menu=[]
    if lang_switch%2== 0:
        punkt_menu=punkt_menu_nach[0]
        lang_bool=True
    else:
        punkt_menu=punkt_menu_nach[1]
        lang_bool=False
    #global conect


    if request.method == 'POST' or request.method == 'GET':
        #conect=True
        print('number-1=',number)
        print(spisok_scenariev)
        bufer=0
        g=0

        for it in spisok_scenariev :
            if number == int(it[0]):
                bufer=g
            g=g+1

        znach=spisok_scenariev[bufer]
        buferr=[]
        video=[]
        pcap_velocity=[]
        #print('2=',znach)
        values=[]

        for it in znach[2]:
            puth=[]
            puth.append(pcap_cortg[it-1][0])
            puth.append(pcap_cortg[it-1][1])
            puth.append(pcap_cortg[it-1][2])
            buferr.append(puth)
        size=0
        ###############################################################################
        g=0
        out_pcap_spis=[]
        string_pcap=[]
        out_pcap_id=[]
        for it in pcap_cortg:
            bufer_str=''
            g=g+1
            out_pcap_spis.append({'key':g,'video':it[0],'br_v':it[1],'path':it[2]})
            bufer_str=str(it[0])+', '+str(it[1])+', '+str(it[2])
            string_pcap.append({'key':g,'string':bufer_str})
        ###############################################################################

        video=0
        dontvideo=0
        #
        scenar_podchodit=spisok_scenariev[bufer][2]
        out_pcap_id=[]
        print('\n !!! spisok=',scenar_podchodit)
        g=1
        for i in scenar_podchodit:
            out_pcap_id.append({'znach':i,'numb':g})
            g=g+1

        for i in     out_pcap_id :
            #print('i=',i)
            for j in out_pcap_spis:
                #print('j=',j)
                if i['znach'] == j['key']:
                    size=size+j['br_v']
                    if j['video'] :
                        video=video+j['br_v']
                    else:
                        dontvideo=dontvideo+j['br_v']




        values.append(video/size*100)
        values.append(dontvideo/size*100)

        start_flag=True
        if start_flag1%2 == 0:
            start_flag=True
        else:
            start_flag=False


        return render_template('epsbiar_scene.html',punkt_menu=punkt_menu,conect=conect,
        lang_switch=lang_bool, scen_number=number,
        set=zip(values,labels),berr=buferr ,size=size,string_pcap=string_pcap,pcap_id=out_pcap_id,
        time_otvet=time_otvet,start_flag1=start_flag)
@app.route('/network/add', methods=[ 'POST'])
def network_add():
    if request.method == 'POST':
        global network_list
        new_id=len(network_list)+1
        name =request.form['name']
        print('name',name)
        print('\nnew_id=',new_id)
        #name =request.form.getlist['name']
        scenar= request.form.getlist('scenar')
        int_sceanar=[]
        for i in  scenar:
            int_sceanar.append(int(i))
        znach=network_list[int_sceanar[0]-1]
        js_jitter=znach[1]
        zagolovok =[]
        jitter_timeup=int(js_jitter['timeup'])
        jitter_timedown=int(js_jitter['timedown'])
        jitter_value=int(js_jitter['value'])
        zagolovok.append(int(js_jitter['timeup']))
        zagolovok.append(int(js_jitter['timedown']))
        zagolovok.append(int(js_jitter['value']))
        js_jitter=znach[2]
        #zagolovok =[]
        burst_timeup=int(js_jitter['timeup'])
        burst_timedown=int(js_jitter['timedown'])
        zagolovok.append(int(js_jitter['timeup']))
        zagolovok.append(int(js_jitter['timedown']))


        json_out={
        "params":{
        "network_scenario":[{
        "id":new_id,
        "name": name,
        "jitter" :{
        "timeup":jitter_timeup,
        "timedown":jitter_timedown,
        "value":jitter_value
        },
        "burst": {
        "timeup":burst_timeup,
        "timedown":burst_timedown
        }
        }]
        }
        }
        print('do json=',json_out)
        try :
            print( 'do novogo scenaria put scenario out=',json)
            rr=req.post(f'http://{udras}/params/network_scenario',json=(json_out))
            js = json.loads(rr.text)
            print('\nout_put_scenar=',js)

            if js['response']['code'] == 0 :
                return redirect(url_for('network_spis'))
            else:
                return redirect(url_for('network_spis'))
        except Exception as ex:
            return  render_template('first.html')

        #print('scenar',spisok_scenariev[int_sceanar[0]-1])
        pass
    #pass
        #pass
@app.route('/izmen_network/new', methods=[ 'POST'])
def network_change():
    global  network_list
    if request.method == 'POST':

        id_change=int(request.form['scenar_number234'])
        timeup_jitter=int(request.form['timeup_jitter'])
        timedown_jitter=int(request.form['timedown_jitter'])
        value_jitter=int(request.form['value_jitter'])
        timeup_burst=int(request.form['timeup_burst'])
        timedown_burst=int(request.form['timedown_burst'])
        bufer_network=0
        for it in network_list:
            if it[3] == id_change:
                break
            bufer_network=bufer_network+1

        name=network_list[bufer_network][0]
        if id_change != 0 :
            print('\n  \n  23456 network_list=',network_list[bufer_network])
            json_out={
            "params":{
            "network_scenario":[{
            "id": id_change,
            "name": name,
            "jitter" :{
            "timeup":timeup_jitter,
            "timedown":timedown_jitter,
            "value":value_jitter
            },
            "burst": {
            "timeup":timeup_burst,
            "timedown":timedown_burst
            }
            }]
            }
            }
            print('do do =',json_out)
            rr=req.put(f'http://{udras}/params/network_scenario',json=(json_out))

            js = json.loads(rr.text)
            print('\nadd change  izmen_network=',js)

            if js['response']['code'] == 0 :
                return redirect(url_for('network_spis'))
            else:
                return redirect(url_for('network_spis'))
        else:
            network_list[id_change]=['Custom',{'timedown': timedown_jitter, 'timeup': timeup_jitter, 'value': value_jitter},{'timedown': timedown_burst, 'timeup': timeup_burst},network_list[bufer_network][3]]
            return redirect(url_for('network_spis'))

    #pass
@app.route('/eps/network/<int:number>', methods=[ 'POST','GET'])
def eps_network(number):
    global lang_switch , conect , number_idd
    number_idd=number

    punkt_menu=[]
    punkt_menu_nach=[['back','Change' ],['Назад','Изменить' ]]

    lang_bool=False
    punkt_menu=[]
    if lang_switch%2== 0:
        punkt_menu=punkt_menu_nach[0]
        lang_bool=True
    else:
        punkt_menu=punkt_menu_nach[1]
        lang_bool=False
    #global conect
    if request.method == 'POST' or request.method == 'GET':
        number_idd=number
        #znach=network_list[number-1]
        bufer_network=0
        print('\n 23network_list=',network_list)
        for it in network_list:
            if it[3] == number:
                break
            bufer_network=bufer_network+1

        znach=network_list[bufer_network]
        print('\n znach=',znach)
        buferr=[]
        video=[]
        pcap_velocity=[]
        js_jitter=znach[1]
        zagolovok =[]
        zagolovok.append(int(js_jitter['timeup']))
        zagolovok.append(int(js_jitter['timedown']))
        zagolovok.append(int(js_jitter['value']))
        js_jitter=znach[2]
        #zagolovok =[]
        zagolovok.append(int(js_jitter['timeup']))
        zagolovok.append(int(js_jitter['timedown']))
        print(zagolovok)
        global start_flag1
        start_flag=False
        if start_flag1%2 == 0:
            start_flag=True
        else:
            start_flag=False
        print('network start_flag=',start_flag)
        network_number=number



        return render_template('epsbiar_network.html',
        punkt_menu=punkt_menu,lang_bool=lang_bool,conect=conect,
        network_number=network_number,zagolovok=zagolovok,time_otvet=time_otvet,start_flag1=start_flag)




@app.route('/LIST_EPS', methods=[ 'POST','GET'])
def LIST_EPS():
    """ выводит список все EPS_BIAR"""
    global  time_otvet , lang_switch , conect , global_number_eps , ind_sce_0_iter

    punkt_menu_nach=[['Total bitrate (bit/sec)','Bitrate (bit/sec)' ,'User scenario','Network_scenario','Tune','Delete','Back'],['Cуммарный битрейт (бит/сек)','Битрейт (бит/сек )' ,'Пользовательский сценарий','Сетевой сценарий','Настроить','Удалить','Назад']]
    lang_bool=False
    if lang_switch%2== 0:
        punkt_menu=punkt_menu_nach[0]
        lang_bool=True
    else:
        punkt_menu=punkt_menu_nach[1]
        lang_bool=False
    global conect

    if request.method == 'POST' or request.method == 'GET' :

        try:
            ind_sce_0_iter=0
            conect=True
            start=time()
            rr=req.get(f'http://{udras}/params/eb')
            stop=time()-start
            time_otvet=stop*1000
            #GET(/params/eb/1?id=)
            buferr=rr.text
            print('\nbuferrrrrrrrr=',buferr)
            js = json.loads(buferr)
            global eps_br ,spisok_scenariev , network_list
            #print('js=',js)
            print('network_list=',network_list)

            if js['response']['code'] == 0 :
                eps_br=[]
                js2=js['params']['eb']
                print('\n js2=',js2)
                global_number_eps=len(js2)
                for it in js2:
                    bufer=[]
                    #print(,it)
                    bufer.append(it['br'])
                    bufer.append(it['user_scenario'])
                    bufer.append(it['network_scenario'])
                    bufer.append(it['id'])
                    lister=[]
                    lister2=[]
                    print('\n rab=',it['user_scenario'])

                    if it['user_scenario']['id']!=0 :

                        for it2 in spisok_scenariev :
                            #print('\nit2=',it2)
                            if  it['user_scenario']['id'] == int(it2[0]):
                                #print('\n raborasd')
                                #print('\n 23it=',it2)
                                lister=it2
                    else:
                        lister= it['user_scenario']
                        #pass

                    bufer.append(lister)

                    if it['network_scenario']['id']!=0 :

                        for it2 in network_list :
                            print('\nit2=',it2)
                            if  int(it['network_scenario']['id']) == int(it2[3]):
                                print('\n raborasd')
                                print('\n 23it=',it2)
                                lister2=it2
                    else:
                        lister2= it['network_scenario']
                        #pass
                    bufer.append(lister2)

                    eps_br.append(bufer)

            print('\n network_scenario=',network_list)
            print('!!!!!!!!!!!!!!!!!!XXXXXXXXXXXXeps_br=eps_br=',eps_br)
            #pass
            buferr=[]
            i=0
            summer_velocity=0
            for it in eps_br:
                i=i+1
                summer_velocity=summer_velocity+it[0]
                print('\n \n it=',it)
                buferr.append({'key':i,'veloc':it[0],'status':it[1]['id'],'status_nt':it[2]['id'],'global_numb':it[3]})
            #print('SCENAR=',spisok_scenariev)
            #print('buferr=',buferr)
            scenar_lister=[]
            #scenar_lister.append({'name':'Custom','indef':0})
            bufer_network=[]
            #bufer_network.append({'name':'Custom','indef':0})
            g=0
            print('\n spisok_scenariev=',spisok_scenariev)
            for i in spisok_scenariev:
                print('\n i=',i)
                scenar_lister.append({'name':i[1],'indef':g,'indef_ir':i[0]})
                g=g+1

            g=0
            print('\n network_list=',network_list)

            for i in network_list:
                print('\n i=',i)
                bufer_network.append({'name':i[0],'indef':g,'der':i[3]})
                g=g+1

            start_flag=False

            if start_flag1%2 == 0:
                start_flag=True    #bool(5)#"true" #True возможно наборот
            else:
                start_flag=  False #bool(0)#"false" #False
            #print('summer_velocity=',summer_velocity)

            iter_nacha=[1]


            return  render_template('epb_table.html',iter_nacha=iter_nacha,lang_bool=lang_bool,conect=conect,punkt_menu=punkt_menu,summer_velocity=summer_velocity,
            start_flag=start_flag,buferr=buferr,
            scenar_lister=scenar_lister,bufer_network=bufer_network,time_otvet=time_otvet)
            pass

        except Exception as ex:
            time_otvet=0
            bufer_network=[]
            summer_velocity=[]
            buferr=[]
            scenar_lister=[]
            conect = False

            return  render_template('epb_table.html',lang_bool=lang_bool
            ,conect=conect,punkt_menu=punkt_menu,summer_velocity=summer_velocity,
            start_flag=start_flag,buferr=buferr,
            scenar_lister=scenar_lister,bufer_network=bufer_network,time_otvet=time_otvet)




@app.route('/start', methods=[ 'POST'])
def start():
    global conect
    if request.method == 'POST':
        try:
            """отрисовка  """
            global start_flag1
            global conect
            conect=True
            start_flag=False
            json_out={}
            if start_flag1%2 == 0:
                start_flag=True  #False  #bool(5)#"true" #True возможно наборот
            else:
                start_flag= False# False #bool(0)#"false" #False

            start=time()
            json_out={"state":{"run":start_flag}}

            start_flag1=start_flag1+1


            print('do json_out=',json_out)
            sesion_1=req.put(f'http://{udras}/state/run',json=json_out)
            stop=time()-start
            time_otvet =stop*1000
            start_flag=True
            if start_flag1%2 == 0:
                start_flag=True
            else:
                start_flag=False

            print('start_generator',sesion_1.text)
            return  redirect(url_for("gra")) #render_template('2_gra.html')

        except Exception as ex:

            conect=False

            return  redirect(url_for("gra"))



@app.route('/Menu', methods = ['GET','POST'])
def Menu():
    global lang_switch , conect

    #start_flag1=start_flag1+1
    #sesion_1=req.put(f'http://{udras}/state/graph')
    punkt_menu_nach=[['back','change' ,'Mode of operation ','Total bitrate','GTP source address','GTP destination address','GTP TEID value range','Path to pcap files','Bit file size'],['назад','изменить' ,'Режим работы','Суммарный битрейт','Адрес источника GTP','Адрес назначения GTP','Диапазон значения TEID GTP','Путь к файлам pcap','Размер файла Мбит']]

    values=[967.67, 1190.89]
    menu=[]
    znach=0
    if GTP_FLAG:
        znach=1

    zagolovok=[global_velocity,znach,ipsrc,ipdst,minteid,maxteid,global_spis,global_pcath_size,global_number_eps]


    param=False
    lang_bool=False
    if lang_switch%2== 0:
        punkt_menu=punkt_menu_nach[0]
        lang_bool=True

    else:
        punkt_menu=punkt_menu_nach[1]
        lang_bool=False

    print('!!!punkt_menu=',conect)
    start_flag=True
    if start_flag1%2 == 0:
        start_flag=True
    else:
        start_flag=False
    return render_template('form.html',punkt_menu=punkt_menu,conect=conect,
    lang_switch=lang_bool, menu=menu,  set=zip(values, labels),rabota_status=rabota_status,param = param,
    zagolovok=zagolovok,start_flag1=start_flag,regim_rabota_mode=regim_rabota_mode,time_otvet=time_otvet)



@app.route('/scenar/add', methods=['GET', 'POST'])
def scenar_add():
    """ Добавления нового сценария  """
    if request.method == 'POST' or request.method == 'GET':
        global spisok_scenariev
        new_id=len(spisok_scenariev)+1
        name =request.form['name']
        print('name',name)
        #name =request.form.getlist['name']
        scenar= request.form.getlist('scenar')
        int_sceanar=[]
        for i in  scenar:
            int_sceanar.append(int(i))

        vr_summ=0
        scenar_izmen=[]
        for i in spisok_scenariev[int_sceanar[0]-1][2]:
            scenar_izmen.append(int(i))

        for i in scenar_izmen:
            #print(pcap_cortg[i-1])
            vr_summ=vr_summ+pcap_cortg[i-1][1]

        json_out={
        "params":{
        "user_scenario":[{
        "id": new_id,
        "name":name,
        "br": int(vr_summ),
        "pcap_id":scenar_izmen
        }]
        }
        }
        print('do json=',json_out)
        try :
            print( 'do novogo scenaria put scenario out=',json)
            rr=req.post(f'http://{udras}/params/user_scenario',json=(json_out))
            js = json.loads(rr.text)
            print('\nout_put_scenar=',js)

            if js['response']['code'] == 0 :
                return redirect(url_for('scenar_spis'))
            else:
                return redirect(url_for('scenar_spis'))
        except Exception as ex:
            return  render_template('first.html')

        #print('scenar',spisok_scenariev[int_sceanar[0]-1])
        pass
    pass
@app.route('/scenar', methods=['GET', 'POST'])
def scenar_spis():
    """ обработка сценариев значений"""
    global lang_switch , conect


    punkt_menu=[]
    punkt_menu_nach=[['scenario','Delete' ,'Delete','Script add','Name','Close','Back'],['сценарий','Удалить' ,'Удалить','Сценарий добавить','Название','Закрыть','Назад']]

    lang_bool=False
    if lang_switch%2== 0:
        punkt_menu=punkt_menu_nach[0]
        lang_bool=True
    else:
        punkt_menu=punkt_menu_nach[1]
        lang_bool=False
    global conect

    if request.method == 'POST' or request.method == 'GET':

        try:
            global spisok_scenariev , time_otvet

            spisok_outt=[]

            #spisok_outt.append([0,'Custom'])
            start= time()

            rr=req.get(f'http://{udras}/params/user_scenario')
            stop=time()-start
            time_otvet =stop*1000
            bufer=rr.text
            json_poputka=json.loads(bufer)
            print('11 json_poputka',bufer)
            print('\nspisok_scenariev',spisok_scenariev)
            nachalo=[]
            bufer=[]
            bufer2=[]
            if json_poputka['response']['code'] == 0 :
                g=0
                if  len(spisok_scenariev)>1:
                    print('\n \n rabotaet!!!!!!!!!!!!!!!!!!!!')
                    nachalo=spisok_scenariev[0]
                    print('nachalo=',nachalo)
                    bufer2.append(nachalo[0])
                    bufer2.append(nachalo[1])

                    print('\n \n rabotaet!!!!!!!!!!!!!!!!!!!!')

                else:
                    #bufer=[]
                    bufer.append(0)
                    bufer.append('Custom')
                    bufer2.append(0)
                    bufer2.append('Custom')

                    bufe_pcap=[]
                    for i in json_poputka['params']['user_scenario'][0]['pcap_id']:
                        bufe_pcap.append(i)
                    bufer.append(bufe_pcap)
                    nachalo=bufer
                spisok_scenariev=[]
                spisok_scenariev.append(nachalo)

                print('rr2=',json_poputka['params']['user_scenario'])
                spisok_outt.append(bufer2)
                for it in json_poputka['params']['user_scenario']:



                    bufer=[]

                    bufer2=[]
                    bufer2.append(it['id'])
                    bufer2.append(it['name'])
                    spisok_outt.append(bufer2)

                    bufer.append(it['id'])
                    bufer.append(it['name'])
                    #spisok_outt.append(bufer)
                    bufe_pcap=[]
                    for i in it['pcap_id']:
                        bufe_pcap.append(i)
                    bufer.append(bufe_pcap)

                    spisok_scenariev.append(bufer)
                    print('spisok_scenariev=',spisok_scenariev)
                global start_flag1
                print('scenar start_flag1=',start_flag1)
                start_flag=False
                if start_flag1%2 == 0:
                    start_flag=True
                else:
                    start_flag=False
                print('scenar start_flag=',start_flag)
                iter_nacha=[1]

                return  render_template('table_scenari.html',punkt_menu=punkt_menu,conect=conect,lang_switch=lang_bool,
                iter_nacha=iter_nacha,spisok_outt=spisok_outt,time_otvet=time_otvet,start_flag1=start_flag) #redirect(f"/eps/{global_number_eps}")

            else:
                return redirect(url_for('gra'))


        except Exception as ex:
            iter_nacha=[]
            spisok_outt=[]
            time_otvet=0
            start_flag=False
            conect=False
            if start_flag1%2 == 0:
                start_flag=True
            else:
                start_flag=False
            return render_template('table_scenari.html',punkt_menu=punkt_menu,conect=conect,lang_switch=lang_bool,
            iter_nacha=iter_nacha,spisok_outt=spisok_outt,time_otvet=time_otvet,start_flag1=start_flag) #redirect(f"/eps/{global_number_eps}")

            #return  render_template('gra.html')


@app.route('/scenar_network', methods=['GET', 'POST'])
def network_spis():
    """ пользовательские сценари """
    global network_list , time_otvet , lang_switch , conect


    punkt_menu=[]
    punkt_menu_nach=[['scenario','Delete' ,'Delete','Script add','Name','Close','Back'],['сценарий','Удалить' ,'Удалить','Сценарий добавить','Название','Закрыть','Назад']]

    lang_bool=False
    if lang_switch%2== 0:
        punkt_menu=punkt_menu_nach[0]
        lang_bool=True
    else:
        punkt_menu=punkt_menu_nach[1]
        lang_bool=False
    global conect

    if request.method == 'POST' or request.method == 'GET':
        spisok_outt=[]

        #global spisok_scenariev



        #spisok_outt.append([0,'Настраиваемый'])

        start= time()
        rr=req.get(f'http://{udras}/params/network_scenario')
        stop=time()-start
        time_otvet =stop*1000
        bufer=rr.text
        json_poputka=json.loads(bufer)
        print('xx json_poputka',bufer)
        #bufer.append(it['name'])
        #bufer.append(it['jitter'])
        #bufer.append(it['burst'])
        nachalo=[]
        bufer=[]
        bufer2=[]
        #if json_poputka['response']['code'] == 0 :
            #g=0
            #if  len(spisok_scenariev)>1:
                #print('\n \n rabotaet!!!!!!!!!!!!!!!!!!!!')
                #nachalo=spisok_scenariev[0]
                #print('nachalo=',nachalo)
                #bufer2.append(nachalo[0])
                #bufer2.append(nachalo[1])

                #print('\n \n rabotaet!!!!!!!!!!!!!!!!!!!!')

            #else:
                #bufer=[]
                #bufer.append(0)
                #bufer.append('Custom')
                #bufer2.append(0)
                #bufer2.append('Custom')

                #bufe_pcap=[]
                #for i in json_poputka['params']['user_scenario'][0]['pcap_id']:
                    #bufe_pcap.append(i)
                #bufer.append(bufe_pcap)
                #nachalo=bufer
            #spisok_scenariev=[]
            #spisok_scenariev.append(nachalo)

        if json_poputka['response']['code'] == 0 :
            g=0
            nachalo=[]
            print()
            if len(network_list)>1 :
                nachalo=network_list[0]
                print('\n \n nachalo=',nachalo)
                print('\n \n network_list=',network_list)
            else:
                bufe_pcap.append('Custom')
                bufe_pcap.append(json_poputka['params']['network_scenario'][0]['jitter'])
                bufe_pcap.append(json_poputka['params']['network_scenario'][0]['burst'])
                bufe_pcap.append(json_poputka['params']['network_scenario'][0]['id'])
                nachalo=bufe_pcap

                #pass
            network_list=[]
            network_list.append(nachalo)
            #if  len(network_list)>1:
                #nachalo=spisok_scenariev[0]
                #print('nachalo=',nachalo)
                #bufer2.append(nachalo[0])
                #bufer2.append(nachalo[1])
            #else:
                #bufer=[]
                #bufer.append(0)
                #bufer.append('Custom')
                #bufer2.append(0)
                #bufer2.append('Custom')

                #bufe_pcap=[]
                #for i in json_poputka['params']['network_scenario'][0]['pcap_id']:
                    #bufe_pcap.append(i)
                #bufe_pcap.append(json_poputka['params']['network_scenario'][0]['jitter'])
                #bufe_pcap.append(json_poputka['params']['network_scenario'][0]['jitter'])
                #bufe_pcap.append(json_poputka['params']['network_scenario'][0]['burst'])
                #bufer.append(bufe_pcap)
                #nachalo=bufer
            #spisok_scenariev=[]
            #spisok_scenariev.append(nachalo)
                #pass
            #print('json_poputka=',json_poputka['params'].keys())
            #print('rr1=',bufer)
            #print('rr1=',json_poputka.keys())
            #print('rr2=',json_poputka['params']['user_scenario'])
            #bufe_pcap=[]
            #bufe_pcap.append('Custom')


            #bufe_pcap.append(json_poputka['params']['network_scenario'][0]['jitter'])
            #bufe_pcap.append(json_poputka['params']['network_scenario'][0]['jitter'])
            #bufe_pcap.append(json_poputka['params']['network_scenario'][0]['burst'])
            spisok_outt.append([0,'Custom'])
            #network_list.append(bufe_pcap)
            for it in json_poputka['params']['network_scenario']:
                print('it=',it)
                bufer=[]
                bufer2=[]
                bufer3=[]
                bufer2.append(it['id'])
                bufer2.append(it['name'])
                bufer3.append(it['name'])
                bufer3.append(it['jitter'])
                bufer3.append(it['burst'])
                bufer3.append(it['id'])
                spisok_outt.append(bufer2)
                network_list.append(bufer3)


        print('posle network_list=',network_list)

        eps_spis=[]
        global start_flag1
        #global start_flag1
        print('network start_flag1=',start_flag1)
        start_flag=False
        if start_flag1%2 == 0:
            start_flag=True
        else:
            start_flag=False
        print('network start_flag=',start_flag)
        iter_nacha=[1]

        return  render_template('table_network.html',punkt_menu=punkt_menu,conect=conect,lang_bool=lang_bool,
        iter_nacha=iter_nacha,spisok_outt=spisok_outt,eps_spis=eps_spis,
        time_otvet= time_otvet,start_flag1=start_flag) #redirect(f"/eps/{global_number_eps}")

@app.route('/grafik', methods=[ 'POST'])
def grafik():
    if request.method == 'POST' :
        global data2_global , data_grafik1 , data_grafik2

        bufer1=[]
        bufer2=[]

        data_grafik1=request.form.getlist('comp_select')
        print('\n \n 22!!!!!!!!!!!!!!=',data_grafik2)

        for it in  data_grafik1:
            bufer1.append(int(it))
        data_grafik1=bufer1

        data_grafik2=request.form.getlist('data2')
        print('\n \n !!!!!!!!!!!!!!=',data_grafik2)
        for it in  data_grafik2:
            bufer2.append(int(it))
        data_grafik2=bufer2
        return  redirect(url_for("gra"))


@app.route('/registr', methods=[ 'POST'])
def registr():
    return redirect(url_for("nachal"))

@app.route('/gra', methods=[ 'GET'])
def gra():
    """отрисовка  """
    #global start_flag
    #start_flag=True
    global start_flag1 , global_number_eps,lang_switch , conect  , port_adres , data2_global

    bufer=0
    select_eps=0
    select_value=0
    #start_flag1=start_flag1+1
    #sesion_1=req.put(f'http://{udras}/state/graph')
    punkt_menu_nach=[['Start','Stop' ,'Menu','List custom script','List EPS-Bearer','List network_scenario'],['Старт','Стоп', 'Меню','Список пользовательских сценариев','Список EPS-Bearer','Список сетевых сценариев']]
    data=[]
    global_number_eps_1=global_number_eps+1
    for it in range(global_number_eps_1) :
        if it == 0:
            data.append({'name':it,'name2':'ALL'})
        else:
            data.append({'name':it,'name2':str(it)})

    perv=True
    if data_grafik2[0] %2 == 0:
        perv=True
    else:
        perv=False




    #data=[{'name':0}, {'name':1}, {'name':2}]
    start_flag=True
    if start_flag1%2 == 0:
        start_flag=True
    else:
        start_flag=False
    #global    epdb
    #sesion_1=req.put(f'http://{udras}/state/graph')
    #lang_switch=lang_switch+1
    lang_bool=False
    if lang_switch%2== 0:
        punkt_menu=punkt_menu_nach[0]
        lang_bool=True

    else:
        punkt_menu=punkt_menu_nach[1]
        lang_bool=False
    #port_adres={'addr':'192.168.0.163','port':'5000'}
    adr=port_adres['addr']
    adr_port=port_adres['port']
    url_output=f'http://{adr}:{adr_port}'

    try:
        #data={'addr':'192.168.0.163','port':'5000'}
        #start=time.clock()
        start = time()
        rr=req.get(f'http://{udras}/init',params=(port_adres))
        stop=time() -start
        conect=True


        return render_template('2_gra.html',bufer_network2=bufer_network2,data_grafik1=data_grafik1,data_grafik2=data_grafik2, perv=perv,url_output=url_output,conect=conect,lang_bool=lang_bool,punkt_menu=punkt_menu,start_flag=start_flag,data=data,epdb=epdb,time_otvet= time_otvet,lang_switch=lang_switch)
    except Exception as ex:
        print('!!!punkt_menu=',conect)
        conect=False

        return render_template('2_gra.html',bufer_network2=bufer_network2,data_grafik1=data_grafik1,data_grafik2=data_grafik2, perv=perv,url_output=url_output,conect=conect,lang_bool=lang_bool,punkt_menu=punkt_menu,start_flag=start_flag,data=data,epdb=epdb,time_otvet= time_otvet,lang_switch=lang_switch)



@app.route('/data/<int:number>', methods=["GET", "POST"])
def data(number):
    if request.method == 'POST' or request.method == 'GET':
        global time_otvet , conect

        if conect :

            if number == 0 :

                try:
                    #rr=req.put(f'http://{udras}/params/eb',json=(json_out))
                    start = time()
                    rr=req.get(f'http://{udras}/stats/eb')
                    js = json.loads(rr.text)
                    print('\nFalse False=',js)
                    stop=time()-start
                    time_otvet= stop*1000
                    print('data time_otvet=',time_otvet)

                    eps_biar_graph=rr.text #.decode('utf-8')

                    #buferr=json.loads(rr.text)
                    #print(buferr)

                    json_poputka=json.loads(eps_biar_graph)

                    if js['response']['code'] == 0 :

                        print('/start=',json_poputka['stats']['time'])

                        timer= str(datetime.fromisoformat(json_poputka['stats']['time'])) #random.randint(100,200000)
                        data=[timer,int(json_poputka['stats']['size']),int(json_poputka['stats']['vpercent']),(time_otvet)]
                        json_data = json.dumps(data)

                        response = make_response(json_data)
                        print(json_data)

                        response.content_type = 'application/json'

                        return response
                except Exception as ex:
                    #conect = False
                    return  render_template('first.html')
                    #else:
                        #return redirect(url_for('LIST_EPS'))

                #print(rr.text)

                #print()

            else:

                try:
                    #rr=req.put(f'http://{udras}/params/eb',json=(json_out))
                    start = time()
                    rr=rr=req.get(f'http://{udras}/stats/eb/{number}')
                    js = json.loads(rr.text)
                    print('\nFalse False=',js)
                    stop=time()-start
                    time_otvet= stop*1000
                    print('data time_otvet=',time_otvet)

                    eps_biar_graph=rr.text #.decode('utf-8')

                    #buferr=json.loads(rr.text)
                    #print(buferr)

                    json_poputka=json.loads(eps_biar_graph)

                    if js['response']['code'] == 0 :

                        print('/start=',json_poputka['stats']['time'])

                        timer= str(datetime.fromisoformat(json_poputka['stats']['time'])) #random.randint(100,200000)
                        data=[timer,int(json_poputka['stats']['size']),int(json_poputka['stats']['vpercent']),(time_otvet)]
                        json_data = json.dumps(data)

                        response = make_response(json_data)
                        print(json_data)

                        response.content_type = 'application/json'

                        return response
                except Exception as ex:
                    #conect = False
                    return  render_template('first.html')




@app.route('/stats/graph', methods=[ 'POST'])
def chart_data():
    if request.method == 'POST':
        global json_data
        json_data=[]
        #def generate_random_data ():

            #eps_biar_graph = (request.get_data()).decode('utf-8')
        eps_biar_graph = (request.get_data())
            #print(eps_biar_graph)

        eps_biar_graph=eps_biar_graph.decode('utf-8')

        json_poputka=json.loads(eps_biar_graph)
        print('spis=',json_poputka['stats']['graph'])
        #for it in json_poputka['stats']:
            #print(it.keys())
        #print('test_js=',json_poputka.keys())

        eps=func_ochist(eps_biar_graph)
        timer=random.randint(100,200000)
        data=[timer,int(eps[3][1]),int(eps[4][1])]
        json_data = json.dumps(data)


        return (eps_biar_graph)
    else:
        return 'Hello, world'
@app.route('/verify', methods = ['POST', 'GET'])
def verify():
    """ обработка поступающих значений"""
    if request.method == 'POST':
        #test = request.form['name']
        return redirect(f"/gra")


if __name__ == "__main__":
    app.run('0.0.0.0', threaded=True)
    #app.run('192.168.0.163',port='5000', threaded=True)
    #socket_io.run(app, debug=True, host='localhost', port=5005)
