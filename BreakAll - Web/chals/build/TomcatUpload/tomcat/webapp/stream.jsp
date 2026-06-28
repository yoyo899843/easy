<%@ page import="org.apache.commons.fileupload.*, org.apache.commons.io.*, org.apache.commons.fileupload.servlet.*, org.apache.commons.fileupload.disk.*, java.io.*, java.util.Iterator, java.util.regex.Pattern" %>
<%
// This pattern is used to get the basename of a filename
final Pattern basenamePattern = Pattern.compile("^.*[/\\\\]");

// Check that we have a file upload request
boolean isMultipart = ServletFileUpload.isMultipartContent(request);

// if not, send to message page with the error message
if(!isMultipart){
    request.setAttribute("msg", "Request was not multipart!");
    request.getRequestDispatcher("dialog.jsp").forward(request, response);
    return;
}

String uploadPath = System.getProperty("os.name").matches("Windows.*") ?
                    "C:\\TEMP\\uploads\\" : "/usr/local/tomcat/webapps/simpleupload/data/";

// Create a new file upload handler
ServletFileUpload upload = new ServletFileUpload();


// Parse the request
FileItemIterator iter = upload.getItemIterator(request);
while (iter.hasNext()) {
    FileItemStream item = iter.next();
    InputStream stream = item.openStream();
    if (!item.isFormField()) {
        String fileName = item.getName();
        //String uploadedFile = uploadPath + basenamePattern.matcher(fileName).replaceFirst("");;
        String uploadedFile = uploadPath + fileName;

        IOUtils.copy(stream, new FileOutputStream(uploadedFile));

        request.setAttribute("msg", "Uploaded '" + fileName + "' to '<a href='data/"+fileName+"'>" + uploadedFile + "</a>'");
    }
}

request.getRequestDispatcher("dialog.jsp").forward(request, response);

%>
