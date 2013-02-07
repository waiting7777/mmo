# -*- coding: utf-8 -*-

execfile("../common/config.py")



for i in range(total_set):

    index = i + 1
    
    output = '{%s}\n\n'%card_set[index]

    for type in card_type:

        head = 0
        tail = 0
        cardinfo = {}
        
        
        f = open('%s/%s.html'%(card_set[index], type), 'r')
        
        line = f.read()
        
        head = line.find('<tbody>')
        
        for j in range(line.count('target="_blank"')):
            
            cardinfo[j+1] = {}
            
            # card image
            head = line.find('href="', head)
            tail = line.find('" ', head)
            
            cardinfo[j+1]['card_image'] = line[head + len('href="'):tail]
            
            # card name
            head = line.find('target="_blank" >', head)
            tail = line.find('</a>', head)
            
            cardinfo[j+1]['card_name'] = line[head + len('target="_blank" >'):tail]
            
            if type == 'spell':
                
                # card faction
                head = line.find('markers/', head)
                tail = line.find('.png', head)
                
                cardinfo[j+1]['card_faction'] = line[head + len('markers/'):tail]
            
            else:
            
                # card faction
                head = line.find('alt="', head)
                tail = line.find('" ', head)
                
                cardinfo[j+1]['card_faction'] = line[head + len('alt="'):tail]
            
            
        print cardinfo
        # raw_input()
        
        output += '[%s]\n'%type
        for key in cardinfo:
            output += cardinfo[key]['card_name'] + '|'
            output += cardinfo[key]['card_faction'] + '|'
            output += cardinfo[key]['card_image'] + '\n'
            
    w = open('%s/total_card.txt'%card_set[index], 'w')
    w.write(output)

