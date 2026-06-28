<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><jsp:include page="inc/header.jsp" /></head>
<body>
<div class="container" style="margin-top: 60px">
<h2 class="title">Simple Upload</h2>
<form name="upload" action="stream.jsp" method="post" enctype="multipart/form-data">
    <div class="field">
        File: <input type="file" name="file">
    </div>
    <div class="field">
        <input type="submit" name="submit" value="Upload" class="button is-success">
    </div>
</form>
<jsp:include page="inc/footer.jsp" />
</div>
</body>
</html>
