$(document).ready(function(){
    var str=window.location.href.split( '=' );
    console.log(str[1])
    var str=str[1].replace(/%20/g, " ");
    console.log(str)
	var rootRef=firebase.database().ref().child("liveChat/"+str);
	rootRef.on("child_added",snap =>{

	console.log(name)
	$("#table_body").append(convertToHtml(snap.val(),snap.key));
	scroll_data();

	});
	function convertToHtml(user,key){
		console.log(key)
		console.log(user)
  var html = '';
  html += '<li class="chat-left">';
    html += '<div class="chat-avatar">';
	html += '<img src="https://www.bootdey.com/img/Content/avatar/avatar3.png">';
	html += '<div class="chat-name text-left">'+user.messageUserName+'</div>';
	html += '</div>'
	html += '<div class="chat-text"  id='+key+'><div class="chat-name"  align="left">'+user.messageUser+' :'+'</div>'+user.messageText+'</div><div><i class="btn btn-outline-danger  btn-sm mx-5 mt-2 fa fa-trash" onClick="on_delete(\''+ key + '\')""></i></div>';
	
	html += '</li>';

  return html;

}
function scroll_data(){
                $("html, nav").animate({
                    scrollTop: $(
                      'html, nav').get(0).scrollHeight
                }, 50);
}




	});

	
	

	
	