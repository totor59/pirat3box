
<div class="col-12 col-sm-8 col-md-6">
<div class="card">
<div class="card-body">
<h4 class="card-title">La Board</h4>
<p class="card-subtitle mb-2 text-muted">Ici vous pouvez même vous insulter bande de chiens de la casse</p>
    <script>
        $(document).ready(function() {
        // scroll the chat from bottom
        $("#chat-room").scrollTop($("#chat-room")[0].scrollHeight);
        function safe_tags(str) {
        return str.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;') ;
        }         
            if (!window.WebSocket) {
                if (window.MozWebSocket) {
                    window.WebSocket = window.MozWebSocket;
                } else {
                    $('#messages').append("<li>Your browser doesn't support WebSockets.</li>");
                }
            }
            ws = new WebSocket('ws://192.168.1.57:8080/websocket');
            ws.onopen = function(evt) {
                $('#messages').append('<li class="text-danger"><b>Vous avez rejoint la room</b></li>');
            }
            ws.onmessage = function(evt) {
                $('#messages').append('<li>' + evt.data + '</li>');
            }
            $('#send-message').submit(function() {
                var usr = docCookies.getItem('w00tw00t');
                var content = $('#message').val();
                var msg = [usr, content];
                if(msg !== '') { 
                    ws.send(JSON.stringify(msg));
                    $('#message').val('').focus();
                    return false;
                }
            });
        });
    </script>

<div id="chat-room" class="chat-room card col-12">
  <div class="card-body">
<ul id="messages" class="list-unstyled col-12">
% if chat:
    % oldDate = ""
    % for msg in chat:
        % if oldDate != msg[5]:
        <li class="row separator">
          <hr class="col-4">
          <span class="text-center col-4">{{ msg [5] }}</span>
          <hr class="col-4">
        </li>
        %end
    <li class=><b>{{ msg[2] }}</b> - {{! msg[4] }}<br>
&nbsp;&nbsp;&nbsp;{{ msg[3] }}</li>
    % oldDate = msg[5]
    % end
    % end
</ul>
</div>
</div>
 <form id="send-message">
    <div class="input-group">
      <span class="input-group-btn">
        <button class="btn btn-secondary" type="submit">Go!</button>
      </span>
      <input type="text" class="form-control" id="message" placeholder="Dites un truc ...">
    </div>
</form>

</div>
</div>
</div>
% if cookie == 0:
<script>
$(document).ready(function() {
    var name = prompt("Quel est ton nom étranger?")
    docCookies.setItem("w00tw00t", name, Infinity);
});
</script>
% end
