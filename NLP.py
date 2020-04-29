import nltk
def nlp_mod(query):
    words=nltk.word_tokenize(query)
    print(words)
    keyword='error'
    agnya=['migrane','forehead','head','insomnia','sleep','sleeping','sleepy']
    nabhi = ['arthritis','joint','digestion', 'stomach','liver','acidity','ulcer','alcohol','infection','joints','infect']
    nabhi_swadishthan =['sugar','sweet', 'diabetes', 'insulin','jaundice','yellow','typhoid','allegry','allergies','itching','rashes','rash','redness']
    mooladhar=['sclerosis','AIDS','sexual','fatigue','numb','muscle','spasms','stiff','weak','depression','sad','anxiety','think','remeber','memory','mood','changes']
    anahat = ['cardio','chest pain','chest','left','left arm','heart','asthma','lung','breathing']
    swadishthan=['blood','pressure','BP','bp', 'hypertension','constipation','constipate','infertility','piles','fertility','importent','impotency','concieve','pregnant','pregnancy','child birth']
    vishudhi=['nose','throat','angina','thyroid','cold','running nose','throat pain','coughing','sinus','spine','back pain','back','cough']

    final = set(words) & set(agnya)
    if len(final)!=0:
        keyword='agnya'
    print(final)

    final = set(words) & set(vishudhi)
    if len(final)!=0:
        keyword='vishudhi'
    print(final)

    final = set(words) & set(swadishthan)
    if len(final)!=0:
        keyword='swadishthan'
    print(final)

    final = set(words) & set(anahat)
    if len(final)!=0:
        keyword='anahat'
    print(final)

    final = set(words) & set(mooladhar)
    if len(final)!=0:
        keyword='mooladhar'
    print(final)

    final = set(words) & set(nabhi)
    if len(final)!=0:
        keyword='nabhi'
    print(final)

    final = set(words) & set(nabhi_swadishthan)
    if len(final)!=0:
        keyword='nabhi_swadishthan'
    print(final)
    
    return keyword

