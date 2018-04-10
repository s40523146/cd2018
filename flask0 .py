<body onload="brython()">
    <div class="paginator" >
        <script type="text/python">{% raw %}

            from browser import document,html
            import re, time

            # 按下按鈕執行以下程式

            @document["mybutton"].bind("click")
            def echo(ev):
                fake_qs = '?foo=%s' %time.time()

                with open('./../../../../data/2a.txt'+fake_qs) as fh:
                    data = [(re.findall('405\d\d\d\d\d', data[int(i)])) for i in range(len(data))]
                num = 0
                for i in range(len(data)):
                    team = data[i]
                    for g in range(len(team)):
                        if g%3 == 0:
                            num += 1
                            document['zone'] <= ('第' + str(num) +'組:' + str(team[g:g+3]) + html.BR())
                        
                        
            @document["mybutton2"].bind("click")
            def delete(ev):
                for row in document['zone']:
                    row.remove()
        {% endraw %}</script>            
        <button id="mybutton" class="next">執行</button><button id="mybutton2" class="next">清除</button>
    </div>
</body>