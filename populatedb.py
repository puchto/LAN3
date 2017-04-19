import sys, os
import django
django.setup()

#os.environ['DJANGO_SETTINGS_MODULE']='LAN3.settings'
from clients.models import Clients_det, Client_service, Speed_packet
#from django.core.management import setup_environ
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LAN3.settings")
#from LAN3 import settings




###script_path = os.path.dirname(__file__)
###project_dir = os.path.abspath(os.path.join(script_path,'..','..','LAN3'))
###sys.path.insert(0, project_dir)

Clients_det.objects.all().delete()
directory = '/home/puchto/Dropbox/Nauka2015/pythonscripts/pliki_robocze/krowa_workfiles/'
filelist = [f for f in os.listdir(directory) if os.path.isfile(directory + f)]
for f in filelist:
    if 'klienci' in f:
        with open(directory + f) as currf:
            for i, line in enumerate(currf, 0):
                rec = line.split('|')
                print (rec[3], end='\n')
                cl_srv = Client_service.objects.get(service = rec[3])
                speeds = Speed_packet.objects.all()
                for sp in speeds:
                    if int(rec[4]) < sp.ds:
                        if len(rec[0].split('_')) == 1:
                                    cl_add_ul = rec[0]
                                    cl_add_nrd = ''
                                    cl_add_nrm = ''
                                    cl_add_rect = ''
                        elif len(rec[0].split('_')) == 2:
                                    cl_add_ul = rec[0].split('_')[0]
                                    cl_add_nrd = rec[0].split('_')[1]
                                    cl_add_nrm = ''
                                    cl_add_rect = ''
                        elif len(rec[0].split('_')) == 3:
                                    cl_add_ul = rec[0].split('_')[0]
                                    cl_add_nrd = rec[0].split('_')[1]
                                    cl_add_nrm = rec[0].split('_')[2]
                                    cl_add_rect = ''
                        elif len(rec[0].split('_')) == 4:
                                    cl_add_ul = rec[0].split('_')[0]
                                    cl_add_nrd = rec[0].split('_')[1]
                                    cl_add_nrm = rec[0].split('_')[2]
                                    cl_add_rect = rec[0].split('_')[3]
                        elif len(rec[0].split('_')) == 5:
                                    cl_add_ul = rec[0].split('_')[0]
                                    cl_add_nrd = rec[0].split('_')[1]
                                    cl_add_nrm = rec[0].split('_')[2]
                                    cl_add_rect = rec[0].split('_')[3] + rec[0].split('_')[4]
                                    
                        cl = Clients_det(cl_add_ul=cl_add_ul,
                                                    cl_add_nrd=cl_add_nrd, 
                                                    cl_add_nrm=cl_add_nrm,
                                                    cl_ip=rec[2],
                                                    cl_mac=rec[1],
                                                    srv=cl_srv,
                                                    speed=sp)
                        cl.save()
                        
                        break
                    
                        
                        
                        
                        
                        