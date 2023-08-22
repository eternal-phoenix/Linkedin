import requests
import json


def request(id):
    r = requests.get(f'https://geo.victoriaville.ca/arcgis/rest/services/IntranetMRC/MatriceGraphiqueMRCCartePublique/MapServer/2/query?f=json&where=UPPER(matricule)%20%3D%20%{id}%27&returnGeometry=true&spatialRel=esriSpatialRelIntersects&outFields=code_muni%2Cmatricule%2Cnom_prenom%2Cnom_prenom_2%2Cn_nb_log%2Cp_nb_locaux%2Ce_etage%2Cd_date_ori%2Cu_util%2Cno_civ_inf%2Cfra_no_inf%2Cno_civ_sup%2Cfra_no_sup%2Cnom_voie%2Cfront%2Cprofondeur%2Cum_front_p%2Csuperficie%2Cum_superf%2Cv_vois%2Cutil_opt%2Cval_terrain%2Cval_batime%2Cval_immeub%2CLOTS%2CMatricule_Complet%2CGenerique%2CLien%2CAdresse%2CPF_No_Matricule%2CDate_Saisie%2CNom_municipalite%2COBJECTID%2CShape_Area%2CShape_Length%2CParc_industriel%2CPourcentageBoise%2CSuperficieBoiseHectare%2CGlobalID%2CDescriptionCodeUsage&outSR=32187&resultOffset=0&resultRecordCount=2000')
    if r.status_code != 200:
        print(r.status_code)
        return None
    try:
        json = r.json()
        if json == None:
            print("json error")
            return None    
        if "error" in json:
            print(json["error"])
            return None   
        return json
    except:
        pass
        return None
    return None

def write_to_file(data):
    with open('ids.json', 'w', newline='', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

currentIDs = []

for i in range(100000000, 10000000000):
    id = f"000000000{i}"[-10:]
    print(id)
    responce = request(id)
    if responce != None:
        currentIDs.append(id)
        write_to_file(currentIDs)
        print(responce)


print(currentIDs)



