'''
Supported color names:

    black (might be a gray)
    red
    green
    yellow (might be an orange)
    blue
    magenta
    cyan
    white (might be light gray)
    reset (reset the color code only)

New in version 2.0.
Parameters:

    text – the string to style with ansi codes.
    fg – if provided this will become the foreground color.
    bg – if provided this will become the background color.
    bold – if provided this will enable or disable bold mode.
    dim – if provided this will enable or disable dim mode. This is badly supported.
    underline – if provided this will enable or disable underline.
    blink – if provided this will enable or disable blinking.
    reverse – if provided this will enable or disable inverse rendering (foreground becomes background and the other way round).
    reset – by default a reset-all code is added at the end of the string which means that styles do not carry over. This can be disabled to compose styles.
'''

import click
from constants import LANG_CODES

def print_entry_header(text, pos='', gen='', ts=''):
    header_line = click.style(text, fg='blue', bold=True)
    if ts:
        header_line += click.style(' [' + ts + ']', dim=True)
    if pos:
        header_line += style_pos(pos)
    if gen:
        header_line += style_gen(gen)
    click.echo(header_line)


def print_lang_direction(tr_from, tr_to):
    str = LANG_CODES[tr_from] + ' -> ' + LANG_CODES[tr_to]
    click.secho(str, dim=True)


def print_translation(entry_num, text, pos='', gen='', syn=[], mean=[], ex=[]):
    synonym_line = click.style(entry_num + '  ', bold=True, dim=True)
    # tr[..]['text'] and tr[..]['syn'][..]['text'] belong on the same
    # line, separated by commas, so add former to latter array
    syn.insert(0,{'text': text, 'pos': pos})
    synonym_line += style_syn(syn)
    click.echo(synonym_line)
    if mean:
        meaning_line = '   '
        meaning_line += style_mean(mean)
        click.echo(meaning_line)
    if ex:
        for x in ex:
            click.echo(style_ex(x))


def style_pos(pos):
    return ' - ' + click.style(pos, fg='cyan')

def style_gen(gen):
    return click.style(' (' + gen + ')', dim=True)

def style_ts(ts):
    return click.style('[' + ts + ']', dim=True)

def style_mean(mean):
    str = '(' + mean[0]['text']
    if len(mean) > 1:
        for m in mean[1:]:
            str += ', ' + m['text']
    str += ')'
    return click.style(str,fg='green')

def style_syn(syn):
    str = ''
    for i,s in enumerate(syn):
        substr = s['text']
        if i > 0:
            substr = ', ' + substr
        str += substr
    return str


def style_ex(ex):
    example = click.style(ex['text'])
    translation = ex['tr'][0]['text']
    return example + ': ' + translation

def print_simple_translation(query, text, tr_from, tr_to):
    s_tr_from = click.style(tr_from + ' ', dim=True)
    s_tr_to = click.style(' ' + tr_to, dim=True)
    s_query = click.style(query + ' ', bold=True, fg='blue')
    click.echo(s_tr_from + s_query + '-> ' + text + s_tr_to)

