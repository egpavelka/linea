import click, requests, vlc, json, xmltodict
from secrets import key

@click.command()
@click.option('--word', '-w', multiple=True, default='', help='Include a Spanish word to look up.')
@click.option('--pronounce', '-p', is_flag=True, help='Play audio recording of the word.')
def cli(word,pronounce):
    if :
        click.echo("Now we're talking.")
    click.echo('yay')

uri = "https://www.dictionaryapi.com/api/v1/references/spanish/xml/%s?key=%s" % (word, key)
doc = json.loads(json.dumps(xmltodict.parse(requests.get(uri).content)))
entries = doc['entry_list']['entry']

for x in entries:
    word = x['hw']
    sound = x['sound']
    posp = x['fl']

    print(word,'-',posp)

    for i,j in enumerate(x['def']['dt']):
        print(x['def']['sn'][i],j['ref-link'])
        if 'vi' in j : print(' ',j['vi'])


# http://www.spanishcentral.com/audio?file=nunca01sp&word=nunca&text=&format=mp3
audio = "http://media.merriam-webster.com/audio/prons/es/me/wav/n/%s" % (filename)
p = vlc.MediaPlayer(audio)
# p.play()

