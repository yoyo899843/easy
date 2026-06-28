<%@ page import="java.io.StringReader" %>
<%@ page import="org.w3c.dom.*" %>
<%@ page import="javax.xml.parsers.*" %>
<%@ page import="org.xml.sax.InputSource" %>
<%
out.println("<br>");
if(request.getParameter("xml") != null) {
        DocumentBuilderFactory docFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder docBuilder = docFactory.newDocumentBuilder();
        StringReader reader = new StringReader(request.getParameter("xml"));
        InputSource inputSource = new InputSource( reader );
        Document doc = docBuilder.parse( inputSource );
        reader.close();

        Element  element = doc.getDocumentElement();
        NodeList myNodes = element.getChildNodes();
        out.println("<h2>XML Parse Result:<h2><pre>");
        for (int i=0; i<myNodes.getLength(); i++){
            out.println(myNodes.item(i).getNodeValue());
        }
        out.println("</pre>");
} else {
        out.println("<h2>XML Parser</h2>");
        out.println("<form><textarea name='xml' placeholder='<root>meow</root>'></textarea><br><br><input type='submit'></form>");
}
%>
