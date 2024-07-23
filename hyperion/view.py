from django.http import HttpResponse
from django.http import HttpRequest


def index(request: HttpRequest):

    return HttpResponse(""" <!DOCTYPE html>
<html>
<head>
<title>Hyperion</title>
<style>
.chat {
  max-width: fit-content;
  margin-left: auto;
  margin-right: auto;
}
</style>
</head>
<body>

<div class="chat">
<p>Chat goes here</p>
<input class="textbox">

</div>

</body>
</html> """)
