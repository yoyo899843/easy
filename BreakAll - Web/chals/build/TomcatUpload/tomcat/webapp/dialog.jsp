<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head><jsp:include page="inc/header.jsp" /></head>
<body>
  <div class="container" style="margin-top: 60px">
<%
  String msg = (String)request.getAttribute("msg");

  if(msg != null)
  	out.println("<p><font size=+1>" + msg + "</font></p>");
%>
<hr>
<p>Click <a href="index.jsp">here</a> to go back.</p>
<jsp:include page="inc/footer.jsp" />
  </div>
</body>
</html>

