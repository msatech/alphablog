$(document).ready(function(){
	var rootRef=firebase.database().ref().child("liveChat");
	rootRef.on("child_added",snap =>{
	$("#table_body").append(convertToHtml(snap.val(),snap.key));


	});


	function convertToHtml(user,key){
		console.log(key)


  var html = '';
	html += '<tr><td><a href="livechat?data='+key+'"   target="_blank">'+key+'</td></tr>';
	//console.log(window.location.href)
  return html;
}
	});
function getURL() {
        alert("The URL of this page is: " + window.location.href);
    }




