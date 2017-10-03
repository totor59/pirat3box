% rebase('layout/base.tpl', title="pirat3box")


<div class="card col-12 col-sm-8 col-md-6" style="width: 20rem;">
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
<h4 class="card-title">Gallery</h4>
<p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>

<ul class="nav nav-tabs" role="tablist">
  <li class="nav-item">
    <a class="nav-link active" href="#videos" role="tab" data-toggle="tab">Vidéos</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#music" role="tab" data-toggle="tab">Musique</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#images" role="tab" data-toggle="tab">Images</a>
  </li>
</ul>

<!-- Tab panes -->
<div class="tab-content">
  <div role="tabpanel" class="tab-pane fade in active" id="videos">...</div>
  <div role="tabpanel" class="tab-pane fade" id="music">bbb</div>
  <div role="tabpanel" class="tab-pane fade" id="images">ccc</div>
</div>
<br>
<h6 class="card-subtitle mb-2 text-muted">Disk usage</h6>
<div class="progress">
<div class="progress-bar progress-bar-striped progress-bar-animated bg-danger" role="progressbar" aria-valuenow="{{diskspace}}" aria-valuemin="0" aria-valuemax="100" style="width: {{diskspace}}%">{{diskspace}}%</div>
</div>
<br>
<form method='post' action='/upload' enctype='multipart/form-data'>
<label for="file" class="label-file btn-outline-info">Uploader un fichier</label>
<input id="file" name="newfile" class="input-file" type="file" onchange="this.form.submit()" accept="">
</form>
<a href="#" class="card-link">Card link</a>
<a href="#" class="card-link">Another link</a>
</div>
</div>
<h1 id="app">
    {% message %}
</h1>


