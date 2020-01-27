<html>
<head><title>ProjectFunder</title>
<style type="text/css">
* {
   margin:0;
   padding:0;
}

body{
   text-align:center;
   background: #efe4bf none repeat scroll 0 0;
}

#wrapper{
   width:960px;
   margin:0 auto;
   text-align:left;
   background-color: #fff;
   border-radius: 0 0 10px 10px;
   padding: 20px;
   box-shadow: 1px -2px 14px rgba(0, 0, 0, 0.4);
}

#header{
 color: #fff;
 background-color: #2c5b9c;
 height: 3.5em;
 padding: 1em 0em 1em 1em;
 
}

#site{
    background-color: #fff;
    padding: 20px 0px 0px 0px;
}
.centerBlock{
	margin:0 auto;
}
</style>

<body>
	<div id="wrapper">
		<div id="header">
		<h1> ProjectFunder Website </h1>
		</div>
	   
		<div id="site">
		
		
		<#list report! as r>
			${r}<br/>
   		</#list>
   		<#if benutzer??>
		Email: ${benutzer.email}<br/>
		Name: ${benutzer.name}<br/>
		Erstellte Projekte: ${anzahlErstellt}<br/>
		Unterstütze Projekte: ${anzahlUnterstuetzt}<br/>
		Erstellte Projekte:<br/>
		<#list erstellte as p>
	    <a href="/view_project?kennung=${p.kennung}">${p.titel}<a/><br/>
	    </#list>
	    Unterstützte Projekte:<br/>
		<#list unterstuetzte as u>
	    <a href="/view_project?kennung=${u.kennung}">${u.titel}<a/><br/>
	    </#list>
	    </#if>
	    
	    
	    
		</div>
		
		
	</div>
</body>
</html>
