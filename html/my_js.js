var a;
a=new QWebChannel(qt.webChannelTransport, function (channel) {
	window.handler = channel.objects.handler;;
	send=function(str){window.handler.rec(str);};
});


function 初始化(){
    try{
        send('初始化');
    }
    catch(err){
        setTimeout(初始化,50)
    }
}

$(function(){
    初始化()
    設置輸入框行爲()
})

function 設置輸入框行爲(){
    $('#輸入框包裝').css('opacity','0.9')
    $('#輸入文字').bind('keypress',
        function(event){
            if(event.keyCode == "13")
                提交()
        }
    );
    $('#輸入文字').focus(function(){ 
        $('#輸入框包裝').css('opacity','0.9')
    }); 
    $('#輸入文字').blur(function(){ 
        $('#輸入框包裝').css('opacity','0.3')  
    }); 
}

緩衝字=''
function 顯示(s){
    if(s.charAt(s.length - 1)=='\n'){
        $('#現字').html('');
        $('#前字').append(緩衝字)
        緩衝字=''
        $('#前字').append(s)
    }else{
        for (i in s){
            if(s[i]=='\r'){
                var p=緩衝字.lastIndexOf('\n')
                緩衝字=緩衝字.substring(0,p+1)
            }
            else
                緩衝字+=s[i];
        }
        $('#現字').html(緩衝字);
    }
    $('html, body').animate({scrollTop: $(document).height()}, 0);
    send('輸出完成');
}

function 輸入(s){
    $('#輸入框').show(300);
    $('#輸入文字').focus();
    $('#提示文字').html(s); 
}

function 提交(){
    $('#輸入框').hide(200);
    send('@'+$('#輸入文字').val());
    $('#輸入文字').val('');
}
