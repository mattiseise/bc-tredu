import sys
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf-8').read()
i = t.index('<header')
head, body = t[:i], t[i:]
doc = ('<!doctype html>\n<html lang="fi">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       '<meta name="description" content="Tredulle 12.11.2026 pidetyn esityksen aineistot: Joustavan opiskeluryhmän diaesitys ja Esteiden raivaajat -video.">\n'
       '<meta name="robots" content="noindex">\n'
       + head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '') +
       '</head>\n<body>\n' + body + '</body>\n</html>\n')
open(dst, 'w', encoding='utf-8', newline='').write(doc)
print('ok', len(doc))
