$("#cadastro").click(function(e){
    e.preventDefault();
    var nome = $("#nome").val();
    var email = $("#email").val();
    var senha = $("#password").val();
    var repetir_senha = $("#repeat_password").val();
    var cep = $("#cep").val();
    var endereco = $("#endereco").val();
    var bairro = $("#bairro").val();
    var numero = $("#numero").val();
    var cidade = $("#cidade").val();
    var uf = $("#uf").val();
    if(nome == "" || email == "" || senha == "" || repetir_senha == "" || cep == "" || 
       endereco == "" || bairro == "" || numero == 0 || cidade == "" || uf == ""){
        alert("Campos vazios detectados, verifique-os.");
    }
    else if(email.indexOf("@") == -1){
        alert("Campo email inválido.");
    }
    else if(senha != repetir_senha){
        alert("Senha digitada é diferente da confirmação.");
    }
    else{
        $("#form_cadastro").submit();
    }
});

$(document).ready(function(){
    $("#cep").mask("99.999-999");
    $('#form_cadastro').submit(function(e) {
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
                    alert("Usuário cadastrado com sucesso!");
                    location.href = "/login";
                }else if(result.mensagem == 'EXISTENTE'){
                    alert("Usuário já cadastrado.");
                    location.href = "/cadastro";
                }
                else{
                    alert("Não foi possível cadastrar o usuário, por favor verifique os campos.");
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

$("#cep").focusout(function() {
    if ($("#cep").val() != "") {
        $.ajax({
            url: 'https://viacep.com.br/ws/' + $(this).val().replace(".", "").replace("-", "") + '/json/',
            dataType: 'json',
            success: function(resposta) {
                $("#endereco").val(resposta.logradouro);
                $("#bairro").val(resposta.bairro);
                $("#cidade").val(resposta.localidade);
                $("#uf").val(resposta.uf);
                $("#complemento").val(resposta.complemento);
                $("#numero").focus();
            }
        });
    }
});