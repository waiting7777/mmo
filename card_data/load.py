# -*- coding: utf-8 -*-

execfile("../common/config.py")

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

for i in range(total_set):

    index = i + 1

    for type in card_type:

        resp = opener.open('http://www.mmdoc.net/card_list/list/type_card/%s/set/%d/'%(type, index))
        respline = resp.read()
        
        if os.path.exists('./%s'%card_set[index]) == False:
            os.system('mkdir ./%s'%card_set[index])
            
        w = open('./%s/%s.html'%(card_set[index], type), 'w')
        w.write(respline)

