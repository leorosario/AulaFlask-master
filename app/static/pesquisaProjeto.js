$('#pesquisar').keyup(function(){
    var $this = $(this);
    var pesquisa = $this.val();
    console.log(pesquisa);
    var achouAlgo = false;
    console.log(pesquisa.length);
    for(var j = 0; j < projetos.length; j++){
        if(pesquisa == projetos[j].id){
            achouAlgo = true;
            $("#listaProjetos").html(
                "<tbody>"+
                    "<tr>"+
                        "<td><h3>Código</h3></td>"+
                        "<td><h3>Nome Projeto</h3></td>"+
                        "<td><h3>Cliente</h3></td>"+
                        "<td><h3>Descrição</h3></td>"+
                        "<th></th>"+
                    "</tr>"+
                    "<tr>"+
                        "<td>"+projetos[j].id+"</td>"+
                        "<td>"+projetos[j].nome+"</td>"+
                        "<td>"+projetos[j].cliente+"</td>"+
                        "<td>"+projetos[j].descricao+"</td>"+
                        "<td>"+
                        "<a href='/admin/projeto/editar/"+projetos[j].id+"'>"+
                        "<button class='btn btn-primary'>"+
                        "<i class='glyphicon glyphicon-pencil'></i> Editar</button>"+
                        "</a>"+
                        "<a href='/admin/projeto/detalhes/"+projetos[j].id+"'>"+
                        "<button class='btn btn-info'>"+
                        "<i class='glyphicon glyphicon-info-sign'></i> Detalhes</button>"+
                        "</a>"+
                        "<a href='/admin/projeto/deletar/"+projetos[j].id+"'>"+
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
        for(var j = 0; j < projetos.length; j++){
            console.log('append');
            achouAlgo = true;
            lista = lista +
            "<tr>"+
                "<td>"+projetos[j].id+"</td>"+
                "<td>"+projetos[j].nome+"</td>"+
                "<td>"+projetos[j].cliente+"</td>"+
                "<td>"+projetos[j].descricao+"</td>"+
                "<td>"+
                "<a href='/admin/projeto/editar/"+projetos[j].id+"'>"+
                "<button class='btn btn-primary'>"+
                "<i class='glyphicon glyphicon-pencil'></i> Editar</button>"+
                "</a>"+
                "<a href='/admin/projeto/detalhes/"+projetos[j].id+"'>"+
                "<button class='btn btn-info'>"+
                "<i class='glyphicon glyphicon-info-sign'></i> Detalhes</button>"+
                "</a>"+
                "<a href='/admin/projeto/deletar/"+projetos[j].id+"'>"+
                "<button class='btn btn-danger'>"+
                "<i class='glyphicon glyphicon-trash'></i> Deletar</button>"+
                "</a>"+
                "</td>"+
            "</tr>";
        }
        console.log(lista);
        $("#listaProjetos").html(
        "<tbody>"+
            "<tr>"+
                "<td><h3>Código</h3></td>"+
                "<td><h3>Nome Projeto</h3></td>"+
                "<td><h3>Cliente</h3></td>"+
                "<td><h3>Descrição</h3></td>"+
                "<th></th>"+
            "</tr>"+
        lista+"</tbody>");
    }

    if(!achouAlgo){
        console.log(achouAlgo);
        $("#listaProjetos").html("<tbody></tbody>");
    }
});