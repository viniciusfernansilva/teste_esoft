$("#criar_conta").click(function(e){
    e.preventDefault();
    location.href = "/cadastro";
});
$("#login").click(function(e){
    e.preventDefault();
    var email = $("#email").val();
    var senha = $("#password").val();
    if(email != "" && senha != ""){
        $("#form_login").submit();
    }
    else{
        alert("Campos vazios, coloque um email/senha válidos!");
    }
});
$(document).ready(function(){
    $('#form_login').submit(function(e) {
        var formData = new FormData($(this)[0]); 
        $.ajax({ 
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            data: formData,
            cache: false,
            contentType: false,
            enctype: 'multipart/form-data',
            processData: false,

            success: function(result){
                if(result.mensagem == 'OK'){
                    location.href = "/home";
                }else{
                    alert("E-mail e/ou senha inválidos!");
                }
            },
            fail: function(msg){
                alert("Ocorreu uma falha! " + msg);
            },
            error: function(msg){
                alert("Ocorreu um erro! " + msg);
            },
            timeout: 180000
        });
        e.preventDefault();
    });
});
