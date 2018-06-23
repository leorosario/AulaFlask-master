$('#pesquisar').keyup(function(){
    var $this = $(this);
    var pesquisa = $this.val();
    console.log(pesquisa);
    var achouAlgo = false;
    console.log(pesquisa.length);
    for(var j = 0; j < clientes.length; j++){
        if(pesquisa == clientes[j].cpfcnpj){
            achouAlgo = true;
            $("#listaClientes").html(
                "<tbody>"+
                    "<tr>"+
                        "<td><h3>CPF/CNPJ</h3></td>"+
                        "<td><h3>Nome</h3></td>"+
                        "<th></th>"+
                    "</tr>"+
                    "<tr>"+
                        "<td>"+clientes[j].cpfcnpj+"</td>"+
                        "<td>"+clientes[j].nome+"</td>"+
                        "<td>"+
                        "<a href='/admin/Cliente/editar/"+clientes[j].id+"'>"+
                        "<button class='btn btn-primary'>"+
                        "<i class='glyphicon glyphicon-pencil'></i> Editar</button>"+
                        "</a>"+
                        "<a href='/admin/Cliente/detalhes/"+clientes[j].id+"'>"+
                        "<button class='btn btn-info'>"+
                        "<i class='glyphicon glyphicon-info-sign'></i> Detalhes</button>"+
                        "</a>"+
                        "<a href='/admin/Cliente/deletar/"+clientes[j].id+"'>"+
                        "<button class='btn btn-danger'>"+
                        "<i class='glyphicon glyphicon-trash'></i> Deletar</button>"+
                        "</a>"+
                        "</td>"+
                    "</tr>"+
                "</tbody>"
            );
        }
    }

    if(pesquisa.length == 0){
        var lista = "";
        for(var j = 0; j < clientes.length; j++){
            console.log('append');
            achouAlgo = true;
            lista = lista +
            "<tr>"+
                "<td>"+clientes[j].cpfcnpj+"</td>"+
                "<td>"+clientes[j].nome+"</td>"+
                "<td>"+
                "<a href='/admin/Cliente/editar/"+clientes[j].id+"'>"+
                "<button class='btn btn-primary'>"+
                "<i class='glyphicon glyphicon-pencil'></i> Editar</button>"+
                "</a>"+
                "<a href='/admin/Cliente/detalhes/"+clientes[j].id+"'>"+
                "<button class='btn btn-info'>"+
                "<i class='glyphicon glyphicon-info-sign'></i> Detalhes</button>"+
                "</a>"+
                "<a href='/admin/Cliente/deletar/"+clientes[j].id+"'>"+
                "<button class='btn btn-danger'>"+
                "<i class='glyphicon glyphicon-trash'></i> Deletar</button>"+
                "</a>"+
                "</td>"+
            "</tr>";
        }
        console.log(lista);
        $("#listaClientes").html(
        "<tbody>"+
            "<tr>"+
                "<td><h3>CPF/CNPJ</h3></td>"+
                "<td><h3>Nome</h3></td>"+
                "<th></th>"+
            "</tr>"+
        lista+"</tbody>");
    }

    if(!achouAlgo){
        console.log(achouAlgo);
        $("#listaClientes").html("<tbody></tbody>");
    }
});