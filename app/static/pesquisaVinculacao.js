$('#pesquisar').keyup(function(){
    var $this = $(this);
    var pesquisa = $this.val();
    console.log(pesquisa);
    var achouAlgo = false;
    console.log(pesquisa.length);
    for(var j = 0; j < vinculacoes.length; j++){
        if(pesquisa == vinculacoes[j].id){
            achouAlgo = true;
            $("#listaVinculacoes").html(
                "<tbody>"+
                    "<tr>"+
                        "<td><h3>Cod FuncionarioXProjeto</h3></td>"+
                        "<td><h3>Funcionario</h3></td>"+
                        "<td><h3>Projeto</h3></td>"+
                        "<td><h3>Coordenador</h3></td>"+
                        "<th></th>"+
                    "</tr>"+
                    "<tr>"+
                        "<td>"+vinculacoes[j].id+"</td>"+
                        "<td>"+vinculacoes[j].funcionario+"</td>"+
                        "<td>"+vinculacoes[j].projeto+"</td>"+
                        "<td>"+vinculacoes[j].coordenador+"</td>"+
                        "<td>"+
                        "<a href='/admin/vinculacao/editar/"+vinculacoes[j].id+"'>"+
                        "<button class='btn btn-primary'>"+
                        "<i class='glyphicon glyphicon-pencil'></i> Editar</button>"+
                        "</a>"+
                        "<a href='/admin/vinculacao/detalhes/"+vinculacoes[j].id+"'>"+
                        "<button class='btn btn-info'>"+
                        "<i class='glyphicon glyphicon-info-sign'></i> Detalhes</button>"+
                        "</a>"+
                        "<a href='/admin/vinculacao/deletar/"+vinculacoes[j].id+"'>"+
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
        for(var j = 0; j < vinculacoes.length; j++){
            console.log('append');
            achouAlgo = true;
            lista = lista +
            "<tr>"+
                "<td>"+vinculacoes[j].id+"</td>"+
                "<td>"+vinculacoes[j].funcionario+"</td>"+
                "<td>"+vinculacoes[j].projeto+"</td>"+
                "<td>"+vinculacoes[j].coordenador+"</td>"+
                "<td>"+
                "<a href='/admin/vinculacao/editar/"+vinculacoes[j].id+"'>"+
                "<button class='btn btn-primary'>"+
                "<i class='glyphicon glyphicon-pencil'></i> Editar</button>"+
                "</a>"+
                "<a href='/admin/vinculacao/detalhes/"+vinculacoes[j].id+"'>"+
                "<button class='btn btn-info'>"+
                "<i class='glyphicon glyphicon-info-sign'></i> Detalhes</button>"+
                "</a>"+
                "<a href='/admin/vinculacao/deletar/"+vinculacoes[j].id+"'>"+
                "<button class='btn btn-danger'>"+
                "<i class='glyphicon glyphicon-trash'></i> Deletar</button>"+
                "</a>"+
                "</td>"+
            "</tr>";
        }
        console.log(lista);
        $("#listaVinculacoes").html(
        "<tbody>"+
            "<tr>"+
                "<td><h3>Cod FuncionarioXProjeto</h3></td>"+
                "<td><h3>Funcionario</h3></td>"+
                "<td><h3>Projeto</h3></td>"+
                "<td><h3>Coordenador</h3></td>"+
                "<th></th>"+
            "</tr>"+
        lista+"</tbody>");
    }

    if(!achouAlgo){
        console.log(achouAlgo);
        $("#listaVinculacoes").html("<tbody></tbody>");
    }
});