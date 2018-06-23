$('#pesquisar').keyup(function(){
    var $this = $(this);
    var pesquisa = $this.val();
    console.log(pesquisa);
    var achouAlgo = false;
    console.log(pesquisa.length);
    for(var j = 0; j < funcionarios.length; j++){
        if(pesquisa == funcionarios[j].matricula){
            achouAlgo = true;
            $("#listaFuncionarios").html(
                "<tbody>"+
                    "<tr>"+
                        "<td><h3>Matrícula</h3></td>"+
                        "<td><h3>Nome</h3></td>"+
                        "<th></th>"+
                    "</tr>"+
                    "<tr>"+
                        "<td>"+funcionarios[j].matricula+"</td>"+
                        "<td>"+funcionarios[j].nome+"</td>"+
                        "<td>"+
                        "<a href='/admin/funcionario/editar/"+funcionarios[j].id+"'>"+
                        "<button class='btn btn-primary'>"+
                        "<i class='glyphicon glyphicon-pencil'></i> Editar</button>"+
                        "</a>"+
                        "<a href='/admin/funcionario/detalhes/"+funcionarios[j].id+"'>"+
                        "<button class='btn btn-info'>"+
                        "<i class='glyphicon glyphicon-info-sign'></i> Detalhes</button>"+
                        "</a>"+
                        "<a href='/admin/funcionario/deletar/"+funcionarios[j].id+"'>"+
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
        for(var j = 0; j < funcionarios.length; j++){
            console.log('append');
            achouAlgo = true;
            lista = lista +
            "<tr>"+
                "<td>"+funcionarios[j].matricula+"</td>"+
                "<td>"+funcionarios[j].nome+"</td>"+
                "<td>"+
                "<a href='/admin/funcionario/editar/"+funcionarios[j].id+"'>"+
                "<button class='btn btn-primary'>"+
                "<i class='glyphicon glyphicon-pencil'></i> Editar</button>"+
                "</a>"+
                "<a href='/admin/funcionario/detalhes/"+funcionarios[j].id+"'>"+
                "<button class='btn btn-info'>"+
                "<i class='glyphicon glyphicon-info-sign'></i> Detalhes</button>"+
                "</a>"+
                "<a href='/admin/funcionario/deletar/"+funcionarios[j].id+"'>"+
                "<button class='btn btn-danger'>"+
                "<i class='glyphicon glyphicon-trash'></i> Deletar</button>"+
                "</a>"+
                "</td>"+
            "</tr>";
        }
        console.log(lista);
        $("#listaFuncionarios").html(
        "<tbody>"+
            "<tr>"+
                "<td><h3>Matrícula</h3></td>"+
                "<td><h3>Nome</h3></td>"+
                "<th></th>"+
            "</tr>"+
        lista+"</tbody>");
    }

    if(!achouAlgo){
        console.log(achouAlgo);
        $("#listaFuncionarios").html("<tbody></tbody>");
    }
});