
<div class="col-12 col-sm-8 col-md-6">
<div class="card">
<div class="card-body">
<h4 class="card-title">La Board</h4>
<p class="card-subtitle mb-2 text-muted">Ici vous pouvez même vous insulter bande de chiens de la casse</p>
    <script>
        $(document).ready(function() {
            if (!window.WebSocket) {
                if (window.MozWebSocket) {
                    window.WebSocket = window.MozWebSocket;
                } else {
                    $('#messages').append("<li>Your browser doesn't support WebSockets.</li>");
                }
            }
            ws = new WebSocket('ws://localhost:8080/websocket');
            ws.onopen = function(evt) {
                $('#messages').append('<li>Connected to chat.</li>');
            }
            ws.onmessage = function(evt) {
                $('#messages').append('<li>' + evt.data + '</li>');
            }
            $('#send-message').submit(function() {
                ws.send($('#name').val() + ": " + $('#message').val());
                $('#message').val('').focus();
                return false;
            });
        });
    </script>
    <form id="send-message">
        <input id="name" type="text" placeholder="name">
        <input id="message" type="text" placeholder="message" />
        <input type="submit" value="Send" />
    </form>
<div id="messages">
% if chat:
    % for msg in chat:
    <li>{{msg[2]}}:{{msg[3]}}</li>
    % end
</div>
</div>
</div>
</div>
