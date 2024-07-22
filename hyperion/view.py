from django.http import HttpResponse


def index(request):

    return HttpResponse(""" <!DOCTYPE html>
<html>
<head>
<title>Hyperion</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This isn't one.</p>

</body>
</html> """)
