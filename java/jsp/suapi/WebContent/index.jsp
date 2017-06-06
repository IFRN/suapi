<%@ page language="java" 
		 contentType="text/html; charset=UTF-8"
    	 pageEncoding="UTF-8"
  		 
  		 import="br.edu.ifrn.SuapClient" 
		 import="org.json.simple.JSONObject"
		 import="org.json.simple.parser.JSONParser"
		 import="org.json.simple.parser.ParseException"
%>

<%
	SuapClient sc = new SuapClient();
	String data = sc.getData(); 
	
	JSONParser parser = new JSONParser(); 
	JSONObject json = (JSONObject) parser.parse(data);
	System.out.print(json); 
	out.println("Matrícula: " + json.get("matricula")); 
%> 