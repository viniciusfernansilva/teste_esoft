$("#cadastro_produto").click(function(e){
    e.preventDefault();
    $(".modal-title").text("Cadastro de Produtos");
    $('#modal_produto').modal('show');
});

$("#salvar").click(function(e){
    e.preventDefault();
    var nome = $("#nome").val();
    var preco = $("#preco").val();
    var estoque = $("#estoque").val();
    
    if(nome == "" || preco == "" || estoque == ""){
        alert("Campos vazios detectados, verifique-os.");
    }
    else if(preco < 0 || estoque < 0 ){
        alert("Preço ou estoque inválidos.");
    }
    else{
        $("#form_produto").submit();
    }
});

$(document).ready(function(){
    $('#form_produto').submit(function(e) {
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
                    alert("Produto salvo com sucesso!");
                    location.href = "/produtos";
                }else if(result.mensagem == 'EXISTENTE'){
                    alert("Produto já cadastrado.");
                    location.href = "/produtos";
                }
                else{
                    alert("Não foi possível cadastrar o produto, por favor verifique os campos.");
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

function editar_produto(id_produto){
    $.get('/get_produto', { id_produto: id_produto}, function(response) {
        if (response.mensagem == "OK"){
            $("#nome").val(response.produto.nome);
            $("#preco").val(response.produto.preco);
            $("#estoque").val(response.produto.estoque);
            $("#id").val(response.produto.id);
        }
        else {
            console.log("Erro na hora de resgatar os dados do produto.");
        }
    });
    $(".modal-title").text("Edição de Produtos");
    $('#modal_produto').modal('show');
}

$("#fechar").click(function(e){
    e.preventDefault();
    $("#nome").val("");
    $("#preco").val("");
    $("#estoque").val("");
    $("#id").val("");   
});

function excluir_produto(id_produto){
    $.get('/del_produto', { id_produto: id_produto}, function(response) {
        if (response.mensagem == "OK"){
            alert("Produto excluído com sucesso.");
            location.href="/produtos";
        }
        else {
            alert("Não foi possível excluir o produto.");
        }
    });
}