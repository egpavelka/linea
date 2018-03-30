import json
import requests
from constants import DICT_BASE, TRNSL_BASE, LANG_CODES
from click_styles import print_entry_header, print_lang_direction, print_translation, print_simple_translation

# click option: --from (lang code)
# HELP command: linea list-codes (list of language codes)
def get_definition(text, tr_from='', tr_to='en'):
    # dictionary lookup requires both language codes (es-en),
    # translate just requires target language and tries to autodetect
    # the original.  if the origin language is not indicated, use
    # the translation api to detect it and then use that with the
    # dictionary api.
    if tr_from:
        lang = tr_from + '-' + tr_to
        translation = (text,lang)
    else:
        translation = call_translation(text,tr_to)
        tr_from = translation['lang'].split('-')[0]
        lang = translation['lang']
    response = call_dictionary(text, lang)
    if 'def' in response and response['def']:
        format_dictionary(response, tr_to, tr_from)
        # return response
    else:
        p_tr_to = LANG_CODES[tr_to]
        p_tr_from = LANG_CODES[tr_from]
        trnsl = ', '.join(translation['text'])
        print_simple_translation(text, trnsl, p_tr_from, p_tr_to)
        # return translation

def api_call(base, text, lang):
    json_url = '%s&text=%s&lang=%s' % (base, text, lang)
    return json.loads(requests.get(json_url).content)


def call_dictionary(text, lang):
    return api_call(DICT_BASE, text, lang)


def call_translation(text, lang):
    return api_call(TRNSL_BASE, text, lang)


def format_dictionary(response, tr_from, tr_to):
    print_lang_direction(tr_from, tr_to)
    for dfn in response['def']:
        header = generate_header(dfn)
        print_entry_header(**header)
        for i,tr in enumerate(dfn['tr']):
            tr['entry_num'] = str(i+1)
            print_translation(**tr)

def generate_header(dfn):
    header = {}
    for key,val in dfn.items():
        if isinstance(val,str):
            header[key] = val + ' '
    return header
