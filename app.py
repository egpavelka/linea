import click, requests, vlc, json, xmltodict
# from secrets import key
key='09a65d92-a84c-4a33-9501-5504c39b28f8'

@click.command()
@click.option('--word', '-w', prompt=True, help='Include a Spanish word to look up.')
# @click.option('--pronounce', '-p', is_flag=True, help='Play audio recording of the word.')
def cli(word):
    uri = "https://www.dictionaryapi.com/api/v1/references/spanish/xml/%s?key=%s" % (word, key)
    doc = json.loads(json.dumps(xmltodict.parse(requests.get(uri).content)))

    entries = doc['entry_list']['entry']

    for x in entries:
        word = x['hw']
        posp = x['fl']

        if 'svr' in x['def']:
            phrases = x['def']['svr']
            num_phr = len(x['def']['svr'])
        
        # audio = "http://media.merriam-webster.com/audio/prons/es/me/wav/n/%s" % (x['sound'])
        # p = vlc.MediaPlayer(audio)

        line_print = "%s - %s" % (word, posp)
        click.echo(line_print)

        for i,j in enumerate(x['def']['dt']):
            def_id = x['def']['sn'][i]
            if type(j) == dict:

                if 'svr' in x['def'] and (x['def']['dt'][-num_phr] == j):
                    phrase = phrases.pop(-num_phr)
                    line_print = "%s %s : %s" % (def_id,phrase['va'],j['ref-link'])
                    click.echo(line_print)
                    num_phr -= 1
                    
                else:
                    line_print = "%s %s" % (def_id,j['ref-link'])
                    click.echo(line_print)

                if 'vi' in j:
                    line_print = " * %s" % (j['vi'])
                    click.echo(line_print)

            elif type(j) == str:
                line_print = "%s %s" % (def_id,j)
                click.echo(line_print)
            else:
                return

        click.echo('')
        

            # if pronounce : p.play()
            # if x['def']['dt'][i+1]:
                # cont to next def
