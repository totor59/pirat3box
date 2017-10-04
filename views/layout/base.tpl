<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{title}}</title>
    <link rel="icon" type="image/png" href="static/favicon.gif" />
    <link rel="stylesheet" href="static/css/lib/bootstrap.min.css">
    <link rel="stylesheet" href="static/css/style.css">
    <script type="text/javascript" src="static/js/lib/jquery.min.js"></script>
</head>
<body>
    <div class="container">
        <div class="row">
        <div class="col-12">
            <div class="jumbotron jumbotron-fluid col-12">
                <div class="row align-items-center justify-content-center">
                    <img src="static/img/pirate-flag.png" class="col-3" alt="">
                    <div class="jumbotron_wrap float-right text-center">
                    <h1 class="display-3">pirat3box</h1>
                    <p class="lead">Pour tous les roubaisiens wallah</p>
                </div>
                </div>
                </div>
            </div>
            % include('gallery.tpl')
            % include('chat.tpl')
        </div>
    </div>
<script type="text/javascript" src="static/js/lib/popper.min.js"></script>
<script type="text/javascript" src="static/js/lib/bootstrap.min.js"></script>
</body>
</html>
