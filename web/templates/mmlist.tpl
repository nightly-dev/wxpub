<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8' />
<meta http-equiv="Cache-Control" content="no-siteapp" />
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="black" />
<meta name="viewport" content="width=device-width,initial-scale=1, minimum-scale=1.0, maximum-scale=1, user-scalable=no" />
<meta name="apple-mobile-web-app-title" content="九妹图社" />
<title>九妹图社</title>
<link href="http://m.99mm.me/css/style.css" rel="stylesheet" type="text/css" />
</head>

<body>
   <ul class="piclist" id="piclist">
   {% for alias in aliaslist %}
   <li>
   <h2>
   <a href="">{{ alt }} - {{ loop.index }}</a>
   </h2>
   <div class="pic">
   <!-- <a href="{{ (url_for('static', filename=alias)) }}"> -->
      <img src="{{ (url_for('static', filename=alias)) }}" alt="{{ alt }}" />
   <!-- </a> -->
   </div>
   <div class="info"><span>{{ dt }} {{ source }}</span><span class="like">浏览(100+)</span></div>
   </li>
   {% endfor %}
   </ul>
 </body>
</html>
