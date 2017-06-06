Exemplo de acesso a API SUAP utilizando JSP - [Prof. Bruno E. G. Gomes](@brunoggomes) - IFRN Parnamirim

O Arquivo suapi_jsp.tar.gz contém um projeto Eclipse com o exemplo

Componentes principais 
* classe br.edu.ifrn.SuapClient - classe que conecta a URL e obtém os dados JSON
* index.jsp - Usa SuapClient, converte o JSON 
para um objeto Java e imprime o resultado. 

Bibliotecas utilizadas (encontram-se no diretório libs do projeto):
* Apache HttpComponents - https://hc.apache.org/httpcomponents-client-4.5.x/index.html
* JSON simple - https://www.mkyong.com/java/json-simple-example-read-and-write-json/
