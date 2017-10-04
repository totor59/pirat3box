
<div class="col-12 col-sm-8 col-md-6">
<div class="card">
<div class="card-body">
%if error:
<div class="col-12 alert alert-danger alert-dismissible fade show" role="alert">
  <button type="button" class="close" data-dismiss="alert" aria-label="Close">
    <span aria-hidden="true">&times;</span>
  </button>
  <strong>Error!</strong> {{error}}
</div>
%elif success:
<div class="col-12 alert alert-success alert-dismissible fade show" role="alert">
  <button type="button" class="close" data-dismiss="alert" aria-label="Close">
    <span aria-hidden="true">&times;</span>
  </button>
  <strong>Cool!</strong> {{success}}
</div>
%end
<h4 class="card-title">Zone Téléchargement</h4>
<p class="card-subtitle mb-2 text-muted">Partage, télécharge, uploade sans pression ...<br>
Pas de stress, pas d'hadopi t'es pas sur internet !</p>

<ul class="nav nav-tabs nav-fill" role="tablist">
  <li class="nav-item">
    <a class="nav-link active" href="#videos" role="tab" data-toggle="tab">Vidéos</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#music" role="tab" data-toggle="tab">Musique</a>
  </li>
   <li class="nav-item">
    <a class="nav-link" href="#images" role="tab" data-toggle="tab">Images</a>
  </li> 
  <li class="nav-item">
    <a class="nav-link" href="#others" role="tab" data-toggle="tab">Divers</a>
  </li>
</ul>

<!-- Tab panes -->
<div class="tab-content">
  <div role="tabpanel" class="tab-pane in active" id="videos">
        <ul>
      % for item in video:
      <li><a href="uploads/music/{{item}}">{{item}}</a></li>
      % end
    </ul>
  </div>
  <div role="tabpanel" class="tab-pane" id="music">
      <ul>
      % for item in audio:
      <li><a href="uploads/music/{{item}}">{{item}}</a></li>
      % end
    </ul>
  </div>
   <div role="tabpanel" class="tab-pane" id="images">
    <ul>
      % for item in img:
      <li><a href="uploads/img/{{item}}">{{item}}</a></li>
      % end
    </ul>
  </div> 
  <div role="tabpanel" class="tab-pane" id="others">
    <ul>
      % for item in others:
      <li><a href="uploads/others/{{item}}">{{item}}</a></li>
      % end
    </ul>
  </div>
</div>
<br>
<h4 class="card-title">Partager un fichier</h4>
<form method='post' action='/upload' class="form-inline" enctype='multipart/form-data'>
  <div class="form-group">
    <input id="file" name="newfile" type="file" class="form-control-file">
  </div>
<button type="submit" class="btn btn-primary">Uploader</button>
</form>
<br>
<h6 class="card-subtitle mb-2 text-muted">Espace disponible</h6>
<div class="progress">
<div class="progress-bar progress-bar-striped progress-bar-animated
bg-{{diskspace['color']}}"
role="progressbar" aria-valuenow="{{diskspace['usage']}}" aria-valuemin="0"
aria-valuemax="100" style="width: {{diskspace['usage']}}%">{{diskspace['usage']}}%</div>
</div>
</div>
</div>
</div>

