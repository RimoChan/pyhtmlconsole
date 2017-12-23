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
        初始化()
    }
}

$(function(){
    初始化()
    $('#輸入文字').bind('keypress',
        function(event){
            if(event.keyCode == "13")
                提交()
        }
    );
})

function 顯示(s){
    var t=$('<span>')
    t.html(s)
    $('#字').append(t);
    $('html, body, .content').animate({scrollTop: $(document).height()}, 0);
    send('輸出完成');
}

function 輸入(s){
    $('#輸入框').fadeIn(400)
    $('#輸入文字').focus();
    // setTimeout(500,function(){$('#輸入文字').focus();})
    $('#提示文字').html(s)
}

function 提交(){
    $('#輸入框').fadeOut(250)
    send('@'+$('#輸入文字').val());
    $('#輸入文字').val('')
}
